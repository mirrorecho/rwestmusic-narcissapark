\new Score <<
    \new Staff {
        \new Voice = "YO" {
            \clef "bass"
            \set Staff.instrumentName = \markup { Vinkleschmidt }
            \set Staff.shortInstrumentName = \markup { V. }
            {
                a4
                a4
                a4
                a4
            }
        }
    }
    \new Lyrics \lyricsto "YO" \lyricmode { hello there my stink }
    

    \new Staff {
        \clef "bass"
        \set Staff.instrumentName = \markup { Frump }
        \set Staff.shortInstrumentName = \markup { F. }
        {
            b4
            b4
            b4
            b4
        }
    }
    \new PianoStaff <<
        \set PianoStaff.instrumentName = \markup { Piano }
        \set PianoStaff.shortInstrumentName = \markup { Pf. }
        \new Staff {
            {
                r1 -\fermata
            }
        }
        \new Staff {
            \clef "bass"
            {
                b1 -\fermata
            }
        }
    >>
>>