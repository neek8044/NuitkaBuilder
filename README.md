# NuitkaBuilder

NuitkaBuilder is a python script used in the terminal that runs the appropriate nuitka command needed to compile a script as a standalone program. (similar to the auto-py-to-exe project). It passes the arguments given to nuitka and then compiles the file main.py. Made for Linux and Unix-based systems, but can be used on Windows as well. 

(in the screenshot main.py was nuitkabuilder so it compiled itself)
![screenshot](https://github.com/neek8044/NuitkaBuilder/blob/master/screenshot.png?raw=true)

The project is Work-In-Progress and I am planning to add more compilation options

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
(example shows compilation process of a standalone onefile with fixed runtime directory)
```
python3 ./nuitkabuilder.py -o -r
```
**NOTE: The file meant to be compiled must be named main.py**

After completion, navigate to ./output/main.dist/ and you should see a 'main.bin' file which is what you should execute.

