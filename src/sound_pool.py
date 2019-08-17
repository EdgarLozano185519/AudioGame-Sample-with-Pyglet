#Credit to Carter Tem who wrote the fixed Sound positioning functions and the actual Sound class.
#Without him, we would have no Sound pool at all.
#Please note: The conversion was done with the 3D Sound_pool by Sam Tupy.
#The package can be found at the following URL: http://www.samtupy.com/dev/simple_3d_Sound_pool.zip
#I did not create any part of this project, I simply acted as a translator of sorts.
#If you wish to change any of the code below for optimizations and such feel free to do so, just let me, Amerikranian know.
import Sound, Sound_positioning

class Sound_pool_item:

 def __init__(self, **kwargbs):
  self.handle=Sound.sound()
  self.filename= kwargbs.get("filename")
  self.x=kwargbs.get("x", 0)
  self.y=kwargbs.get("y", 0)
  self.z=kwargbs.get("z", 0)
  self.looping=kwargbs.get("looping", 0)
  self.pan_step=kwargbs.get("pan_step", 0)
  self.volume_step=kwargbs.get("volume_step", 0)
  self.behind_pitch_decrease=kwargbs.get("behind_pitch_decrease", 0)
  self.start_pan=kwargbs.get("start_pan", 0)
  self.start_volume=kwargbs.get("start_volume", 0)
  self.start_pitch=kwargbs.get("start_pitch", 0)
  self.start_offset=kwargbs.get("start_offset",0)
  self.upper_range=kwargbs.get("upper_range", 0)
  self.lower_range=kwargbs.get("lower_range", 0)
  self.left_range=kwargbs.get("left_range", 0)
  self.right_range=kwargbs.get("right_range", 0)
  self.backward_range=kwargbs.get("backward_range", 0)
  self.forward_range=kwargbs.get("forward_range", 0)
  self.looping=kwargbs.get("looping", False)
  self.is_3d=kwargbs.get("is_3d", False)
  self.stationary=kwargbs.get("stationary", False)
  self.persistent=kwargbs.get("persistent", False)
  self.paused=kwargbs.get("paused", False)

 def reset(self,pack=""):
  self.__init__()

 def update(self,listener_x,listener_y,listener_z,max_distance):
  if max_distance>0 and self.looping:
   total_distance=self.get_total_distance(listener_x,listener_y,listener_z)
   if total_distance>max_distance and self.handle.handle!=None:
    self.handle.close()
    return
   if total_distance<=max_distance and self.handle.handle==None:
    try:
     self.handle.load(self.filename)
    except:
     pass
     return
    if self.handle.handle.position>0: self.handle.handle.position=self.start_offset
    self.update_listener_position(listener_x,listener_y,listener_z)
    if not self.paused: self.handle.play_looped()
    return
  self.update_listener_position(listener_x,listener_y,listener_z)

 def update_listener_position(self,listener_x,listener_y,listener_z):
  if self.handle.handle==None: return
  if self.stationary: return
  delta_left=self.x-self.left_range
  delta_right=self.x+self.right_range
  delta_backward=self.y-self.backward_range
  delta_forward=self.y+self.forward_range
  delta_upper=self.z+self.upper_range
  delta_lower=self.z-self.lower_range
  True_x=listener_x
  True_y=listener_y
  True_z=listener_z
  if not self.is_3d:
   if listener_x>=delta_left and listener_x<=delta_right:
    Sound_positioning.position_sound_custom_1d(self.handle, listener_x, listener_x, self.pan_step, self.volume_step, self.start_pan, self.start_volume)
    return
   if listener_x<delta_left: Sound_positioning.position_sound_custom_1d(self.handle, listener_x, delta_left, self.pan_step, self.volume_step, self.start_pan, self.start_volume)
   if listener_x>delta_right: Sound_positioning.position_sound_custom_1d(self.handle, listener_x, delta_right, self.pan_step, self.volume_step, self.start_pan, self.start_volume)
   return
  if listener_x<delta_left: True_x=delta_left
  elif listener_x>delta_right: True_x=delta_right
  if listener_y<delta_backward: True_y=delta_backward
  elif listener_y>delta_forward: True_y=delta_forward
  if listener_z<delta_lower: True_z=delta_lower
  elif listener_z>delta_upper: True_z=delta_upper 
  Sound_positioning.position_sound_custom_3d(self.handle, listener_x, listener_y, listener_z, True_x, True_y, True_z,0,self.pan_step, self.volume_step, self.behind_pitch_decrease, self.start_pan, self.start_volume, self.start_pitch,False)

 def get_total_distance(self,listener_x,listener_y,listener_z):
  if self.stationary: return 0
  delta_left=self.x-self.left_range
  delta_right=self.x+self.right_range
  delta_backward=self.y-self.backward_range
  delta_forward=self.y+self.forward_range
  delta_lower=self.z-self.lower_range
  delta_upper=self.z+self.upper_range
  True_x=listener_x
  True_y=listener_y
  True_z=listener_z
  distance=0
  if not self.is_3d:
   if listener_x>=delta_left and listener_x<=delta_right: return distance
   if listener_x<delta_left: distance=delta_left-listener_x
   if listener_x>delta_right: distance=listener_x-delta_right
   return distance
  if listener_x<delta_left: True_x=delta_left
  elif listener_x>delta_right: True_x=delta_right
  if listener_y<delta_backward: True_y=delta_backward
  elif listener_y>delta_forward: True_y=delta_forward
  if listener_z<delta_lower: True_z=delta_lower
  elif listener_z>delta_upper: True_z=delta_upper
  if  listener_x<True_x: distance=(True_x-listener_x)
  if listener_x>True_x: distance=(listener_x-True_x)
  if listener_y<True_y: distance+=(True_y-listener_y)
  if listener_y>True_y: distance+=(listener_y-True_y)
  if listener_z<True_z: distance+=(True_z-listener_z)
  if listener_z>True_z: distance+=(listener_z-True_z)
  return distance

