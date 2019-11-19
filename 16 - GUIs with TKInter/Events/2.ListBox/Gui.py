from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Song Maker")
        self.configure(bg="#ccc", padx=10, pady=10)

        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyrics_entry_box()
        self.__add_lyrics_label()
       
    def __add_heading_Label(self):
        self.heading_label = Label(self)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(   bg="#eee", font="Arial 18", text="Song Maker")
    
    def __add_instrction_label(self):
        self._instrction_label = Label(self)
        self._instrction_label.grid(row=1, columm=0)
        self._instruction.configure(font="Arial 18", text="Lyrics to add:")
    
    def __add_lyrics_entry_box(self):
        self._lyrics_entry_box =Entry
        self._lyrics_entry_box.grid(row=2, columm=0)
        self._lyrics_entry.configure(width=40)
    
    def __add_add_button(self):
        self.add_button=Button(self)
        self.add_button.grid(row=2, column=1)
        self.add_button.configure(text="Add")
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)
    
    def __add_lyrics_label(self):
        self._lyrics_label = Label(self)
        self._lyrics_label.grid(row=3, columm=0)
        self._lyrics.configure(font="Arial 18", text="Lyrics:")





