import itertools

l=[]
with open("input.txt") as ef:
    r=ef.readlines()
    for k in range(len(r)):
        l.append(r[k].split())

val = []
for i in range(12):
    val.append(i+1)


def distance(p1,p2):
    if p1<p2:
        d=l[p1-1][p2-1]
    if p2<p1:
        d=l[p2-1][p1-1]
    return d

orders = itertools.permutations(val)
#end=(1,)
small = 20000

distlist=[]

for i in orders:
    if i[0]==1:
        #tup=i+end
        #print(i)
        dist=0
        for j in range(len(i)-1):
            d=distance(i[j],i[j+1])
            dist=dist+int(d)
        #print(dist)
        #print(i[j+1])
        d=distance(1,i[j+1])
        dist=dist+int(d)
        #print(dist)
        if dist<small:
            small=dist
            print(small)

#print(distlist)

print(small)
