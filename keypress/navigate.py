from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def navigate(key):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(0.01)

# Regular movement
def up():
    navigate(Key.up)

def down():
    navigate(Key.down)

def left():
    navigate(Key.left)

def right():
    navigate(Key.right)

# utility 

def enter():
    navigate(Key.enter)

def backspace():
    navigate(Key.backspace)

def tab():
    navigate(Key.tab)


def activate_mark():
    #markere tekst, start fra højre mod venstre
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift_l)

def copy():
    keyboard.release(Key.ctrl_l)   
    keyboard.release(Key.shift_l)
    keyboard.press(Key.ctrl_l)   
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl_l)

def paste():
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')

def select_explorer():
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.press('e')
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release('e')

# run code, need extension installed(Code Runner)
def runcode():
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.alt_l)
    keyboard.press('n')

    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.alt_l)
    keyboard.release('n')

#move current line up or down.
def moveline(key):
    keyboard.press(Key.alt_l)
    keyboard.press(key)
    keyboard.release(Key.alt_l)
    keyboard.release(key)

def moveline_up():
    moveline(Key.up)
    
def moveline_down():
    moveline(Key.down)
