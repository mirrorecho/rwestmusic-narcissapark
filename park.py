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

class LineRoll(Line):
    transpose=0

    def music(self, **kwargs):
        return Line("<af c' ef' af'>2.").music(**kwargs)

    def after_music(self, music, **kwargs):
        super().after_music(music, **kwargs)
        arpeggio = indicatortools.Arpeggio()
        attach(arpeggio, music[0])
        mutate(music).transpose(self.transpose)

piano1_big_chord = Line("<c, e g c>2.")

class PianoDown2(MultiLine):
    voice1 = piano1_chord
    voice2 = Line("<af,, af,>2._( s2. s2. s2._)")

class PianoDown2Short(MultiLine):
    voice1 = Line("<d f bf>2. | <bf, d f>2. ")
    voice2 = Line("<bf,, bf,>2._( s2._) ")

piano_down1 = Line("s2.") + LineRoll() + LineRoll(transpose=12) + LineRoll(transpose=24)
piano_down1_short = Line("s2.") + LineRoll(transpose=2)
piano_down1_short_b = Line("s2.") + LineRoll(transpose=4)

class PianoDown2Play(PianoDown2):
    voice1 = piano1_chord + Line("c2.( ~ <af, c ef>2. ~ <af, c ef>2.)")

class PianoDown2PlayB(PianoDown2):
    voice1 = Tr(piano1_chord,2) + Line("r4 d2( ~ <bf, d f>2. ~ <bf, d f>2.)")
    voice2 = Tr(PianoDown2.voice2, 2)

class PianoDown2Night(PianoDown2):
    voice1 = piano1_chord + Line("s2. c2.( ~ <af, c ef>2.)")
    voice2 = Line("<af,, af,>2. ~ <af,, af,>2. _( s2. s2._)")

class PianoDown2Narcissa(MultiLine):
    voice1 = Line("s2. | r4 r <e g> ~ | <e g>2. | <c e g>2.")
    voice2 = Line("<c,, c,>2. ~ <c,, c,>2. _( s2. s2._)")

# ------------------------------------------------------------------------------------------
# CHORUS
class PlayPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.play.frump")
    vinkle = BubbleMaterial("park.chorus.play.vinkle")
    piano1 = (piano_down1 + Line("")).latch(dynamic="p", instruction="exuberantly") + Tr(piano_down1, 2) + Line("")
    piano2 = PianoDown2Play() + PianoDown2PlayB()

class NightDayPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.night_day.frump")
    vinkle = BubbleMaterial("park.chorus.night_day.vinkle")
    piano1 = (piano_down1 + Line("") ).latch(dynamic="mp") + piano_down1_short + piano_down1_short_b
    piano2 = PianoDown2Night() + PianoDown2Short().latch(instruction="cresc.") + Tr(PianoDown2Short(), 2)

class NarcissaPhrase(SongPhrase):
    frump = BubbleMaterial("park.chorus.narcissa.frump")
    vinkle = BubbleMaterial("park.chorus.narcissa.vinkle")
    piano1 = LineRoll(transpose=-8) + LineRoll(transpose=4) + LineRoll(transpose=16) + LineRoll(transpose=28) + Line("<d' g' b' d''>2.\\mf\\< <d'' g'' b'' d'''>2. <d' fs' a' d''>2. <d'' fs'' a'' d'''>2.\\!")
    piano2 = PianoDown2Narcissa() + Line("<d, d>4 <d, d> <d, d> | <d, d>4 <d, d> <d, d> | <d, d>4 <d, d> <d, d> | <d, d>4 <d, d> <d, d> | ")

class NarcissaPhrase2(SongPhrase):
    frump = BubbleMaterial("park.chorus.narcissa2.frump")
    vinkle = BubbleMaterial("park.chorus.narcissa2.vinkle")
    piano1 = Line("""<e' g' b' e''>4->\\f <e' g' b' e''>4 <e' g' b' e''>4 | <e'' g'' b'' e'''>2.->
            <f' a' c'' f''>4-> <f' a' c'' f''> <f' a' c'' f''> | <f'' a'' c''' f'''>2.->
            <c' e' g' c''>4-> <c' e' g' c''> <c' e' g' c''> | <d'' f'' g'' b''>2.->
            """)  + LineRoll(transpose=28).latch(dynamic="ff") + Line("R2.")
    piano2 = Line("""<e, e>4-> <e, e>-> <e, e>-> | <e, e>-> <e, e>-> <e, e>-> |
            <f, f>-> <f, f>-> <f, f>-> | <f, f>-> <f, f>-> <f, f>-> |
            <g, g>-> <g, g>-> <g, g>-> | <g,, g,>2.->  |
            <c,, g,, c,>2.-> ~ | <c,, g,, c,>2.
            """) 

