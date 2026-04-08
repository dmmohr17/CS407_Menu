**How to Run**
* Requires download of Python and Pygame. Our group ran the project using a virtual environment on VSCode (but not required)
* [main](main.py) runs the game
* Button commands are displayed at the bottom of the screen. Use WASD as player one to navigate the menu, and the arrows as player two

To run this program on windows, simply use the following commmand from the directory on level with `main.py`.
```bash
python main.py
python.exe main.py # In case of issues on Windows, use this version
```
To run this program on linux WSL (Ubuntu), navigate to `main.py` and press `ctrl` + `f5`.

***NOTE***: This program requires little in terms of hardware, but is expected to have a working keyboard with all basic keys, numpad not required. 

**Requirements**
Required packages to run this program include `Numpy` and `Pygame`, as well as python. 

To verify your python version, please use the following.

```bash
python --version 
python.exe --version # For Windows
python3.exe --version # For Python 3 on windows, only needed if python.exe defaults to version 2 or older, or python 3 is not installed.
```

As this program is python based, it can run on any platform with python installed, including windows, MacOS, and Linux kernels. 

To install packages, milage my vary by OS. The command used should (and likely will) take the form of the following:

```bash
pip install Numpy
pip install Pygame
```

**TODO**
* Add sounds - character and stage names
* Add ability to backtrack through selections (deselect character without going back home)
* Polish all screens - colors, text, etc.
