import sound_lib
from sound_lib import stream
from sound_lib import output
import sound_lib.effects
from sound_lib.effects import tempo as t

o=output.Output()
s=stream.FileStream(file="test.ogg")
ss = t.Tempo(channel=sound_lib.channel.Channel(s))
s.play_blocking()
