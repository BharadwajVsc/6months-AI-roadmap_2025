import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# recognizer and engine
listening = sr.Recognizer()
engine = pt.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear():
    cmd = ""  # initialize
    try:
        with sr.Microphone() as mic:
            print("taking input....")
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if "ash" in cmd:
                cmd = cmd.replace("ash", "")
                print(cmd)
    except Exception as e:
        print("Error while listening:", e)
    return cmd


def run():
    cmd = hear()
    print("You said:", cmd)
    if "play" in cmd:
        song = cmd.replace("play", "")
        speak("Playing " + song)
        pk.playonyt(song)


run()
