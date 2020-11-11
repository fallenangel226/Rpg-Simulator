"""
This modules holds all character attributes and facilitates character creations

"""


# This class handles the creation of the the player's character stat tree.
class Attributes:
    # Initializer for character stats. this will be loaded either from a saved file or from the creation of a
    # new character. This also gets updated whenever a player levels up.
    def __init__(self, attributes=None):
        if attributes is None:
            self.base_attributes = [1, 100, 2, 3, 0, "sword", 0, None]
        else:
            self.base_attributes = attributes

    # This function builds the player's stat tree after the stats have been updated, loaded, or at the
    # start of a new character.
    def characterbuilder(self, exp=None):
        stat_tree = {"level": self.base_attributes[0],
                     "health": self.base_attributes[1],
                     "attack": self.base_attributes[2],
                     "defence": self.base_attributes[3],
                     "magic": self.base_attributes[4],
                     "weapon": self.base_attributes[5],
                     "exp": self.base_attributes[6],
                     "defence counter": self.base_attributes[7]}
        if exp is not None:
            stat_tree["exp"] = exp
        else:
            pass
        return stat_tree

    def levelup(self, stats):
        attributes = [stats["level"], stats["health"], stats["attack"], stats["defence"], stats["magic"],
                      stats["weapon"], stats["exp"], stats["defence counter"]]
        exp_needed = int((((attributes[0] + 1) * attributes[0]) / 2) * 100)

        if attributes[6] >= exp_needed:
            self.base_attributes[0] += 1
            self.base_attributes[1] += 10
            self.base_attributes[2] += 2
            self.base_attributes[3] += 2
            self.base_attributes[4] += 2
            stat_tree = self.characterbuilder(attributes[6])
            return [stat_tree, "You have leveled up."]
        else:
            stat_tree = {"level": attributes[0],
                         "health": attributes[1],
                         "attack": attributes[2],
                         "defence": attributes[3],
                         "magic": attributes[4],
                         "weapon": attributes[5],
                         "exp": attributes[6],
                         "defence counter": attributes[7]}
            return [stat_tree, "Exp needed for next level: " + str(exp_needed - attributes[6])]




