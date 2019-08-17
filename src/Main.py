from Player import *
from Map import *
from Menu import *
from Window import *
from Menus import *

sp.p.set_pack_name("sounds/")
sp.p.set_ext(".ogg")

class main_app:

 def __init__(self):
  self.window_handler = Window("Testing app")
  self.menu_handler = Menu()
  self.player = Player()
  self.map_handler = Map(0, 0, 0, 100, 100, 100)
  self.main_menu_logic()

 def main_menu_logic(self):
  c = mainmenu(self.menu_handler)
  if c == 0: self.mainloop()
  elif c == 1:
   pygame.quit()
   print("Exitting")
   exit()

 def mainloop(self):
  while 1:
   self.contkeyloop()
   pygame.display.update()
   pygame.time.wait(2) #Sleep for 2 milliseconds to relieve our system

 def key_pressed(self, key):
  return pygame.key.get_pressed()[key]

 def contkeyloop(self):
  for event in pygame.event.get():
   if event.type == pygame.QUIT: #User pressed the close button
    pygame.quit()
    exit()
   if event.type == pygame.KEYDOWN:
    if event.key == pl.K_c: speak(self.player.get_string_coordinates())
  if self.player.can_move():
   if self.key_pressed(pl.K_UP) and self.player.y < self.map_handler.get_max_y(): self.player.move(1)
   elif self.key_pressed(pl.K_RIGHT) and self.player.x < self.map_handler.get_max_x(): self.player.move(2)
   elif self.key_pressed(pl.K_DOWN) and self.player.y > self.map_handler.get_min_y(): self.player.move(3)
   elif self.key_pressed(pl.K_LEFT) and self.player.x > self.map_handler.get_min_x(): self.player.move(4)

m_a = main_app()