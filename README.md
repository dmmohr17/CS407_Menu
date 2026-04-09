**How to Download and Install (Two Methods)**

**METHOD 1:**
* Go to dist folder and download and run the "main.exe" file

*OR*

**METHOD 2**
* Requires download of Python and Pygame. Our group ran the project using a virtual environment on VSCode (but not required)
* Download this repo and initialize all submodules:
```bash
  git clone https://github.com/dmmohr17/CS407_Menu.git
  cd CS407_Menu
  git submodule update --init --recursive
```

* Replicate environment using `venv`:
1. Install venv: `python -m venv venv`
2. Spin up virtual environment:

```bash
python3 -m venv venv         # create virtual env
source venv/bin/activate     # activate
pip install -r requirements.txt  # install dependencies
```

**How to Run**
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
