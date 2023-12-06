import os
import re
answer1, answer2, i, j, game = 0,0,1,0, 1

pattern =  re.compile('[^\s\d.]')
data = []
partLocations = set()#set so that any numbers with 2 symbols aren't doublecounted
symbolLocations = []#(x,y) coordinates of symbols in data[][]
gearLocations = []

f = open("input.txt", "r")
for i, line in enumerate(f):#read the input file
    line = line.strip()
    data.append(list(line))#copy the file line by line so we get a 2d list of characters
    for j, character in enumerate(list(line)):
        if(character == '*'):
            symbolLocations.append([i,j, True])#potential gears. need to confirm later on
        elif(pattern.search(character)):#is this character any other symbol?
            #if so, we need mark it for search
            symbolLocations.append([i, j, False])

            #print([i,j, pattern.search(character).group()])
numRows = i
numCols = j
for symbol in symbolLocations:#now run through the list of symbols
    yStart = max(0, symbol[0] - 1)
    yEnd = min(numRows, symbol[0] + 1)
    xStart = max(0, symbol[1] - 1)
    xEnd = min(numCols, symbol[1] + 1)
    gearCheck = symbol[2]
    numGears =  0
    gearList = []
    for row in range(yStart, yEnd+1):
        for col in range(xStart, xEnd+1):
            #print(row, col)
            tempCol = col#search backwards first
            partNumber = []
            if(data[row][col].isdigit()):#found part of a part number!
                if((row*numCols + col) not in partLocations):
                    while(data[row][tempCol].isdigit() and tempCol > -1):                    
                        partNumber.insert(0, data[row][tempCol])
                        partLocations.add((row*numCols + tempCol) )
                        tempCol-=1
                    tempCol = col+1#now search forwards
                    while(data[row][tempCol].isdigit()):
                        partNumber.append(data[row][tempCol])
                        partLocations.add((row*numCols + tempCol))
                        tempCol+=1
                        if(tempCol > numCols):#need to break here so it doesn't go out of bounds in the while statement
                            break
                        
                    partNumber = int(''.join(partNumber))
                    answer1 += partNumber
                    if(gearCheck):#is this symbol a *
                        numGears += 1
                        gearList.append(partNumber)
                    print (partNumber)
    if(numGears == 2):#ignore any cases where there are 3 parts next to a gear
        answer2 +=gearList[0]*gearList[1]
        print(gearList)

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)


