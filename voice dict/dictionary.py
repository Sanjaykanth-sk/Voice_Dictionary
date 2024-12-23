import pyttsx3
import requests

class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio) 
        engine.runAndWait()

class Finding_word:
    def Dictionary(self):
        speak = Speaking()
        speak.speak("Which word do you want to find the meaning of, Sanjay")
        query = str(input())
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{query}")
        if response.status_code == 200:
            meanings = response.json()[0]['meanings']
            for meaning in meanings:
                definition = meaning['definitions'][0]['definition']
                print(definition)
                speak.speak(f"The meaning is {definition}")
        else:
            speak.speak("Sorry, I couldn't find the meaning of that word.")

if __name__ == '__main__':
    word = Finding_word()
    word.Dictionary()   
