import turtle
t = turtle.Pen()
angle = 0
for y in range(0,360):
	t.left(angle)
	for x in range(0,4): 
			t.forward(200)
			t.left(90)
	angle = angle + 1

# turtle.getscreen()._root.mainloop() 
t.mainloop()