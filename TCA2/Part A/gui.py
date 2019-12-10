from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.santa_image = PhotoImage(file="U:/Problem Solving through Programming/COM404/santa.gif")
        

        # set window properties
        self.title("Letter to Santa")
        self.configure(width=400,bg="#f66",padx=15,pady=15)
        

        # add components
        self.__add_global_frame()
        self.__add_heading_label()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_santa_image_label()
        self.__add_letter_text()
        self.__add_post_button()


             

    def __add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.grid(row=1, column=0)
        self.global_frame.configure( bg="#f33", 
                                    padx=5,pady=5)

    def __add_heading_label(self):
        self.heading_label = Label(self.global_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(fg="#fff",bg="#f33", font="Arial 18", text="Write to Santa!", pady=5)
    
    def __add_name_label(self):
        self.name_label = Label(self.global_frame)
        self.name_label.grid(row=1, column=1, sticky=W)
        self.name_label.configure(bg="#f33",fg="#fff",font= "Arial 12", padx=5,text="Your name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self.global_frame)
        self.name_entry.grid(row=1,column=2,sticky=W)
        self.name_entry.configure()

    def __add_santa_image_label(self):
        self.santa_image_label=Label(self.global_frame)
        self.santa_image_label.grid(row=1,column=0,sticky=E)
        self.santa_image_label.configure(bg="#f33",image=self.santa_image)
    
    def __add_letter_text(self):
        self.letter_text=Message(self.global_frame)
        self.letter_text.grid(row=2,column=3,sticky=N+S+E+W)
        self.letter_text.configure(width=30,pady=0)

    def __add_post_button(self):
        self.post_button=Button(self.global_frame)
        self.post_button.grid(row=4, column=0, columnspan=5)
        self.post_button.configure(bg="#ff0", text="Post Letter")
        self.post_button.bind(("<ButtonRelease-1>",self._post_buttonclicked))

    def __post_buttonclicked(self,Event):
        messagebox.title("Sent")
        messagebox.showinfo("Your letter has been posted!") 
        



        

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()