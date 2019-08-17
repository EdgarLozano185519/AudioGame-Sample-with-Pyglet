from accessible_output2.outputs.auto import Auto
from accessible_output2.outputs import auto
def find_tts():
 screen_readers=["Dolphin","jaws","NVDA","Unnamed Output","VoiceOver","Window-Eyes"]
 outputs=Auto().outputs
 sr=None
 for possible_output in outputs:
  if not possible_output.name in screen_readers: #revirce for sapi
   continue
  if possible_output.is_active():
   sr=possible_output
 return sr
def find_reader():
 screen_readers=["Dolphin","jaws","NVDA","Unnamed Output","VoiceOver","Window-Eyes"]
 outputs=Auto().outputs
 sr=None
 for possible_output in outputs:
  if not possible_output.name in screen_readers: continue
  if possible_output.is_active(): sr=possible_output
 if sr==None:
  for possible_output in outputs:
   if possible_output.name in screen_readers: continue
   if possible_output.is_active(): sr=possible_output
 return sr
def speak(text, interrupt=True):
 global tts
 if not tts or not tts.is_active():
   tts=find_reader()
 tts.speak(text, interrupt)
tts=None