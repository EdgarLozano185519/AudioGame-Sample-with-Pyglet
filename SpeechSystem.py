import ctypes

class SpeechSystem:

    # This function prepares for screen reader detection
    # If a number greater than 0 is passed, SAPI will be used regardless of screen reader
    def __init__(self, num):
        self.mydll = ctypes.cdll.LoadLibrary("Tolk.dll")
        if num > 0:
            self.mydll.Tolk_TrySAPI()
            self.mydll.Tolk_PreferSAPI(True)
        self.mydll.Tolk_Load()

    # This is the function to speak a string
    # Includes numbers as well
    def speak(self,mystring):
        self.mydll.Tolk_Output(str(mystring))

    # Call this after finishing with the tolk library
    def unload(self):
        self.mydll.Tolk_Unload()
