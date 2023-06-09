# NuitkaBuilder

NuitkaBuilder is a python script used in the terminal that runs the appropriate nuitka command needed to compile a script as a standalone program. (similar to the auto-py-to-exe project). It passes the arguments given to nuitka and then compiles the file main.py. Made for Linux and Unix-based systems, but can be used on Windows as well. 

![screenshot](https://github.com/neek8044/NuitkaBuilder/blob/master/screenshot.png?raw=true)
*(in the screenshot main.py was nuitkabuilder so it compiled itself)*

---

### Why not just use Nuitka?
#### Better Terminal UI
  - More readable
  - Colored
  - Less cluttered

#### PyInstaller-like arguments
  - For example, instead of using `--file-reference-choice=runtime`, you can use `--cwd-runtime`

#### Predifined options and shortcuts

  Here is a comparison of both of the commands:
  - Nuitka command: 
    ```
    python3 -m nuitka --standalone --follow-imports --output-dir="./output/" --onefile --file-reference-choice=runtime main.py
    ```
  - NuitkaBuilder: 
    ```
    python3 nuitkabuilder.py -o -r
    ```

The project is Work-In-Progress and more compilation options will be added.

---

### Dependencies
- Python 3.7+
- Nuitka compiler (pip3 install nuitka)
- Patchelf (Install it with your package manager. Not needed by Windows users)

#### Optional dependencies
- Wine compatibility layer when using `--windows` argument ([winehq.org](https://winehq.org/). Not needed by Windows users)
- Ordered Set for optimal performance (pip3 install ordered-set)

---

### Options
- `--onefile`, `--single`, `-o` - Compiles the output to a single file instead of a directory
- `--cwd-runtime`, `--runtime`, `-r` - Sets working dir to the local dir (where the file is ran from) upon execution. If your script reads local files, this is recommended.
- `--windows`, `--wine`, `-w` - Uses the Wine compatibility layer to compile a Microsoft Windows version of the program. (Wine needs to be installed separately. Both python, nuitka, and nuitka dependencies for Windows have to be installed inside of Wine afterwards.)
- `--debug`, `-d` - Shows command to be executed and nuitka output to the terminal instead of hiding it. (used to track errors, obviously)

---

### Usage
(example shows compilation process of a standalone onefile with fixed runtime directory)
```
python3 ./nuitkabuilder.py -o -r
```
**NOTE: The file meant to be compiled _must_ be named main.py**

After completion, navigate to ./output/main.dist/ and you should see a 'main.bin' file which is what you should execute with the rest of the files shipped together. If you used the onefile option, go to ./output/ and there should be a standalone main.bin file (you can delete the rest in this case).
