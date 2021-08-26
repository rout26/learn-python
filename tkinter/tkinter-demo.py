from tkinter import *
from tkinter import messagebox


def hello():
    messagebox.showinfo('Hello', 'Hello World')

window = Tk()
window.geometry("500x300")

btn1 = Button(window, text='Click me', command=hello)
btn1.pack()

window.mainloop()