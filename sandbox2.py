#Import required libraries
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")

def setup_hover(button_name):
   color = button_name.cget("bg")
   button_name.bind('<Enter>', lambda e: on_enter(e, button_name, color)) 

   button_name.bind('<Leave>', lambda e: on_leave(e, color, button_name))
#Define functions
def on_enter(e, name, color):
   name.config(background='dark '+color, foreground= "white")

def on_leave(e, color, name):
   name.config(background=color, foreground= 'black')
   
#Create a to_click

to_click= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), bg="green")
to_click.pack(pady= 20)

to_click2= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), bg="blue")
to_click2.pack(pady= 20)

setup_hover(to_click)
setup_hover(to_click2)

win.mainloop()