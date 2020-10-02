import os
import sys
from cx_Freeze import setup, Executable
import sys
sys.argv.append("build")
try: 
    currentdir = os.path.dirname(os.path.realpath(__file__))
    main = os.path.join(currentdir, "main.py")
    rock = os.path.join(currentdir, "rock.png")
    paper = os.path.join(currentdir, "paper.png")
    scissor = os.path.join(currentdir, "scissor.png")
    base = None    
    if sys.platform=='win32':
        base = "Win32GUI"
    executables = [Executable(main, base=base)]

    setup(name="RPS", options = {"build.exe" : {"packages":["tkinter", "PIL", "os", "random"], "include_files":[rock, paper, scissor]}}, version="1.0", executables=executables)
except Exception as e:
    print("oops ",e)