import pyglet

class GameWindow:
    # This class is used to start window
    def place_window(self, mystring):
        tempstring = str(mystring)
        self.gamewindow = pyglet.window.Window(caption=tempstring)
        label = pyglet.text.Label(tempstring,
            font_name="Times New Roman",
            font_size=36,
            x=self.gamewindow.width//2, y=self.gamewindow.height//2,
            anchor_x="center", anchor_y="center")
        return self.gamewindow