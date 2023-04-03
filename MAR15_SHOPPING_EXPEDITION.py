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
