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

'''
def marker():
    #markere tekst, start fra højre mod venstre
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift_l)
    keyboard.press(Key.left)
    
    keyboard.release(Key.Key.ctrl_l)
    keyboard.release(Key.shift)
    keyboard.release(Key.left)
    
    
#Copypasta
keyboard.press(Key.ctrl_l)
keyboard.press('c')
    


copypasta()
'''

