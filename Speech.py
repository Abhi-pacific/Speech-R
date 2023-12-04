import speech_recognition 
import pyttsx3
# this is an object which make sure to understand what we are saying 
recorgnizer = speech_recognition.Recognizer()

while True:
    try:
        # Using microphone as input here
        with speech_recognition.Microphone() as mic:
            # This line is responcible for to understand when we start and when we stop
            recorgnizer.adjust_for_ambient_noise(mic,duration=0.2)
            print('listening....')
            audio = recorgnizer.listen(mic)

            text = recorgnizer.recognize_google(audio)
            text = text.lower()

            print(f'Recprgnized ... {text}')
    
    except speech_recognition.UnknownValueError:
        recorgnizer  = speech_recognition.Recognizer()
        continue
        