from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

keyboard.press(Key.ctrl_l)
keyboard.press('f')
keyboard.release('f')
keyboard.release(Key.ctrl_l)

time.sleep(1)

my_string = "test123".replace(" ", "")

char_list = list(my_string)

for letter in char_list:
    keyboard.press(letter)
    keyboard.release(letter)




