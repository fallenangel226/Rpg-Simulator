"""
This is WorldRPG's main script. Everything starts and ends right here
"""

# Imported Modules
from logistics import *
from tkinter import *
import Encounter
import Character
import GUI


# Main Script
# This class currently controls the character creation
class CharacterBuildController:
    def type_controller(self, selection):
        char_type = {"knight": ["Knight", 2, 0, 0],
                     "mage": ["Mage", 0, 0, 2],
                     "ranger": ["Ranger", 1, 1, 0]}
        return char_type[selection]

    def builder(self, base_attributes):
        create_character = Character.Attributes(base_attributes)
        character_stat_tree = create_character.characterbuilder()
        return character_stat_tree


# This class is the bulk of the game. This facilitates communication between all the modules
class CombatController:
    def health_check(self, player_stat, opponent):
        player = player_stat
        if player["health"] <= 0:
            prompt = "You have died"
            temp_list = [True, prompt]
            return temp_list
        elif opponent["health"] <= 0:
            build = Character.Attributes(player_stat["base attributes"])
            player["exp"] += opponent["exp"]
            prompt1 = "You have killed your opponent\nYou gain " + str(opponent["exp"]) + " experiance."
            player_update = build.levelup(player)
            temp_list = [False, player_update[0], prompt1, player_update[1]]
            return temp_list
        else:
            return

    def firststrike(self, playerlvl):
        opponent_builder = Encounter.OpponentBuilder()
        opponent = opponent_builder.monstermaker(int(playerlvl))
        dice_roll = Combat()
        first = dice_roll.d20
        if first >= 11:
            prompt = "Player has first strike."
            temp_list = [opponent, prompt, False]
            return temp_list

        else:
            prompt = "Opponent has first strike."
            temp_list = [opponent, prompt, True]
            return temp_list

    # This function handles all turn based stat tree adjustments and disyplay prompts for both player and
    # opponents.
    def action_controller(self, att, opp, action=None):
        player = att
        opponent = opp
        selection = action
        results = [player, opponent]
        player["defence counter"] = None
        opponent_counter = opponent["defence counter"]
        prompt_return = 0
        dice_roll = Combat()
        if selection is None:
            prompt_return = 1
            opp_choice = dice_roll.d20
            if opp_choice >= 13:
                selection = 1
            elif opp_choice >= 6:
                selection = 2
            elif opp_choice <= 5:
                selection = 3
            else:
                print("OPP selection error")
        else:
            pass
        # Call to logistics module's attack function
        if selection == 1:
            combat_counter = dice_roll.attack(player, opponent)
            if combat_counter is None:
                prompt_selection = [["Your attack was unsuccessful", ""],
                                    ["Your opponent's attack was unsuccessful", ""]]
                results.append(prompt_selection[prompt_return][0])
                results.append(prompt_selection[prompt_return][1])

            else:
                if opponent_counter is None:
                    opponent["health"] -= combat_counter
                    prompt_selection = [["You attack your opponent for " + str(combat_counter) + " damage.", ""],
                                        ["Your opponent attacks you for " + str(combat_counter) + " damage.",
                                         ""]]
                    results.append(prompt_selection[prompt_return][0])
                    results.append(prompt_selection[prompt_return][1])
                else:
                    player_counter = combat_counter - opponent_counter
                    if player_counter > 0:
                        opponent["health"] -= player_counter
                        prompt_selection = [
                            [str(player_counter) + " damage makes it through your opponents defence.",
                             "Your opponent was defending..."],
                            [str(opponent_counter) + " damage makes it through your defence.",
                             "You are defending against your opponents attack..."]]
                        results.append(prompt_selection[prompt_return][0])
                        results.append(prompt_selection[prompt_return][1])
                    else:
                        prompt_selection = [
                            ["your opponents defence canceled your attack.", "Your opponent was defending..."],
                            ["your defence canceled your opponent's attack.",
                             "You are defending against your opponents attack..."]]
                        results.append(prompt_selection[prompt_return][0])
                        results.append(prompt_selection[prompt_return][1])
        # Call to logistics module's defend function
        elif selection == 2:
            player_counter = dice_roll.defend(player, opponent)
            if player_counter is not None:
                player["defence counter"] = player_counter
                prompt_selection = [["You are successfully blocking your opponents next turn.", ""],
                                    ["Your opponent prepares to defend themselves.", ""]]
                results.append(prompt_selection[prompt_return][0])
                results.append(prompt_selection[prompt_return][1])
            else:
                prompt_selection = [["Your block was unsuccessful.", ""],
                                    ["Your opponent tried to defend but failed.", ""]]
                results.append(prompt_selection[prompt_return][0])
                results.append(prompt_selection[prompt_return][1])
        # Call to logistics module's spell function
        # FIXME: calls to a function that hasn't been built
        elif selection == 3:
            results.append("spells under construction")
            results.append("")
        # Call to logistics module's escape function
        elif selection == 4:
            escape = dice_roll.escape()
            if escape is True:
                player["health"] = player["base attributes"][4]
                results.append("You successfully evaded your opponent.")
                results.append("Health restored")
                results.append(True)
            else:
                results.append("You failed to avoid capture.")
                results.append("")
        else:
            print("Something broke!")
        if len(results) != 5:
            results.append(False)
        else:
            pass
        return results


if __name__ == "__main__":
    root = Tk()
    start = GUI.Interface(root)








