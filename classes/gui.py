# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Frame, Button, PhotoImage
from classes.Menu import Menu
from classes.Options import Options

class gui(Tk) :
    def __init__(self, *args, **kwargs) -> None:

        self.assets_path = "./assets"
        #init app :
        Tk.__init__(self, *args, **kwargs)
        self.title('Tic tac toe')
        self.geometry('1200x700')
        self.bg = "#6992FC"
        self.pages=[Menu, Options]
        self.resizable(False, False)

        # creating a container
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 

        for F in (self.pages):
            page_name = F.__name__
            frame = F(parent=container, controller=self, bg=self.bg)
  
            self.frames[page_name] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame("Menu")


    # to display the current frame passed as
    # parameter
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
    def relative_to_assets(self, path: str) -> str:
            return self.assets_path+"/"+path
        
        