class Chorus(GridSequence, Song):
    grid_sequence = (PlayPhrase, NightDayPhrase, NarcissaPhrase, NarcissaPhrase2)

class ChorusFinal(NarcissaPhrase):
    frump = rest_phrase
    vinkle = rest_phrase

class ChorusFinalFinal(NarcissaPhrase2):
    frump = rest_phrase
    vinkle = rest_phrase

# ------------------------------------------------------------------------------------------
# INTRO
class IntroIntro(SongPhrase):
    piano1 = Line("""<e g c'>2.( \\p ^"exuberantly" | <e' g' c''>) | <fs a d'>(\\< | <fs' a' d''>) | 
                    <c e g c'>( | <c' e' g' c''>) | <d fs a d'>( | <d' fs' a' d''>)\\! """)
    piano2 = Line("c2. ~ | c2. | d2. ~ | d2. | c,2. ~ | c,2. | d,2. ~ | d,2. | ")

class Intro(SongPhrase):
    piano1 = Line("""
        e'8(\\mf\\< g' c'' e'' g''4) | r4 <c'' e'' g'' c'''> <c'' e'' g'' c'''> | 
        ef'8( g' bf' ef'' g''4) | r4 <ef'' g'' bf'' ef'''>8 <ef'' g'' bf'' ef'''>8 <ef'' g'' bf'' ef'''>4 |
        f'''8(\\!\\f c''' a'' f'' a'' c''') | f'''8( c''' a'' f'' a'' c''') | 
        c'''( g'' e'' c'' g'4) | <f' g' b'>2. -> |
        """)
    piano2 = Line("""
        <c, g, c>4 <c, g, c> <c, g, c> |  <c, g, c>4 <c, g, c> <c, g, c> | 
        <ef, bf, ef> <ef, bf, ef> <ef, bf, ef> | <ef, bf, ef> <ef, bf, ef> <ef, bf, ef> |
        <f, c f> <f, c f> <f, c f> | <f, c f> <f, c f> <f, c f> | 
        <g, g> <g, g> <g, g> | <g,, g,>2. -> |
        """)

class IntroMinor(SongPhrase):
    piano1 = Line("""
        e'8(\\mf\\< g' c'' e'' g''4) | r4 <c'' e'' g'' c'''> <c'' e'' g'' c'''> | 
        ef'8( g' bf' ef'' g''4) | r4 <ef'' g'' bf'' ef'''>8 <ef'' g'' bf'' ef'''>8 <ef'' g'' bf'' ef'''>4 |
        f'''8(\\!\\f c''' af'' f'' af'' c''') | f'''8( c''' af'' f'' af'' c''') | 
        c'''( g'' ef'' c'' g'4) | <f' af' b'>2. -> |
        """)
    piano2 = Intro.piano2

# ------------------------------------------------------------------------------------------
# VERSE 1

class Piano1StartVerse(Line):
    music = BubbleMaterial("park.piano.lick_a") + BubbleMaterial("park.piano.lick_b")
    instruction="lightly"

class LarkPhrase(SongPhrase):
    piano1 = Piano1StartVerse()
    piano2 = BubbleMaterial("park.piano.bass_walkup_a") + BubbleMaterial("park.piano.bass_walkup_b")
    frump = BubbleMaterial("park.verse1.frump_lark")

class HugePhrase(SongPhrase):
    vinkle = BubbleMaterial("park.verse1.vinkle_huge")
    piano1 = Tr(BubbleMaterial("park.piano.lick_a"), 1) + BubbleMaterial("park.piano.lick_b2")
    piano2 = Tr(BubbleMaterial("park.piano.bass_walkup_a"), 1) + BubbleMaterial("park.piano.bass_walkup_b2")

class PianoLickA3(Line): 
    music = BubbleMaterial("park.piano.lick_a3")
    def after_music(self, music, **kwargs):
        super().after_music(music, **kwargs)
        arpeggio = indicatortools.Arpeggio()
        attach(arpeggio, music[0])

class AstroPhrase(SongPhrase):
    frump = BubbleMaterial("park.verse1.frump_astro")
    piano1 = PianoLickA3() + Tr(BubbleMaterial("park.piano.lick_b"), -5)
    piano2 = BubbleMaterial("park.piano.bass_walkup_a3")+ Tr(BubbleMaterial("park.piano.bass_walkup_b"), -5)

class Verse1(GridSequence, Song):
    grid_sequence = (LarkPhrase, HugePhrase, AstroPhrase)


# ------------------------------------------------------------------------------------------
# VERSE 2

