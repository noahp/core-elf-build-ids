import os
import sys

try:
    from elftools.elf.elffile import ELFFile
    from elftools.elf.sections import NoteSection
    from elftools.elf.segments import NoteSegment
    from rich import print
except ImportError:
    print("[!] Please install elftools + rich")
    sys.exit(1)


def get_build_id(elf_file):
    if not os.path.exists(elf_file):
        return "[unable to find file]"

    with open(elf_file, "rb") as f:
        elf = ELFFile(f)
        for section in elf.iter_sections():
            if isinstance(section, NoteSection):
                for note in section.iter_notes():
                    if section.name == ".note.gnu.build-id":
                        return note.n_desc
    assert False, "No build-id found in {}".format(elf_file)


def get_nt_file_entries(elf_file):
    files = []

    with open(elf_file, "rb") as f:
        elf = ELFFile(f)
        for segment in elf.iter_segments():
            if not isinstance(segment, NoteSegment):
                continue
            for note in segment.iter_notes():
                if note["n_type"] != "NT_FILE":
                    continue

                desc = note["n_desc"]
                files = sorted(set(desc["filename"]))
                break

    return files


def get_files_and_build_ids(elf_file):
    files = get_nt_file_entries(elf_file)

    result = []

    for file in files:
        build_id = get_build_id(file)
        result.append((file.decode("utf8"), build_id))

    return result
