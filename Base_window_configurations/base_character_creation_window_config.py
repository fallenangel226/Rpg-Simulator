from tkinter import *
import tkinter.font as tkfont
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

    def creation_window(self):
        # Variables
        directory = os.getcwd()
        character_type = "Character Type"
        character_race = "Character Race"
        character_image = "/race_elf.png"
        race_prompt = "Something about the race backstory goes here"
        race_ability = "Something about their ability goes here"
        attack_points = 0
        defense_points = 0
        magic_points = 0
        attribute_points = 5

        # Image Configurations
        left_arrow_img = PhotoImage(file=directory + "/left_arrow.png")
        reduced_left_arrow = left_arrow_img.subsample(3, 3)
        reduced2_left_arrow = left_arrow_img.subsample(4, 4)
        reduced3_left_arrow = left_arrow_img.subsample(5, 5)
        right_arrow_img = PhotoImage(file=directory + "/right_arrow.png")
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
        char_back_button = Button(character_button_frame, bg="black", width=25, height=30, image=reduced_left_arrow,
                                  activebackground="burlywood3")
        character_race = Label(character_button_frame, text=character_race, bg="burlywood4", font=title_font2)
        char_next_button = Button(character_button_frame, bg="black", width=25, height=30, image=reduced_right_arrow,
                                  activebackground="burlywood3")
        character_info = Label(character_text_frame, text=race_prompt, bg="burlywood3", font=prompt_font)
        character_ability = Label(character_text_frame, text=race_ability, bg="burlywood3", font=prompt_font2)
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
                                  activebackground="burlywood3")
        character_type = Label(attributes_first_frame, text=character_type, bg="burlywood3", font=info_font2)
        type_next_button = Button(attributes_first_frame, bg="black", width=20, height=25, image=reduced2_right_arrow,
                                  activebackground="burlywood3")
        att_title = Label(attributes_text_frame, text="      Attributes      ", bg="burlywood4", font=title_font)
        att_attack = Label(attributes_second_frame, text="Attack", bg="burlywood3", font=info_font2)
        attack_down_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                    image=reduced3_left_arrow, activebackground="burlywood3")
        attack_counter = Label(attributes_second_frame, text=attack_points, bg="burlywood3", font=info_font2)
        attack_up_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                  image=reduced3_right_arrow, activebackground="burlywood3")
        att_defense = Label(attributes_second_frame, text="Defense", bg="burlywood3", font=info_font2)
        defense_down_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                     image=reduced3_left_arrow, activebackground="burlywood3")
        defense_counter = Label(attributes_second_frame, text=defense_points, bg="burlywood3", font=info_font2)
        defense_up_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                   image=reduced3_right_arrow, activebackground="burlywood3")
        att_magic = Label(attributes_second_frame, text="Magic", bg="burlywood3", font=info_font2)
        magic_down_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                   image=reduced3_left_arrow, activebackground="burlywood3")
        magic_counter = Label(attributes_second_frame, text=magic_points, bg="burlywood3", font=info_font2)
        magic_up_button = Button(attributes_second_frame, bg="black", width=15, height=15,
                                 image=reduced3_right_arrow, activebackground="burlywood3")
        att_point_title = Label(attributes_second_frame, text="Attribute points remaining", bg="burlywood3",
                                font=info_font)
        att_point_counter = Label(attributes_second_frame, text=attribute_points, bg="burlywood3", font=info_font2)
        finish_button = Button(attributes_button_frame, text="Finalize Character", width=20, height=3,
                               font=button_font, fg="white", bg="wheat4", relief=RAISED, bd=3,
                               activebackground="burlywood3")
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

        self.master.mainloop()


if __name__ == "__main__":
    root = Tk()
    game = Interface(root)
    game.creation_window()
