from tkinter import *
import tkinter.font as tkfont
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
import os


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
        right_button = Button(button_frame, text="Rigth", bg="black", image=right_arrow, relief=RAISED,
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


if __name__ == "__main__":
    root = Tk()
    game = Interface(root)
    game.world_window()
