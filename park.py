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

piano1_chord = Line("<c ef af>2.")
piano1_big_chord = Line("<c, e g c>2.")

class PianoDown2(MultiLine):
    voice1 = piano1_chord
    voice2 = Line("<af,, af,>2. ~ <af,, af,>2. ~ <af,, af,>2. ~ <af,, af,>2.")

class PianoDown2Short(MultiLine):
    voice1 = piano1_chord
    voice2 = Line("<af,, af,>2. ~ <af,, af,>2.")

piano_down1 = Line("s2.") + Tr(piano1_chord, 12) + Tr(piano1_chord, 24) + Tr(piano1_chord, 36) 
piano_down1_short = Line("s2.") + Tr(piano1_chord, 12)

def piano_up4(music):
    return music + Tr(music, 12) + Tr(music, 24) + Tr(music, 36)


# ------------------------------------------------------------------------------------------
# CHORUS
class PlayPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.play.frump")
    vinkle = BubbleMaterial("park.chorus.play.vinkle")
    piano1 = (piano_down1 + Tr(piano_down1, 2)).latch(dynamic="p")
    piano2 = PianoDown2() + Tr(PianoDown2(), 2)

class NightDayPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.night_day.frump")
    vinkle = BubbleMaterial("park.chorus.night_day.vinkle")
    piano1 = (piano_down1 + Tr(piano_down1_short, 2) + Tr(piano_down1_short, 4)).latch(dynamic="mp")
    piano2 = PianoDown2() + Tr(PianoDown2Short(), 2) + Tr(PianoDown2Short(), 4)

class NarcissaPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.narcissa.frump")
    vinkle = BubbleMaterial("park.chorus.narcissa.vinkle")
    piano1 = Tr(piano_down1, 4) + Line("<d' g' b'>2. <d'' g'' b''>2. <d' fs' a'>2. <d'' fs'' a''>2.")
    piano2 = Tr(PianoDown2(), 4) + Line("<d, d>2.-> <d, d>2.-> <d, d>2.-> <d, d>2.->")

class NarcissaPhrase2(SongPhrase):
    frump = BubbleMaterial("park.chorus.narcissa2.frump")
    vinkle = BubbleMaterial("park.chorus.narcissa2.vinkle")
    piano1 = Line("""<e' g' b' e''>2.-> <e'' g'' b'' e'''>2.->
            <f' a' c'' f''>2.-> <f'' a'' c''' f'''>2.->
            <g' c'' e''>2.-> <g'' b'' d''' g'''>2.->
            <c''' e''' g''' c''''>2.-> ~ <c''' e''' g''' c''''>2.
            """)
    piano2 = Line("""<e, e>2.-> <e, e>2.-> 
            <f, f>2.-> <f, f>2.->
            <g, g>2.-> <g, g>2.->
            <c, c>2.-> ~ <c, c>2.""")

class Chorus(GridSequence, Song):
    grid_sequence = (PlayPhrase, NightDayPhrase, NarcissaPhrase, NarcissaPhrase2)

# ------------------------------------------------------------------------------------------
# INTRO
class Intro(Chorus):
    frump = rest_phrase * 3
    vinkle = rest_phrase * 3

# ------------------------------------------------------------------------------------------
# VERSE 1

class PianoWalkUp(SongPhrase):
    piano1 = BubbleMaterial("park.piano.lick_a") + BubbleMaterial("park.piano.lick_b")
    piano2 = BubbleMaterial("park.piano.bass_walkup_a") + BubbleMaterial("park.piano.bass_walkup_b")

class LarkPhrase(PianoWalkUp):
    frump = BubbleMaterial("park.verse1.frump_lark")

class HugePhrase(SongPhrase):
    vinkle = BubbleMaterial("park.verse1.vinkle_huge")
    piano1 = Tr(BubbleMaterial("park.piano.lick_a"), 1) + BubbleMaterial("park.piano.lick_b2")
    piano2 = Tr(BubbleMaterial("park.piano.bass_walkup_a"), 1) + BubbleMaterial("park.piano.bass_walkup_b2")

class AstroPhrase(SongPhrase):
    frump = BubbleMaterial("park.verse1.frump_astro")
    piano1 = Tr(PianoWalkUp.piano1, 2)
    piano2 = Tr(PianoWalkUp.piano2, 2)

class Verse1(GridSequence, Song):
    grid_sequence = (LarkPhrase, HugePhrase, AstroPhrase)


# ------------------------------------------------------------------------------------------
# VERSE 2

class MusakPhrase(LarkPhrase):
    frump = BubbleMaterial("park.verse2.frump_musak")

class AndrewPhrase(HugePhrase):
    vinkle = BubbleMaterial("park.verse2.vinkle_andrew")

class GrassPhrase(AstroPhrase):
    frump = BubbleMaterial("park.verse2.frump_grass")

class Verse2(GridSequence, Song):
    grid_sequence = (MusakPhrase, AndrewPhrase, GrassPhrase)

# ------------------------------------------------------------------------------------------
# VERSE 3
class LightsPhrase(LarkPhrase):
    vinkle = BubbleMaterial("park.verse3.vinkle_lights")
    frump = rest_phrase

class DronesPhrase(HugePhrase):
    frump = BubbleMaterial("park.verse3.frump_drones")
    vinkle = rest_phrase

class BurnhamPhrase(AstroPhrase):
    vinkle = BubbleMaterial("park.verse3.vinkle_burnham")
    frump = rest_phrase

class Verse3(GridSequence, Song):
    grid_sequence = (LightsPhrase, DronesPhrase, BurnhamPhrase)

# ------------------------------------------------------------------------------------------
# CODA?

# ------------------------------------------------------------------------------------------
# FINAL SCORE

class SongMusic(GridSequence, Song):
    grid_sequence = (SongStart, 
        # Intro,
        Verse1, 
        # Chorus,
        # Verse2, 
        # Verse3,
        # Chorus
        )

score = SongScore( SongMusic() )
score.make_pdf()
# print(score)
# score.show()
