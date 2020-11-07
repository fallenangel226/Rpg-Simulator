"""
This is WorldRPG's main script. Everything starts and ends right here

"""

# Imported Modules
from logistics import *
from Interface import *
import Encounter
import Character
import time


# Main Script

# This class manages gameplay aspects of combat
class Gameplay:
    def __init__(self):
        self.play = Character.Attributes(None)
        self.opponent = {}
        self.player = {}
        self.dice_roll = Combat
        self.player_counter = None
        self.opponent_counter = None
        self.combat_counter = None

    def firststrike(self):
        self.dice_roll = Combat()
        builder = Encounter.OpponentBuilder()
        self.player = self.play.characterbuilder()
        self.opponent = builder.monstermaker(self.player["level"])
        first = self.dice_roll.d20
        if first >= 11:
            print("Player has first strike.")
            start.playerturn()
        else:
            print("Opponent has first strike.")
            time.sleep(1)
            print("Player Stats:\n", self.player)
            print("Opponent stats:\n", self.opponent)
            time.sleep(1)
            start.opponentturn()

    # This function controls the users turn. It allows the user to choose which action to perform
    # and then calls to the corresponding function in the data manipulation module
    def playerturn(self):
        self.dice_roll = Combat()
        self.player_counter = None
        time.sleep(2)
        print("Player Stats:\n", self.player)
        print("Opponent stats:\n", self.opponent)
        selection = str(input("1. Attack \n"
                              "2. Defend \n"
                              "3. Spell \n"
                              "4. Escape \n"))
        # Call to logistics module's attack function
        if selection == "1":
            time.sleep(2)
            self.combat_counter = self.dice_roll.attack(self.player, self.opponent)
            if self.combat_counter is None:
                print("Your attack was unsuccessful")
                start.opponentturn()
            else:
                if self.opponent_counter is None:
                    self.opponent["health"] -= self.combat_counter
                    print("You attack your opponent for ", self.combat_counter, " damage.")
                    time.sleep(1)
                    self.combat_counter = None
                    start.deathcheck(self.opponent["health"])
                    start.opponentturn()
                else:
                    print("Your opponent was defending...")
                    time.sleep(1)
                    self.player_counter = self.combat_counter - self.opponent_counter
                    if self.player_counter > 0:
                        self.opponent["health"] -= self.player_counter
                        print(self.player_counter, " damage makes it through your opponents defence.")
                        self.combat_counter = None
                        self.opponent_counter = None
                        self.player_counter = None
                        start.deathcheck(self.opponent["health"])
                        start.opponentturn()
                    else:
                        print("your opponents defence canceled your attack.")
                        self.combat_counter = None
                        self.opponent_counter = None
                        self.player_counter = None
                        start.opponentturn()
        # Call to logistics module's defend function
        elif selection == "2":
            time.sleep(2)
            self.player_counter = self.dice_roll.defend(self.player, self.opponent)
            if self.player_counter is not None:
                print("You are successfully blocking your opponents next turn.")
                start.opponentturn()
            else:
                print("Your block was unsuccessful.")
                start.opponentturn()
        # Call to logistics module's spell function
        # FIXME: calls to a function that hasn't been built
        elif selection == "3":
            time.sleep(1)
            print("Under construction")
            start.opponentturn()
        # Call to logistics module's escape function
        elif selection == "4":
            time.sleep(2)
            escape = self.dice_roll.escape()
            if escape is True:
                print("You successfully evaded your opponent.")
                self.player["health"] = 100
                start.firststrike()
            else:
                print("You failed to avoid capture.")
                start.opponentturn()
        else:
            time.sleep(2)
            print("please enter the number only.")
            start.playerturn()

    # This function facilitates the automation of the opponents turn in conjunction to the users turn.
    # This call to the same corresponding functions in the data manipulation module.
    def opponentturn(self):
        self.dice_roll = Combat()

        self.opponent_counter = None
        print("Your Opponent is deciding what to do......")
        time.sleep(3)
        selection = self.dice_roll.d20
        # Call to logistics module's spell function
        # FIXME: calls to a function that hasn't been built
        if selection <= 6:
            time.sleep(2)
            print("Opponent tried to cast a broken spell.")
            start.playerturn()
        #  Call to logistics module's defend function
        elif selection <= 12:
            time.sleep(2)
            self.opponent_counter = self.dice_roll.defend(self.player, self.opponent)
            if self.opponent_counter is not None:
                print("Your opponent prepares to defend themselves.")
                start.playerturn()
            else:
                print("Your opponent tried to defend but failed.")
                start.playerturn()
        # Call to logistics module's attack function
        elif selection > 12:
            time.sleep(2)
            self.combat_counter = self.dice_roll.attack(self.opponent, self.player)
            if self.combat_counter is None:
                print("Your opponent's attack was unsuccessful")
                start.playerturn()
            else:
                if self.player_counter is None:
                    self.player["health"] -= self.combat_counter
                    print("Your opponent attacks you for ", self.combat_counter, " damage.")
                    self.combat_counter = None
                    start.deathcheck(self.player["health"])
                    start.playerturn()
                else:
                    print("You are defending against your opponents attack...")
                    time.sleep(1)
                    self.opponent_counter = self.combat_counter - self.player_counter
                    if self.opponent_counter > 0:
                        self.player["health"] -= self.opponent_counter
                        print(self.opponent_counter, " damage makes it through your defence.")
                        self.combat_counter = None
                        self.opponent_counter = None
                        self.player_counter = None
                        start.deathcheck(self.player["health"])
                        start.playerturn()
                    else:
                        print("your defence canceled your opponent's attack.")
                        self.combat_counter = None
                        self.opponent_counter = None
                        self.player_counter = None
                        start.playerturn()

    def deathcheck(self, health):
        currenthealth = health
        if currenthealth <= 0:
            time.sleep(2)
            if self.player["health"] <= 0:
                print("You have died")
            elif self.opponent["health"] <= 0:
                print("You have killed your opponent")
                self.play.base_attributes[6] += 25
                levelcheck = Character.Inplay()
                player_update = levelcheck.levelup(self.play.base_attributes)
                self.play = Character.Attributes(player_update)
                self.player = self.play.characterbuilder()
            else:
                pass
            time.sleep(1)
            next_battle = int(input("Start new battle?\n1.Yes? 2.No?\n"))
            if next_battle == 1:
                self.opponent["health"] = 100
                start.firststrike()
            elif next_battle == 2:
                exit()
            else:
                print("I didn't understand.\nPlease enter a number.")
                start.deathcheck(currenthealth)
        else:
            return


if __name__ == "__main__":
    start = Gameplay()
    start.firststrike()








