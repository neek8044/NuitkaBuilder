# Nick Roussis
# https://github.com/neek8044

import subprocess
import time
import sys
import os

try:
    from colorama import Fore, Style
except ImportError:
    if input("--> Module 'colorama' not found. Run 'pip3 install colorama' now? [Y/n] : ").lower() == "n":
        print("Aborted.")
        sys.exit()
    else:
        os.system("pip3 install --upgrade colorama")
        print("Done, please rerun.")
        sys.exit()


# Parsing options with argv
extras = []
wine = False
debug = False

if "--onefile" in sys.argv or "--single" in sys.argv or "-o" in sys.argv:
    extras.append("--onefile")
if "--cwd-runtime" in sys.argv or "--runtime" in sys.argv or "-r" in sys.argv:
    extras.append("--file-reference-choice=runtime")
if "--windows" in sys.argv or "--wine" in sys.argv or "-w" in sys.argv:
    wine = True
if "--debug" in sys.argv or "-d" in sys.argv:
    debug = True

extras = " ".join(extras)


cwd = os.getcwd()
os.system("") # for an unknown reason colors do not work without an 'os.system' command in specific terminals


# Starting info
print(
    "\nReport issues on Github: https://github.com/neek8044/NuitkaBuilder\n", 
    Fore.YELLOW + "\nNOTE: Linux requires 'patchelf' to be installed. You should install it with your package manager to use this program.\nYou may want to install 'ordered-set' with 'pip3 install ordered-set' for best compilation performance.",  
    Fore.BLUE + "\n--> Building standalone for main.py" + Fore.RESET
)


# Executing nuitka for compilation
start = time.time()
full_command = str("wine " if wine else "") + f"python{'' if wine else '3'} -m nuitka --standalone {extras} --follow-imports --output-dir=\"{cwd}/output/\" main.py"

print(Fore.MAGENTA + "Executing: " + full_command + Fore.RESET) if debug else ...

nuitka = subprocess.Popen(
    full_command, 
    cwd=cwd, shell=True, 
    stdout=subprocess.DEVNULL if debug == False else None, 
    stderr=subprocess.STDOUT
)


# Terminal animation
anim_chars = ["\\", "|", "/", "-"]

while nuitka.poll() is None:
    for i in anim_chars:
        print("--> Please wait, compiling... " + i, " "*10 if wine else "", end="\r")
        time.sleep(0.1)


end = time.time()
timeout = 3

# Code cannot be compiled as quickly as the timeout set, thus it must have failed. (might improve in the future)
if end - start < timeout:
    print(Fore.RED + "ERROR: Seems like an issue was encountered while building main.py.\nWhat to do:\n\t-> Make sure to have a 'main.py' file in this local folder.\n\t-> Make sure to have Nuitka installed in your Python3.\n\t-> If you are using Wine/Windows mode, check if Wine is installed and that you have Python 3 with Nuitka installed in Wine." + Fore.RESET)
else:
    print(Fore.GREEN + "\nFinished building main.py (./output/main.dist/)" + Fore.RESET)


input("\nPress ENTER to exit...\n")
sys.exit()

