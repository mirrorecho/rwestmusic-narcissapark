import _settings
from abjad import *
from calliope.bubbles import *
from lyrics import FRUMP_LYRICS, VINKLE_LYRICS
from base import *

# ------------------------------------------------------------------------------------------
# NOTES FOR BUBBLES DEVELOPMENT
# - short-cut for BubbleMaterial class
# - short-cut for Line class?
# - put bubbles short-cuts in optional import
# - a bubble type that sets bubble attributes automatically from material names in dictionary
# - separating out pitch and rhythm in the material
# - start a bubble (in particular a line) on a particular pitch
# - better lyrics handling!
# - overlaying mutations on lines (and by extenion larger bubbles)
# - font for title, composer, etc.
# - bar numbers


# ------------------------------------------------------------------------------------------
# SOME MATERIAL

piano_hanker = Line("<g' c''>4")*3
piano1_every = Line("<c' c''>4")*3
piano2_every = Line("<af, ef af>4")*3

class PianoWalkUp(SongPhrase):
    piano1 = BubbleMaterial("park.piano.lick1")*2 + piano_hanker*4
    piano2 = BubbleMaterial("park.piano.bass_walkup")


# ------------------------------------------------------------------------------------------
# INTRO


# ------------------------------------------------------------------------------------------
# CHORUS
class PlayPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.play.frump")
    vinkle = BubbleMaterial("park.chorus.play.vinkle")
    piano1 = piano1_every* 4 + Tr(piano1_every*4, 2)
    piano2 = piano2_every* 4 + Tr(piano2_every*4, 2)

class NightDayPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.night_day.frump")
    piano1 = Tr(piano1_every*3, 2) + Tr(piano1_every*3, 4) + Tr(piano1_every*2, 7)
    piano2 = Tr(piano2_every*3, 2) + Tr(piano2_every*3, 4) + Line("<g, c e>4")*3 + Line("<g, b, d>4")*3

class NarcissaPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.narcissa.frump")
    piano2 = Tr(piano2_every, -1)*2 + Line("<g, c e>4")*3 + Tr(piano2_every, -1) + Tr(piano2_every*4, 4)

class Chorus(GridSequence, Song):
    grid_sequence = (PlayPhrase, NightDayPhrase, NarcissaPhrase)

# ------------------------------------------------------------------------------------------
# VERSE 1
class LarkPhrase(PianoWalkUp):
    frump = BubbleMaterial("park.verse1.frump_lark")

class HugePhrase(SongPhrase):
    vinkle = BubbleMaterial("park.verse1.vinkle_huge")
    piano1 = Tr(PianoWalkUp.piano1, 1)
    piano2 = Tr(PianoWalkUp.piano2, 1)

class AstroPhrase(SongPhrase):
    frump = BubbleMaterial("park.verse1.frump_astro")
    piano1 = Tr(PianoWalkUp.piano1, 2)
    piano2 = Tr(PianoWalkUp.piano2, 2)

class Verse1(GridSequence, Song):
    grid_sequence = (LarkPhrase, HugePhrase, AstroPhrase)


# ------------------------------------------------------------------------------------------
# VERSE 2

class MusakPhrase(LarkPhrase):
    pass

class AndrewPhrase(HugePhrase):
    pass

class GrassPhrase(AstroPhrase):
    pass

class Verse2(GridSequence, Song):
    grid_sequence = (MusakPhrase, AndrewPhrase, GrassPhrase)

# ------------------------------------------------------------------------------------------
# VERSE 3

# ------------------------------------------------------------------------------------------
# CODA?

# ------------------------------------------------------------------------------------------
# FINAL SCORE

class SongMusic(GridSequence, Song):
    grid_sequence = (SongStart, 
        # Intro,
        Verse1, 
        Chorus,
        # Verse2, 
        # Verse3,
        # Chorus
        )

score = SongScore( SongMusic() )
score.make_pdf()
# print(score)
# score.show()
