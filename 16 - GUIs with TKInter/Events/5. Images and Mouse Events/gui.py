from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        
        self.bus_image=PhotoImage(file="U:/Problem Solving through Programming/COM404/16 - GUIs with TKInter/Events/5. Images and Mouse Events/bus.gif")
        self.map_image=PhotoImage(file="U:/Problem Solving through Programming/COM404/16 - GUIs with TKInter/Events/5. Images and Mouse Events/map.gif")
                   
        self.add_heading_label()
        self.add_map_frame()
        self.add_map_image()
        self.add_bus_image()
        
        
        
    def add_heading_label(self):
        self.heading_label =Label()
        self.heading_label.grid(row=0,column=0)  
        self.heading_label.configure(font="Arial 24", text="Buss Journey.") 
       
    def add_map_frame(self):
        self.map_frame =Frame()
        self.map_frame.grid(row=1,column=0)
        self.map_frame.configure(width=400, height=400)
       
        
    def add_map_image(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)
        
    
    def add_bus_image(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>",self.bus_move)
        
    def bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
        self.bus_image_label.place(x=event.x, y=event.y)
        
        