from tkinter import *
from functools import partial       #To prevent unwanted windows
import random


class Converter:
    def __init__(self, parent):
        
        # formatting variables...
        background_color = "light blue"

        # initialise list to hold calculation history
        self.all_calc_list = ['0 degrees C is -17.8 degrees F', '0 degrees C is 32 degrees F', '24 degrees C is 75.2 degrees F', '100 degrees C is 37.8 degrees F']

        # Converter Main screen gui...
        self.converter_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, font=("Arial", "14"), text="History", padx=10, pady=10, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)
    
    def history(self, calc_history):
        History(self, calc_history)

class History:
    
    def __init__(self, partner, calc_history):
        background = "#a9ef99"      # pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box,  bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations. Please use the export button to create a text file of all your calculations for this session", font="arial 10 italic", justify=LEFT, fg="maroon", bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # History output goes here.. (row 2)


        # generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for i in range(0, 7):
                history_string += calc_history[len(calc_history) - i - 1] + "\n"

        else:
            for i in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(i) - 1] + "\n"
                self.history_text.config(text="Here is your calculation history. You can use the export button to save this data to a text file if desired.")

        # label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string, bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export / dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export", font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font="arial 12 bold", command=partial(self.close_history))
        self.dismiss_button.grid(row=0, column=1)




    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
