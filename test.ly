yoHan = { c2 }


\new Score <<
    \new Staff {
        \clef "bass"
        \set Staff.instrumentName = \markup { Frump }
        \set Staff.shortInstrumentName = \markup { F. }
        \context Voice = "Frump" {
            {
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
        }

    }
    \new Lyrics \lyricsto "Frump" \lyricmode  { Oh my can't you see me?  }       
    \new Lyrics \lyricsto "Frump" \lyricmode  { Oh my can't you see me?  }       
    
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