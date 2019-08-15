import pyglet.media
import pyglet.resource


class Sound:
    def load(self, mystring, streamed):
        self.source = pyglet.resource.media(mystring, streaming=streamed)
        self.player = pyglet.media.Player()

    def play(self):
        if self.looped == False:
            self.source.play()
        else:
            self.player.play()

    def get_sound(self):
        return self.source

    def loop(self, looped):
        self.looped = looped
        self.player.loop = looped
        if looped:
            self.player.queue(self.source)

    def pause(self):
        self.player.pause()

    def set_volume(self, volume):
        self.player.volume = volume

    def get_volume(self):
        return self.player.volume

    def set_time(self, secs):
        self.player.seek(secs)

    def set_position(self, x, y, z):
        self.player.position = (x, y, z)
