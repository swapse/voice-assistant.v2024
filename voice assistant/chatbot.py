from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os 
import time
from datetime import datetime
import webbrowser

x = sr.Recognizer()
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = x.listen(source)
        voice = ""
    try:
            voice = x.recognize_google(audio, language="en-US")
    except sr.UnknownValueError:
        time.sleep(5)
        speak("İ dont understand")
        exit()
    except sr.RequestError:
        print("system alert")
    return voice




def response(voice):
        # speak("hello user how can i help you?")
        if "hello" in voice:
            speak("hello bro how can i help you") 
        if "wait" in voice:
            speak("ok im waiting 15 seconds")
            time.sleep(15)
            speak("how can i help you")
        if "how are you" in voice:
            speak("İ am fine thanks and you ")
        if "which day" in voice:
            today = time.strftime("%A")
            speak(today)
        if "goodbye" in voice:
            speak("have a nice day")
            exit()
        if "what time" in voice:
            s = datetime.now().strftime("%H:%M")
            speak(s)
        if "open google" in voice:
            speak("opening google what do you want")
            # webbrowser.open("www.google.com")
            search = record()
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            speak("{}opening".format(search))
        if "open spotify" in voice:
            os.startfile(r"C:\Users\axi-s\AppData\Roaming\Spotify\Spotify.exe")
            speak("spotify opening")
        if "open youtube" in voice:
            speak("youtube opening what do you want?")
            search = record()
            url = "https://www.youtube.com/results?search_query={}".format(search)
            webbrowser.get().open(url)
            speak("{}opening".format(search))
        

def speak(string):
    tts = gTTS(text=string, lang="en", slow=False)
    dosya = "konus.mp3"
    tts.save(dosya)
    playsound(dosya)
    os.remove(dosya)





# def testo(wake):
#     if "okay chris" in wake:
#         playsound("DING.mp3")
#         wake = record()
#         if wake != "":
#             voice = wake.lower()
#             print(wake)
#             response(voice)




# def speak(string):
#     tts = gTTS(text=string, lang="en", slow=False)
#     dosya = "konus.mp3"
#     tts.save(dosya)
#     playsound(dosya)
#     os.remove(dosya)


playsound("DING.mp3")
# speak("hello user how can i help you")




while True:
    wake = record()
    if wake != "":
        wake= wake.lower()
        print(wake)
        response(wake)
