# Nick Roussis
# https://github.com/neek8044

import subprocess
import time
import sys
import os

try:
    from colorama import Fore
except ImportError:
    print("--> Module 'colorama' not found. Run 'pip3 install colorama' to continue.")
    sys.exit()

# Parsing options with argv
extras = []
wine = False
debug = False

if "--onefile" in sys.argv or "-single" in sys.argv or "-o" in sys.argv:
    extras.append("--onefile")
if "--cwd-runtime" in sys.argv or "-runtime" in sys.argv or "-r" in sys.argv:
    extras.append("--file-reference-choice=runtime")
if "--windows" in sys.argv or "-wine" in sys.argv or "-win" in sys.argv or "-w" in sys.argv:
    wine = True
if "--debug" in sys.argv or "-d" in sys.argv:
    debug = True

extras = " ".join(extras)


cwd = os.getcwd()
os.system("") # for an unknown reason colors do not work without an 'os.system' command in specific terminals


# Starting info
print(
    Fore.YELLOW + "NOTE: Linux requires 'patchelf' to be installed. Use 'apt/dnf/yum install patchelf' or 'pacman -S patchelf' if it does not work.\n" + "NOTE: You may want to install 'ordered-set' with 'pip3 install ordered-set' for best compilation performance.\n" + Fore.BLUE + "STATUS: Building standalone directory for main.py" + Fore.RESET
)


# Executing nuitka for compilation
start = time.time()
nuitka = subprocess.Popen(
    str("wine" if wine else "") + f"python3 -m nuitka --standalone {extras} --follow-imports --output-dir=\"{cwd}/output/\" main.py", 
    cwd=cwd, shell=True, 
    stdout=subprocess.DEVNULL if debug == False else subprocess.STDOUT, 
    stderr=subprocess.STDOUT
)


# Terminal animation
anim_chars = ["\\", "|", "/", "-"]

while nuitka.poll() is None:
    for i in anim_chars:
        print("--> Please wait... " + i, end="\r")
        time.sleep(0.1)


end = time.time()
if end - start < 5:
    print(Fore.RED + "ERROR: Could not build main.py.\nWhat to do:\n\t-> Make sure to have a 'main.py' file in this local folder.\n\t-> Make sure to have Nuitka installed in your Python3.\n\t-> If you are using Wine/Windows mode, check if Wine is installed and that you have Python 3 with Nuitka installed in Wine." + Fore.RESET)
else:
    print(Fore.GREEN + "\nSTATUS: Finished building main.py (./output/)" + Fore.RESET)

print("\nFind this project on Github: https://github.com/neek8044/NuitkaBuilder")
input("Press ENTER to exit...\n")

