import speech_recognition as sr
import subprocess  
import wmi

#Python creates keyboeard event
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        print('A moment of silence, please.')
        recognizer.adjust_for_ambient_noise(source)
        print('Set minimum energy threshold to ' + str(recognizer.energy_threshold))
        print('Talk..')
        audio = recognizer.listen(source)
        print('Got it! Now to recognize it...')

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

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

def write(words_list):
    for word in words_list.split():
            result = write_keywords(word)
            if result != 'none':
                exec(result)

def open_visual_studio_code():
    subprocess.Popen([r"C:\Users\Elias\AppData\Local\Programs\Microsoft VS Code\Code.exe"]) 

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

    words_list = words.split()[2:]
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
    words_list = words.split()[2:]
    words_to_write = "".join(words_list).replace(" ", "")

    for letter in words_to_write:
        keyboard.press(letter)
        keyboard.release(letter)

def keywords_overall(x):
    tmp = None
    return {
        'write': 'write(words_list["transcription"])',
        'open': 'open(words_list["transcription"])',
        'new' : 'new_file()',
        'save' : 'save_file(words_list["transcription"])',
        'undo' : 'undo()',
        'write': 'write(words_list["transcription"])'
    }.get(x, 'none')

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    replace_dict = {
        "plus": "+", 
        "minus": "-", 
        "multiply": "*",
        "divide": "/", 
        "equals": "=", 
        "is": "if", 
        "underscore": "_", 
        "colon": ":", 
        "true": "True", 
        "false": "False", 
        "greater than": ">",
        "is greater than": ">",
        "if greater than": ">",
        "dot": ".",
        "python": "py",
        "Python": "py",
        "ride": "write"
        }

    program_running = True
    while program_running:
        words_list = recognize_speech_from_mic(recognizer, microphone)
        words_list['transcription'].lower()
            
        for key, value in replace_dict.items():
            words_list['transcription'] = str(words_list['transcription']).replace(key, value)

        for word in words_list['transcription'].split():
            result = keywords_overall(word)
            if result != 'none':
                exec(result)


        program_running = False
        print('***' + str(words_list['transcription']) + '***')

    print('Done')