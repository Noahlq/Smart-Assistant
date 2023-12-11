import os
import speech_recognition as sr
from dotenv import load_dotenv
from entrances import entrances

class voice_recognition:
    
    
    def listen_portuguese(self):
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            print('Diga Algo!')
            recognize.adjust_for_ambient_noise(source)
            entrance = recognize.listen(source)
            portuguese_entrance = recognize.recognize_google(entrance,language='pt-BR')
            entrance = entrances()
            entrance.portuguese_return_for_entrance(portuguese_entrance)

    def listen_english(self):
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Something!')
            recognize.adjust_for_ambient_noise(source)
            entrance = recognize.listen(source)
            english_entrance = recognize.recognize_google(entrance,language='en-US')
            print(english_entrance)

    def listen_spanish(self):
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            print('Di Algo!')
            recognize.adjust_for_ambient_noise(source)
            entrance = recognize.listen(source)
            spanish_entrance = recognize.recognize_google(entrance,language='es-ES')
            print(spanish_entrance)


    def main(self):
        os.environ['LANGUAGE'] = 'pt-BR'
        load_dotenv('./program.env')
        LANGUAGE = os.getenv('LANGUAGE')

        if LANGUAGE == 'pt-BR':
            self.listen_portuguese()
        elif LANGUAGE == 'en-US':
            self.listen_english()
        elif LANGUAGE == 'es-ES':
            self.listen_spanish()
    

            
if __name__ == '__main__':
    recognizer = voice_recognition()
    recognizer.main()