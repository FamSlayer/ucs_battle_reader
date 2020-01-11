
MOVES_THAT_BURN = ["Ember", "Fire Blast", "Fire Fang", "Fire Punch", "Flame Wheel", "Flamethrower", "Flare Blitz", "Fling", "Infernal Blade", "Inferno", "Lava Plume", "Radioacid", "Radioacid", "Scald", "Tri Attack", "Will-O-Wisp",]
MOVES_THAT_TOXIC = ["Fling", "Nuclear Waste", "Toxic"]
MOVES_THAT_POISON = ["Gunk Shot", "Poison Fang", "Poison Gas", "Poison Jab", "Poison Powder", "Poison Sting", "Poison Tail", "Sludge", "Sludge Bomb", "Sludge Wave", "Smog"]




player_1 = "Skullex"
player_2 = "Poisseman"

f = open(player_1 + " vs " + player_2 + ".txt",'r').read()
##f = open("status battle 2.txt",'r').read()



def DeterminePoisonSource(nickname, trainer):
    print("Determining poison source of " + nickname + " belonging to " + trainer)
    opp_trainer = player_1
    if trainer == player_1:
        opp_trainer = player_2


    p_lines = f.split(nickname[1:] + "fainted")[0].split('\n')

    j = len(p_lines)
    while(j > 0):
        j-=1
        if (nickname + " was badly poisoned!") in p_lines[j]:
            k = j
            while(k > 0):
                k-=1
                if opp_trainer in p_lines[k][:len(opp_trainer)+1] and " used " in p_lines[k]:
                    # loop through all possible TOXIC moves
                    for move in MOVES_THAT_TOXIC:
                        if move in p_lines[k]:
                            print(p_lines[k])
                            burned_by_enemy = True
                            enemy_nickname = p_lines[k].split(" used ")[0].split("'s ")[1]
                            return (enemy_nickname, True)
                        
                # check to see if we got it from toxic spikes
                elif (trainer + " sent out " + nickname) in p_lines[k]:
                    print("poison inflicted by Toxic Spikes!")
                    h = k
                    while(h > 0):
                        h-=1
                        if " used Toxic Spikes!" in p_lines[h] and (opp_trainer + "'s") in p_lines[h] and "Poison spikes were scattered all around your team's feet!" in p_lines[h+1]:
                            killer_nickname = p_lines[h].split(" used Toxic Spikes")[0].split("'s ")[-1]
                            return (killer_nickname, True)

                elif "Turn " in p_lines[k]:
                    return (nickname, False)
            break
            
        elif (nickname + " was poisoned!") in p_lines[j]:
            k = j
            while(k > 0):
                k-=1
                if opp_trainer in p_lines[k][:len(opp_trainer)+1] and " used " in p_lines[k]:
                    # loop through all possible TOXIC moves
                    for move in MOVES_THAT_POISON:
                        if move in p_lines[k]:
                            print(p_lines[k])
                            burned_by_enemy = True
                            enemy_nickname = p_lines[k].split(" used ")[0].split("'s ")[1]
                            return (enemy_nickname, True)
                        
                # check to see if we got it from toxic spikes
                elif (trainer + " sent out " + nickname) in p_lines[k]:
                    print("poison inflicted by Toxic Spikes!")
                    h = k
                    while(h > 0):
                        h-=1
                        if " used Toxic Spikes!" in p_lines[h] and (opp_trainer + "'s") in p_lines[h] and "Poison spikes were scattered all around " in p_lines[h+1]:
                            killer_nickname = p_lines[h].split(" used Toxic Spikes")[0].split("'s ")[-1]
                            return (killer_nickname, True)

                elif "Turn " in p_lines[k]:
                    return (nickname, False)
                
            break

    
    return (nickname, False)


def DetermineBurnSource(nickname, trainer):
    print("Determining burn source of " + nickname + " belonging to " + trainer)
    split_string = nickname + " was burned!"
    burned_instances = f.split(split_string)
    
    prev_lines = burned_instances[-2].split('\n')
    
    opp_trainer = player_1
    if trainer == player_1:
        opp_trainer = player_2

    m = len(prev_lines)
    while(m > 0):
        m-=1
        # check enemy pokemon's attack and see if it could have burned
        if opp_trainer in prev_lines[m][:len(opp_trainer)+1] and " used " in prev_lines[m]:
            # loop through all possible burn moves
            for move in MOVES_THAT_BURN:
                if move in prev_lines[m]:
                    print(prev_lines[m])
                    enemy_nickname = prev_lines[m].split(" used ")[0].split("'s ")[1]
                    return (enemy_nickname, True)

        elif "Turn " in prev_lines[m]:
            return (nickname, False)

    
    return (nickname, False)


