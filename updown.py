def updown(m):
	import random
	n=random.randint(1,m)
	for i in range(1,11):
		sel=raw_input("Guess number:")
		sel=int(sel)
		if sel==n:
			print "Good! you win!"
			break
		elif sel>n:
			print "Down!"
		elif sel<n:
			print "Up!"
	print n
	raw_input("Press any botton:")

updown(101)