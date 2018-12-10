from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

'''keyboard.press(Key.ctrl_l)
keyboard.press('n')
keyboard.release('n')
keyboard.release(Key.ctrl_l)'''

time.sleep(1)

'''keyboard.press(Key.ctrl_l)
keyboard.press('s')
keyboard.release('s')
keyboard.release(Key.ctrl_l)'''

time.sleep(1)

my_string = "test . p y".replace(" ", "")
char_list = list(my_string)

for letter in char_list:
    keyboard.press(letter)
    keyboard.release(letter)





