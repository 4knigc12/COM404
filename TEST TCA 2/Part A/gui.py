from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.default_image1 = PhotoImage(file="U:/Problem Solving through Programming/COM404/defaultimage.gif")
        self.valid_image = PhotoImage(file="U:/Problem Solving through Programming/COM404/emailcorrect.gif")
        self.nonValid_image = PhotoImage(file="U:/Problem Solving through Programming/COM404/emailwrong.gif")

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#eee", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_default_image()
        self.__add_email_entry()
        ##self.__add_email_validation()   
        self.__add_subscribe_button()
        

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure( font="Arial 14", text="RECEIVE OUR NEWSLETTER", padx=10, pady=10)
        

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="Please enter your email below to receiver our newsletter",padx=0, pady=0)

    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, sticky=E)
        self.email_label.configure( pady=20,
                                    text="Email:", padx=10 )

    def __add_default_image(self):
        self.default_image= Label(self.outer_frame)
        self.default_image.grid(row=2, column=1, sticky=E)
        self.default_image.configure(image=self.default_image1, pady=20)

    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        self.email_entry.configure(bd=2,)
        self.email_entry.bind("<KeyRelease>",self.__email_entryimput)

    def __email_entryimput(self,event):
        if len(self.email_entry.get())== 0:
            self.mail_image_label.configure(image=self.valid_image)
        else:
            self.mail_image_label.configure(image=self.nonValid_image)
    
    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fcc",
                                        text="Subscribe")
        
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()