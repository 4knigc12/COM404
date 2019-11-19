# gui.py

from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Tickets")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
        

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee",
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(   bg="#eee", font="Arial 18", text="Entrance Ticket")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="How many Tickets are needed ")

    def __add_tickets_entry(self):
        self.tickets_entry = Entry(self.outer_frame)
        self.tickets_entry.grid(row=2, column=0, sticky=W)
        self.tickets_entry.configure(width=40)

    def __add_buy_button(self,):
        self.buy_button=Button(self.outer_frame)
        self.buy_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.buy_button.configure(text="Buy")
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self,event):
        messagebox.showinfo("purchaesd!", "You have purcahsed the tickets!")