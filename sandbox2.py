#Import required libraries
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")
#Define functions
def on_enter(e):
   to_click.config(background='OrangeRed3', foreground= "white")

def on_leave(e):
   to_click.config(background= 'SystemButtonFace', foreground= 'black')
#Create a to_click
to_click= Button(win, text= "Click Me", font= ('Helvetica 13 bold'))
to_click.pack(pady= 20)

#Bind the Enter and Leave Events to the to_click
to_click.bind('<Enter>', on_enter)
to_click.bind('<Leave>', on_leave)
win.mainloop()