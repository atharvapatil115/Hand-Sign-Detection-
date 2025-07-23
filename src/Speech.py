import pyttsx3 


class text_to_speech():
    def convert_text_to_speech(Text):
        engine = pyttsx3.init()
        engine.setProperty('rate',150)
        engine.say(Text)
        engine.runAndWait()