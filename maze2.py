import turtle
 
wn=turtle.Screen() 
t1=turtle.Turtle() 

def savetracks():
	tracks=list()
	for i in range(0,17):
		tracks.append(i)
	t1.speed(1) 
	t1.penup() 
	t1.goto(-400,300)
	t1.pendown() 
	t1.pencolor("Red") 
	t1.right(90)
	tracks[0]=t1.pos() 
	t1.fd(400)
	tracks[1]=t1.pos() 
	t1.backward(150)
	tracks[2]=t1.pos() 
	t1.left(90)
	tracks[3]=t1.pos() 
	t1.fd(300) 
	tracks[4]=t1.pos()
	t1.left(90)
	tracks[5]=t1.pos() 
	t1.fd(300) 
	tracks[6]=t1.pos()
	t1.back(150) 
	tracks[7]=t1.pos()
	t1.right(90) 
	tracks[8]=t1.pos()
	t1.fd(300) 
	tracks[9]=t1.pos()
	t1.left(90) 
	t1.right(90) 
	t1.right(90)
	tracks[10]=t1.pos() 
	t1.fd(200)
	tracks[11]=t1.pos()
	tracks[12]=t1.pos() 
	t1.fd(300) 
	tracks[13]=t1.pos()
	t1.back(100) 
	tracks[14]=t1.pos()
	t1.left(90) 
	tracks[15]=t1.pos()
	t1.fd(200) 
	tracks[16]=t1.pos()
	print tracks
	return tracks
		
def replaytracks(tracks):
	for i in range(0,16):
		t1.penup()
		t1.goto(tracks[i])
		t1.pendown()
	 	t1.goto(tracks[i+1])

def lab7():
	res=savetracks()
	t1.home()
	t1.clear()
	replaytracks(res)
	wn.exitonclick()

def main():
	lab7()	

main()
	
if __name__=="main":
	main()
