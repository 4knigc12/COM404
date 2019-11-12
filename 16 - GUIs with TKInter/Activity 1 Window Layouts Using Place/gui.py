from tkinter import *
class Gui(Tk):
    def __init__(self):
        super().__init__()
        
     # set window attributes
        self.geometry("450x200") #Resize Gui object to be to be 500 pixels by 500 pixels
        self.title("Newsletter") # Sets the title of the window.
        self.configure(bg="#eee", height=250, width=400)
        
        self.add_backgroud_canvas()
        self.add_heading_label()
        self.add_email_entry()
        self.add_email_label()
        self.add_middle_label()
        self.add_email_button()
        
       

        # add window components by
    def add_heading_label(self):   # ...creating an object of the component stored in an attribute
        self.heading_label = Label()
        self.heading_label.place(x=75, y=35)
    
    # ...setting the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 24", text="Recieve our newsletter.")
    # ...assigning any event handlers to the component
        
    def add_middle_label(self):
        self.middle_label = Label()
        self.middle_label.place(x=50, y=75)
        self.middle_label.configure(font="Arial 11", text="Please enter your email below to receive our newsletter. ")
        
        
    def add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=80, y=110)
        self.email_label.configure(font="Arial 10", text="Email: ")
    
        
        
    def add_email_entry(self):
        self.email_entry = Entry(width=45)
        self.email_entry.place(x=90, y=110)
    
    def add_email_button(self):
        self.email_button=Button(width=20)
        self.email_button.place(x=150, y=140)
        self.email_button.configure(bg="#F08080", font="Arial 9", text=" submit")
        
    def add_backgroud_canvas(self):
        self.backgroud_canvas=Canvas(width=500)
        self.backgroud_canvas.place(x=0 ,y=0)
        self.backgroud_canvas.configure(bg="#808A87")
      
        
        
        
        
        
        
         
   

    
     

  # handle events
  # (callback functions to handle events will go here)
  