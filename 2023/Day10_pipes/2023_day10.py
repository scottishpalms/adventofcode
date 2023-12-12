answer1, answer2 = 0,0
f = open("input.txt", "r")
up, down, left, right = 0,1,2,3
lastDirection =  -1
sPos = (0,0)
upPipes = {'|', '7', 'F', 'S'}
downPipes = {'|', 'L', 'J', 'S'}
leftPipes = {'-', 'F', 'L', 'S'}
rightPipes = {'-', '7', 'J', 'S'}
maze = []
for i, line in enumerate(f):#read the input file
    maze.append(line.strip()) #load the input into the 2D array Maze
    for j, pipe in enumerate(maze[-1]):
        if pipe =='S':
            sPos = (i,j)

i = sPos[0]
j = sPos[1]

currentPos = maze[i][j]
firstTime = True
steps = 0
while(currentPos!='S' or firstTime == True):
    steps += 1
    print(currentPos, i, j)
    firstTime = False
    #check up:
    if(currentPos in downPipes or currentPos =='S') and lastDirection != down:#when you look up, you have to make sure that your current pipe is one that is in the downPipe list (so that the pipe above you could connect down to it)
        if maze[i-1][j] in upPipes:
            i -= 1
            j+= 0
            currentPos = maze[i][j]
            lastDirection = up
            continue
    #check down
    if(currentPos in upPipes or currentPos == 'S') and lastDirection != up:
        if maze[i+1][j] in downPipes:
            i += 1
            j += 0
            currentPos = maze[i][j]
            lastDirection = down
            continue
    #check left
    if(currentPos in rightPipes or currentPos == 'S') and lastDirection != right:
        if maze[i][j-1] in leftPipes:
            i += 0
            j -= 1
            currentPos = maze[i][j]
            lastDirection = left
            continue
    #check right
    if((currentPos in leftPipes or currentPos == 'S') and lastDirection != left ):
        if maze[i][j+1] in rightPipes:
            i += 0
            j += 1
            currentPos = maze[i][j]
            lastDirection = right
            continue
print(maze)
print("Part 1 Answer: ", steps/2)
print("Part 2 Answer: ", answer2)


