### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day6"
answer1, answer2, i, j, k = 0,0,0,0,0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

""" grid directions:
   (row, col)
    0123456 right
   0
   1  
   2
   down
"""
def getNextPos(pos, dir, currentDir):
    newPos = pos[:]
    newPos[0] += dir[currentDir][0]
    newPos[1] += dir[currentDir][1]
    return newPos

def calculateSteps(currentPos, nextPos, dir, currentDir):
    MAX_STEPS = 10000
    steps = 0
    totalSteps = 0
    while(nextPos[0] >=0 and nextPos[0] < height and nextPos[1] >=0 and nextPos[1] < width and totalSteps < MAX_STEPS):
        #print(nextPos)
        if(grid[nextPos[0]][nextPos[1]]=='#'):
            currentDir = (currentDir +1) % 4
            #print(grid[nextPos[0]][nextPos[1]])
        elif (grid[nextPos[0]][nextPos[1]] !='x'):
            grid[nextPos[0]][nextPos[1]] = 'x'
            # for line in grid:
            #     print("".join(line))
            # print("\n")
            steps += 1
            currentPos = nextPos
        else:
            currentPos = nextPos
        totalSteps+=1
        nextPos = getNextPos(currentPos, dir, currentDir)
    #print(totalSteps)
    if(totalSteps >= MAX_STEPS-10):
        return steps, 1
    return steps, 0


currentPos = [0,0]
down = [1,0]
up = [-1,0]
left = [0, -1]
right = [0, 1]
dir = [up, right, down, left]
currentDir = 0
grid, obstacles = [], []

#get the grid pulled in
for lineNumber, line in enumerate(f):
    grid.append(list(line.strip()))
    for cell, pos in enumerate(line.strip()):
        if(pos == '^'):
            currentPos = [lineNumber, cell]
        elif (pos == '.'):
            obstacles.append([lineNumber, cell])
width = len(line.strip())
height = len(grid)

#part1:
startingPos = currentPos[:]
nextPos = getNextPos(currentPos, dir, currentDir)
answer1 = calculateSteps(currentPos, nextPos, dir, currentDir)[0]

#part2:
progress = 0
for obstacle in  obstacles:
    #reset everything
    currentPos = startingPos[:]
    currentDir = 0
    nextPos = getNextPos(currentPos, dir, currentDir)

    grid[obstacle[0]][obstacle[1]] = '#' #add an obstacle to the grid
    answer2 += calculateSteps(currentPos, nextPos, dir, currentDir)[1]
    grid[obstacle[0]][obstacle[1]] = '.' #clear out the obstacle for the next run
    
    #lazy %done tracking
    progress +=1
    if(progress % 500 == 0):
        print((progress/len(obstacles))*100, "%")

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)