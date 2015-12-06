import _settings
from abjad import *
from calliope.bubbles import *
from lyrics import FRUMP_LYRICS, VINKLE_LYRICS

# ------------------------------------------------------------------------------------------
# BASE SCORE, PARTS, AND PHRASES

class SongScore(BubbleScore):
    piano = BubblePiano()
    frump = BubbleStaff(
            instrument=instrumenttools.BaritoneVoice(instrument_name="Frump", short_instrument_name="F."), clef="bass",
            commands=(
                ("addlyrics {" 
                    + FRUMP_LYRICS["verse1"] 
                    + FRUMP_LYRICS["chorus"] 
                    # + FRUMP_LYRICS["verse2"] 
                    # + FRUMP_LYRICS["verse3"] 
                    # + FRUMP_LYRICS["chorus"] 
                    + "} ", "after"),
                )
            )
    vinkle = BubbleStaff(
            instrument=instrumenttools.BaritoneVoice(instrument_name="Vinkle", short_instrument_name="V."), clef="bass",
            commands=(
                ("addlyrics {" 
                    + VINKLE_LYRICS["verse1"] 
                    + VINKLE_LYRICS["chorus"] 
                    # + VINKLE_LYRICS["verse2"] 
                    # + VINKLE_LYRICS["verse3"] 
                    # + VINKLE_LYRICS["chorus"] 
                    + "} ", "after"),
                )
            )
    sequence = ("frump","vinkle","piano")

class Song(Bubble):
    piano1 = Placeholder()
    piano2 = Placeholder()
    frump = Placeholder()
    vinkle = Placeholder()

class SongStart(Song):
    piano1 = Line( commands=( ("time 3/4", "before"), ) )
    piano2 = Line( commands=( ("time 3/4", "before"), ) )
    frump = Line( commands=( ("time 3/4", "before"), ) )
    vinkle = Line( commands=( ("time 3/4", "before"), ) )

rest_phrase = BubbleMaterial("park.rest_phrase")

class SongPhrase(Song):
    piano1 = rest_phrase
    piano2 = rest_phrase
    frump = rest_phrase
    vinkle = rest_phrase

