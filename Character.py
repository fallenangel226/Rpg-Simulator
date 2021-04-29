"""
This modules holds all character attributes and facilitates character creations and basic inventory. The inventory
part will be moved to its own module to be able to implement item stores and potentially a crafting system. This module
also handles player leveling though only in basic form. That will be redesigned to allow player to distribute attribute
points that are gain by their own choosing

"""


# This class handles the creation of the the player's character stat tree.
class Attributes:
    # Initializer for character stats. this will be loaded either from a saved file or from the creation of a
    # new character. This also gets updated whenever a player levels up.
    def __init__(self, attributes):
        # list layout: name, type, race, level, health, attack, defense, magic
        self.base_attributes = [attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6], attributes[7]]

    # This function builds the player's stat tree after the stats have been updated, loaded, or at the
    # start of a new character.
    def characterbuilder(self, exp=None):
        stat_tree = {"name": self.base_attributes[0],
                     "type": self.base_attributes[1],
                     "race": self.base_attributes[2],
                     "level": self.base_attributes[3],
                     "health": self.base_attributes[4],
                     "attack": self.base_attributes[5],
                     "defence": self.base_attributes[6],
                     "magic": self.base_attributes[7],
                     "weapon": "sword",
                     "exp": 0,
                     "defence counter": None,
                     "spells": ["fire", "ice", "lightning"],
                     "base attributes": self.base_attributes}
        if exp is not None:
            stat_tree["exp"] = exp
        else:
            pass
        return stat_tree

    def levelup(self, stats):
        exp_needed = int((((stats["level"] + 1) * stats["level"]) / 2) * 75)
        if stats["exp"] >= exp_needed:
            self.base_attributes[3] += 1
            self.base_attributes[4] += 10
            self.base_attributes[5] += 2
            self.base_attributes[6] += 2
            self.base_attributes[7] += 2
            stat_tree = self.characterbuilder(stats["exp"])
            return [stat_tree, "You have leveled up."]
        else:
            return [stats, "Exp needed for next level: " + str(exp_needed - stats["exp"])]


# This class is used for holding and manipulating the player's inventory.
# This is just the inital implementation of the inventory system.
class Inventory:
    def __init__(self):
        self.item_type = ["Potion", "Hi-Potion"]
        self.item_amount = [5, 5, 5]

    # This function returns the attribute key and item counter for the item chosen
    def use_item(self, item_type):
        single_use_specs = {"Potion": ["health", 50],
                            "Hi-Potion": ["health", 100]}
        selected_item_spec = single_use_specs[item_type]
        self.storage(item_type)
        return selected_item_spec

    # This functions returns the contents of the player's inventory
    def storage(self, change=None):
        if change is None:
            return [self.item_type, self.item_amount]
        else:
            item_index = self.item_type.index(change)
            self.item_amount[item_index] -= 1
            return



