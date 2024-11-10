from tkinter import *

window = Tk()
window.title("Welcome to Tkinter Window")
window.geometry('300x300')

greeting = Label(text = "Hello friend" , fg = 'black' , bg = 'white')
button = Button(text = "Click Me" , bg = 'black' , fg = 'white')
entry = Entry(fg = "yellow" , bg="blue" , width = 50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master = window , relief=RAISED , borderwidth = 5)
frame.pack()
label = Label(master=frame , text = "Sample Frame")
label.pack()

textbox = Text(fg = "green" , bg = "yellow")
textbox.pack()