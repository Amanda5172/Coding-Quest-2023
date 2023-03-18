wincodes=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

wx=0
wo=0
d=0

def check(checkwin):
    t=0
    for i in range(len(wincodes)):
        r= False
        t=0
        for j in range(len(wincodes[i])):
            if str(wincodes[i][j]) in checkwin:
                t=t+1
        if t==3:
            r= True
            break

    return r

with open("input.txt","r") as ef:
    t=ef.readlines()

for i in range(len(t)):
    o=t[i]
    g=o.replace(' ','')
    px=[]
    po=[]

    for i in range(len(g)):
        if i<4:
            if i%2==0:
                px.append(g[i])
            else:
                po.append(g[i])
        if i>=4 and i%2==0:
            px.append(g[i])
            px.sort()
            r=check(px)
            if r==True:
                wx=wx+1
                break
        elif i>=4 and i%2==1:
            po.append(g[i])
            po.sort()
            r=check(po)
            if r==True:
                wo=wo+1
                break
    if r!=True:
        d=d+1


print(wx)
print(wo)
print(d)


print(wx*wo*d)

