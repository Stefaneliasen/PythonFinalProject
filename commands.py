from pynput.keyboard import Key, Controller
import time
import subprocess

keyboard = Controller()

import os

def write_if(words_list):
    if_statement = ""
    words_list = words_list.split()[3:]
    for word in words_list:
        if_statement += " " + word
    print("if" + if_statement + ":")

def write_for(words_list):
    print('for')

def write_code_keywords(x):
    return {
        'if': 'write_if(words_list)',
        'for': 'write_for(words_list)'
    }.get(x, 'none')

def write_code(words_list):
    for word in words_list.split():
            result = write_code_keywords(word)
            if result != 'none':
                exec(result)

def write_keywords(x):
    return {
        'code': 'write_code(words_list)',
    }.get(x, 'none')

def open_visual_studio_code():
    subprocess.Popen([os.environ['VSCODEVARIABLE'] + "\Code.exe"]) 

def open_keywords(x):
    return {
        'code': 'open_visual_studio_code()',
    }.get(x, 'none')

def open(words_list):
    for word in words_list.split():
            result = open_keywords(word)
            if result != 'none':
                exec(result)

# opens a new fan
def new_file():
    keyboard.press(Key.ctrl_l)
    keyboard.press('n')
    keyboard.release('n')
    keyboard.release(Key.ctrl_l)

def save_file(words):
    keyboard.press(Key.ctrl_l)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl_l)

    time.sleep(1)

    words_list = words.split()[1:]
    words_to_write = "".join(words_list).replace(" ", "")

    for letter in words_to_write:
        keyboard.press(letter)
        keyboard.release(letter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def undo():
    keyboard.press(Key.ctrl_l)
    keyboard.press('z')
    keyboard.release('z')
    keyboard.release(Key.ctrl_l)

def write(words):
    words_list = words.split()[1:]
    words_to_write = " ".join(words_list);

    for letter in words_to_write:
        keyboard.press(letter)
        keyboard.release(letter)

def keywords_overall(x):
    return {
        'edit': 'commands.write(words_list["transcription"])',
        'open': 'commands.open(words_list["transcription"])',
        'new' : 'commands.new_file()',
        'save' : 'commands.save_file(words_list["transcription"])',
        'undo' : 'commands.undo()'
    }.get(x, 'none')