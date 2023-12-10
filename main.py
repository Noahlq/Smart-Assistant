import os
import speech_recognition as sr
from dotenv import load_dotenv

class voice_recognition:

    def listen_portuguese(self):
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Diga algo!')
            self.recognizer.adjust_for_ambient_noise(source)
            self.entrance = self.recognizer.listen(source)
            portuguese_entrance = self.recognizer.recognize_google(self.entrance,language='pt-BR')
            print(portuguese_entrance)

    def listen_english(self):
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Something!')
            self.recognizer.adjust_for_ambient_noise(source)
            self.entrance = self.recognizer.listen(source)
            portuguese_entrance = self.recognizer.recognize_google(self.entrance,language='en-US')
            print(portuguese_entrance)

    def listen_spanish(self):
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Diga algo!')
            self.recognizer.adjust_for_ambient_noise(source)
            self.entrance = self.recognizer.listen(source)
            spanish_entrance = self.recognizer.recognize_google(self.entrance,language='es-ES')
            print(spanish_entrance)


    def main(self):
        os.environ['LANGUAGE'] = 'en-US'
        load_dotenv('./program.env')
        LANGUAGE = os.getenv('LANGUAGE')
        print(LANGUAGE)

        if LANGUAGE == 'pt-BR':
            self.listen_portuguese()
        elif LANGUAGE == 'en-US':
            self.listen_english()
        elif LANGUAGE == 'es-ES':
            self.listen_spanish()
    

            
if __name__ == '__main__':
    recognizer = voice_recognition()
    recognizer.main()