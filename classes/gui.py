# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class gui :
    def __init__(self) -> None:
        #attributes :

        self.window = Tk()
        self.assets_path = "./assets"

        #init :
        self.default_window()

    def relative_to_assets(self, path: str) -> str:
        return self.assets_path+"/"+path

    def default_window(self) -> None :
        self.window.title('Tic tac toe')
        self.window.geometry("1200x700")
        self.window.configure(bg = "#6992FC")
        
        

    def menu_window(self) -> None :
        button_image_1 = PhotoImage(
        file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=389.0,
            y=96.0,
            width=423.0,
            height=92.0
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=389.0,
            y=235.0,
            width=423.0,
            height=92.0
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=389.0,
            y=374.0,
            width=423.0,
            height=92.0
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=389.0,
            y=513.0,
            width=423.0,
            height=92.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()
        
        


""" def relative_to_assets(path: str) -> str:
    ASSETS_PATH = "./assets"
    return ASSETS_PATH+"/"+path



window = Tk()

window.geometry("1200x700")
window.configure(bg = "#6992FC")


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=389.0,
    y=96.0,
    width=423.0,
    height=92.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=389.0,
    y=235.0,
    width=423.0,
    height=92.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=389.0,
    y=374.0,
    width=423.0,
    height=92.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=389.0,
    y=513.0,
    width=423.0,
    height=92.0
)
window.resizable(False, False)
window.mainloop()
 """