def DetermineLeechSeedSource(nickname, trainer):
    print("Determining Leech Seed source of " + nickname + " belonging to " + trainer)
    split_string = nickname + " was seeded!"
    burned_instances = f.split(split_string)
    
    prev_lines = burned_instances[-2].split('\n')

    opp_trainer = player_1
    if trainer == player_1:
        opp_trainer = player_2

    m = len(prev_lines)
    while(m > 0):
        m-=1
        # check to see if enemy used leech seed
        if opp_trainer in prev_lines[m] and " used Leech Seed!" in prev_lines[m]:
            enemy_nickname = prev_lines[m].split(" used ")[0].split("'s ")[1]
            return(enemy_nickname, True)

        elif "Turn " in prev_lines[m]:
            return (nickname, False)
    
    return ("none", False)


def DetermineDestinyBondSource(nickname, trainer):
    print("Determining Destiny Bond source of " + nickname + " belonging to " + trainer)
    return (nickname, trainer)


def DetermineStealthRockSource(nickname, trainer):
    split_string = "Pointed stones dug into " + nickname + "!\n" + nickname + " fainted!"
    prior_lines = f.split(split_string)[0].split('\n')

    # get opponent's trainer name
    opponent = player_1
    if trainer == player_1:
        opponent = player_2
    
    # find last time opponent used spikes
    i = len(prior_lines)
    while(i>0):
        i-=1
        if " used Stealth Rock!" in prior_lines[i] and (opponent + "'s") in prior_lines[i] and "Pointed stones float in the air around " in prior_lines[i+1]:
            killer_nickname = prior_lines[i].split(" used Stealth Rock!")[0].split("'s ")[-1]
            return (killer_nickname, opponent)

    return ("none",trainer)

def DetermineSpikesSource(nickname, trainer):
    split_string = nickname + " is hurt by the spikes!\n" + nickname + " fainted!"
    prior_lines = f.split(split_string)[0].split('\n')

    # get opponent's trainer name
    opponent = player_1
    if trainer == player_1:
        opponent = player_2
    
    # find last time opponent used spikes
    i = len(prior_lines)
    while(i>0):
        i-=1
        if " used Spikes!" in prior_lines[i] and (opponent + "'s") in prior_lines[i] and "Spikes were scattered all around " in prior_lines[i+1]:
            killer_nickname = prior_lines[i].split(" used Spikes!")[0].split("'s ")[-1]
            return (killer_nickname, opponent)

    return ("none",trainer)




##########################################################
#                                                        #
#     THIS IS WHERE THE ACTUAL BATTLE READING STARTS     #
#                                                        #
##########################################################



components = f.split(" fainted!")[:-1]
for c in components:
    
    print("NEXT DEATH:")
    
    orig_lines = c.split('\n')[-10:]
    pokemon_nickname = orig_lines[-1]

    # sneaky stuff: splitting the entire text of the battle by
    #   "XPokemon Fainted" but one letter past 
    lines = f.split(pokemon_nickname[1:] + " fainted!")[0].split('\n')[-10:]

    # this is what the program prints as proof of the kill
    kill_line = ""
    
    i = len(lines)
    while(i>0):
        i-=1
        if pokemon_nickname in lines[i]:
            # Death by Direct Damage
            if "% damage!" in lines[i]:
                while(i>0):
                    i-=1
