# ucs_battle_reader
This is a battle reader for the Uranium Competitive Series, which is a draft league for a pokemon fan game.

Direct damage (accounted for, the easiest part)


Passive Kills (accounted for)

Poison
	- distinguishes between badly poison and regularly poisoned
	- checks if poison was inflicted by toxic spikes (also checks number of tspikes layers for badly poisoned)
	- self inflicted poison by toxic orb
	- fling inflicted poison by toxic orb
	- secondary effect of moves like poison jab (see: MOVES_THAT_POISON and MOVES_THAT_TOXIC)
Burn
	- distinguishes between self inflicted by burn orb
	- secondary effect of moves like Radioacid (see: MOVES_THAT_BURN_
		- included in this list is will-o-wisp because there does not need to be a different check
		
Leech Seed
Destiny Bond
Stealth Rock
Spikes
Rocky Helmet
Aftermath


Self Inflicted Kills

Memento, Explosion, Final Gambit
Life Orb damage
Recoil damage 



Unaccounted for:
whirlpool, fire spin, sand tomb, infestation, magma storm, bind, wrap, metal whip (non functional on sim rn)
bad dreams, nightmare,
sandstorm, hail
confusion
anything else you can think of