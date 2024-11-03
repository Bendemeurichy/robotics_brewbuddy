import requests
import json
import random

class Assistant:
    def __init__(self, settings):
        self.settings = settings

    def __random(self, array):
        return random.choice(array)

    def say(self, message, options={}, cb=None):
        speed = options.get('speed', self.settings.get('voice_speed', 0.5125))
        lang = options.get('lang', self.settings.get('voice_lang', 'en-US'))
        pitch = options.get('pitch', self.settings.get('voice_pitch', 1))
        demon_voice = self.settings.get('demonVoice', True)

        if isinstance(message, str) and len(message) > 0 and demon_voice:
            try:
                url = f"https://www.google.com/speech-api/v2/synthesize?enc=mpeg&client=chromium&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&text={message}&lang={lang}&speed={speed}&pitch={pitch}"
                response = requests.get(url)
                if response.status_code == 200:
                    with open('output.mp3', 'wb') as f:
                        f.write(response.content)
                    # Play the audio file using a suitable library
                    if cb:
                        cb('output.mp3')
            except Exception as e:
                print(f"Error: {e}")

    def welcome(self):
        self.say(self.greeting + ", " + self.human)


    def updateSettings(self, settings):
        self.settings = settings

    def happy(self):
        self.say("I'm happy")

    @property
    def greeting(self):
        return self.__random(sentences['human'])

    @property
    def greeting(self):
        return self.__random(sentences['greeting'])



if __name__ == "__main__":
    sentences = {
        "greeting": ["Hello", "Hi"],
        "human": ["Human"]
    }
    settings = {
        "voice_speed": 0.5125,
        "voice_lang": "en-US",
        "voice_pitch": 1,
        "demonVoice": True
    }
    assistant = Assistant(settings)
    assistant.welcome()
