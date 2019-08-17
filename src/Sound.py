#Written By Carter Tem
#No part of this class was done by me, Amerikranian. This is Carter's work alone.
import math
import sound_lib
from sound_lib import output
from sound_lib import stream
o=output.Output()
class sound():
 def __init__(self):
  self.handle=None
  self.freq=44100
 def load(self,filename=""):
  if self.handle:
   self.close()
  self.handle =stream.FileStream(file=filename)
  self.freq=self.handle.get_frequency()
 def play(self):
  self.handle.looping=False
  self.handle.play()
 def play_wait(self):
  self.handle.looping=False
  self.handle.play_blocking()
 def play_looped(self):
  self.handle.looping=True
  self.looping=True
  self.handle.play()
 def stop(self):
  if self.handle and self.handle.is_playing:
   self.handle.stop()
   self.handle.set_position(0)
 @property
 def volume(self):
  if not self.handle:
   return False
  return round(math.log10(self.handle.volume)*20)
 @volume.setter
 def volume(self,value):
  if not self.handle:
   return False
  self.handle.set_volume(10**(float(value)/20))
 @property
 def pitch(self):
  if not self.handle:
   return False
  return (self.handle.get_frequency()/self.freq)*100
 @pitch.setter
 def pitch(self, value):
  if not self.handle:
   return False
  self.handle.set_frequency((float(value)/100)*self.freq)
 @property
 def pan(self):
  if not self.handle:
   return False
  return self.handle.get_pan()*100
 @pan.setter
 def pan(self, value):
  if not self.handle:
   return False
  self.handle.set_pan(float(value)/100)
 def close(self):
  if self.handle:
   self.handle.free()
   self.__init__()