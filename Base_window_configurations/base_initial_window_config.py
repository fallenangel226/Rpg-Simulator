from tkinter import *
import tkinter.font as tkfont


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

        # First game window

    def init_window(self):
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
                            relief=RAISED, bd=3, activebackground="burlywood3", font=button_font)
        cont_button = Button(control_button_frame, text="Continue\nGame", width=9, height=4, fg="white", bg="wheat4",
                             relief=RAISED, bd=3, activebackground="burlywood3", font=button_font)
        load_button = Button(control_button_frame, text="Load\nGame", width=9, height=4, fg="white", bg="wheat4",
                             relief=RAISED, bd=3, activebackground="burlywood3", font=button_font)
        exit_button = Button(control_button_frame, text="Exit\nGame", width=9, height=4, fg="white", bg="wheat4",
                             relief=RAISED, bd=3, activebackground="burlywood3", font=button_font)
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

        self.master.mainloop()


if __name__ == "__main__":
    root = Tk()
    game = Interface(root)
    game.init_window()
