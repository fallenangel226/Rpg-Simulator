"""
This modules holds all character attributes and facilitates character creations

"""


# This class handles the creation of the the player's character stat tree.
class Attributes:
    # Initializer for character stats. this will be loaded either from a saved file or from the creation of a
    # new character. This also gets updated whenever a player levels up.
    def __init__(self, attributes):
        if attributes is None:
            self.base_attributes = [1, 100, 2, 3, 0, "sword", 90]
        else:
            self.base_attributes = attributes

    # This function builds the player's stat tree after the stats have been updated, loaded, or at the
    # start of a new character.
    def characterbuilder(self):
        stat_tree = {"level": self.base_attributes[0],
                     "health": self.base_attributes[1],
                     "attack": self.base_attributes[2],
                     "defence": self.base_attributes[3],
                     "magic": self.base_attributes[4],
                     "weapon": self.base_attributes[5],
                     "exp": self.base_attributes[6]}
        return stat_tree


# This class controls any manipulation of the players stats throughout the game.
class Inplay:
    # This function serves to level up the player when the correct amount of experience points have be acquired.
    def levelup(self, player):
        attributes = player
        exp_needed = int((((attributes[0] + 1) * attributes[0]) / 2) * 100)

        if attributes[6] >= exp_needed:
            attributes[0] += 1
            attributes[1] += 10
            attributes[2] += 2
            attributes[3] += 2
            attributes[4] += 2
            print("You have leveled up.")
            return attributes
        else:
            print("exp needed for next level: ", exp_needed)
            return attributes
