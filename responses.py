import pyttsx3

class Response:
    def response(self, response):
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()