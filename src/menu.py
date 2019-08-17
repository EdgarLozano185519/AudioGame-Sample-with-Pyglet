import pygame, pygame.locals as pl, sound_pool as sp, dialog, timer

from speech import speak
class menu_exception(Exception):
 pass

class menu_item:
 def __init__(self,text,can_click=True,slider=False,sliderval=0,minval=0,maxval=0):
  if can_click: self.text=text
  else: self.text=text+", unavailable"
  self.can_click=can_click
  self.slider=slider
  self.sliderval=sliderval
  if minval<=self.sliderval and maxval>=self.sliderval:
   self.minval=minval
   self.maxval=maxval
  else: raise menu_exception("Invalid argument for slider values.")

class Menu:
<<<<<<< HEAD:src/menu.py
    def __init__(self):
        self.items = []
        self.click_exists = 0
        self.current = 0

    def add_item(self, mystring):
        self.items.append(str(mystring))

    def add_click(self, soundstring):
        self.click = soundstring
        self.click_exists += 1
        return self.click

    def get_click_exists(self):
        return self.click_exists

    def get_next(self):
        temp = self.current + 1
        if temp < len(self.items):
            self.current = temp
        return self.current

    def get_previous(self):
        temp = self.current - 1
        if temp >= 0:
            self.current = temp
        return self.current

    def current_as_string(self):
        return self.items[self.current]

    def get_current(self):
        return self.current
=======
 def __init__(self,allow_reset=False,allow_top=True,intro="",musicsound="",movesound="",music_volume=0,menuenter="",speak_intro_int=False):
  self.menu_choices = []
  self.allow_reset=allow_reset
  self.allow_top=allow_top
  self.musicsound=musicsound
  self.movesound=movesound
  self.intro=intro
  self.music_volume=music_volume
  self.menuenter=menuenter
  self.speak_menu_int=speak_intro_int

 def add_item(self,itemname,can_click=True,slider=False,sliderval=0,minval=0,maxval=0):
  self.menu_choices.append(menu_item(itemname,can_click,slider,sliderval,minval,maxval))

 def reset(self,everything=False):
  if not everything:
   del self.menu_choices[:]
   self.intro=""
   self.musicsound=""
  else: self.__init__()

 def add_music(self, x):
  self.musicsound=x

 def set_music_volume(self,volume):
  self.music_volume=volume

 def return_text(self,key):
  if key<0 or key>self.len(menu_choices)-1: return -1
  return self.menu_choices[choice].text

 def set_move_sound(self,sound):
  self.movesound = sound

 def set_enter_sound(self,sound):
  self.enter_sound=sound

 def set_intro(self,intro):
  self.intro=intro

 def choose_text(self, choice):
  if not choice.slider: return choice.text
  return choice.text+". Currently set to " + str(choice.sliderval)

 def run(self,updater = None):
  if len(self.menu_choices)==0: return -2
  choice = 0
  if self.intro!="": speak(self.intro,self.speak_menu_int)
  if self.musicsound!="": msnd=sp.p.play_stationary_extended(self.musicsound,True,0,0,self.music_volume,100)
  speak(self.menu_choices[choice].text,False)
  while 1:
   if updater: updater() #Menus that still want the game to go on
   for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
     if event.key == pl.K_UP and choice>0:
      choice-=1
      if self.movesound!="": sp.p.play_stationary(self.movesound,False)
      speak(self.choose_text(self.menu_choices[choice]))
     elif event.key == pl.K_DOWN and choice<len(self.menu_choices)-1:
      choice+=1
      if self.movesound!="": sp.p.play_stationary(self.movesound,False)
      speak(self.choose_text(self.menu_choices[choice]))
     elif event.key==pl.K_PAGEUP and self.musicsound!="" and msnd.handle.volume!=0:
      msnd.handle.volume+=5
     elif event.key==pl.K_PAGEDOWN and self.musicsound!="" and msnd.handle.volume-5>=-100: 
      msnd.handle.volume-=5
     elif self.allow_top and event.key==pl.K_UP and choice==0:
      if self.movesound!="": sp.p.play_stationary(self.movesound,False)
      choice=len(self.menu_choices)-1
      speak(self.choose_text(self.menu_choices[choice]))
     elif self.allow_top and event.key==pl.K_DOWN and choice==len(self.menu_choices)-1:
      if self.movesound!="": sp.p.play_stationary(self.movesound,False)
      choice=0
      speak(self.choose_text(self.menu_choices[choice]))
     elif event.key==pl.K_RETURN:
      if self.menuenter!="": sp.p.play_stationary(self.menuenter,False)
      if self.menu_choices[choice].can_click and not self.menu_choices[choice].slider:
       if self.musicsound!="": self.fade(msnd, 2)
       return choice
      elif self.menu_choices[choice].slider: speak("This is a slider. Use left and right arrows to change it's value.")
      else: dialog.dlg("Unavailable.")
     elif event.key==pl.K_RIGHT and self.menu_choices[choice].slider:
      if self.menu_choices[choice].sliderval==self.menu_choices[choice].maxval: speak("Unable to go higher.")
      else:
       self.menu_choices[choice].sliderval+=1
       speak(str(self.menu_choices[choice].sliderval))
     elif event.key==pl.K_LEFT and self.menu_choices[choice].slider:
      if self.menu_choices[choice].sliderval==self.menu_choices[choice].minval: speak("Unable to go lower.")
      else:
       self.menu_choices[choice].sliderval-=1
       speak(str(self.menu_choices[choice].sliderval))
     elif self.allow_reset and event.key==pl.K_ESCAPE:
      if self.musicsound!="": self.fade(msnd,3)
      return -1
   pygame.display.update()
   pygame.time.wait(2)

 def fade(self,handle,ftime):
  if type(handle) is int: return
  tmr=timer.timer()
  while handle.handle.volume!=-100:
   if tmr.elapsed>=ftime:
    tmr.restart()
    handle.handle.volume-=1
  sp.p.destroy_sound(handle)
>>>>>>> 3a304afdec2933bf9877e240ef4373759a3faaf6:src/Menu.py
