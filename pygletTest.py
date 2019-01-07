from GameLoop import *
import pyglet
game = GameLoop()
window = game.place_window()
window.push_handlers(game)

@window.event
def on_draw():
    window.clear()

def update(dt):
    game.update(dt)

game.load_sounds()
game.set_up_menus()
game.speak_random()
pyglet.clock.schedule_interval(update, 1 / 1000.0)
pyglet.app.run()
game.close()
