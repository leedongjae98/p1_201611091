sel1=raw_input("entered your height:")
sel2=raw_input("entered your weight:")
def computeBMI(height,weight):
    bmi=weight/(height*height)
    print bmi
    
    if bmi>=18.5 and bmi<25.0:
        print "normal weight"
    elif bmi>=25.0 and bmi<30:
        print "over weight"
    elif bmi<18.5:
        print "low weight"
    elif bmi>=30:
        print "over over weight"
    else:
        print "error"
sel1=float(sel1)
sel2=float(sel2)
print (computeBMI(sel1,sel2))
raw_input("press any button:")

