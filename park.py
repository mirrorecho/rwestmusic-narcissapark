import settings
from abjad import *
from calliope.bubbles import *

class SongScore(BubbleScore):
    piano1 = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 1", short_instrument_name="vln.1"))
    piano2 = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 1", short_instrument_name="vln.1"))
    voice = BubbleStaff(instrument=instrumenttools.Violin(instrument_name="Violin 1", short_instrument_name="vln.1"))

class Song(Bubble):
    piano1 = Placeholder()
    piano2 = Placeholder()
    voice = Placeholder()

class Lick1(Song):
    piano1 = Line("r1\\fermata")
    piano2 = piano1
    voice = Line('a1\\fermata')

class ParkMusic(GridSequence, Song):
    grid_sequence = (Lick1, )

score = SongScore( ParkMusic() )
score.make_pdf()
print(score)