# NuitkaBuilder

NuitkaBuilder is a python script used in the terminal that runs the appropriate nuitka command needed to compile a script as a standalone program. (similar to the auto-py-to-exe project). Made for Linux and Unix-based systems, but can be used on Windows as well.

The project is Work-In-Progress and I am planning to add more compilation options

![screenshot](https://github.com/neek8044/NuitkaBuilder/blob/main/screenshot.png?raw=true)

#### Dependencies
- Python 3.x
- Nuitka compiler (pip3 install nuitka)
- Patchelf (Install it with your package manager)

#### Optional dependencies
- Wine compatibility layer (winehq.org)
- Ordered Set for optimal performance (pip3 install ordered-set)

### Options
- `--onefile`, `--single`, `-o` - Compiles the output to a single file instead of a directory
- `--cwd-runtime`, `--runtime`, `-r` - Sets working dir to the local dir (where the file is ran from) upon execution. If your script reads local files, this is recommended.
- `--windows`, `--wine`, `-w` - Uses the Wine compatibility layer to compile a Microsoft Windows version of the program. (Wine needs to be installed separately. Both python and nuitka have to be installed inside of Wine afterwards.)
- `--debug`, `-d` - Shows nuitka output to the terminal instead of hiding it. (used to track errors, obviously)

### Usage
**NOTE: The main file name to compile MUST be main.py**
(example shows compilation process of a standalone onefile with fixed runtime directory)
```
chmod +x ./nuitkabuilder.bin && ./nuitkabuilder.bin -o -r
```
or
```
python3 ./nuitkabuilder.py -o -r
```

After completion, navigate to ./output/main.dist/ and you should see a 'main.bin' which is what you should execute.

