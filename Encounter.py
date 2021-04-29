"""
This modules handles all encounter variables such as monster creation, item drop, experience gain, etc
FIXME: Change monstermaker to accept a second input of a dice roll created in the logistics modules chance function
FIXME: then remove the chance function out of this module. Update the leveler function to increase/decrease exp drops
FIXME: for each monster. Possibly make exp random, or loosely reliant upon the specific build characteristics like
FIXME: weapon type or some other random choice like that. Add in a random currency drop to implement store
FIXME: system and inventory controller

"""
# Import statements
from random import randint


# This class controls the creation of monsters for each new battle
class OpponentBuilder:
    # This function builds the new opponents stat tree then returns that tree back to main for use in the combat
    # class of this module
    def monstermaker(self, level):
        # This function increases opponent stats to keep the game balanced when the player's level
        # increases past level 5
        def leveler(stats):
            creature_stats = stats
            creature_stats["level"] += 1
            creature_stats["health"] += 10
            creature_stats["attack"] += 2
            creature_stats["defence"] += 2
            creature_stats["magic"] += 2
            return creature_stats

        # This function selects the monster from the given land type
        def newmonster(land, roll):
            monster_list = land
            creature = None
            dice_roll = roll
            if dice_roll <= 33:
                creature = monster_list[0]
            elif dice_roll <= 66:
                creature = monster_list[1]
            elif dice_roll >= 67:
                creature = monster_list[2]
            else:
                pass
            stat_tree["type"] = creature[0]
            stat_tree["health"] = creature[1]
            stat_tree["attack"] = creature[2]
            stat_tree["defence"] = creature[3]
            stat_tree["magic"] = creature[4]
            stat_tree["exp"] = creature[6]
            return creature[5]

        # This function controls the dice roll for monster selection
        def chance():
            # Die roll 1 determines a value between 0-9
            d10 = randint(0, 9)
            cast1 = d10
            # Die roll 2 determines a value between 0-9 then multiplies it by 10
            d10 = randint(0, 9)
            cast2 = d10
            castcorr = cast2 * 10
            # Combines roll1 and roll2 to create the chance percentage
            percent = cast1 + castcorr
            return percent

        # Variable declarations
        player_level = level
        stat_tree = {"level": 1,
                     "type": None,
                     "health": 100,
                     "attack": None,
                     "defence": None,
                     "magic": None,
                     "weapon": None,
                     "exp": None,
                     "land": None,
                     "defence counter": None}
        weapon_list = []
        percentile = chance()
        monsters = {"mountain": (("Kobold", 75, 3, 2, 0, ("sword", "axe", "mace"), 30),
                                 ("Dwarf", 100, 2, 3, 0, ("hammer", "mace", None), 45),
                                 ("Goblin", 50, 4, 1, 0, ("sword", "axe", "dagger"), 25)),
                    "forest": (("Wurm", 100, 4, 1, 0, (None, None, None), 37),
                               ("Spider", 75, 2, 3, 0, (None, None, None), 49),
                               ("Sprite", 50, 1, 2, 2, ("dagger", "sword", None), 20)),
                    "swamp": (("Bat", 50, 2, 3, 0, (None, None, None), 15),
                              ("Rat", 50, 3, 2, 0, (None, None, None), 20),
                              ("Skeleton", 75, 2, 1, 2, ("sword", "mace", "axe"), 45)),
                    "plains": (("Giant", 110, 3, 2, 0, ("sword", "mace", "axe"), 65),
                               ("Knight", 100, 2, 3, 0, ("sword", "axe", None), 50),
                               ("Priest", 50,  0, 2, 3, (None, None, None), 25)),
                    "island": (("Flayer", 50, 0, 1, 4, (None, None, None), 15),
                               ("Octopus", 75, 4, 1, 0, (None, None, None), 35),
                               ("Eagle", 100, 3, 2, 0, (None, None, None), 59))}
        # this selects which dictionary key to send into the newmonster function
        if percentile <= 20:
            percentile = chance()
            weapon_list = newmonster(monsters.get("mountain"), percentile)
            stat_tree["land"] = "mountain"
        elif percentile <= 40:
            percentile = chance()
            weapon_list = newmonster(monsters.get("forest"), percentile)
            stat_tree["land"] = "forest"
        elif percentile <= 60:
            percentile = chance()
            weapon_list = newmonster(monsters.get("swamp"), percentile)
            stat_tree["land"] = "swamp"
        elif percentile <= 80:
            percentile = chance()
            weapon_list = newmonster(monsters.get("plains"), percentile)
            stat_tree["land"] = "plains"
        elif percentile >= 81:
            percentile = chance()
            weapon_list = newmonster(monsters.get("island"), percentile)
            stat_tree["land"] = "island"
        else:
            print("something broke in monster maker!")
            exit()
        percentile = chance()
        if percentile <= 33:
            stat_tree["weapon"] = weapon_list[0]
        elif percentile <= 66:
            stat_tree["weapon"] = weapon_list[1]
        elif percentile >= 67:
            stat_tree["weapon"] = weapon_list[2]
        else:
            print("something broke in weapon selection")
            exit()
        if player_level >= 5:
            lvl_die_roll = randint(0, player_level)
            while lvl_die_roll >= 1:
                stat_tree = leveler(stat_tree)
                lvl_die_roll -= 1
        else:
            pass
        return stat_tree
