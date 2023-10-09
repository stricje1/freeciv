
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
    Jeffrey Strickland
"

[file]
gfx = "enviro/terrain1"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 96
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

; terrain
 0,  0, "t.l0.desert1"

 1,  0, "t.l0.plains1"

 2,  0, "t.l0.grassland1"

 3,  0, "t.l0.forest1"

 4,  0, "t.l0.hills1"

 5,  0, "t.l0.mountains1"

 6,  0, "t.l0.tundra1"

 7,  0, "t.l0.arctic1"

 8,  0, "t.l0.swamp1"

 9,  0, "t.l0.jungle1"
 
10,  0, "t.l0.inaccessible1"


; Terrain special resources: 

 0,  2, "ts.oasis" 				; Jeffrey Strickland
 0,  4, "ts.oil"				; Jeffrey Strickland

 1,  2, "ts.wheat"				; Jeffrey Strickland
 1,  4, "ts.cows"				; Jeffrey Strickland

 2,  2, "ts.vegitables"			; Jeffrey Strickland
 2,  4, "ts.silk"				; Jeffrey Strickland

 3,  2, "ts.coal"               ; Jeffrey Strickland
 3,  4, "ts.wine"				; Jeffrey Strickland

 4,  2, "ts.gold"				; Jeffrey Strickland
 4,  4, "ts.iron"				; Jeffrey Strickland

 5,  2, "ts.game"               ; Jeffrey Strickland
 5,  4, "ts.furs"               ; Jeffrey Strickland

 6,  2, "ts.pigs"				; Jeffrey Strickland
 6,  4, "ts.silver"				; Jeffrey Strickland
; 6,  6, "ts.copper"			; Jeffrey Strickland

 7,  2, "ts.peat"
 7,  4, "ts.spice"
 7,  6, "ts.marble"				; Jeffrey Strickland

 8,  2, "ts.gems"               ; Jeffrey Strickland
 8,  4, "ts.fruit"              ; Jeffrey Strickland
 8,  6, "ts.pheasant"			; Jeffrey Strickland

 9,  2, "ts.fish"               ; Jeffrey Strickland
 9,  4, "ts.whales"				; Jeffrey Strickland
 9,  6, "ts.lumber"             ; Jeffrey Strickland

 10, 2, "ts.seals"              ; Jeffrey Strickland
 10, 4, "ts.deer"				; Jeffrey Strickland
 10, 6, "ts.corn"				; Jeffrey Strickland

 11, 2, "ts.horses"				; Jeffrey Strickland
 11, 4, "ts.rice"				; Jeffrey Strickland
 11, 6, "ts.sheep"				; Jeffrey Strickland
 
 14, 6, "ts.flueggea_virosa"	; Jeffrey Strickland
 14, 8, "ts.olives"				; Jeffrey Strickland

;roads
 12, 0, "road.road_isolated"	; Jeffrey Strickland
 12, 1, "road.road_n"			; Jeffrey Strickland
 12, 2, "road.road_ne"			; Jeffrey Strickland
 12, 3, "road.road_e"			; Jeffrey Strickland
 12, 4, "road.road_se"			; Jeffrey Strickland
 12, 5, "road.road_s"			; Jeffrey Strickland
 12, 6, "road.road_sw"			; Jeffrey Strickland
 12, 7, "road.road_w"			; Jeffrey Strickland
 12, 8, "road.road_nw"			; Jeffrey Strickland

;rails (improved roads)
 13, 0, "road.rail_isolated"	; Jeffrey Strickland 
 13, 1, "road.rail_n"			; Jeffrey Strickland
 13, 2, "road.rail_ne"			; Jeffrey Strickland
 13, 3, "road.rail_e"			; Jeffrey Strickland
 13, 4, "road.rail_se"			; Jeffrey Strickland
 13, 5, "road.rail_s"			; Jeffrey Strickland
 13, 6, "road.rail_sw"			; Jeffrey Strickland
 13, 7, "road.rail_w"			; Jeffrey Strickland
 13, 8, "road.rail_nw"			; Jeffrey Strickland

;add-ons
 0,  6, "tx.oil_mine"			; Jeffrey Strickland
 1,  6, "tx.irrigation"			; Jeffrey Strickland
 2,  6, "tx.farmland"			; Jeffrey Strickland
 3,  6, "tx.mine"				; Jeffrey Strickland
 4,  6, "tx.pollution"
 5,  6, "tx.village"			; Jeffrey Strickland
 6,  6, "tx.fallout"

 15,  0, "t.dither_tile"
 15,  0, "tx.darkness"
 15,  2, "mask.tile"
 15,  2, "t.unknown1"
  7,  0, "t.blend.arctic" ;ice over neighbors
 15,  3, "t.blend.coast"
 15,  3, "t.blend.lake"
 15,  4, "user.attention"
 15,  5, "tx.fog"
}
