#get permutation
#get distance

#function to sort data?
import math

l=[]
with open("input.txt") as ef:
    r=ef.readlines()
    for k in range(len(r)):
        l.append(r[k].split())

print(l)



def distance(p1,p2):
    d=l[p1-1][p2-1]
    return d


start=1
placesbeen=[1]
dist=0
distlist=[]
n=0


def Possible(place):
    global placesbeen
    global start
    global dist
    
    if place not in placesbeen:
        placesbeen.append(place)
        dist=dist+int(distance(start,place))
        start=place
        return True
    

def Path():
    global dist
    
    for i in range(12):
        if Possible(i+1):
            Path()
            print(placesbeen)#need to go to every point, need to end at 1
            if len(placesbeen)>1:
                placesbeen.remove(placesbeen[i-1])
                #dist=dist-int(distance(placesbeen[i-1],placesbeen[i]))
    return
    print(placesbeen)
        
    
    #print(placesbeen)
    #print(distlist)
    #distlist.append(dist-600)

Path()
    
