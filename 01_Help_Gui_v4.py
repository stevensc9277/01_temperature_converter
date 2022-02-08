from tkinter import *
from functools import partial       #To prevent unwanted windows
import random


class Converter:
    def __init__(self):
        
        # formatting variables...
        background_color = "light blue"

        # Converter Main screen gui...
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
