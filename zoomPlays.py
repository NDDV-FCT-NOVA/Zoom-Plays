from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import keypresser
import keyholder
import threading
import keypresser2

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
SPACE = 0x39

# Capabilities
capabilities = DesiredCapabilities.FIREFOX
capabilities['loggingPrefs'] = { 'browser':'ALL'}

driver = webdriver.Firefox(desired_capabilities=capabilities)
driver.get("https://zoom.us/j/98469567104?pwd=R2FhVGVSU1drY0ZtL0JIOHU1SUNZUT09")

meetingPw = 'Tt0uY5'
    
c = ''

def stringToKeyCode(s):
    switcher = {
        'w': W,
        'up': W,
        'cima': W,
        'a': A,
        'left': A,
        'esquerda': A,
        's': S,
        'down': S,
        'baixo': S, 
        'd': D,
        'right': D,
        'direita': D,
        'dispara': SPACE,
        'disparar': SPACE,
        'shoot': SPACE
    }
    return switcher.get(s, 0x00)

def printThing():
    threading.Timer(1.0, printThing).start()
    print("-----------------------")
    elementName = driver.find_elements_by_class_name("chat-item__chat-info-msg")
    # print(elementName[len(elementName)-1].text)
    cz = elementName[-1].text.split("\n")
    c = cz[-1].strip(' \t\n\r').lower()
    print(c)
    keyCode = stringToKeyCode(c)
    keypresser2.PressAndHoldKey(keyCode, 0.3)

printThing()

