
item=[]
quantity=[]

with open("input.txt","r") as ef:
    t=ef.readlines()
    for k in range(len(t)):
        x,y,z=t[k].split()

        if z not in item:
            item.append(z)
            quantity.append(int(y))
        else:
            r=item.index(z)
            quantity[r]=quantity[r]+int(y)

        
        

print(item)
print(quantity)


mod=1

for i in range(len(quantity)):
    mod = mod * (quantity[i] % 100)

print(mod)

