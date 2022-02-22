from tkinter import *
from functools import partial       # to prevent unwanted windows
import random


class Converter:
    def __init__(self, parent):
        
        # formatting variables
        background_colour = "light blue"

        # initialise list to hold calculation history
        self.all_calc_list = ['0 degrees C is -17.8 degrees F', '0 degrees C is 32 degrees F', '40 degrees C is 104 degrees F', '40 degrees C is 4.4 degrees F', '12 degrees C is 53.6 degrees F', '24 degrees C is 75.2 degrees F', '100 degrees C is 37.8 degrees F']

        # converter frame
        self.converter_frame = Frame(bg=background_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_colour, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame, bg=background_colour, text="Type in the amount to be converted and then push on of the buttons below...", font=("Arial 10 italic"), justify=LEFT, wrap=250, padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # conversion buttons frame (row 3, orchid1 | khaki1)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centigrade", font="Arial 10 bold", bg="Khaki1", padx=10, pady=10, command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", font="Arial 10 bold", bg="Orchid1", padx=10, pady=10, command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold", fg="purple", bg=background_colour, pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # history / help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font="Arial, 12 bold", text="Calculation history", width=15, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold", text="Help", width=5)
        self.help_button.grid(row=0, column=1)  
              
    def temp_convert(self, low):
        print(low) 

        error = "#ffafaf" # pale pink background for when entry box has errors

        # retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # check and convert to fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            #  check and convert to centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                # input is invalid (too cold!!)
                answer = "Too cold"
                has_errors = "yes"

            # display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # add answer to list for history 
            if answer != "Too cold":
                self.all_calc_list.append(answer)
                print(self.all_calc_list)


        except ValueError:
            self.converted_label.configure(text="Enter a number!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

        return rounded                                                                             

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
