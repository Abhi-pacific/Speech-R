import speech_recognition
import pyttsx3
from bardAi import reply

class Audio:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
        self.engine.setProperty('rate',145)
        self.engine.setProperty('volume',1.0)
        self.playaudio('Welcome to the Lost Ai')
        
    
    def startup(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
                    self.audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(self.audio)
                    text = text.lower()
                    print(f'Recognized... {text}')

                    try:
                        responce = reply(text)
                    except:
                        self.playaudio('please check update your API')
                    
                    if text == 'quit' or text == 'exit':
                        self.playaudio('thanks for using.')
                        break
                    else:
                        self.playaudio(responce)
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                continue

    def playaudio(self,data):
        self.engine.say(data)
        self.engine.runAndWait()


A1 = Audio()
A1.startup()