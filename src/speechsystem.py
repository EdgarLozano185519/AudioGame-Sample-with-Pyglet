import speech


class SpeechSystem:
    def __init__(self):
        self.interupt_speaking = True  # Used for the messages in speak function

    # This is the function to speak a string
    # Includes numbers as well
    def speak(self, mystring):
        speech.speak(str(mystring), self.interupt_speaking)
