"""
This is the GUI and main program for Shaker
"""

from tkinter import *
from tkinter.ttk import *


class App(Tk):
    def __init__(self):
        super().__init__()

        # Window geometry and title
        self.title = "Shaker"
        self.geometry("760x600")

        # Define all elements
        name_bar = Label(self, text="Welcome to Shaker!")
        ingredients = Text(self, height=20, width=40)
        instructions = Text(self, height=20, width=40)
        self.photo_image = PhotoImage(file="./square_test_pattern.png")
        drink_img = Label(self, text="Photo goes here")
        prev_button = Button(self, text="<<")
        home_button = Button(self, text="Home")
        next_button = Button(self, text=">>")
        add_button = Button(self, text="Add")
        edit_button = Button(self, text="Edit")
        search_bar = Text(self, height=1, width=40)
        random_button = Button(self, text="Random")

        # Assign elements to grid
        name_bar.grid(row=0, column=0, columnspan=4, sticky=E+W)
        drink_img.grid(row = 1, column=4, columnspan=2)
        ingredients.grid(row=1, column = 0, columnspan=2, rowspan=5, sticky = N+S+W+E)
        instructions.grid(row=1, column = 2, columnspan=2, rowspan=5, sticky = N+S+W+E)
        prev_button.grid(row=6, column=0, sticky = W+E)
        home_button.grid(row=6, column=1, columnspan=2, sticky = W+E)
        next_button.grid(row=6, column=3, sticky = W+E)
        add_button.grid(row=4, column=4, sticky = W+E)
        edit_button.grid(row=4, column=5, sticky = W+E)
        search_bar.grid(row=5, column=4, columnspan=2, sticky = W+E)
        random_button.grid(row=6, column=4, columnspan=2, sticky = W+E)



if __name__ == "__main__":
    app = App()
    app.mainloop()

mainloop()
