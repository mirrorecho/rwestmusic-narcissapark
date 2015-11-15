import settings
from abjad import *
from calliope.bubbles import *

class FrumpStaff(BubbleGridStaff):
    frump = BubbleVoice(name="Frump")
    # for reasons that are not entirely clear, instrument and clef need to be set as attributes,
    # not parameters.... WHY?
    instrument=instrumenttools.BaritoneVoice(instrument_name="Frump", short_instrument_name="F.")
    clef="bass"
    commands=(
        ("""addlyrics { Yo yo yo } """, "after"),)

# class SomeMusic1(Bubble):
#     class Meta:
#         sequence = ("one", "two", "three")

# class SomeMusic2(Bubble):
#     class Meta:
#         sequence = ("one", "two", "three")

# class SomeMusic3(Bubble):
#     def violin_1(self, *args, **kwargs):
#         return Line("R1")


class SongScore(BubbleScore):
    piano = BubblePiano()
    # frump_staff = FrumpStaff()
    frump = BubbleStaff(
            instrument=instrumenttools.BaritoneVoice(instrument_name="Frump", short_instrument_name="F."), 
            clef="bass",
            commands=(
                ("""addlyrics { 
                    
                    What a lark
                    Fun and games from dawn past dark
                    Huge projections
                    Huge reflections
                    Astroturf in all directions

                    Musak bland but very loud (loud boring chords here)
                    It’s sure to draw a raucous crowd
                    Andrew Weber, Philip Glass
                    No one will even miss the grass

                    Lights that flash and search the sky
                    Drones o’re head will dive and fly
                    Never mind old Burnham’s promise
                    Forget the war and the Islamists

                    Come and play 
                    Ev-er-y night and day
                    At our Narcissapark!
                    
                } """, "after"),)
            )
    vinkle = BubbleStaff(instrument=instrumenttools.BaritoneVoice(instrument_name="Vinkle", short_instrument_name="V."), clef="bass")
    # sequence = ("frump_staff","vinkle","piano")
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


class RestPhrase(Line):
    music = "R2. R2. R2. R2.     R2. R2. R2. R2."

class SongPhrase(Song):
    piano1 = RestPhrase()
    piano2 = RestPhrase()
    frump = RestPhrase()
    vinkle = RestPhrase()


# class SomeMusic1(Song):
#     # piano1 = PolyLine("a'1 a'1", "g'2 g'2 g'2 g'2", "b2. b4 b1")
#     piano1 = Line("g1 g1 g1")
#     piano2 = Line("g1 g1 g1")
#     frump = LineLyrics("c2 d | e f | g a ", 
#         lyrics = "Oh my can't you see me?")
#     vinkle = LineLyrics("b1 b1 b1",
#         lyrics = "Yes I can!")

# class SomePianoStuff(Line):
#     music = Sequence( SomeMusic.piano1, SomeMusic.piano2 )
    # # OR:
    # music = SomeMusic.piano1 + SomeMusic.piano2

# class SomeMusic2(SomeMusic1):
#     pass
    # frump = SomeMusic.frump.change_lyrics("Oh my can't you see me?")

class SongMusic(GridSequence, Song):
    grid_sequence = (SongStart, SongPhrase )

# class Lick1(Song):
#     piano1 = Line("r1\\fermata")
#     piano2 = Line("b1\\fermata")
#     frump = Line("a4 a a a")
#     voice2 = Line("b4 b b b")

# class ParkMusic(GridSequence, Song):
#     grid_sequence = ( Lick1, Lick1 )

# FrumpStaff().make_pdf()

# print( FrumpStaff() )

score = SongScore( SongMusic() )
print(score)
score.make_pdf()
# print(score)
# score.show()
