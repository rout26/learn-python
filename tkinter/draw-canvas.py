from tkinter import *

window=Tk()
window.title('My page')
canvas=Canvas(window,width=500,height=500, bg='blue')
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 490, 100)

canvas.create_text(150, 150, text='He said, "It\'s my curse,',
font=('Times', 15))


canvas.create_text(220, 250, text='My cousin rides round',
font=('Courier', 22))
canvas.create_text(220, 300, text='on a goose."', font=('Courier', 30))



window.mainloop()