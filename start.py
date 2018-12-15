import speech_recognition as sr
import subprocess  
import wmi
import time
import subprocess
import remote

from pynput.keyboard import Key, Controller
from whitelist import full_replace_dict

keyboard = Controller()
    
def recognize_speech_from_mic(recognizer, microphone, intro=False):
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

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    if(intro):
        with microphone as source:
            print('-----------------------------------------------------')
            print('| Welcome to our python speech recognition project! |')
            print('-----------------------------------------------------\n')
            recognizer.adjust_for_ambient_noise(source, 0.5)
            print("\U0001f916  : Please tell me your name?")
            audio = recognizer.listen(source)
    else:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print('\U0001f916  : Please tell me something do to')
            audio = recognizer.listen(source)

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

def pickMicrophone():
    print("Please tell me what microphone you would like to use: ")
    print("------------------------------------------------------")
    for idx, option in enumerate(sr.Microphone.list_microphone_names()):
        print(str(idx) + ": " + option)
    print("------------------------------------------------------")
    result = input("Please enter a number: ")
    print("\n")
    if(int(result) > len(sr.Microphone.list_microphone_names())):
        pickMicrophone()
    else:
        print("You have chosen option number: " + result + "\n")
        return sr.Microphone(device_index=int(result))


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = pickMicrophone()
    nameValidation = recognize_speech_from_mic(sr.Recognizer(), sr.Microphone(), True)

    print('\U0001f916  : Welcome ' + str(nameValidation['transcription']) + ".")

    program_running = True
    while program_running:
        words_list = recognize_speech_from_mic(recognizer, microphone)
        if(str(words_list['transcription']) == 'None'):
            print("Hello")
        else:
            for key, value in full_replace_dict.items():
                words_list['transcription'] = str(words_list['transcription']).replace(key, value)

            for idx, word in enumerate(words_list['transcription'].split()):
                result = remote.keywords_overall(word)
                if result != 'none':
                    exec(result)
            print('\U0001f916  : ' + str(words_list['transcription']))

    print("------------")
    print('| Goodbye! |')
    print("------------")