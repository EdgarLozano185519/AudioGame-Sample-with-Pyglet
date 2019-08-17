#Written by Stevo.
import time
def ms():
 return time.time()*1000
class timer:
 def __init__(self):
  self.starttime=ms()
  self.paused_at_time=0
  self.paused=False
 @property
 def elapsed(self):
  if not self.paused:
   return ms() -self.starttime
  else:
   return self.paused_at_time
 def restart(self):
  self.starttime=ms()
 def set_time(self, x):
  """Note, must pass in negatives to add the value. Handy for punishing a player by subtracting the time on the clock. On the other hand, positive values will decrease the timer."""
  self.starttime+=x
 def pause(self):
  if self.paused: return
  self.paused=True
  self.paused_at_time=ms()-self.starttime
 def resume(self):
  if not self.paused: return
  self.paused=False
  self.starttime=ms() -self.paused_at_time