import speech_recognition as sr

# initialize the recognizer
def speechtotext(str):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recognizing...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        if text != str:
            print("try again")
        else:
            print("Correct answer")