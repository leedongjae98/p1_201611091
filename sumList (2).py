x=list()
def sumList(aList):

	sum=0
	for i in range(0,aList):
		if(i%4==0 and i%5):
			x.append(i)
	for i in range(0,len(x)):
		sum+=x[i]
	return sum
def main(x):
	print sumList(x)
main(1001)
