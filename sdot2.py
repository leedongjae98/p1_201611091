
dott=list()
for i in range(0,4):
	dott.append(i)

dott[0]=(0.00,0.00)
dott[1]=(100.00,0.00)
dott[2]=(100.00,-100.00)
dott[3]=(0.00,-100.00)

def drawSquareFrom(size,dott):
	for i in range(0,4):
		t1.penup()
		t1.setpos(dott[i])
		t1.pendown()
		t1.fd(size)
		t1.right(90)


import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

pos=(0,0)
	

drawSquareFrom(100,dott)