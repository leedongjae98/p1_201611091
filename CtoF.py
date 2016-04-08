def Temperature():
    sel=raw_input("C or F:")
    sell=raw_input("Temperature?:")

    tem=int(sell)
    if(sel=='C'):
        print "you entered C"
        CtoF=(tem*1.8)+32
        print CtoF
        print 'F'
    else:
        if(sel=='F'):
            print "you entered F"
            FtoC=(tem-32)*(5/9.0)
            print FtoC
            print 'C'
        else:
            print "sorry"
Temperature()
raw_input("press any button:")
