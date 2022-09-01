import sys

from core_elf_build_ids.build_ids import get_nt_file_entries, get_build_id


def main():
    assert len(sys.argv) == 2, "Usage: {} <ELF file>".format(sys.argv[0])

    core_file = sys.argv[1]

    nt_files = get_nt_file_entries(core_file)

    print("Found files with build ids:")

    for file in nt_files:
        build_id = get_build_id(file)
        print(file.decode("utf-8"), "-", build_id)


if __name__ == "__main__":
    main()
