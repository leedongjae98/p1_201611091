sel1=raw_input("player1 choose R,S or P:")
sel2=raw_input("player2 choose R,S or P:")
def RSP(u1,u2):
    if u1==u2:
        res="Draw."
    elif u1=="S":
        if u2=="R":
            res="R win!!"
        else:
            res="S win!!"
    elif u1=="R":
        if u2=="P":
            res="P win!!"
        else:
            res="R win!!"
    elif u1=="P":
        if u2=="S":
            res="S win!!"
        else:
            res="P win!!"
    else:
        res="error!! plz choose R,S or P!"
    return res

print(RSP(sel1,sel2))

raw_input("press any button:")






