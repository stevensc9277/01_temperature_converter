#Import required libraries
from tkinter import *
from turtle import color
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")

#Define functions
def on_enter(e, name):
   name.config(background='green', foreground= "white")

def on_leave(e, color, name):
   name.config(background=color, foreground= 'black')
   
#Create a to_click

to_click= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), bg="yellow")
to_click.pack(pady= 20)

to_click2= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), bg="blue")
to_click2.pack(pady= 20)

names = [to_click, to_click2]
# find colors
original = to_click.cget('bg')

#Bind the Enter and Leave Events to the to_click
names.bind('<Enter>', lambda e: on_enter(e, names[0])) 

names.bind('<Leave>', lambda e: on_leave(e, original, names[1]))

win.mainloop()