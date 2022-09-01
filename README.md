# core-elf-build-ids

Parses a ELF format core file and dumps GNU Build IDs for all `NT_FILE` entries,
assuming they are available on the current file system.

See `elfutils`'s `unstrip` (often called `eu-unstrip`) for a similar utility.

```bash
# build the sample program, load it in gdb, run it to main, generate a core file
❯ gcc -o hello hello.c && gdb hello -batch --ex 'b main' --ex 'r' --ex 'generate-core-file core.file'

# parse the core file for build ids
❯ python core_build_ids.py core.file
Found files with build ids:
/home/noah/dev/github/core-file-ntfiles/hello - cf247ad8d0651798479811263357311d40484d80
/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 - 61ef896a699bb1c2e4e231642b2e1688b2f1a61e
/usr/lib/x86_64-linux-gnu/libc.so.6 - 69389d485a9793dbe873f0ea2c93e02efaa9aa3d
```
