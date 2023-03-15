grid=[['S', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
score=0
snakepos=[[0,0]]

def displaygrid():
    for i in range(20):
        for j in range(20):
            print(grid[i][j], end="")
        print()

def move(moves,r,c):
    global row
    global column
    
    match moves:
        case "R":
            column=c+1 #row stays the same
        case "L":
            column=c-1
        case "U":
            row=r-1#do this bcos if grid[-1] will show cannot
        case "D":
            row=r+1    

def possible(row, column):
    global grid
    global score
    
    po=True
    if row<0 or row>19 or column<0 or column>19:
        po=False
        #print("Out of range")
    elif grid[row][column]=='S':
        po=False
        #print("Hit snake")
    elif grid[row][column]=='F':
        score=score+101
        #print("Ate fruit")
    else:
        score=score+1
    return po


    
def fruit(s):
    global fruitco
    global grid
    grid[int(fruitco[s+1])][int(fruitco[s])]='F'
    s=s+2
    return s

def movesnake(snakelength,row,column):
    global snakepos
    global grid
    global s
    if grid[row][column]=='F':
        grid[row][column]='S' #how to remove the end of the snake ->make it move
        snakepos.append([row,column])
        s=fruit(s)
        #displaygrid()
    else:
        grid[row][column]='S'
        snakepos.append([row,column])
        grid[snakepos[0][0]][snakepos[0][1]]='.'
        snakepos.remove(snakepos[0])
    
    


t="RRRRRRRRRRDDDDDDDDDDUUUUULLLLLLDDDDDDDDDDDDRRRRRRUUUUUUUUUUULLLLLLUUUURRDDRDRDDRDRDRDRDDDDRRRRRRUULLLLLLDLDLDLUUUUUUUULLLLLLLLUUURRRRDDDRRRRRRRRRRRRUUULLDDDRRDDDDDDDDDDLLLLLLLLLLLUUUUUUUUUUUUUUUULLLLLDDDRURRDDDDDDLLDRRRRRRUUUUUUURURRRRRRDDDDDDDDDDDDDLLLLLDRRRRRRRRUUUUUULLLLLLLUUUUUUUUURRRDDDDDDLLLDDRRRRUUUUURRDDDDDDLLLLLLLLLLLLLLLDDDDRRRRUUURUUUUUUUUURRRRRDDDDRRRRRDDDDDDLLLLLLDLLLLLUUUUUUUUURRDDDDDDDDDDDDDLLLLUUUUURRRUUURRDDDDLLDRRRRRRRRRRUUUUUUULLLDDDRDDDLLLDDRRRRRRUUUUUUUUUUUUULLLLDDDDDDDDDDDDDDLLLLUUUUUUUUUUURRRRRRRDDDDDDDLLLLLLDDDDDLDLLLUUUUUULLLLLLLUUUUUUUUURRRRRRRRRDDDDDDDDDDRRRRRRRRUULLLLLLUUUUURRRUUUUULLLLDDLDLLLLLDDDDRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLDDDDLLLDDDDDDDDDDRRRRRRRRRRRRRRRUUUUUUUUUULLLLLLLLLULLLLLLLUURRRRRRRRRRRRRRRRRDDDDDDDDDDDLLLLLLLLLDDDDLLLLLLLLDRRRRRRRRRUUURRRRRRRRDDDDLLLLLLLLLLLLLLLLLLUUUURRRRRRRULLLLLLLUUUUUUUUUUUURRRRRRRRDDDDDRDDDDDDDDDDDRRRRRDRRRRUULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRUULLLLLLLLLLLLLLLLDDDDDDDD"
orfruit="5,5 8,17 5,2 17,14 2,4 17,6 17,17 1,1 2,3 4,9 13,2 12,15 18,15 12,1 17,5 2,14 7,3 17,6 7,13 6,5 5,17 17,12 16,7 15,15 14,14 10,8 15,5 12,12 9,18 7,16 1,3 16,13 12,11 13,6 11,1 5,4 15,8 6,3 5,14 5,3 5,1 17,12 10,14 13,14 18,14 6,14 7,1 15,16 13,4 18,3 9,1 3,13"

orfruit=orfruit.replace(',',' ')

fruitco=[]
for i in orfruit.split():
    fruitco.append(i)


po=True
i=0
row=0
column=0
score=0
snakelength=1
s=0
s=fruit(s)
#displaygrid()

while po==True and i<len(t):
    move(t[i],row,column)
    #print(row,column)
    po = possible(row,column)
    if po==True:
        movesnake(snakelength,row,column)
    #print(score)
    i=i+1
    #check using hints
    #if i==100:
        #print(t[i-1])
        #print(row,column)
        #displaygrid()
        #print(score)

#displaygrid()
print(score)

