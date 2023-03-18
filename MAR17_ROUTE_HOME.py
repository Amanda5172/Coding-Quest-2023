j=[]

with open("input.txt","r") as ef:
    t=ef.readlines()
    for i in range(len(t)):
        j.append(t[i].split())


start="TYC"
placesbeen=["TYC"]
time=0
timelist=[]

def Possible(place):
    global placesbeen
    global start
    global time
    
    if place[0:3] not in placesbeen:
        placesbeen.append(place[0:3])
        time=time+int(place[4::])+600
        start=place[0:3]
        return True

def Path():
    global time
    
    while start!="EAR":
        for i in range(len(j)):
            if j[i][0]==start:
                for k in range(len(j[i])-2):
                    if Possible(j[i][k+2]):
                        Path()
                        placesbeen.remove(j[i][k+2][0:3])
                        time=time-600-int(j[i][k+2][4::])
                return
    
    #print(placesbeen)
    #print(time)
    timelist.append(time-600)

Path()
print(timelist)
print(min(timelist))

