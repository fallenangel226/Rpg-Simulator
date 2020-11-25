import time
from tkinter import *
import tkinter.font as tkfont
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
import os
import main


class Interface(Frame):
    def __init__(self, master=None):
        self.progress = main.CombatController()
        self.create = main.CharacterBuildController()
        self.player = {}
        self.opponent = {}
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
        self.master.after(0, self.init_window())
        self.master.mainloop()

    # This is the first frame you see when the game starts. It holds options for new game, continue, load, and
    # currently a exit call. The only functional buttons are new game and exit until I implement a save and load
    # configuration.
    def init_window(self):
        # This sub function destroys this frame and calls to the character creation frame
        def new_game(self):
            main_container.after(0, self.creation_window())
            main_container.destroy()

        # Not implemented
        def continue_game(self):
            pass

        # Not implemented
        def load_game(self):
            pass

        # Font styling
        title_font: tkfont = tkfont.Font(size=35, family="David", slant="italic")
        title_font2: tkfont = tkfont.Font(size=12, family="Windings", weight="bold")
        button_font: tkfont = tkfont.Font(size=12, family="Helvetica Bold Round")
        mystic_font: tkfont = tkfont.Font(size=13, family="Vijaya", slant="italic", weight="bold")

        # Main frame configurations
        main_container = Frame(self.main_frame, bg="wheat4", width=800, height=1000)
        main_container.grid_columnconfigure(1, weight=2, minsize=300)
        main_container.grid_columnconfigure(2, weight=2, minsize=00)
        main_container.grid_rowconfigure(2, weight=2, minsize=600)
        main_container.grid_rowconfigure((1, 3), minsize=50)
        graphic_container = Frame(main_container, bg="burlywood4", width=700, height=800,
                                  highlightthickness=1, highlightbackground="black")
        graphic_container.grid_columnconfigure(2, weight=2, minsize=700)
        graphic_container.grid_columnconfigure((1, 3), minsize=10)
        graphic_container.grid_rowconfigure((2, 4), weight=2, minsize=300)
        graphic_container.grid_rowconfigure((1, 5), minsize=40)
        control_container = Frame(main_container, bg="burlywood4", width=300, height=800,
                                  highlightthickness=3, highlightbackground="black")
        control_container.grid_columnconfigure(2, weight=2, minsize=150)
        control_container.grid_columnconfigure((1, 3), minsize=10)
        control_container.grid_rowconfigure(2, weight=2, minsize=480)
        control_container.grid_rowconfigure((1, 3), minsize=50)
        pad_frame1 = Frame(main_container, width=1000, height=50, bg="darkolivegreen",
                           highlightthickness=3, highlightbackground="black", relief=RAISED)
        pad_frame1.grid_columnconfigure(2, weight=2, minsize=990)
        pad_frame1.grid_columnconfigure((1, 3), minsize=5)
        pad_frame1.grid_rowconfigure(2, weight=2, minsize=30)
        pad_frame1.grid_rowconfigure((1, 3), minsize=5)
        pad_frame2 = Frame(main_container, width=1000, height=50, bg="darkolivegreen",
                           highlightthickness=3, highlightbackground="black", relief=RAISED)
        pad_frame2.grid_columnconfigure(2, weight=2, minsize=990)
        pad_frame2.grid_columnconfigure((1, 3), minsize=5)
        pad_frame2.grid_rowconfigure(2, weight=2, minsize=30)
        pad_frame2.grid_rowconfigure((1, 3), minsize=5)
        main_container.pack(fill=BOTH, expand=TRUE)
        graphic_container.grid(row=2, column=2)
        control_container.grid(row=2, column=1)
        pad_frame1.grid(row=1, column=1, columnspan=2, sticky=N)
        pad_frame2.grid(row=3, column=1, columnspan=2, sticky=S)

        # Graphics frame sub frame configurations
        graphic_prompt_frame = Frame(graphic_container, bg="burlywood3", width=550, height=350,
                                     highlightthickness=3, highlightbackground="black")
        graphic_prompt_frame.grid_columnconfigure(2, weight=2, minsize=530)
        graphic_prompt_frame.grid_columnconfigure((1, 3), minsize=10)
        graphic_prompt_frame.grid_rowconfigure((2, 3), weight=1, minsize=165)
        graphic_prompt_frame.grid_rowconfigure((1, 4), minsize=10)
        graphic_img_frame = Frame(graphic_container, bg="burlywood3", width=350, height=250,
                                  highlightthickness=3, highlightbackground="black")
        graphic_img_frame.grid_columnconfigure(2, weight=1, minsize=330)
        graphic_img_frame.grid_columnconfigure((1, 3), minsize=10)
        graphic_img_frame.grid_rowconfigure(2, weight=1, minsize=230)
        graphic_img_frame.grid_rowconfigure((1, 3), minsize=10)
        graphic_prompt_frame.grid(row=2, column=2)
        graphic_img_frame.grid(row=4, column=2, sticky=S)

        # Control frame sub frame configurations
        control_button_frame = Frame(control_container, bg="black", width=200, height=500,
                                     highlightthickness=3, highlightbackground="black")
        control_button_frame.grid_columnconfigure(2, weight=1)
        control_button_frame.grid_columnconfigure((1, 3), minsize=5)
        control_button_frame.grid_rowconfigure((2, 4, 6, 8), weight=2)
        control_button_frame.grid_rowconfigure((1, 9), minsize=45)
        control_button_frame.grid_rowconfigure((3, 5, 7), minsize=15)
        control_button_frame.grid(row=2, column=2)

        # Padding frame sub frame configurations
        pad_frame1_subframe = Frame(pad_frame1, width=945, height=40)
        pad_frame1_subframe.grid_columnconfigure(2, weight=1)
        pad_frame2_subframe = Frame(pad_frame2, width=945, height=40)
        pad_frame1_subframe.grid(row=2, column=2)
        pad_frame2_subframe.grid(row=2, column=2)

        # Graphics frame widget configurations
        title_prompt_main = Label(graphic_prompt_frame, bg="burlywood3", text="Welcome to WorldRPG",
                                  font=title_font)
        title_prompt_sub = Label(graphic_prompt_frame, bg="burlywood3", text="by\nFallenangel226",
                                 font=title_font2)
        title_image_logo = Label(graphic_img_frame, bg="burlywood3", text="This is a place holder for game logo",
                                 font=title_font2)
        title_prompt_main.grid(row=2, column=2, sticky=S)
        title_prompt_sub.grid(row=3, column=2, sticky=N)
        title_image_logo.grid(row=2, column=2)

        # Control frame widget configurations
        new_button = Button(control_button_frame, text="New\nGame", width=9, height=4, fg="white", bg="wheat4",
                            relief=RAISED, bd=3, activebackground="burlywood3", font=button_font,
                            command=lambda: new_game(self))
        cont_button = Button(control_button_frame, text="Continue\nGame", width=9, height=4, fg="white", bg="wheat4",
                             relief=RAISED, bd=3, activebackground="burlywood3", font=button_font,
                             command=lambda: continue_game(self), state="disabled")
        load_button = Button(control_button_frame, text="Load\nGame", width=9, height=4, fg="white", bg="wheat4",
                             relief=RAISED, bd=3, activebackground="burlywood3", font=button_font,
                             command=lambda: load_game(self), state="disabled")
        exit_button = Button(control_button_frame, text="Exit\nGame", width=9, height=4, fg="white", bg="wheat4",
                             relief=RAISED, bd=3, activebackground="burlywood3", font=button_font, command=lambda: exit())
        new_button.grid(row=2, column=2)
        cont_button.grid(row=4, column=2)
        load_button.grid(row=6, column=2)
        exit_button.grid(row=8, column=2)

        # Padding frame widget configurations
        mystic_text1 = Label(pad_frame1_subframe, bg="darkolivegreen",
                             text="Shirak!  Ast kiranann kair soth-arn suh kali jalaran  "
                                  "Ast kiranann kair gadunrm soth-arn suh kalijalaran  "
                                  "Ast bilak parbilakir, suh tangus moipiar   Dulak!",
                             font=mystic_font)
        mystic_text2 = Label(pad_frame2_subframe, bg="darkolivegreen",
                             text="Abdis tukng! Kumpul-ah kepudanya Kuasahan!   Burus longang"
                                  " degagng birsish Sekalilagang!   Degagng kuashnya, lampar "
                                  "Terbong kilat mati yanjahat!   Xts vrie!", font=mystic_font)
        mystic_text1.pack(fill=BOTH, expand=TRUE)
        mystic_text2.pack(fill=BOTH, expand=TRUE)
        self.main_frame.update()

    # Not Implemented yet
    def world_window(self):
        # Variables
        directory = os.getcwd()
        player_name = "Player Name"
        player_lvl = "Player Level"
        player_health = 100
        player_image = "/race_elf.png"
        general_prompt = "In game general prompts go here"

        # Image configurations
        character_img = PhotoImage(file=directory + player_image)
        arrow_img1 = PhotoImage(file=directory + "/left_arrow.png")
        arrow_img2 = PhotoImage(file=directory + "/right_arrow.png")
        arrow_img3 = PhotoImage(file=directory + "/up_arrow.png")
        arrow_img4 = PhotoImage(file=directory + "/down_arrow.png")
        button_bg_img1 = PhotoImage(file=directory + "/button_bg1.png")
        button_bg_img2 = PhotoImage(file=directory + "/button_bg2.png")
        reduced_button_bg_img1 = button_bg_img1.subsample(2, 2)
        reduced_button_bg_img2 = button_bg_img2.subsample(3, 3)
        reduced_character_img = character_img.subsample(2, 2)
        left_arrow = arrow_img1.subsample(2, 4)
        right_arrow = arrow_img2.subsample(2, 4)
        up_arrow = arrow_img3.subsample(4, 2)
        down_arrow = arrow_img4.subsample(4, 2)

        # Progressbar styling
        bar_style = Style()
        bar_style.theme_use("clam")
        bar_style.configure("Horizontal.TProgressbar", background="darkolivegreen", bordercolor="black")

        # Font styling
        info_font: tkfont = tkfont.Font(size=14, family="Windings")
        info_font2: tkfont = tkfont.Font(size=12, family="Windings")
        prompt_font: tkfont = tkfont.Font(size=16, slant="italic", family="David", weight="bold")
        button_font: tkfont = tkfont.Font(size=11, family="Helvetica Bold Round")

        # Main frame configurations
        main_container = Frame(self.main_frame, bg="wheat4", width=800, height=1000,
                               highlightthickness=5, highlightbackground="black")
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_columnconfigure(2, weight=2)
        main_container.grid_rowconfigure(1, weight=2)
        main_container.grid_rowconfigure(2, weight=1)
        player_info_container = Frame(main_container, bg="burlywood4", width=350, height=600)
        player_info_container.grid_columnconfigure(2, weight=1, minsize=330)
        player_info_container.grid_columnconfigure((1, 3), minsize=10)
        player_info_container.grid_rowconfigure(2, weight=1, minsize=150)
        player_info_container.grid_rowconfigure(4, weight=2, minsize=360)
        player_info_container.grid_rowconfigure((1, 3, 5), minsize=5)
        map_container = Frame(main_container, bg="burlywood4", width=650, height=600,
                              highlightthickness=3, highlightbackground="black")
        control_container = Frame(main_container, bg="burlywood4", width=1000, height=250)
        control_container.grid_columnconfigure(2, weight=1)
        control_container.grid_columnconfigure(4, weight=2)
        control_container.grid_columnconfigure((1, 3, 5), minsize=10)
        control_container.grid_rowconfigure(2, weight=1)
        control_container.grid_rowconfigure((1, 3), minsize=10)
        main_container.pack(fill=BOTH, expand=TRUE)
        player_info_container.grid(row=1, column=1)
        map_container.grid(row=1, column=2)
        control_container.grid(row=2, column=1, columnspan=2)

        # Player info frame sub frame configurations
        player_info = Frame(player_info_container, bg="burlywood3", width=300, height=160,
                            highlightthickness=5, highlightbackground="black")
        player_info.grid_columnconfigure(2, weight=1, minsize=130)
        player_info.grid_columnconfigure(3, weight=1, minsize=150)
        player_info.grid_columnconfigure((1, 4), minsize=10)
        player_info.grid_rowconfigure((2, 3, 4), weight=1, minsize=26)
        player_info.grid_rowconfigure((1, 5), minsize=5)
        player_image = Frame(player_info_container, bg="burlywood3", width=230, height=390,
                             highlightthickness=5, highlightbackground="black")
        player_info.grid(row=2, column=2)
        player_image.grid(row=4, column=2, sticky=N)

        # Map frame sub frame configurations
        map_subframe = Frame(map_container, bg="burlywood3", width=650, height=600,
                             highlightthickness=5, highlightbackground="black")
        map_subframe.grid_columnconfigure(2, weight=2, minsize=630)
        map_subframe.grid_columnconfigure((1, 3), minsize=10)
        map_subframe.grid_rowconfigure(2, weight=2, minsize=580)
        map_subframe.grid_rowconfigure((1, 3), minsize=10)
        map_subframe.pack(fill=BOTH, expand=TRUE)

        # Control frame sub frame configurations
        button_frame = Frame(control_container, bg="burlywood3", width=400, height=200,
                             highlightthickness=5, highlightbackground="black")
        button_frame.grid_columnconfigure((2, 4, 6), weight=1)
        button_frame.grid_columnconfigure(8, weight=2)
        button_frame.grid_columnconfigure(1, minsize=20)
        button_frame.grid_columnconfigure(9, minsize=10)
        button_frame.grid_columnconfigure((3, 5), minsize=5)
        button_frame.grid_columnconfigure(7, minsize=90)
        button_frame.grid_rowconfigure((2, 4, 6), weight=1)
        button_frame.grid_rowconfigure((1, 7), minsize=2)
        button_frame.grid_rowconfigure((3, 5), minsize=1)
        prompt_frame = Frame(control_container, bg="burlywood3", width=600, height=200,
                             highlightthickness=5, highlightbackground="black")
        prompt_frame.grid_columnconfigure(2, weight=2, minsize=540)
        prompt_frame.grid_columnconfigure((1, 3), minsize=20)
        prompt_frame.grid_rowconfigure(2, weight=1, minsize=175)
        prompt_frame.grid_rowconfigure((1, 3), minsize=15)
        button_frame.grid(row=2, column=2)
        prompt_frame.grid(row=2, column=4)

        # Player info frame widget configurations
        prompt1 = Label(player_info, text="Name: ", font=info_font, bg="burlywood3")
        prompt2 = Label(player_info, text="Level: ", font=info_font, bg="burlywood3")
        player_name = Label(player_info, text=player_name, font=info_font2, bg="burlywood3")
        player_level = Label(player_info, text=player_lvl, font=info_font2, bg="burlywood3")
        hp_bar = Progressbar(player_info, length=200, orient=HORIZONTAL, mode="determinate")
        character = Label(player_image, image=reduced_character_img, bg="burlywood3")
        prompt1.grid(row=2, column=2)
        player_name.grid(row=2, column=3, sticky=W)
        prompt2.grid(row=3, column=2)
        player_level.grid(row=3, column=3, sticky=W)
        hp_bar.grid(row=4, column=2, columnspan=2)
        character.pack(fill=BOTH, expand=TRUE, anchor=N)

        # Control frame widget configurations
        move_button_background = Label(button_frame, image=reduced_button_bg_img1, bg="burlywood3")
        up_button = Button(button_frame, text="UP", bg="black", image=up_arrow, relief=RAISED,
                           bd=3, activebackground="burlywood3")
        down_button = Button(button_frame, text="Down", bg="black", image=down_arrow, relief=RAISED,
                             bd=3, activebackground="burlywood3")
        left_button = Button(button_frame, text="Left", bg="black", image=left_arrow, relief=RAISED,
                             bd=3, activebackground="burlywood3")
        right_button = Button(button_frame, text="Right", bg="black", image=right_arrow, relief=RAISED,
                              bd=3, activebackground="burlywood3")
        center_button = Button(button_frame, text="Center", bg="black", image=reduced_button_bg_img2, relief=RAISED,
                               bd=3, activebackground="burlywood3")
        button_background = Label(button_frame, bg="black", width=25, height=15)
        inventory_button = Button(button_frame,  text="Inventory",  width=14, height=2, font=button_font,
                                  fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        log_button = Button(button_frame,  text="Quest Log",  width=14, height=2, font=button_font,
                            fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        skills_button = Button(button_frame, text="Skill Tree", width=14, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3")
        game_prompt = Label(prompt_frame, text=general_prompt, bg="burlywood3", font=prompt_font)
        move_button_background.grid(row=2, column=2, rowspan=5, columnspan=5)
        up_button.grid(row=2, column=4, sticky=S)
        down_button.grid(row=6, column=4, sticky=N)
        left_button.grid(row=4, column=2, sticky=E)
        right_button.grid(row=4, column=6, sticky=W)
        center_button.grid(row=4, column=4)
        button_background.grid(row=2, column=8, rowspan=5)
        inventory_button.grid(row=2, column=8)
        log_button.grid(row=4, column=8)
        skills_button.grid(row=6, column=8)
        game_prompt.grid(row=2, column=2, sticky=NW)

        # Map frame widget configurations
        temp_text = Label(map_subframe, text="This is a place holder for the game map.", bg="burlywood3",
                          font=prompt_font)
        temp_text.grid(row=2, column=2)

        # temp progressbar whatever
        hp_bar["value"] = player_health

        self.master.mainloop()

    # This frame currently is for setting up a new character, allowing the user to choose a race, base fighting style,
    # name, and the assigning of initial attribute points. In time this frame will also be used to control character
    # equipment and the assigning of gained skill points
    def creation_window(self):
        # This sub function adjusts the base attribute points based on the desired character type. It calls back to
        # the main module's CharacterBuildController for use in the type_controller function. It uses the variable
        # choice to select a string from attribute_selection as the required parameter for type_controller. The Results
        # from type_controller are returned as attribute_results to be applied to their corresponding variables
        def attribute(self, direction):
            attribute_selection = ["knight", "mage", "ranger"]
            att_length = len(attribute_selection)
            choice = int(choice_counter.get())
            if direction is True:
                choice = choice - 1
            else:
                choice += 1

            if choice < 0:
                choice = att_length - 1
            elif choice > (att_length - 1):
                choice = 0
            else:
                pass
            choice_counter.set(choice)
            # This is the call back to the main module
            attribute_results = self.create.type_controller(attribute_selection[choice])
            # Variable reassignment/updates
            character_type_text.set(attribute_results[0])
            attack_points.set(attribute_results[1])
            defense_points.set(attribute_results[2])
            magic_points.set(attribute_results[3])
            attribute_points.set(5)
            # frame refresh
            main_container.update()

        # This sub function adjusts the attack attribute with the attack up and down buttons
        def attack(direction):
            attack_adjust = int(attack_points.get())
            remaining_points = int(attribute_points.get())
            # Direction based adjustment, (True for back False for forward), also checks variables to verify they are
            # within range to perform desired action
            if direction is True:
                if attack_adjust <= 0:
                    return
                else:
                    attack_adjust -= 1
                    remaining_points += 1
            else:
                if remaining_points <= 0:
                    return
                else:
                    attack_adjust += 1
                    remaining_points -= 1
            attack_points.set(attack_adjust)
            attribute_points.set(remaining_points)
            main_container.update()

        # This sub function adjusts the defense attribute with the defense up and down buttons
        def defense(direction):
            defense_adjust = int(defense_points.get())
            remaining_points = int(attribute_points.get())
            # Direction based adjustment, (True for back False for forward), also checks variables to verify they are
            # within range to perform desired action
            if direction is True:
                if defense_adjust <= 0:
                    return
                else:
                    defense_adjust -= 1
                    remaining_points += 1
            else:
                if remaining_points <= 0:
                    return
                else:
                    defense_adjust += 1
                    remaining_points -= 1
            defense_points.set(defense_adjust)
            attribute_points.set(remaining_points)
            main_container.update()

        # This sub function adjusts the magic attribute with the magic up and down buttons
        def magic(direction):
            magic_adjust = int(magic_points.get())
            remaining_points = int(attribute_points.get())
            # Direction based adjustment, (True for back False for forward), also checks variables to verify they are
            # within range to perform desired action
            if direction is True:
                if magic_adjust <= 0:
                    return
                else:
                    magic_adjust -= 1
                    remaining_points += 1
            else:
                if remaining_points <= 0:
                    return
                else:
                    magic_adjust += 1
                    remaining_points -= 1
            magic_points.set(magic_adjust)
            attribute_points.set(remaining_points)
            main_container.update()

        # This sub function is controlled the finish_button. It sets up the basic character attribute list with the
        # desired variables like name, type, race, and starting attribute stats. This list is passed back to the main
        # module's CharacterBuildController for use in the builder function. See Character module for more details on
        # character stats.
        def build_character(self):
            name_length = len(name_input.get())
            attributes = [name_input.get(), character_type_text.get(), character_race_text.get(),1, 100, int(attack_points.get()),
                          int(defense_points.get()), int(magic_points.get())]
            if name_length == 0:
                return
            else:
                if int(attribute_points.get()) != 0:
                    return
                else:
                    self.player = self.create.builder(attributes)
                    temp = self.progress.firststrike(self.player["level"])
                    main_container.after(0, self.combat_window(temp[0], temp[1], temp[2]))
                    main_container.destroy()

        # Variables
        directory = os.getcwd()
        choice_counter = StringVar()
        character_type_text = StringVar()
        character_race_text = StringVar()
        race_prompt = StringVar()
        race_ability = StringVar()
        attack_points = StringVar()
        defense_points = StringVar()
        magic_points = StringVar()
        attribute_points = StringVar()
        choice_counter.set(0)
        race_selection = ["Elf", "Human", "Dwarf"]
        character_type_text.set("Knight")
        character_race_text.set(race_selection[0])
        character_image = "/images/race_elf.png"
        race_prompt.set("Something about the race backstory goes here")
        race_ability.set("Something about their ability goes here")
        attack_points.set(2)
        defense_points.set(0)
        magic_points.set(0)
        attribute_points.set(5)

        # Image Configurations
        left_arrow_img = PhotoImage(file=directory + "/images/left_arrow.png")
        reduced_left_arrow = left_arrow_img.subsample(3, 3)
        reduced2_left_arrow = left_arrow_img.subsample(4, 4)
        reduced3_left_arrow = left_arrow_img.subsample(5, 5)
        right_arrow_img = PhotoImage(file=directory + "/images/right_arrow.png")
        reduced_right_arrow = right_arrow_img.subsample(3, 3)
        reduced2_right_arrow = right_arrow_img.subsample(4, 4)
        reduced3_right_arrow = right_arrow_img.subsample(5, 5)
        character_image = PhotoImage(file=directory + character_image)
        reduced_character_image = character_image.subsample(x=2, y=2)

        # Font styling
        info_font: tkfont = tkfont.Font(size=14, family="Windings", underline=1)
        info_font2: tkfont = tkfont.Font(size=12, family="Windings", weight="bold")
        title_font: tkfont = tkfont.Font(size=20, family="Windings", underline=1)
        title_font2: tkfont = tkfont.Font(size=20, family="Windings")
        prompt_font: tkfont = tkfont.Font(size=14, slant="italic", family="David")
        prompt_font2: tkfont = tkfont.Font(size=12, slant="italic", family="David")
        button_font: tkfont = tkfont.Font(size=13, family="Helvetica Bold Round")
        mystic_font: tkfont = tkfont.Font(size=13, family="Vijaya", slant="italic", weight="bold")

        # Main frame configurations
        main_container = Frame(self.main_frame, bg="wheat4", width=800, height=1000)
        main_container.grid_columnconfigure(1, weight=2, minsize=300)
        main_container.grid_columnconfigure(2, weight=2, minsize=00)
        main_container.grid_rowconfigure(2, weight=2, minsize=600)
        main_container.grid_rowconfigure((1, 3), minsize=50)
        character_frame = Frame(main_container, bg="burlywood4", width=700, height=800,
                                highlightthickness=3, highlightbackground="black")
        character_frame.grid_columnconfigure(2, weight=2)
        character_frame.grid_columnconfigure((1, 3), minsize=10)
        character_frame.grid_rowconfigure(2, weight=2, minsize=215)
        character_frame.grid_rowconfigure(4, weight=1, minsize=50)
        character_frame.grid_rowconfigure(6, weight=2, minsize=150)
        character_frame.grid_rowconfigure((3, 5), minsize=5)
        character_frame.grid_rowconfigure((1, 7), minsize=10)
        attributes_container = Frame(main_container, bg="burlywood4", width=300, height=800,
                                     highlightthickness=3, highlightbackground="black")
        attributes_container.grid_columnconfigure(2, weight=2, minsize=280)
        attributes_container.grid_columnconfigure((1, 3), minsize=10)
        attributes_container.grid_rowconfigure(2, weight=2, minsize=160)
        attributes_container.grid_rowconfigure(4, weight=1, minsize=50)
        attributes_container.grid_rowconfigure(6, weight=2, minsize=375)
        attributes_container.grid_rowconfigure(8, weight=1, minsize=75)
        attributes_container.grid_rowconfigure((3, 5, 7), minsize=5)
        attributes_container.grid_rowconfigure(1, minsize=15)
        attributes_container.grid_rowconfigure(9, minsize=10)
        pad_frame1 = Frame(main_container, width=1000, height=50, bg="darkolivegreen",
                           highlightthickness=3, highlightbackground="black", relief=RAISED)
        pad_frame1.grid_columnconfigure(2, weight=2, minsize=990)
        pad_frame1.grid_columnconfigure((1, 3), minsize=5)
        pad_frame1.grid_rowconfigure(2, weight=2, minsize=30)
        pad_frame1.grid_rowconfigure((1, 3), minsize=5)
        pad_frame2 = Frame(main_container, width=1000, height=50, bg="darkolivegreen",
                           highlightthickness=3, highlightbackground="black", relief=RAISED)
        pad_frame2.grid_columnconfigure(2, weight=2, minsize=990)
        pad_frame2.grid_columnconfigure((1, 3), minsize=5)
        pad_frame2.grid_rowconfigure(2, weight=2, minsize=30)
        pad_frame2.grid_rowconfigure((1, 3), minsize=5)
        main_container.pack(fill=BOTH, expand=TRUE)
        character_frame.grid(row=2, column=2)
        attributes_container.grid(row=2, column=1)
        pad_frame1.grid(row=1, column=1, columnspan=2, sticky=N)
        pad_frame2.grid(row=3, column=1, columnspan=2, sticky=S)

        # Race frame sub frame configurations
        character_img_frame = Frame(character_frame, bg="burlywood3", width=350, height=500,
                                    highlightthickness=2, highlightbackground="black")
        character_button_frame = Frame(character_frame, bg="burlywood4", width=700, height=50)
        character_button_frame.grid_columnconfigure((2, 6), weight=2)
        character_button_frame.grid_columnconfigure(4, weight=1, minsize=175)
        character_button_frame.grid_columnconfigure((1, 3, 5, 7), minsize=10)
        character_button_frame.grid_rowconfigure(2, weight=1)
        character_button_frame.grid_rowconfigure((1, 3), minsize=10)
        character_text_frame = Frame(character_frame, bg="burlywood3", width=475, height=150,
                                     highlightthickness=2, highlightbackground="black")
        character_text_frame.grid_columnconfigure(2, weight=2, minsize=455)
        character_text_frame.grid_columnconfigure((1, 3), minsize=10)
        character_text_frame.grid_rowconfigure(2, weight=2, minsize=90)
        character_text_frame.grid_rowconfigure(3, weight=1, minsize=40)
        character_text_frame.grid_rowconfigure((1, 4), minsize=10)
        character_img_frame.grid(row=2, column=2)
        character_button_frame.grid(row=4, column=2)
        character_text_frame.grid(row=6, column=2)

        # Attributes frame sub frame configurations
        attributes_first_frame = Frame(attributes_container, bg="burlywood3", width=200, height=160,
                                       highlightthickness=3, highlightbackground="black")
        attributes_first_frame.grid_columnconfigure((2, 4, 6), weight=1, minsize=40)
        attributes_first_frame.grid_columnconfigure((3, 5), minsize=1)
        attributes_first_frame.grid_columnconfigure((1, 7), minsize=5)
        attributes_first_frame.grid_rowconfigure((2, 4), weight=1, minsize=70)
        attributes_first_frame.grid_rowconfigure((1, 5), minsize=10)
        attributes_first_frame.grid_rowconfigure(3, minsize=5)
        attributes_text_frame = Frame(attributes_container, bg="burlywood4", width=200, height=50)
        attributes_second_frame = Frame(attributes_container, bg="burlywood3", width=200, height=375,
                                        highlightthickness=3, highlightbackground="black")
        attributes_second_frame.grid_columnconfigure((2, 3, 4), weight=1, minsize=10)
        attributes_second_frame.grid_columnconfigure((1, 5), minsize=1)
        attributes_second_frame.grid_rowconfigure((2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24), weight=1, minsize=20)
        attributes_second_frame.grid_rowconfigure((1, 25), minsize=10)
        attributes_second_frame.grid_rowconfigure((3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23), minsize=2)
        attributes_button_frame = Frame(attributes_container, bg="black", width=200, height=75,
                                        highlightthickness=3, highlightbackground="black")
        attributes_button_frame.grid_columnconfigure(2, weight=2, minsize=180)
        attributes_button_frame.grid_columnconfigure((1, 3), minsize=10)
        attributes_button_frame.grid_rowconfigure(2, weight=1, minsize=55)
        attributes_button_frame.grid_rowconfigure((1, 3), minsize=5)
        attributes_first_frame.grid(row=2, column=2)
        attributes_text_frame.grid(row=4, column=2, sticky=S)
        attributes_second_frame.grid(row=6, column=2, sticky=N)
        attributes_button_frame.grid(row=8, column=2)

        # Padding frame sub frame configurations
        pad_frame1_subframe = Frame(pad_frame1, width=945, height=40)
        pad_frame1_subframe.grid_columnconfigure(2, weight=1)
        pad_frame2_subframe = Frame(pad_frame2, width=945, height=40)
        pad_frame1_subframe.grid(row=2, column=2)
        pad_frame2_subframe.grid(row=2, column=2)

        # Character frame widget configurations
        character_img = Label(character_img_frame, image=reduced_character_image, bg="burlywood3")
        character_img.image = reduced_character_image
        char_back_button = Button(character_button_frame, bg="black", width=25, height=30, image=reduced_left_arrow,
                                  activebackground="burlywood3", state="disabled")
        char_back_button.image = reduced_left_arrow
        character_race = Label(character_button_frame, textvariable=character_race_text, bg="burlywood4",
                               font=title_font2)
        char_next_button = Button(character_button_frame, bg="black", width=25, height=30, image=reduced_right_arrow,
                                  activebackground="burlywood3", state="disabled")
        char_next_button.image = reduced_right_arrow
        character_info = Label(character_text_frame, textvariable=race_prompt, bg="burlywood3", font=prompt_font)
        character_ability = Label(character_text_frame, textvariable=race_ability, bg="burlywood3", font=prompt_font2)
        character_img.pack(fill=BOTH, expand=TRUE)
        char_back_button.grid(row=2, column=2)
        character_race.grid(row=2, column=4)
        char_next_button.grid(row=2, column=6)
        character_info.grid(row=2, column=2, sticky=NW)
        character_ability.grid(row=3, column=2, sticky=NW)

        # Attributes frame widget configurations
        character_name = LabelFrame(attributes_first_frame, text="Character Name ", bg="burlywood3",
                                    width=170, height=75, font=info_font, labelanchor=N, relief="flat")
        name_input = Entry(character_name, width=23, bg="wheat", font=info_font2)
        type_back_button = Button(attributes_first_frame, bg="black", width=20, height=25, image=reduced2_left_arrow,
                                  activebackground="burlywood3", command=lambda: attribute(self, True))
        type_back_button.image = reduced2_left_arrow
        character_type = Label(attributes_first_frame, textvariable=character_type_text, bg="burlywood3",
                               font=info_font2)
        type_next_button = Button(attributes_first_frame, bg="black", width=20, height=25, image=reduced2_right_arrow,
                                  activebackground="burlywood3", command=lambda: attribute(self, False))
        type_next_button.image = reduced2_right_arrow
        att_title = Label(attributes_text_frame, text="      Attributes      ", bg="burlywood4", font=title_font)
        att_attack = Label(attributes_second_frame, text="Attack", bg="burlywood3", font=info_font2)
        attack_down_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                    image=reduced3_left_arrow, activebackground="burlywood3",
                                    command=lambda: attack(True))
        attack_down_button.image = reduced3_left_arrow
        attack_counter = Label(attributes_second_frame, textvariable=attack_points, bg="burlywood3", font=info_font2)
        attack_up_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                  image=reduced3_right_arrow, activebackground="burlywood3",
                                  command=lambda: attack(False))
        attack_up_button.image = reduced3_right_arrow
        att_defense = Label(attributes_second_frame, text="Defense", bg="burlywood3", font=info_font2)
        defense_down_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                     image=reduced3_left_arrow, activebackground="burlywood3",
                                     command=lambda: defense(True))
        defense_down_button.image = reduced3_left_arrow
        defense_counter = Label(attributes_second_frame, textvariable=defense_points, bg="burlywood3", font=info_font2)
        defense_up_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                   image=reduced3_right_arrow, activebackground="burlywood3",
                                   command=lambda: defense(False))
        defense_up_button.image = reduced3_right_arrow
        att_magic = Label(attributes_second_frame, text="Magic", bg="burlywood3", font=info_font2)
        magic_down_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                   image=reduced3_left_arrow, activebackground="burlywood3",
                                   command=lambda: magic(True))
        magic_down_button.image = reduced3_left_arrow
        magic_counter = Label(attributes_second_frame, textvariable=magic_points, bg="burlywood3", font=info_font2)
        magic_up_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                 image=reduced3_right_arrow, activebackground="burlywood3",
                                 command=lambda: magic(False))
        magic_up_button.image = reduced3_right_arrow
        att_point_title = Label(attributes_second_frame, text="Attribute points remaining", bg="burlywood3",
                                font=info_font)
        att_point_counter = Label(attributes_second_frame, textvariable=attribute_points, bg="burlywood3",
                                  font=info_font2)
        finish_button = Button(attributes_button_frame, text="Finalize Character", width=20, height=3,
                               font=button_font, fg="white", bg="wheat4", relief=RAISED, bd=3,
                               activebackground="burlywood3", command=lambda: build_character(self))
        character_name.grid(row=2, column=2, columnspan=5, sticky=S)
        name_input.pack(fill=X, expand=TRUE)
        type_back_button.grid(row=4, column=2, sticky=NE)
        character_type.grid(row=4, column=4, sticky=N)
        type_next_button.grid(row=4, column=6, sticky=NW)
        att_title.pack(fill=BOTH, expand=TRUE)
        att_attack.grid(row=2, column=2, columnspan=3)
        attack_down_button.grid(row=4, column=2, sticky=E)
        attack_counter.grid(row=4, column=3)
        attack_up_button.grid(row=4, column=4, sticky=W)
        att_defense.grid(row=6, column=2, columnspan=3)
        defense_down_button.grid(row=8, column=2, sticky=E)
        defense_counter.grid(row=8, column=3)
        defense_up_button.grid(row=8, column=4, sticky=W)
        att_magic.grid(row=10, column=2, columnspan=3)
        magic_down_button.grid(row=12, column=2, sticky=E)
        magic_counter.grid(row=12, column=3)
        magic_up_button.grid(row=12, column=4, sticky=W)
        att_point_title.grid(row=22, column=2, columnspan=3)
        att_point_counter.grid(row=24, column=3)
        finish_button.grid(row=2, column=2)

        # Padding frame widget configurations
        mystic_text1 = Label(pad_frame1_subframe, bg="darkolivegreen",
                             text="Shirak!  Ast kiranann kair soth-arn suh kali jalaran  "
                                  "Ast kiranann kair gadunrm soth-arn suh kalijalaran  "
                                  "Ast bilak parbilakir, suh tangus moipiar",
                             font=mystic_font)
        mystic_text2 = Label(pad_frame2_subframe, bg="darkolivegreen",
                             text="Abdis tukng! Kumpul-ah kepudanya Kuasahan!   Burus longang"
                                  " degagng birsish Sekalilagang!   Degagng kuashnya, lampar "
                                  "Terbong kilat mati yanjahat!   Xts vrie!", font=mystic_font)
        mystic_text1.pack(fill=BOTH, expand=TRUE)
        mystic_text2.pack(fill=BOTH, expand=TRUE)

        self.main_frame.update()

    # This frame handles the combat aspect of the game, where the user can gain experience and level up,
    # essentially the bulk of the game at this point. I don't have the inventory or spell casting setup yet so the
    # buttons are just place holders.
    def combat_window(self, opp_stat, prompt, fs):
        # This sub function handles the users turn by taking a given parameter and calling back to the main modules
        # CombatController's action_controller, along with the player's stat tree and the opponents stat tree.
        # The stat trees are returned(player_results) updated and accompanied by 2 prompts.
        def turn(self, action):
            player_results = self.progress.action_controller(self.player, self.opponent, action)
            # Stat tree updating
            self.player = player_results[0]
            self.opponent = player_results[1]
            # Action prompt updating
            player_action_prompt1_text.set(player_results[2])
            player_action_prompt2_text.set(player_results[3])
            # Check for escape function call
            escaped = player_results[4]
            # Opponent health bar update
            opp_hp_bar["value"] = int(self.opponent["health"])
            # User button disabling in preparation of opponent's turn
            attack_button.config(state="disabled")
            defend_button.config(state="disabled")
            spells_button.config(state="disabled")
            escape_button.config(state="disabled")
            item_button.config(state="disabled")
            # Updates the frame
            main_container.update()
            time.sleep(1)
            # Destroys current frame and creates a new one with a call to main modules
            # CombatController's firststrike function for a new opponent
            if escaped is True:
                time.sleep(2)
                temp = self.progress.firststrike(self.player["level"])
                main_container.after(0, self.combat_window(temp[0], temp[1], temp[2]))
                main_container.destroy()
            # Call to main modules CombatController's health_checker, to verify player and opponent health
            else:
                death_list = self.progress.health_check(self.player, self.opponent)
                if death_list is not None:
                    # This is performed if the player dies
                    if death_list[0] is True:
                        player_action_prompt1_text.set(death_list[1])
                        attack_button.config(state="normal")
                        defend_button.config(state="normal")
                        spells_button.config(state="normal")
                        escape_button.config(state="normal")
                        item_button.config(state="normal")
                        main_container.update()
                        time.sleep(2)
                        main_container.after(0, self.init_window())
                        main_container.destroy()
                    # This is performed if the opponent dies
                    else:
                        self.player = death_list[1]
                        player_action_prompt1_text.set(death_list[2])
                        player_action_prompt2_text.set(death_list[3])
                        main_container.update()
                        time.sleep(2)
                        temp = self.progress.firststrike(self.player["level"])
                        main_container.after(0, self.combat_window(temp[0], temp[1], temp[2]))
                        main_container.destroy()
                # If neither dies it passes to the next function for the opponents turn
                else:
                    next_turn(self)

        # This sub function handles the opponent's turn. It calls to the same function in the main module as the
        # previous function but without the action specifier. The opponents choice is handled within that call.
        # The results are returned in the same manner as the previous function except that the opponent stat tree
        # is returned at index[0] of opp_results as opposed to index[1] in player_results. The 2 sub functions are so
        # similar that im sure I will combine them in to one function soon.
        def next_turn(self):
            opp_action_prompt1_text.set("Your opponent is deciding what to do...")
            main_container.update()
            time.sleep(2)
            opp_results = self.progress.action_controller(self.opponent, self.player)
            # Stat tree update
            self.opponent = opp_results[0]
            self.player = opp_results[1]
            # Opponent action prompt update
            opp_action_prompt1_text.set(opp_results[2])
            opp_action_prompt2_text.set(opp_results[3])
            # Player health bar update
            player_hp_bar["value"] = int(self.player["health"])
            # Updates the frame
            main_container.update()
            time.sleep(1)
            # Call to main modules CombatController's health_checker, to verify player and opponent health
            death_list = self.progress.health_check(self.player, self.opponent)
            if death_list is not None:
                # This is performed if the player dies
                if death_list[0] is True:
                    player_action_prompt1_text.set(death_list[1])
                    main_container.update()
                    time.sleep(3)
                    main_container.after(0, self.init_window())
                    main_container.destroy()
                # This is performed if the opponent dies
                else:
                    self.player = death_list[1]
                    player_action_prompt1_text.set(death_list[2])
                    player_action_prompt2_text.set(death_list[3])
                    main_container.update()
                    time.sleep(2)
                    temp = self.progress.firststrike(self.player["level"])
                    main_container.after(0, self.combat_window(temp[0], temp[1], temp[2]))
                    main_container.destroy()
            # If neither dies it passes back to the user for input
            else:
                pass
            # User button enabling
            attack_button.config(state="normal")
            defend_button.config(state="normal")
            spells_button.config(state="normal")
            escape_button.config(state="normal")
            item_button.config(state="normal")

        # Variables
        self.opponent = opp_stat
        first_turn = fs
        opp_name_text = StringVar()
        opp_level_text = StringVar()
        player_name_text = StringVar()
        player_level_text = StringVar()
        opp_effects_att_text = StringVar()
        opp_effects_def_text = StringVar()
        opp_effects_mag_text = StringVar()
        opp_effects_weapon_text = StringVar()
        player_effects_att_text = StringVar()
        player_effects_def_text = StringVar()
        player_effects_mag_text = StringVar()
        player_effects_weapon_text = StringVar()
        player_effects_exp_text = StringVar()
        opp_action_prompt1_text = StringVar()
        opp_action_prompt2_text = StringVar()
        player_action_prompt1_text = StringVar()
        player_action_prompt2_text = StringVar()

        opp_name_text.set("Name: " + str(self.opponent["type"]))
        opp_level_text.set("Level: " + str(self.opponent["level"]))
        player_name_text.set("Name: " + str(self.player["name"]))
        player_level_text.set("Level: " + str(self.player["level"]))
        opp_effects_att_text.set("Attack: " + str(self.opponent["attack"]))
        opp_effects_def_text.set("Defense: " + str(self.opponent["defence"]))
        opp_effects_mag_text.set("Magic: " + str(self.opponent["magic"]))
        opp_effects_weapon_text.set("Weapon: " + str(self.opponent["weapon"]))
        player_effects_att_text.set("Attack: " + str(self.player["attack"]))
        player_effects_def_text.set("Defense: " + str(self.player["defence"]))
        player_effects_mag_text.set("Magic: " + str(self.player["magic"]))
        player_effects_weapon_text.set("Weapon: " + str(self.player["weapon"]))
        player_effects_exp_text.set("Exp: " + str(self.player["exp"]))
        opp_action_prompt1_text.set("")
        opp_action_prompt2_text.set("")
        player_action_prompt1_text.set(prompt)
        player_action_prompt2_text.set("")

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
        opp_name = Label(opp_info, textvariable=opp_name_text, font=info_font, bg="burlywood3")
        opp_level = Label(opp_info, textvariable=opp_level_text, font=info_font, bg="burlywood3")
        opp_hpbar_label = Label(opp_info_subframe, text="HP ", font=info_font2, bg="burlywood3")
        opp_mpbar_label = Label(opp_info_subframe, text="MP ", font=info_font2, bg="burlywood3")
        opp_hp_bar = Progressbar(opp_info_subframe, orient=HORIZONTAL, length=200, mode="determinate")
        opp_mp_bar = Progressbar(opp_info_subframe, orient=HORIZONTAL, length=200, mode="determinate")
        opp_hp_bar["maximum"] = int(opp_stat["health"])
        opp_hp_bar["value"] = int(self.opponent["health"])
        opp_mp_bar["value"] = 100
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
        player_name = Label(player_info, textvariable=player_name_text, font=info_font, bg="burlywood3")
        player_level = Label(player_info, textvariable=player_level_text, font=info_font, bg="burlywood3")
        player_hpbar_label = Label(player_info_subframe, text="HP ", font=info_font2, bg="burlywood3")
        player_mpbar_label = Label(player_info_subframe, text="MP ", font=info_font2, bg="burlywood3")
        player_hp_bar = Progressbar(player_info_subframe, orient=HORIZONTAL, length=200, mode="determinate", )
        player_mp_bar = Progressbar(player_info_subframe, orient=HORIZONTAL, length=200, mode="determinate", )
        player_hp_bar["maximum"] = int(self.player["base attributes"][4])
        player_hp_bar["value"] = int(self.player["health"])
        player_mp_bar["value"] = 100
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
        opp_effects_att = Label(opp_effects, textvariable=opp_effects_att_text, font=effects_font2, bg="burlywood3")
        opp_effects_def = Label(opp_effects, textvariable=opp_effects_def_text, font=effects_font2, bg="burlywood3")
        opp_effects_mag = Label(opp_effects, textvariable=opp_effects_mag_text, font=effects_font2, bg="burlywood3")
        opp_effects_weapon = Label(opp_effects, textvariable=opp_effects_weapon_text, font=effects_font2,
                                   bg="burlywood3")
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
        player_effects_att = Label(player_effects, textvariable=player_effects_att_text, font=effects_font2,
                                   bg="burlywood3")
        player_effects_def = Label(player_effects, textvariable=player_effects_def_text, font=effects_font2,
                                   bg="burlywood3")
        player_effects_mag = Label(player_effects, textvariable=player_effects_mag_text, font=effects_font2,
                                   bg="burlywood3")
        player_effects_weapon = Label(player_effects, textvariable=player_effects_weapon_text, font=effects_font2,
                                      bg="burlywood3")
        player_effects_exp = Label(player_effects, textvariable=player_effects_exp_text, font=effects_font2,
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
        player_effects_exp.grid(row=8, column=2, sticky=W)
        player_effects_active_title.grid(row=10, column=2, sticky=W)
        player_effects_active1.grid(row=12, column=2, sticky=W)
        player_effects_active2.grid(row=13, column=2, sticky=W)
        player_effects_passive_title.grid(row=15, column=2, sticky=W)
        player_effects_passive1.grid(row=17, column=2, sticky=W)
        player_effects_passive2.grid(row=18, column=2, sticky=W)

        # Opponent prompt frame widget configurations
        opp_action_prompt1 = Label(opp_prompt, textvariable=opp_action_prompt1_text, font=prompt_font, bg="burlywood3")
        opp_action_prompt2 = Label(opp_prompt, textvariable=opp_action_prompt2_text, font=prompt_font, bg="burlywood3")
        opp_action_prompt1.grid(row=2, column=2)
        opp_action_prompt2.grid(row=3, column=2)

        # Player prompt frame widget configurations
        player_action_prompt1 = Label(player_prompt, textvariable=player_action_prompt1_text, font=prompt_font,
                                      bg="burlywood3")
        player_action_prompt2 = Label(player_prompt, textvariable=player_action_prompt2_text, font=prompt_font,
                                      bg="burlywood3")
        player_action_prompt1.grid(row=2, column=2)
        player_action_prompt2.grid(row=3, column=2)

        # Button frame widget configurations
        attack_button = Button(button_frame, text="Attack", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3",
                               command=lambda: turn(self, 1))
        defend_button = Button(button_frame, text="Defend", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3",
                               command=lambda: turn(self, 2))
        spells_button = Button(button_frame, text="Cast", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3",
                               command=lambda: turn(self, 3), state="disabled")
        escape_button = Button(button_frame, text="Escape", width=15, height=2, font=button_font,
                               fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3",
                               command=lambda: turn(self, 4))
        item_button = Button(button_frame, text="Inventory", width=15, height=2, font=button_font,
                             fg="white", bg="wheat4", relief=RAISED, bd=3, activebackground="burlywood3",
                             state="disabled")
        attack_button.grid(row=2, column=2)
        defend_button.grid(row=2, column=4)
        spells_button.grid(row=2, column=6)
        escape_button.grid(row=2, column=8)
        item_button.grid(row=2, column=10)
        self.main_frame.update()
        # This is ran after the frame is built to determine who had first strike(True is opponent, False is player)
        if first_turn is True:
            attack_button.config(state="disabled")
            defend_button.config(state="disabled")
            spells_button.config(state="disabled")
            escape_button.config(state="disabled")
            item_button.config(state="disabled")
            main_container.update()
            time.sleep(1)
            main_container.after(1000, lambda: next_turn(self))
        else:
            pass
