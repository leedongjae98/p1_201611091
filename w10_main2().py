def peoplemany():
    people=list()
    sumx=0
    sumy=0
    sumsum=list()
    sumgu=0


    people=[
        (74425,76326),
        (61164,61636),
        (109688,115744),
        (144796,146776),
        (174996,181676),
        (177841,177434),
        (204630,205980),
        (223373,232245),
        (161055,166130),
        (171576,176735),
        (279169,293772),
        (239450,251066),
        (148690,156510),
        (237792,242641),
        (283869,296762),
        (209344,210282),
        (118965,114441),
        (186503,186856),
        (195734,203014),
        (254381,249472),
        (271654,295354),
        (319197,335045),
        (229829,231671)
        ]
    for i in range(0,len(people)):
        sumsum.append(i)
        
    for i in range(0,len(people)):
        print people[i][0],people[i][1]
        sumx=sumx+people[i][0]
        sumy=sumy+people[i][1]
        sumsum[i]=[people[i][0]+people[i][1]]
        
    for i in range(0,len(people)):
        sumgu=sumgu+sumsum[i][0]
        
        
    print sumx/len(people)
    print sumy/len(people)
    print sumgu/len(people)
    print sumsum

def lab10():
    peoplemany()

def main():
    lab10()


if __name__=="main":
    main()