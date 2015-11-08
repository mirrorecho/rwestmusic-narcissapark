import settings
from abjad import *
from calliope.bubbles import *

class FrumpStaff(BubbleGridStaff):
    frump = BubbleVoice(name="Frump")

class SongScore(BubbleScore):
    piano = BubblePiano()
    frump_staff = FrumpStaff(clef="bass")
    voice2 = BubbleStaff(instrument=instrumenttools.BaritoneVoice(instrument_name="Vinkleschmidt", short_instrument_name="F."), clef="bass")
    sequence = ("frump_staff","voice2","piano")

class Song(Bubble):
    piano1 = Placeholder()
    piano2 = Placeholder()
    frump = Placeholder()
    voice2 = Placeholder()

class Lick1(Song):
    piano1 = Line("r1\\fermata")
    piano2 = Line("b1\\fermata")
    frump = Line("a4 a a a")
    voice2 = Line("b4 b b b")

class ParkMusic(GridSequence, Song):
    grid_sequence = ( Lick1, )

# FrumpStaff().make_pdf()

print(FrumpStaff())

# score = SongScore( Lick1() )
# print(score)
# score.make_pdf()
# print(score)
# score.show()
