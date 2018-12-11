import speech_recognition as sr
import subprocess  
import wmi

import commands

from pynput.keyboard import Key, Controller
import time
import subprocess

keyboard = Controller()


def recognize_speech_from_mic(recognizer, microphone, flag=False):
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
    if(flag):
        with microphone as source:
            print('Welcome to our python speech recognition project!')
            recognizer.adjust_for_ambient_noise(source)
            print("Please tell me your name")
            audio = recognizer.listen(source)
            print("Got it! please give me a moment to validate...")
    else:
        with microphone as source:
            print('A moment of silence, please.')
            recognizer.adjust_for_ambient_noise(source)
            print('Talk..')
            audio = recognizer.listen(source)
            print("Validating input...")

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

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    replace_dict = {
        "plus": "+", 
        "minus": "-", 
        "multiply": "*",
        "divide": "/", 
        "equals": "=", 
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
        }

    nameValidation = recognize_speech_from_mic(sr.Recognizer(), sr.Microphone(), True)

    print('Welcome ' + str(nameValidation['transcription']) + ". Lets begin!")

    program_running = True
    while program_running:
        words_list = recognize_speech_from_mic(recognizer, microphone)
        if(str(words_list['transcription']) == 'None'):
            print("You did not say anything. Please tell me what to do")
        else:
            for key, value in replace_dict.items():
                words_list['transcription'] = str(words_list['transcription']).replace(key, value)

            for idx, word in enumerate(words_list['transcription'].split()):
                result = commands.keywords_overall(word)
                if result != 'none':
                    exec(result)
            print('***' + str(words_list['transcription']) + '***')
    
    print('Done')