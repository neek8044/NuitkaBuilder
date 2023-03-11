# NuitkaBuilder

NuitkaBuilder is a python script used in the terminal that runs the appropriate nuitka command needed to compile a script as a standalone program. (similar to the auto-py-to-exe project). Made for Linux and Unix-based systems, but can be used on Windows as well.

The project is Work-In-Progress and I am planning to add more compilation options

**Dependencies:**
- Python 3.x
- Nuitka compiler (pip3 install nuitka)
- Patchelf (Install it with your package manager)
Optional:
- Wine compatibility layer (winehq.org)
- Ordered Set for optimal performance (pip3 install ordered-set)

### How to use
Options:
- `--onefile`, `--single`, `-o` - Compiles the output to a single file instead of a directory
- `--cwd-runtime`, `--runtime`, `-r` - If your script reads for local files, this is recommended.
- `--windows`, `--wine`, `-w` - Uses the Wine compatibility layer to compile a Microsoft Windows version of the program. (Wine needs to be installed separately. Both python and nuitka have to be installed inside of Wine afterwards.)
- `--debug`, `-d` - Shows nuitka output to the terminal instead of hiding it.

