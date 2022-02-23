from tkinter import *
from functools import partial       #To prevent unwanted windows
import re


class Converter:
    def __init__(self, parent):
        
        # formatting variables
        background_colour = "light blue"

        # initialise list to hold calculation history
        self.all_calc_list = []

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

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold", text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)  

    def help(self):
        print("You asked for help")
        
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box and then push one of the buttons to convert the number to either degrees C or degrees F. \n\nThe Calculation History area shows up to seven past calculations (most recent at the top). \n\nYou can also export your full calculation history to a text file if desired.")

       
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
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)


        except ValueError:
            self.converted_label.configure(text="Enter a number!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def history(self, calc_history):
        History(self, calc_history)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

        return rounded     

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
        self.export_button = Button(self.export_dismiss_frame, text="Export", font="arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font="arial 12 bold", command=partial(self.close_history))
        self.dismiss_button.grid(row=0, column=1)


    def export(self, calc_history):
        get_export = Export(self, calc_history)

    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

class Export:
    
    def __init__(self, partner, calc_history):
        background = "#a9ef99"      # pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # set up GUI frame
        self.export_frame = Frame(self.export_box,  bg=background, width=300)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # export instructions (label, row 1)
        self.export_text = Label(self.export_frame, width=40, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file", justify=LEFT, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # warning text.. (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists, its contents will be replaced with your calculation history", justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)
       
        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background)
        self.save_error_label.grid(row=4)

        # save / cancel frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", font="arial 12 bold", command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        # cancel button
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", font="arial 12 bold", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)
    
    def save_history(self, parent,calc_history):
        
        # regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
                has_error = "yes"
                break

        if filename == " ":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            # change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        
        else:
            # If there are no errrors, generate text file and then close dialogue box
            
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

    def close_export(self, partner):
        # put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

class Help:
    
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box,  bg=background)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange", font=("Arial", "10", "bold"), command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()   


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
