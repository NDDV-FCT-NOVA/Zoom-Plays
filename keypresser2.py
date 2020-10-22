# Written by DougDoug (DougDoug on Youtube, DougDougW on Twitch)

# Hello!
# This file contains the main logic to process Twitch chat and convert it to game commands.
# All sections that you need to update are labeled with a "TODO" comment.
# The source code primarily comes from:
    # Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    # PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/

# There are 2 other files needed to run this code:
    # TwitchPlays_AccountInfo.py is where you put your Twitch username and OAuth token. This is to keep your account details separated from the main source code.
    # TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

# Disclaimer: 
    # This code is NOT optimized or well-organized. I am not a Python programmer.
    # I created a simple version that works quickly, and I'm sharing it for educational purposes.

###############################################
# Import and define our functions / key codes to send key commands

# General imports
import time
import subprocess
import ctypes
import random
import string

# Controller imports
import pyautogui
import pynput
from pynput.mouse import Button, Controller

SendInput = ctypes.windll.user32.SendInput

# KEY PRESS NOTES
# The standard "Twitch Plays" tutorial key commands do NOT work in DirectX games (they only work in general windows applications)
# Instead, we use DirectX key codes and input functions below.
# This DirectX code is partially sourced from: https://stackoverflow.com/questions/53643273/how-to-keep-pynput-and-ctypes-from-clashing

# Presses and permanently holds down a keyboard key
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Releases a keyboard key if it is currently pressed down
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Helper function. Holds down a key for the specified number of seconds, then releases it.
def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)

# Mouse Controller, using pynput
    # pynput.mouse functions are found at: https://pypi.org/project/pynput/
    # NOTE: pyautogui's click() function permanently holds down in DirectX, so I used pynput instead for mouse instead.
mouse = Controller()

###############################################
# DIRECTX KEY CODES
# These codes identify each key on the keyboard.
# Note that DirectX's key codes (or "scan codes") are NOT the same as Windows virtual hex key codes. 
#   DirectX codes are found at: https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
ESC = 0x01
ONE = 0x02
TWO = 0x03
THREE = 0x04
FOUR = 0x05
FIVE = 0x06
SIX = 0x07
SEVEN = 0x08
EIGHT = 0x09
NINE = 0x0A
ZERO = 0x0B
MINUS = 0x0C
EQUALS = 0x0D
BACKSPACE = 0x0E
SEMICOLON = 0x27
TAB = 0x0F
CAPS = 0x3A
ENTER = 0x1C
LEFT_CONTROL = 0x1D
LEFT_ALT = 0x38
LEFT_SHIFT = 0x2A
SPACE = 0x39
DELETE = 0x53
COMMA = 0x33
PERIOD = 0x34
BACKSLASH = 0x35
NUMPAD_0 = 0x52
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49
NUMPAD_PLUS = 0x4E
NUMPAD_MINUS = 0x4A
LEFT_ARROW = 0xCB
RIGHT_ARROW = 0xCD
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
LEFT_MOUSE = 0x100
RIGHT_MOUSE = 0x101
MIDDLE_MOUSE = 0x102
MOUSE3 = 0x103
MOUSE4 = 0x104
MOUSE5 = 0x105
MOUSE6 = 0x106
MOUSE7 = 0x107
MOUSE_WHEEL_UP = 0x108
MOUSE_WHEEL_DOWN = 0x109
########################################################