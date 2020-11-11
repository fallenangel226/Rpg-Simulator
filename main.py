"""
This is WorldRPG's main script. Everything starts and ends right here
"""

# Imported Modules
from logistics import *
from tkinter import *
import tkinter.font as tkfont
import Encounter
import Character
import time


# Main Script
# This class runs the game. It handles all calls out other modules and creates the user interface.
class Interface(Frame):
    def __init__(self, master=None):
        self.player_builder = Character.Attributes()
        self.player_attributes = None
        self.player = self.player_builder.characterbuilder()
        self.opponent = {}
        self.prompt_list = [None, None]

        Frame.__init__(self, master)
        self.text_font: tkfont = tkfont.Font(size=14)
        self.text_font2: tkfont = tkfont.Font(size=20)
        self.master = master
        self.master.geometry("1000x800")
        self.master.title("WorldRPG")
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=None)
        filemenu.add_command(label="Open", command=None)
        filemenu.add_command(label="Save", command=None)
        # Adds a solid line in the file menu after save and before exit
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)
        # Builds the drop down menu for "File"
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)
        self.main_frame = Frame(self.master, width=800, height=1000)
        self.main_frame.pack()

    # This function handles all turn based stat tree adjustments and disyplay prompts for both player and
    # opponents.
    def gameprogression(self, player, opp, action):
        player = player
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
                prompt_selection = [["Your attack was unsuccessful", None],
                                    ["Your opponent's attack was unsuccessful", None]]
                results.append(prompt_selection[prompt_return][0])
                results.append(prompt_selection[prompt_return][1])

            else:
                if opponent_counter is None:
                    opponent["health"] -= combat_counter
                    prompt_selection = [["You attack your opponent for " + str(combat_counter) + " damage.", None],
                                        ["Your opponent attacks you for " + str(combat_counter) + " damage.",
                                         None]]
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
                prompt_selection = [["You are successfully blocking your opponents next turn.", None],
                                    ["Your opponent prepares to defend themselves.", None]]
                results.append(prompt_selection[prompt_return][0])
                results.append(prompt_selection[prompt_return][1])
            else:
                prompt_selection = [["Your block was unsuccessful.", None],
                                    ["Your opponent tried to defend but failed.", None]]
                results.append(prompt_selection[prompt_return][0])
                results.append(prompt_selection[prompt_return][1])
        # Call to logistics module's spell function
        # FIXME: calls to a function that hasn't been built
        elif selection == 3:
            results.append("Under construction")
            results.append(None)
        # Call to logistics module's escape function
        elif selection == 4:
            escape = dice_roll.escape()
            if escape is True:
                player["health"] = self.player_builder.base_attributes[1]
                self.prompt_list[0] = "You successfully evaded your opponent."
                self.main_frame.destroy()
                self.nxt_window()
            else:
                results.append("You failed to avoid capture.")
                results.append(None)
        else:
            print("Something broke!")
        return results

    # This function runs gameprogression and deathcheck as the opponent
    def opponentaction(self):
        results = self.gameprogression(self.opponent, self.player, None)
        self.deathcheck(results[1])
        self.player = results[1]
        self.opponent = results[0]
        self.prompt_list = [results[2], results[3]]
        self.main_frame.destroy()
        self.game_window(True)

    # this function runs gameprogression and deathcheck as the player
    def playeraction(self, choice):
        results = self.gameprogression(self.player, self.opponent, choice)
        self.deathcheck(results[1])
        self.player = results[0]
        self.opponent = results[1]
        self.prompt_list = [results[2], results[3]]
        self.main_frame.destroy()
        self.game_window(False)

    # Determines who has first turn at start of new battle
    def firststrike(self):
        opponent_builder = Encounter.OpponentBuilder()
        self.opponent = opponent_builder.monstermaker(self.player["level"])
        dice_roll = Combat()
        first = dice_roll.d20
        if first >= 11:
            self.prompt_list[0] = "Player has first strike."
            self.main_frame.destroy()
            self.game_window(True)

        else:
            self.prompt_list[0] = "Opponent has first strike."
            self.main_frame.destroy()
            self.game_window(False)

    # Status check to determine if anyone died, and if so who. Then runs the corresponding script
    def deathcheck(self, health):
        defending = health["health"]
        if defending <= 0:
            if self.player["health"] <= 0:
                self.prompt_list[0] = "You have died"
                self.player_builder = Character.Attributes()
                self.player = self.player_builder.characterbuilder()
                self.main_frame.destroy()
                self.nxt_window()
            elif self.opponent["health"] <= 0:
                self.prompt_list[0] = "You have killed your opponent"
                self.player["exp"] += self.opponent["exp"]
                player_update = self.player_builder.levelup(self.player)
                self.player = player_update[0]
                self.prompt_list[1] = player_update[1]
                self.main_frame.destroy()
                self.nxt_window()
            else:
                pass
        else:
            return
    # First game window
    def init_window(self):
        container = Frame(self.main_frame, bg="green", width=1000, height=600)
        container2 = Frame(self.main_frame, bg="black", width=1000, height=200)
        text1 = Label(container, bg="green", text="New game?", font=self.text_font2)
        text2 = Label(container, bg="green", text=self.prompt_list[1], font=self.text_font)
        text3 = Label(container, bg="green", text=self.prompt_list[0], font=self.text_font2)
        yes_button = Button(container2, text="Yes", width=20, height=10, command=lambda: self.firststrike())
        no_button = Button(container2, text="No", width=20, height=10, command=exit)

        text3.place(x=500, y=400, anchor=S)
        text2.place(x=500, y=100, anchor=S)
        text1.place(x=500, y=300, anchor=S)
        yes_button.place(x=260, y=20)
        no_button.place(x=600, y=20)
        container.pack(side=TOP)
        container2.pack(side=BOTTOM)
        self.master.mainloop()

    # Next opponent game window.
    def nxt_window(self):
        self.main_frame = Frame(self.master, width=800, height=1000)
        self.main_frame.pack()
        container = Frame(self.main_frame, bg="green", width=1000, height=600)
        container2 = Frame(self.main_frame, bg="black", width=1000, height=200)
        text1 = Label(container, bg="green", text="New game?", font=self.text_font2)
        text2 = Label(container, bg="green", text=self.prompt_list[1], font=self.text_font)
        text3 = Label(container, bg="green", text=self.prompt_list[0], font=self.text_font2)
        yes_button = Button(container2, text="Yes", width=20, height=10, command=lambda: self.firststrike())
        no_button = Button(container2, text="No", width=20, height=10, command=exit)

        text3.place(x=500, y=400, anchor=S)
        text2.place(x=500, y=100, anchor=S)
        text1.place(x=500, y=300, anchor=S)
        yes_button.place(x=260, y=20)
        no_button.place(x=600, y=20)
        container.pack(side=TOP)
        container2.pack(side=BOTTOM)
        self.master.mainloop()

    # Main game window
    def game_window(self, turn):
        prompt1 = "Player's Stats\nLevel: " + str(self.player["level"]) + "   " \
                  "Health: " + str(self.player["health"]) + "   Attack: " + str(self.player["attack"]) + "   " \
                  "Defense: " + str(self.player["defence"]) + "   Magic: " + str(self.player["magic"]) + "   " \
                  "Weapon: " + str(self.player["weapon"]) + "   EXP: " + str(self.player["exp"])
        prompt2 = str(self.opponent["type"]) + "'s Stats\nLevel: " + str(self.opponent["level"]) + "   " \
                  "Health: " + str(self.opponent["health"]) + "   Attack: " + str(self.opponent["attack"]) + "   " \
                  "Defense: " + str(self.opponent["defence"]) + "   Magic: " + str(self.opponent["magic"]) + "   " \
                  "Weapon: " + str(self.opponent["weapon"]) + "   Land Type: " + str(self.opponent["land"])
        prompt3 = self.prompt_list[0]
        prompt4 = self.prompt_list[1]
        self.main_frame = Frame(self.master, width=800, height=1000)
        self.main_frame.pack()
        container = Frame(self.main_frame, bg="green", width=1000, height=600)
        container2 = Frame(self.main_frame, bg="black", width=1000, height=200)
        button_frame = Frame(container2, bg="black", width=1000, height=200)
        temp_frame = Frame(container2, bg="black", width=1000, height=200)
        text1 = Label(container, bg="green", text=prompt1, font=self.text_font)
        text2 = Label(container, bg="green", text=prompt2, font=self.text_font)
        text3 = Label(container, bg="green", text=prompt3, font=self.text_font2)
        text4 = Label(container, bg="green", text=prompt4, font=self.text_font2)
        text5 = Label(container2, bg="black", fg="white",
                      text="Opponent is deciding what to do....", font=self.text_font2)
        attack_button = Button(button_frame, text="Attack", width=13, height=6,
                               command=lambda: self.playeraction(1), font=self.text_font)
        defend_button = Button(button_frame, text="Defend", width=13, height=6,
                               command=lambda: self.playeraction(2), font=self.text_font)
        spell_button = Button(button_frame, text="Cast\nSpell", width=13, height=6,
                              command=lambda: self.playeraction(3), font=self.text_font)
        escape_button = Button(button_frame, text="Escape", width=13, height=6,
                               command=lambda: self.playeraction(4), font=self.text_font)
        opp_button = Button(temp_frame, text="Opponents turn", width=40, height=5,
                            command=lambda: self.opponentaction(), font=self.text_font)
        if turn is True:
            button_frame.pack()
        else:
            temp_frame.pack()

        text1.place(x=500, y=100, anchor=S)
        text2.place(x=500, y=200, anchor=S)
        text3.place(x=500, y=300, anchor=S)
        text4.place(x=500, y=400, anchor=S)

        attack_button.place(x=100, y=20, anchor=N)
        defend_button.place(x=300, y=20, anchor=N)
        spell_button.place(x=700, y=20, anchor=N)
        escape_button.place(x=900, y=20, anchor=N)
        opp_button.place(x=500, y=20, anchor=N)

        container.pack(side=TOP)
        container2.pack(side=BOTTOM)
        self.master.mainloop()


if __name__ == "__main__":
    root = Tk()
    game = Interface(root)
    game.init_window()
