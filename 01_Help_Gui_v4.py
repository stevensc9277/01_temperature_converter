from tkinter import *
from functools import partial       #To prevent unwanted windows
import random


class Converter:
    def __init__(self, parent):
        
        # formatting variables...
        background_color = "light blue"

        # Converter Main screen gui...
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        # temperature conversion heading (row 0)
        self.temp_converter_label = Label(text="Temperature Converter", font=("Arial", "16", "bold"), padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
