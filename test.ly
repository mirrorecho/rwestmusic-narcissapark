\new Score <<
    \new Staff {
        \clef "bass"
        \set Staff.instrumentName = \markup { Frump }
        \set Staff.shortInstrumentName = \markup { F. }
        {
            c2
            d2
            e2
            f2
            g2
            a2
            c2
            d2
            e2
            f2
            g2
            a2
            c2
            d2
            e2
            f2
            g2
            a2
        }
    }
        \addlyrics { Oh my can't you see POOP? Oh my can't you see POOP? Oh my can't you see POOP?  } 
    \new Staff {
        \clef "bass"
        \set Staff.instrumentName = \markup { Vinkle }
        \set Staff.shortInstrumentName = \markup { V. }
        {
            b1
            b1
            b1
            b1
            b1
            b1
            b1
            b1
            b1
        }
    }
    \addlyrics { Yes I can! Yes I can! Yes I can!  }
    \new PianoStaff <<
        \set PianoStaff.instrumentName = \markup { Piano }
        \set PianoStaff.shortInstrumentName = \markup { Pf. }
        \new Staff {
            {
                g1
                g1
                g1
                g1
                g1
                g1
                g1
                g1
                g1
            }
        }
        \new Staff {
            \clef "bass"
            {
                g1
                g1
                g1
                g1
                g1
                g1
                g1
                g1
                g1
            }
        }
    >>
>>