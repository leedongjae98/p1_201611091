def drawSquareAt(size,pos):
	dot=list()
	t1.penup()
	t1.setpos(pos)
	t1.pendown()
	for i in range(0,4):
		dot.append(i)
	for i in range(0,4):
		dot[i]=t1.pos()
		t1.fd(size)
		t1.right(90)
	print dot

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

pos=(0,0)

drawSquareAt(100,pos)