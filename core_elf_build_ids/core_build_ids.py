import sys

from core_elf_build_ids.build_ids import get_files_and_build_ids

# todo, use click and enable machine output (json etc)
def main():
    assert len(sys.argv) == 2, "Usage: {} <ELF file>".format(sys.argv[0])

    core_file = sys.argv[1]

    files_and_build_ids = get_files_and_build_ids(core_file)

    print("Found files with build ids:", file=sys.stderr)

    for file, build_id in files_and_build_ids:
        print(file, "-", build_id)


if __name__ == "__main__":
    main()
