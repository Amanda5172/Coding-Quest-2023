j=[]

def binary(num):
    k=bin(num)
    c=0
    sb=2**15
    check=False

    for i in k:
        if i =='1':
            c=c+1

    if c%2==0: 
        check=True
            
    if num>=sb:
        ap=num-sb
    else:
        ap=num

    #print(ap)
    if check==True:
        j.append(ap)
        

with open("input.txt","r") as ef:
    t=ef.readlines()

    for i in range(len(t)):
        binary(int(t[i]))

print(j)



total=0

for i in j:
    total=total+i

ave=total/len(j)

print(ave)
