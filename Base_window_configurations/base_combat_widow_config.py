from tkinter import *
import tkinter.font as tkfont
from tkinter.ttk import Progressbar
from tkinter.ttk import Style


class Interface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1000x800")
        self.master.title("WorldRPG")
        self.master.resizable(False, False)
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
        self.main_frame.pack(fill=BOTH, expand=TRUE)

    def game_window(self):
        # Variables
        opp_name_text = "Name: Opponent"
        opp_level_text = "Level: "
        player_name_text = "Name: Player"
        player_level_text = "Level: "

        opp_effects_att_text = "Attack: "
        opp_effects_def_text = "Defense: "
        opp_effects_mag_text = "Magic: "
        opp_effects_weapon_text = "Weapon: "
        player_effects_att_text = "Attack: "
        player_effects_def_text = "Defense: "
        player_effects_mag_text = "Magic: "
        player_effects_weapon_text = "Weapon: "

        opp_action_prompt1_text = "Opponent first action prompt"
        opp_action_prompt2_text = "Opponent second action prompt"
        player_action_prompt1_text = "Player first action prompt"
        player_action_prompt2_text = "player second action prompt"

        # Progressbar styling
        bar_style = Style()
        bar_style.theme_use("clam")
        bar_style.configure("Horizontal.TProgressbar", background="darkolivegreen", bordercolor="black")

        # Font styling
        info_font: tkfont = tkfont.Font(size=14, family="Windings")
        info_font2: tkfont = tkfont.Font(size=12, family="Windings")
        prompt_font: tkfont = tkfont.Font(size=20, slant="italic", family="David")
        effects_font: tkfont = tkfont.Font(size=13, underline=1, weight="bold", family="Windings")
        effects_font2: tkfont = tkfont.Font(size=10, family="Windings")
        button_font: tkfont = tkfont.Font(size=11, family="Helvetica Bold Round")

        # Main window frame configurations
        main_container = Frame(self.main_frame, width=800, height=1000, bg="black")
        opponent_frame = Frame(main_container, width=800, height=325, bg="burlywood4",
                               highlightbackground="black", highlightthickness=8)
        player_frame = Frame(main_container, width=800, height=425, bg="burlywood4",
                             highlightbackground="black", highlightthickness=8)
        main_container.pack(fill=BOTH, expand=TRUE)
        opponent_frame.pack(fill=BOTH, expand=TRUE)
        player_frame.pack(fill=BOTH, expand=TRUE)
        opponent_frame.grid_columnconfigure((1, 2, 3), weight=1, minsize=200)
        opponent_frame.grid_columnconfigure(4, minsize=5)
        opponent_frame.grid_rowconfigure((1, 2, 3), weight=1)
        player_frame.grid_columnconfigure((1, 2, 3), weight=1, minsize=200)
        player_frame.grid_columnconfigure(4, minsize=5)
        player_frame.grid_rowconfigure((1, 2, 3), weight=1)

        # Opponent frame sub frame configurations
        opp_info = Frame(opponent_frame, width=500, height=75, bg="burlywood3",
                         highlightthickness=3, highlightbackground="black")
        opp_info.grid_columnconfigure((1, 2), minsize=200)
        opp_info.grid_columnconfigure(3, minsize=10)
        opp_info.grid_rowconfigure((1, 2), weight=1)
        opp_info.grid_rowconfigure(3, minsize=10)
        opp_prompt = LabelFrame(opponent_frame, width=725, height=225,
                                highlightthickness=3, highlightbackground="black", bg="burlywood3")
        opp_prompt.grid_columnconfigure(2, weight=3, minsize=705)
        opp_prompt.grid_columnconfigure((1, 3), minsize=10)
        opp_prompt.grid_rowconfigure((2, 3), weight=2, minsize=102)
        opp_prompt.grid_rowconfigure((1, 4), minsize=10)
        opp_effects = Frame(opponent_frame, width=200, height=375,
                            highlightthickness=3, highlightbackground="black", bg="burlywood3")
        opp_effects.grid_columnconfigure(2, weight=2)
        opp_effects.grid_columnconfigure((1, 3), minsize=10)
        opp_effects.grid_rowconfigure((2, 10, 15), weight=2)
        opp_effects.grid_rowconfigure((4, 5, 6, 7, 8, 12, 13, 17, 18), weight=1)
        opp_effects.grid_rowconfigure((1, 19), minsize=10)
        opp_effects.grid_rowconfigure((3, 9, 11, 14, 16), minsize=5)
        opp_info.grid(row=0, column=1, columnspan=3)
        opp_prompt.grid(row=1, column=1, columnspan=2, rowspan=2, sticky=E)
        opp_effects.grid(row=0, column=3, rowspan=3)

        # Player frame sub frame configurations
        player_info = Frame(player_frame, width=550, height=75,
                            highlightthickness=3, highlightbackground="black", bg="burlywood3")
        player_info.grid_columnconfigure((1, 2), minsize=200)
        player_info.grid_columnconfigure(3, minsize=10)
        player_info.grid_rowconfigure((1, 2), weight=1)
        player_info.grid_rowconfigure(3, minsize=10)
        player_prompt = LabelFrame(player_frame, width=725, height=225,
                                   highlightthickness=3, highlightbackground="black", bg="burlywood3")
        player_prompt.grid_columnconfigure(2, weight=3, minsize=705)
        player_prompt.grid_columnconfigure((1, 3), minsize=10)
        player_prompt.grid_rowconfigure((2, 3), weight=2, minsize=102)
        player_prompt.grid_rowconfigure((1, 4), minsize=10)
        player_effects = LabelFrame(player_frame, width=200, height=300,
                                    highlightthickness=3, highlightbackground="black", bg="burlywood3")
        player_effects.grid_columnconfigure(2, weight=2)
        player_effects.grid_columnconfigure((1, 3), minsize=10)
        player_effects.grid_rowconfigure((2, 10, 15), weight=2)
        player_effects.grid_rowconfigure((4, 5, 6, 7, 8, 12, 13, 17, 18), weight=1)
        player_effects.grid_rowconfigure((1, 19), minsize=10)
        player_effects.grid_rowconfigure((3, 9, 11, 14, 16), minsize=5)
        button_frame = Frame(player_frame, width=700, height=50,
                             highlightthickness=3, highlightbackground="black", bg="black")
        button_frame.grid_columnconfigure((2, 4, 6, 8, 10), weight=1)
        button_frame.grid_columnconfigure((1, 11), minsize=15)
        button_frame.grid_columnconfigure((3, 5, 7, 9), minsize=5)
        button_frame.grid_rowconfigure(2, weight=2)
        button_frame.grid_rowconfigure((1, 3), minsize=5)
        player_info.grid(row=0, column=1, columnspan=3)
        player_prompt.grid(row=1, column=1, columnspan=2, rowspan=1, sticky=E)
        player_effects.grid(row=0, column=3, rowspan=2)
        button_frame.grid(row=2, column=1, columnspan=3, sticky=S)

        # Opponent info frame widget configurations
        opp_info_subframe = Frame(opp_info, width=575, height=25, bg="burlywood3")
        opp_info_subframe.grid_columnconfigure(1, minsize=10)
        opp_info_subframe.grid_columnconfigure((2, 3), weight=1)
        opp_info_subframe.grid_columnconfigure(4, minsize=20)
        opp_info_subframe.grid_columnconfigure((5, 6), weight=2)
        opp_name = Label(opp_info, text=opp_name_text, font=info_font, bg="burlywood3")
        opp_level = Label(opp_info, text=opp_level_text, font=info_font, bg="burlywood3")
        opp_hpbar_label = Label(opp_info_subframe, text="HP ", font=info_font2, bg="burlywood3")
        opp_mpbar_label = Label(opp_info_subframe, text="MP ", font=info_font2, bg="burlywood3")
        opp_hp_bar = Progressbar(opp_info_subframe, orient=HORIZONTAL, length=200, mode="determinate")
        opp_mp_bar = Progressbar(opp_info_subframe, orient=HORIZONTAL, length=200, mode="determinate")
        opp_name.grid(row=0, column=1, sticky=W)
        opp_level.grid(row=0, column=2, sticky=W)
        opp_info_subframe.grid(row=1, column=1, columnspan=2, sticky=W)
        opp_hpbar_label.grid(row=0, column=2)
        opp_hp_bar.grid(row=0, column=3)
        opp_mpbar_label.grid(row=0, column=5)
        opp_mp_bar.grid(row=0, column=6)

        # Player info frame widget configurations
        player_info_subframe = Frame(player_info, width=575, height=25, bg="burlywood3")
        player_info_subframe.grid_columnconfigure(1, minsize=10)
        player_info_subframe.grid_columnconfigure((2, 3), weight=1)
        player_info_subframe.grid_columnconfigure(4, minsize=20)
        player_info_subframe.grid_columnconfigure((5, 6), weight=2)
        player_name = Label(player_info, text=player_name_text, font=info_font, bg="burlywood3")
        player_level = Label(player_info, text=player_level_text, font=info_font, bg="burlywood3")
        player_hpbar_label = Label(player_info_subframe, text="HP ", font=info_font2, bg="burlywood3")
        player_mpbar_label = Label(player_info_subframe, text="MP ", font=info_font2, bg="burlywood3")
        player_hp_bar = Progressbar(player_info_subframe, orient=HORIZONTAL, length=200, mode="determinate",
                                    style="hp_bar_style.Horizontal.TProgressbar")
        player_mp_bar = Progressbar(player_info_subframe, orient=HORIZONTAL, length=200, mode="determinate",
                                    style="mp_bar_style.Horizontal.TProgressbar")
        player_name.grid(row=0, column=1, sticky=W)
        player_level.grid(row=0, column=2, sticky=W)
        player_info_subframe.grid(row=1, column=1, columnspan=2, sticky=W)
        player_hpbar_label.grid(row=0, column=2)
        player_hp_bar.grid(row=0, column=3)
        player_mpbar_label.grid(row=0, column=5)
        player_mp_bar.grid(row=0, column=6)

        # Opponent effects frame widget configurations
        opp_effects_title = Label(opp_effects, text="Attributes               ", font=effects_font,
                                  bg="burlywood3")
        opp_effects_att = Label(opp_effects, text=opp_effects_att_text, font=effects_font2, bg="burlywood3")
        opp_effects_def = Label(opp_effects, text=opp_effects_def_text, font=effects_font2, bg="burlywood3")
        opp_effects_mag = Label(opp_effects, text=opp_effects_mag_text, font=effects_font2, bg="burlywood3")
        opp_effects_weapon = Label(opp_effects, text=opp_effects_weapon_text, font=effects_font2, bg="burlywood3")
        opp_effects_armor = Label(opp_effects, text="armor: something", font=effects_font2, bg="burlywood3")
        opp_effects_active_title = Label(opp_effects, text="Active Effects           ", font=effects_font,
                                         bg="burlywood3")
        opp_effects_active1 = Label(opp_effects, text="active effect 1", font=effects_font2, bg="burlywood3")
        opp_effects_active2 = Label(opp_effects, text="active effect 2", font=effects_font2, bg="burlywood3")
        opp_effects_passive_title = Label(opp_effects, text="Passive Effects          ", font=effects_font,
                                          bg="burlywood3")
        opp_effects_passive1 = Label(opp_effects, text="passive effect 1", font=effects_font2, bg="burlywood3")
        opp_effects_passive2 = Label(opp_effects, text="passive effect 2", font=effects_font2, bg="burlywood3")
        opp_effects_title.grid(row=2, column=2, sticky=W)
        opp_effects_att.grid(row=4, column=2, sticky=W)
        opp_effects_def.grid(row=5, column=2, sticky=W)
        opp_effects_mag.grid(row=6, column=2, sticky=W)
        opp_effects_weapon.grid(row=7, column=2, sticky=W)
        opp_effects_armor.grid(row=8, column=2, sticky=W)
        opp_effects_active_title.grid(row=10, column=2, sticky=W)
        opp_effects_active1.grid(row=12, column=2, sticky=W)
        opp_effects_active2.grid(row=13, column=2, sticky=W)
        opp_effects_passive_title.grid(row=15, column=2, sticky=W)
        opp_effects_passive1.grid(row=17, column=2, sticky=W)
        opp_effects_passive2.grid(row=18, column=2, sticky=W)

        # Player effects frame widget configurations
        player_effects_title = Label(player_effects, text="Attributes               ", font=effects_font,
                                     bg="burlywood3")
        player_effects_att = Label(player_effects, text=player_effects_att_text, font=effects_font2,
                                   bg="burlywood3")
        player_effects_def = Label(player_effects, text=player_effects_def_text, font=effects_font2,
                                   bg="burlywood3")
        player_effects_mag = Label(player_effects, text=player_effects_mag_text, font=effects_font2,
                                   bg="burlywood3")
        player_effects_weapon = Label(player_effects, text=player_effects_weapon_text, font=effects_font2,
                                      bg="burlywood3")
        player_effects_armor = Label(player_effects, text="armor: something", font=effects_font2,
                                     bg="burlywood3")
        player_effects_active_title = Label(player_effects, text="Active Effects           ", font=effects_font,
                                            bg="burlywood3")
        player_effects_active1 = Label(player_effects, text="active effect 1", font=effects_font2, bg="burlywood3")
        player_effects_active2 = Label(player_effects, text="active effect 2", font=effects_font2, bg="burlywood3")
        player_effects_passive_title = Label(player_effects, text="Passive Effects          ", font=effects_font,
                                             bg="burlywood3")
        player_effects_passive1 = Label(player_effects, text="passive effect 1", font=effects_font2, bg="burlywood3")
        player_effects_passive2 = Label(player_effects, text="passive effect 2", font=effects_font2, bg="burlywood3")
        player_effects_title.grid(row=2, column=2, sticky=W)
        player_effects_att.grid(row=4, column=2, sticky=W)
        player_effects_def.grid(row=5, column=2, sticky=W)
        player_effects_mag.grid(row=6, column=2, sticky=W)
        player_effects_weapon.grid(row=7, column=2, sticky=W)
        player_effects_armor.grid(row=8, column=2, sticky=W)
        player_effects_active_title.grid(row=10, column=2, sticky=W)
        player_effects_active1.grid(row=12, column=2, sticky=W)
        player_effects_active2.grid(row=13, column=2, sticky=W)
        player_effects_passive_title.grid(row=15, column=2, sticky=W)
        player_effects_passive1.grid(row=17, column=2, sticky=W)
        player_effects_passive2.grid(row=18, column=2, sticky=W)

        # Opponent prompt frame widget configurations
        opp_action_prompt1 = Label(opp_prompt, text=opp_action_prompt1_text, font=prompt_font, bg="burlywood3")
        opp_action_prompt2 = Label(opp_prompt, text=opp_action_prompt2_text, font=prompt_font, bg="burlywood3")
        opp_action_prompt1.grid(row=2, column=2)
        opp_action_prompt2.grid(row=3, column=2)

        # Player prompt frame widget configurations
        player_action_prompt1 = Label(player_prompt, text=player_action_prompt1_text, font=prompt_font, bg="burlywood3")
        player_action_prompt2 = Label(player_prompt, text=player_action_prompt2_text, font=prompt_font, bg="burlywood3")
        player_action_prompt1.grid(row=2, column=2)
        player_action_prompt2.grid(row=3, column=2)

        # Button frame widget configurations
        attack_button = Button(button_frame, text="Attack", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        defend_button = Button(button_frame, text="Defend", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        spells_button = Button(button_frame, text="Cast", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        escape_button = Button(button_frame, text="Escape", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        item_button = Button(button_frame, text="Inventory", width=15, height=2, font=button_font,
                             fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        attack_button.grid(row=2, column=2)
        defend_button.grid(row=2, column=4)
        spells_button.grid(row=2, column=6)
        escape_button.grid(row=2, column=8)
        item_button.grid(row=2, column=10)

        self.master.mainloop()


if __name__ == "__main__":
    root = Tk()
    game = Interface(root)
    game.game_window()