class MusakPhrase(LarkPhrase):
    frump = BubbleMaterial("park.verse2.frump_musak")

weber_glass1 = (Line("<c'' c'''>8---> r <ef' ef''>---> r <bf' bf''>---> r <ef' ef''>---> r af'--->[ bf'--->] c''--->[ df''--->] <bf' bf''>---> r <ef'' ef'''>---> r ") * 6).latch(dynamic="mf") + Line("r2.\\fermata")
weber_glass2 = Line("R2. R2. R2. R2. R2. R2. R2. R2. ") + Line("<af, ef af>8---> <af, ef af>---> r <af, ef af>---> r <af, ef af>--->")*8 + Line("r2.\\fermata")

class AndrewPhrase(HugePhrase):
    frump = rest_phrase + rest_phrase + Line("R2. | R2. | R2. | R2. | r2.\\fermata | R2. | R2. | R2. | R2. | ")
    piano1 = Tr(BubbleMaterial("park.piano.lick_a"), 1) + weber_glass1 + BubbleMaterial("park.piano.lick_b2")
    piano2 = Tr(BubbleMaterial("park.piano.bass_walkup_a"), 1) + weber_glass2 +  BubbleMaterial("park.piano.bass_walkup_b2")
    vinkle = BubbleMaterial("park.verse2.vinkle_andrew")

class GrassPhrase(AstroPhrase):
    frump = BubbleMaterial("park.verse2.frump_grass")

class Verse2(GridSequence, Song):
    grid_sequence = (MusakPhrase, AndrewPhrase, GrassPhrase)

# ------------------------------------------------------------------------------------------
# VERSE 3
piano_lights_a1 = Line("<ef g c'>4\p <ef g c'> <ef g c'> | <ef g c'>( <ef' g' c''>2) |")
piano_lights_b1 = Line("""<d a c'>4( <f' f''>  <a' d'' f''> ~ |
                    <a' d'' f''>) <e' b'>( <e'' b''> ~ |
                    <e'' b''>) <b' e'' g''>\\< <b' e'' g''> ~ |
                    <b' e'' g''> <cs''! a''>( <a' ds''!>) |
                    <gs'! e''>( e' cs') |
                    <gs bs>\\!\\mf <gs bs> <fs ds'> |""")
piano_lights_a2 = Line("<c,, c,>2. ~ | <c,, c,>2.")
piano_lights_b2 = Line("""<c, c>2. | <g,, g,>2. ~ | 
                    <g,, g,>2. | <fs,, fs,>2. | <gs,,! gs,!>2. ~ | <gs,, gs,>2. | """)

piano_lights_c1 = Line("""<e b d'>2 <fs cs'>4  |
                    <gs b>( <g bf>) g |
                    g2. |
                    g8( bf df' e' g' bf' |
                    df'' e'' g'' bf'' df''' e''' |
                    g'''2.) |""")
piano_lights_c2 = Line("<d, d>2( a,4) | <ef, ef>2. | df2. | df,4 df, df, | df, df, df, | df,2. |")

class LightsPhrase(SongPhrase):
    piano1 = piano_lights_a1 + piano_lights_b1
    piano2 = piano_lights_a2 + piano_lights_b2
    vinkle = BubbleMaterial("park.verse3.vinkle_lights")

class DronesPhrase(SongPhrase):
    piano1 = Tr(piano_lights_a1, "+M1") + Tr(piano_lights_b1, "+m2")
    piano2 = Tr(piano_lights_a2, "+M1") + Tr(piano_lights_b2, "+m2")
    frump = BubbleMaterial("park.verse3.frump_drones")

class BurnhamPhrase(SongPhrase):
    piano1 = Tr(piano_lights_a1, "+M2") + piano_lights_c1
    piano2 = Tr(piano_lights_a2, "+M2") + piano_lights_c2
    vinkle = BubbleMaterial("park.verse3.vinkle_burnham")

class Verse3(GridSequence, Song):
    grid_sequence = (LightsPhrase, DronesPhrase, BurnhamPhrase)

# ------------------------------------------------------------------------------------------
# CODA?

# ------------------------------------------------------------------------------------------
# FINAL SCORE

class SongMusic(GridSequence, Song):
    grid_sequence = (SongStart, 
        IntroIntro,
        Intro,
        Verse1, 
        Chorus,
        Intro,
        Verse2, 
        Chorus,
        IntroMinor,
        Verse3,
        Chorus,
        ChorusFinal,
        ChorusFinalFinal,
        )

score = SongScore( SongMusic() )
score.play()
# score.save()
score.make_pdf()
# print(score)
# score.show()
