[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
    Alexandre Beraud <a_beraud@lemel.fr>
    Enrico Bini <e.bini@sssup.it> (fundamentalism icon)
    GriffonSpade (tribal and federation)
"

[file]
gfx = "templars/misc/governments" 

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 25
dy = 25

tiles = { "row", "column", "tag"

; Government icons:

  0,  0, "gov.anarchy"
  0,  1, "gov.tribal"
  0,  2, "gov.despotism"
  0,  3, "gov.monarchy"
  0,  4, "gov.fundamentalism"
  0,  5, "gov.federation"
  0,  6, "gov.theocracy"
  0,  7, "gov.republic"
  0,  8, "gov.democracy"
  0,  9, "gov.communism"
  0, 10, "gov.ecclesiastical"
  
}