class Sound_pool:

 def __init__(self):
  self.items=[] #The placeholder for the items
  self.max_distance=40 #The max distance the Sounds should play at
  self.pan_step=20.0
  self.volume_step=2.0
  self.behind_pitch_decrease=4.0
  self.last_listener_x=0
  self.last_listener_y=0
  self.last_listener_z=0
  self.clean_frequency=3 #How often the pool should be cleaned
  self.packname = ""
  self.ext = ""

 def play_stationary(self,filename,looping,persistent=False):
  return self.play_stationary_extended(filename, looping, 0, 0, 0, 100, persistent)

 def play_stationary_extended(self,filename, looping, offset, start_pan,start_volume,start_pitch,persistent=False):
  self.clean_frequency-=1
  if self.clean_frequency<=0: self.clean_unused()
  s=Sound_pool_item(filename=filename,looping=looping,start_offset=offset,start_pan=start_pan,start_volume=start_volume,start_pitch=start_pitch,persistent=persistent,stationary=True)
  try:
   s.handle.load(self.packname+filename + self.ext)
  except:
   s.reset()
   return -1 
  if s.start_offset>0: s.handle.position=s.start_offset
  if start_pan!=0.0: s.handle.pan=start_pan
  if start_volume<0.0: s.handle.volume=start_volume
  s.handle.pitch=start_pitch
  if looping: s.handle.play_looped()
  else: s.handle.play()
  self.items.append(s)
  return s

 def play_1d(self,filename,listener_x,Sound_x,looping,persistent=False):
  return self.play_extended_1d(filename, listener_x, Sound_x, 0, 0, looping, 0, 0, 0, 100, persistent)

 def play_extended_1d(self, filename, listener_x, Sound_x, left_range, right_range, looping, offset = 0.0, start_pan = 0.0, start_volume = 0.0, start_pitch = 100.0, persistent=False):
  self.clean_frequency-=1
  if self.clean_frequency<=0: self.clean_unused()
  s=Sound_pool_item(filename=filename,x=Sound_x,looping=looping,stationary=True,start_pan=start_pan,start_volume=start_volume,start_pitch=start_pitch,persistent=persistent,pan_step=self.pan_step,volume_step=self.volume_step,behind_pitch_decrease=0.0,left_range=left_range,right_range=right_range,backward_range=0,forward_range=0,is_3d=False,start_offset=offset)
  if self.max_distance>0 and s.get_total_distance(listener_x, 0, 0)>self.max_distance:
   if not looping:
    s.reset()
    return -2
   else:
    self.last_listener_x=listener_x
    s.handle.pitch=start_pitch
    s.update(self.listener_x, 0, 0, self.max_distance)
    self.items.append(s)
    return s
  try:
   s.handle.load(self.packname+filename + self.ext)
  except:
   s.reset()
   return -1
  if s.start_offset>0: s.handle.position=s.start_offset
  s.handle.pitch=start_pitch
  self.last_listener_x=listener_x
  s.update(listener_x, 0, 0, self.max_distance)
  if looping: s.handle.play_looped()
  else: s.handle.play()
  self.items.append(s)
  return s

 def play_2d(self,filename, listener_x, listener_y, Sound_x,   Sound_y,   looping,   persistent=False):
  return self.play_extended_2d(filename, listener_x, listener_y, Sound_x, Sound_y, 0, 0, 0, 0, looping, 0, 0, 0, 100, persistent) 

 def play_extended_2d(self,filename,   listener_x,   listener_y,   Sound_x,   Sound_y,   left_range,   right_range,   backward_range,   forward_range,   looping,   offset = 0.0, start_pan = 0.0, start_volume = 0.0, start_pitch = 100, persistent=False):
  self.clean_frequency-=1
  if self.clean_frequency<=0: self.clean_unused()
  s=Sound_pool_item(filename=filename,x=Sound_x,y=Sound_y,looping=looping,start_pan=start_pan,start_volume=start_volume,start_pitch=start_pitch,persistent=persistent,pan_step=self.pan_step,volume_step=self.volume_step,behind_pitch_decrease=self.behind_pitch_decrease,left_range=left_range,right_range=right_range,backward_range=backward_range,forward_range=forward_range,is_3d=True,start_offset=offset)
  if self.max_distance>0 and s.get_total_distance(listener_x, listener_y, 0)>self.max_distance:
   if looping==False:
    s.reset() 
    return -2 
   else:
    self.last_listener_x=listener_x 
    self.last_listener_y=listener_y 
    s.update(listener_x, listener_y, 0, self.max_distance) 
    self.items.append(s)
    return s
  try:
   s.handle.load(self.packname+filename + self.ext)
  except:
   s.reset() 
   return -1 
  if s.start_offset>0: s.handle.position=s.start_offset
  self.last_listener_x=listener_x 
  self.last_listener_y=listener_y 
  s.update(listener_x, listener_y, 0, self.max_distance) 
  if looping: s.handle.play_looped() 
  else: s.handle.play() 
  self.items.append(s)
  return s

 def play_3d(self,filename,   listener_x,   listener_y,   listener_z,   Sound_x,   Sound_y,   Sound_z,   looping,   persistent=False):
  return self.play_extended_3d(filename, listener_x, listener_y, listener_z, Sound_x, Sound_y, Sound_z, 0, 0, 0, 0, 0, 0, looping, 0, 0, 0, 100, persistent) 

 def play_extended_3d(self,filename,   listener_x,   listener_y,   listener_z,   Sound_x,   Sound_y,   Sound_z, left_range, right_range,   backward_range,   forward_range,   upper_range,   lower_range,   looping,   offset = 0.0, start_pan = 0.0, start_volume = 0.0, start_pitch = 100, persistent = False):
  self.clean_frequency-=1
  if self.clean_frequency<=0: self.clean_unused()
  s=Sound_pool_item(filename=filename,x=Sound_x,y=Sound_y,z=Sound_z,looping=looping,pan_step=self.pan_step,volume_step=self.volume_step,behind_pitch_decrease=self.behind_pitch_decrease,start_pan=start_pan,start_volume=start_volume,start_pitch=start_pitch,left_range=left_range,right_range=right_range,backward_range=backward_range,forward_range=forward_range,lower_range=lower_range,upper_range=upper_range,is_3d=True,persistent=persistent,start_offset=offset)
  if self.max_distance>0 and s.get_total_distance(listener_x, listener_y, listener_z)>self.max_distance:
   if looping==False:
    s.reset() 
    return -2 
   else:
    self.last_listener_x=listener_x 
    self.last_listener_y=listener_y 
    self.last_listener_z=listener_z 
    s.update(listener_x, listener_y, listener_z, self.max_distance) 
    self.items.append(s)
    return s
  try:
   s.handle.load(self.packname+filename + self.ext)
  except:
   s.reset() 
   return -1 
  if s.start_offset>0: s.handle.position=s.start_offset
  self.last_listener_x=listener_x 
  self.last_listener_y=listener_y 
  self.last_listener_z=listener_z 
  s.update(listener_x, listener_y, listener_z, self.max_distance) 
  if looping: s.handle.play_looped() 
  else: s.handle.play() 
  self.items.append(s)
  return s

 def Sound_is_active(self,s):
  if s.looping==False and s.handle==None: return False 
  if s.looping==False and not s.handle.is_playing: return False 
  return True

 def Sound_is_playing(self,s):
  if not self.Sound_is_active(s): return False
  return s.handle.handle.is_playing

 def pause_Sound(self,s):
  if not self.Sound_is_active(s): return False
  if s.paused: return False 
  s.paused=True
  if s.handle.handle.is_playing: s.handle.stop()
  return True 

 def resume_Sound(self,s):
  if not s.paused: return False
  s.paused=False 
  if self.max_distance>0 and s.get_total_distance(self.last_listener_x, self.last_listener_y, self.last_listener_z)>self.max_distance:
   if s.handle!=None: s.handle.close() 
   return True
  s.update(self.last_listener_x, self.last_listener_y, self.last_listener_z, self.max_distance) 
  if s.handle.handle!=None and not self.items[s].handle.handle.is_playing:
   if s.looping: s.handle.play_looped() 
   else: s.handle.play()
  return True

 def pause_all(self):
  for i in self.items:
   if self.Sound_is_playing(i): self.pause_Sound(i) 

 def resume_all(self):
  for i in self.items:
   if i.handle.handle!=None: self.resume_Sound(i) 

 def destroy_all(self):
  for i in self.items: i.reset()

 def update_listener_1d(self,listener_x):
  self.update_listener_3d(listener_x, 0, 0) 

 def update_listener_2d(self,listener_x,   listener_y):
  self.update_listener_3d(listener_x, listener_y, 0) 

 def update_listener_3d(self,listener_x,   listener_y,   listener_z):
  if len(self.items)==0: return 
  self.last_listener_x=listener_x 
  self.last_listener_y=listener_y 
  self.last_listener_z=listener_z 
  for i in self.items: i.update(listener_x, listener_y, listener_z, self.max_distance)

 def update_Sound_1d(self,s,   x):
  return self.update_Sound_3d(s, x, 0, 0) 

 def update_Sound_2d(self,s,   x,   y):
  return self.update_Sound_3d(s, x, y, 0) 

 def update_Sound_3d(self,s,   x,   y,   z):
  s.x=x 
  s.y=y 
  s.z=z 
  s.update(self.last_listener_x, self.last_listener_y, self.last_listener_z, self.max_distance)
  return True 

 def update_Sound_start_values(self,s,start_pan,   start_volume,   start_pitch):
  s.start_pan=start_pan 
  s.start_volume=start_volume 
  s.start_pitch=start_pitch 
  s.update(last_listener_x, last_listener_y, last_listener_z, self.max_distance) 
  if s.stationary and s.handle!=None:
   s.handle.pan=start_pan 
   s.handle.volume=start_volume 
   s.handle.pitch=start_pitch 
   return True 
  if s.is_3d==False and s.handle.pitch!=start_pitch: s.handle.pitch=start_pitch 
  return True 

 def update_Sound_range_1d(self,s,   left_range,   right_range):
  return self.update_Sound_range_3d(s, left_range, right_range, 0, 0, 0, 0) 

 def update_Sound_range_2d(self,s,   left_range,   right_range,   backward_range,   forward_range):
  return self.update_Sound_range_3d(s, left_range, right_range, backward_range, forward_range, 0, 0) 

 def update_Sound_range_3d(self,s,   left_range,   right_range,   backward_range,   forward_range,   lower_range,   upper_range):
  s.left_range=left_range 
  s.right_range=right_range 
  s.backward_range=backward_range 
  s.forward_range=forward_range 
  s.lower_range=lower_range 
  s.upper_range=upper_range 
  s.update(self.last_listener_x, self.last_listener_y, self.last_listener_z, self.max_distance) 
  return True 

 def destroy_sound(self,s):
  s.reset() 
  return True 

 def clean_unused(self):
  if len(self.items)==0: return
  for i in self.items:
   if i.looping: continue
   if i.persistent: continue
   if i.handle.handle==None or not i.handle.handle.is_playing and not i.paused:
    self.items.remove(i)
    self.clean_frequency=3

 def set_pack_name(self, name):
  self.packname = name

 def set_ext(self, extension):
  self.ext = extension

p=Sound_pool()