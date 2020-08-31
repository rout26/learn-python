from tkinter import *

tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 490, 100)

canvas.create_text(150, 150, text='He said, "It\'s my curse,',
font=('Times', 15))
canvas.create_text(200, 200, text='But it could be worse,',
font=('Helvetica', 20))
canvas.create_text(220, 250, text='My cousin rides round',
font=('Courier', 22))
canvas.create_text(220, 300, text='on a goose."', font=('Courier', 30))



tk.mainloop()