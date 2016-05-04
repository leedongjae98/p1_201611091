import math
sel=list()
gb=tuple()
gb=[37.579775,126.976967]
gb[0]
Locat=list()
Locat=[(37.575803,126.097335),(37.571565,126.976525),(37.576399,126.985394),(37.570117,126.982886),(37.574455,126.957660)]
for i in range(0,len(Locat)):
    sel.append(math.sqrt((gb[0]-Locat[i][0])**2+(gb[1]-Locat[i][1])**2))
    
print min(sel)
    
    