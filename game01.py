import turtle
import sys

wn=turtle.Screen()

wn.bgpic("C:\Users\game.gif")

t1=turtle.Turtle()
ta=turtle.Turtle()
tb=turtle.Turtle()
tc=turtle.Turtle()
td=turtle.Turtle()

t1.shape("turtle")
ta.shape("turtle")
tb.shape("turtle")
tc.shape("turtle")
td.shape("turtle")

t1.color("Blue")
ta.color("Green")
tb.color("Green")
tc.color("Green")
td.color("Green")

t1.penup()
ta.penup()
tb.penup()
tc.penup()
td.penup()

t1.goto(-150,-200)
ta.goto(200,300)
tb.goto(270,300)
tc.goto(360,300)
td.goto(450,300)

ta.right(180)
tb.left(90)
tc.right(90)

t1.shapesize(5)

headd=t1.heading()
t1.right(90)
headc=t1.heading()
t1.right(90)
heada=t1.heading()
t1.right(90)
headb=t1.heading()

def k1():
	t1.setheading(headb)

def k2():
	t1.setheading(heada)

def k3():
	t1.setheading(headc)

def k4():
	t1.setheading(headd)

wn.onkey(k1, "w")
wn.onkey(k2, "a")
wn.onkey(k3, "s")
wn.onkey(k4, "d")

t1.speed(400)

j=1

def ago(j):
	ta.speed(j)
	ta.goto(200,-240)
	ta.color("Red")
	ta.goto(200,-300)
	if not t1.heading()==ta.heading():
		sys.exit()
	ta.color("Green")
	ta.speed(200)
	ta.goto(200,300)

def bgo(j):
	tb.speed(j)
	tb.goto(270,-240)
	tb.color("Red")
	tb.goto(270,-300)
	if not t1.heading()==tb.heading():
		sys.exit()
	tb.color("Green")
	tb.speed(200)
	tb.goto(270,300)

def cgo(j):
	tc.speed(j)
	tc.goto(360,-240)
	tc.color("Red")
	tc.goto(360,-300)
	if not t1.heading()==tc.heading():
		sys.exit()
	tc.color("Green")
	tc.speed(200)
	tc.goto(360,300)

def dgo(j):
	td.speed(j)
	td.goto(450,-240)
	td.color("Red")
	td.goto(450,-300)
	if not t1.heading()==td.heading():
		sys.exit()
	td.color("Green")
	td.speed(200)
	td.goto(450,300)

tw=turtle.Turtle()
twn=turtle.Turtle()
twn.penup()
twn.goto(0,-50)

def gamestart():
	tw.write("Gamestart!!")
	twn.clear()
	for j in range(1,4):
		for i in range(1,11):
			import random
			r=random.randint(1,5)
			if r==1:
				ago(j)
			if r==2:
				bgo(j)
			if r==3:
				cgo(j)
			if r==4:
				dgo(j)
	twn.write("Clear!!")

t0=turtle.Turtle()
t0.penup()
t0.goto(-400,100)
t0.write("오른쪽 초록 거북이가 아래까지 내려오지전에 wasd로 파란거북이의 방향을 초록거북이의 방향과 일치시키시오")

ts=turtle.Turtle()
ts.penup()
ts.goto(-400,75)
ts.write("게임을 시작 할려면 g를 눌려주세요. 게임속도는 점점 빨라집니다.")

wn.onkey(gamestart, "g")
wn.listen()

wn.exitonclick()
