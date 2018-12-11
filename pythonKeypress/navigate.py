from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def navigate(key):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(1)

'''
#arrow key up
navigate(Key.up)
#keyboardpress enter
navigate(Key.enter)
#keyboardpress backspace
navigate(Key.backspace) 
#arrow key right
navigate(Key.right)
navigate(Key.left)
navigate(Key.tab)
navigate(Key.down) '''

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


