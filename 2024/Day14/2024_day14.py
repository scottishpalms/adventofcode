### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day14"
answer1, answer2 = 0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
    GRID_WIDTH = 11
    GRID_HEIGHT = 7
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
     GRID_WIDTH = 101
     GRID_HEIGHT = 103
import re
ITERATIONS = 100
POSx = 0
POSy = 1
VELx = 2
VELy = 3
midX = (GRID_WIDTH-1)//2 
midY = (GRID_HEIGHT-1)//2 
""" grid directions:
   (row, col)=(y, x): NEED TO FLIP COMPARED TO INPUT
    0123456 right x
   0
   1  
   2
   down y
"""
grid = []
def calcNextPos(bot):
     bot[POSx] = (bot[POSx] + bot[VELx]) % GRID_WIDTH
     bot[POSy] = (bot[POSy] + bot[VELy]) % GRID_HEIGHT
     return bot

def printGrid(bots):
    grid=[]
    for row in range(0, GRID_HEIGHT):
        grid.append([])
        for col in range(0, GRID_WIDTH):
            grid[row].append(".")
            
    for bot in bots:
        if (grid[bot[POSy]][bot[POSx]] == "."):
            grid[bot[POSy]][bot[POSx]] = 1
        else: grid[bot[POSy]][bot[POSx]]+=1
    
    
    for row in grid:
        rowStr = ""
        for pos in row:
            rowStr += str(pos)
        print(rowStr)
    print("")

def isChristmasTree(robots):
    TREE_HEIGHT = 5

    christmas = True
    botSet = set()
    for bot in robots:
        botSet.add((bot[POSx],bot[POSy]))
    for bot in botSet:
        rightPos = bot
        leftPos = bot    
        for row in range(0, TREE_HEIGHT):
            if(rightPos in botSet and leftPos in botSet):
                rightPos = (rightPos[0]+1, rightPos[1]+1)
                leftPos = (leftPos[0]-1, leftPos[1]+1)
                if row==4:
                    return True
            else:
                christmas = False
                break
    return  christmas


robots = []
pattern = r'(-?\d+),(-?\d+).*?(-?\d+),(-?\d+)'
for line in f:
    robots.append([int(num) for group in re.findall(pattern, line) for num in group]) #this is atrocious as a oneliner. 

for turn in range(0, ITERATIONS):
    for bot in robots:     
        bot = calcNextPos(bot)
    #printGrid(robots)
    answer2+=1

print("midx:", midX, "midY:", midY)
quads = [0,0,0,0]
for bot in robots:
    if(bot[POSx]<midX):
        if(bot[POSy]<midY):
            quads[0] += 1
        elif(bot[POSy]>midY):
            quads[1] += 1
    elif(bot[POSx]>midX):
        if(bot[POSy]<midY):
            quads[2] += 1
        elif(bot[POSy]>midY):
            quads[3] += 1
    
answer1 = 1
for quad in quads:
    answer1 *= quad 
            

               

while not isChristmasTree(robots):
    for bot in robots:
    #bot = robot.copy()
        bot = calcNextPos(bot)
          #printGrid(robots)
    
    answer2+=1
    if(answer2 % 1000 == 0):
        print(answer2)


printGrid(robots)


     

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)