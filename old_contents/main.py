import speech_recognition as sr
import subprocess  
import wmi

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
        #print('Set minimum energy threshold to ' + str(recognizer.energy_threshold))
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

def show_all_processes():
    # Prints all open processes on your windows machine
    c = wmi.WMI ()
    for process in c.Win32_Process ():
        print (process.ProcessId, process.Name)

def open_visual_studio_code():
    # opens visual studio code, on my machine(Elias)
    subprocess.Popen([r"C:\Users\Elias\AppData\Local\Programs\Microsoft VS Code\Code.exe"]) 

def write(write_this):
    f = open("edit_this_file.py", "a+")
    f.write(write_this)

# Basic needs more improvements
def keywords_overall(x):
    return {
        'show': 'show_all_processes()',
        'open': 'open_visual_studio_code()',
        'edit': 'write("hello world")',
    }.get(x, 'none')

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    program_running = True
    while program_running:
        words_list = recognize_speech_from_mic(recognizer, microphone)
        for word in words_list['transcription'].split():
            result = keywords_overall(word)
            if result != 'none':
                exec(result)
                
        print('*** ' + words_list['transcription'] + ' ***')

    print('Done')