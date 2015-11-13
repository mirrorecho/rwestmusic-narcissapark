from abjad import *

#  GREAT EXAMPLE OF TEMPORARY POLOYPHONY
m1="b'2 a's"
m2="c'4 c'4 c'4 c'4"

c1 = Container(m1)
c2 = Container(m2)
c = Container()
command_voices = indicatortools.LilyPondCommand('\\ ', 'after')
attach(command_voices, c1)
c.is_simultaneous = True
c.append(c1)
c.append(c2)
command_one_voice = indicatortools.LilyPondCommand('oneVoice', 'after')
attach(command_one_voice, c)
v=Voice(name="Frump")

v.append("e'1")
v.append(c)
v.extend("d'2 d'2")

s = Staff()
s.append(v)

# show(s)
# print(format(s))


# EXAMPLE OF ADDING LYRICS
s = Staff()
v=Voice(name="Frump")

v.append("e'1")
v.append(m2)
v.extend("d'2 d'2")
lyrics_command = indicatortools.LilyPondCommand("addlyrics { Yo is yo mama yo mama }", "after")
attach(lyrics_command, v)
s.append(v)
show(s)