##                    print(lines[i])
                    if " used " in lines[i]:
                        kill_line = lines[i]
                        break
                break
            
            # Death by some type of poison
            elif " was hurt by poison!" in lines[i]:
                print("poisoned to death")
                print(lines[i])
                
                trainer_name = player_1
                while(i>0):
                    i-=1
                    if (player_2 + "'s") in lines[i][:len(player_2)+1] and pokemon_nickname in lines[i]:
                        trainer_name = player_2
                        break
                    if "Turn " in lines[i]:
                        break

                attack_line = DeterminePoisonSource(pokemon_nickname, trainer_name)
                if(attack_line[1]):
                    kill_line = attack_line[0] + " got an indirect kill with poison damage!"
                else:
                    kill_line = pokemon_nickname + " died a self-inflicted death to poison :("
                break

            # Death by burn
            elif " was hurt by its burn!" in lines[i]:
                print("burned to death")
                print(lines[i])

                trainer_name = player_1
                while(i>0):
                    i-=1
                    #print(lines[i])
                    if player_2 in lines[i][:len(player_2)+1] and pokemon_nickname in lines[i]:
                        #print("super genius brain calculation")
                        trainer_name = player_2
                        break
                    if "Turn " in lines[i]:
                        break
                    
                attack_line = DetermineBurnSource(pokemon_nickname, trainer_name)
                if(attack_line[1]):
                    kill_line = attack_line[0] + " got an indirect kill with burn damage!"
                else:
                    kill_line = pokemon_nickname + " died a self-inflicted death to burn :("
                break

            # Death by leech seed
            elif " health is sapped by Leech Seed!" in lines[i]:
                print("death by LEECH SEED")
                print(lines[i])
                
                trainer_name = player_1
                while(i>0):
                    i-=1
                    #print(lines[i])
                    if player_2 in lines[i][:len(player_2)+1] and pokemon_nickname in lines[i]:
                        #print("super genius brain calculation")
                        trainer_name = player_2
                        break
                    if "Turn " in lines[i]:
                        break
                    
                attack_line = DetermineLeechSeedSource(pokemon_nickname, trainer_name)
                kill_line = attack_line[0] + " got an indirect kill with leech seed!" 
                break

            # Death by stealth rock
            elif "Pointed stones dug into" in lines[i]:
                print("stealth rock death")

                trainer_1 = player_1 in lines[-3]
                trainer_string = player_1
                if not trainer_1:
                    trainer_string = player_2

                killer_nickname = DetermineStealthRockSource(pokemon_nickname, trainer_string)
                kill_line = killer_nickname[1] + "'s " + killer_nickname[0] + " got an indirect kill with Stealth Rock!"
                break

            elif " is hurt by the spikes!" in lines[i]:
                print("death by spikes")

                trainer_1 = player_1 in lines[-3]
                trainer_string = player_1
                if not trainer_1:
                    trainer_string = player_2

                print("need to determine killer of " + pokemon_nickname + " belonging to " + trainer_string)
                killer_nickname = DetermineSpikesSource(pokemon_nickname, trainer_string)
                kill_line = killer_nickname[1] + "'s " + killer_nickname[0] + " got an indirect kill with Spikes!"
                break

            elif " used Memento!" in lines[i] or " used Explosion!" in lines[i] or " used Final Gambit!" in lines[i] or " used Fission Burst!" in lines[i] or " used Struggle!" in lines[i]:
                print("self kill!")
                kill_line = lines[i]
                break

            elif " is hurt!" in lines[i]:
                print('"is hurt!" death - possible sources: aftermath')
                if " fainted!" in lines[-3]:
                    killer_nickname = lines[-3].split(" fainted!")[0]
                    kill_line = killer_nickname + " got an indirect kill with aftermath!"                    
                break
            
            elif " is hurt by its Life Orb!" in lines[i]:
                print("self kill to life orb")
                kill_line = pokemon_nickname + " died from Life Orb recoil!"
                break

            elif " is hurt by " in lines[i] and "'s Rocky Helmet!" in lines[i]:
                print("rockey helmet kill")
                killer_nickname = lines[i].split(" is hurt by ")[-1].split("'s Rocky Helmet!")[0]
                kill_line = killer_nickname + " got a kill with Rocky Helmet!"
                break

            elif " was hit by recoil!" in lines[i]:
                print("self kill to recoil move!")
                break


    # if we get to the end and there was no kill, then we have to check destiny bond
    #   this line says "took its foe down with it" but comes AFTER the fainted line
    #   which is why we check for it here instead of earlier
    if kill_line == "":
        # look for destiny bond kill
        dbond_lines = f.split(pokemon_nickname[1:] + " fainted!")[1].split('\n')[1:5]

        if " took its attacker down with it!" in dbond_lines[0]:
            killer_nickname = dbond_lines[0].split(" took its attacker down with it!")[0]
            print(killer_nickname + " got a DIRECT kill on " + pokemon_nickname + " with Destiny Bond!")
            kill_line = dbond_lines[0]
            
    
    print(kill_line)
        
    print(pokemon_nickname + " fainted!")
    print()
