#This should be used only for placing additional menus
#m must be the object of the menu class
def mainmenu(m):
 m.reset()
 m.add_item("Start game")
 m.add_item("Exit")
 m.add_music("music/mainMenuMusic")
 m.set_intro("Welcome!")
 m.set_move_sound("clicks/click")
 return m.run()