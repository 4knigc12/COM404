from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.fliped_image =PhotoImage(file="U:/Problem Solving through Programming/COM404/16 - GUIs with TKInter/Events/Image-and-click-events/giphy (1).gif")
        self.coding_image =PhotoImage(file="U:/Problem Solving through Programming/COM404/16 - GUIs with TKInter/Events/Image-and-click-events/giphy.gif")   
        # set window attributes
        self.title("Coding")
        
        # add components
        self.add_heading_label()
        self.add_coding_image()
        self.add_button_icon()
        
        
        
    def add_heading_label(self):
        self.heading_label =Label()
        self.heading_label.grid(row=0, column=0, columnspan= 3)
        self.heading_label.configure(bg="#eee", font="Arial 10", text="How i code")
        
    def add_button_icon(self,):
        self.click_button=Button()
        self.click_button.grid(row=3, column=0, columnspan=3,)
        self.click_button.configure(text="Flip")
        self.click_button.bind("<ButtonRelease-1>", self.button_clicked)
        self.click_button.bind("<ButtonRelease-3>", self.button2_clicked)
        
        
    def add_coding_image(self):
        self.coding_image_label =Label()
        self.coding_image_label.grid(row=1, column=0)
        self.coding_image_label.configure(image=self.coding_image)
        
     
                
    def button_clicked(self,event):
         self.coding_image_label.configure(image = self.fliped_image)
    def button2_clicked(self,event):
         self.coding_image_label.configure(image = self.coding_image)
         
