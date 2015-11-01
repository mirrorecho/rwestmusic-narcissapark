import settings
from abjad import *
from calliope.bubbles import *

class SongScore(BubbleScore):
    piano = BubblePiano()
    voice1 = BubbleStaff(instrument=instrumenttools.BaritoneVoice(instrument_name="Vinkleschmidt", short_instrument_name="V."), clef="bass")
    voice2 = BubbleStaff(instrument=instrumenttools.BaritoneVoice(instrument_name="Frump", short_instrument_name="F."), clef="bass")
    sequence = ("voice1","voice2","piano")

class Song(Bubble):
    piano1 = Placeholder()
    piano2 = Placeholder()
    voice1 = Placeholder()
    voice2 = Placeholder()

class Lick1(Song):
    piano1 = Line("r1\\fermata")
    piano2 = Line("b1\\fermata")
    voice1 = Line("a4 a a a")
    voice2 = Line("b4 b b b")

class ParkMusic(GridSequence, Song):
    grid_sequence = (Lick1, )

score = SongScore( ParkMusic() )
print(score)
score.make_pdf()
# print(score)
# score.show()
