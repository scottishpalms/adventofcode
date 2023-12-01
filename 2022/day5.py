import numpy as np
import copy

rows, cols = (1000,1000)
crates = np.empty([rows,cols], dtype=str)
instructions = []
i,j=0,0
answer1, answer2 = '',''

f = open("input.txt", "r")
for line in f:#get the crate initial positions into a numpy array
    if(line[1] == '1'):
        break
    
    row = []
    for char in line:
        if char.isalpha():
            crates[j,i] = (char)
        j+=1
    i+=1
    j=0
    
listCrates = crates.tolist()#convert to a python list to make use of .pop() and .append()
i,j=0,0
#There's a ton of empty columns right now. get rid of them:
for j in range(0,rows):
    listCrates[i].reverse()   
    if all(char == '' for char in listCrates[i]):
        listCrates.pop(i)
    else: i+=1  

i,j=0,0
#There's still some empty "cells." get rid of them:
for row in listCrates: #get rid of empty cells
    for char in range(0,len(row)):       
        if listCrates[i][j] == '':
            listCrates[i].pop(j)
        else:
            j+=1
    i+=1
    j=0

#Now that the crates are loaded, we can finally get the instructions
lastCharWasNumber = False
i=0
for line in f:
   row = []
   if (line[0] == "\n"):continue#burn the blank iterator value
   for char in line:
       if (lastCharWasNumber and char.isnumeric()):
           row[0] = 10*row[0] + int(char) #REALLY dirty way of accounting for moves >10
           continue
       else: lastCharWasNumber = False
       if char.isnumeric():
           row.append(int(char))
           lastCharWasNumber = True
           i+=1
   instructions.append(row)

listCrates1 = copy.deepcopy(listCrates)#shallow copy doesn't work on 2d lists
listCrates2 = copy.deepcopy(listCrates)#use deep copy instead
crane9001 = []
#move[0] = number of crates to move
#move[1] = stack to pull from 
#move[2] = stack to add to
for move in instructions:
    print(move)
    move[1] -= 1#offset instructions by 1 since arrays start at 0
    move[2] -= 1
    numCratesToMove = move[0]
    while (move[0]>0):        
        crane9000 = listCrates1[move[1]].pop()
        #crane9001 = listCrates2[move[1]].pop((move[0]-1)*-1) #failed attempt to do something clever for part 2
        crane9001.append(listCrates2[move[1]].pop())
        listCrates1[move[2]].append(crane9000)        
        move[0]-=1
    while(numCratesToMove > 0):#clever attempt wasn't panning out. do it the lazy way. 
        listCrates2[move[2]].append(crane9001.pop())
        numCratesToMove -= 1

for row in listCrates1:
    answer1+=row.pop()
for row in listCrates2:
    answer2+=row.pop()
print("Part 1 answer: ", answer1)
print("Part 2 answer: ", answer2)

#print('\n'.join(map(''.join, listCrates2)))#print out 2d array
