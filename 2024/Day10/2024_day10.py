### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day10"
answer1, answer2 = 0, 0
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


def explorePath(grid, startingRow, startingCol, startingDirection):
     desiredLevel = grid[startingRow][startingCol] + 1
     #print(f"Exploring ({startingRow}, {startingCol}) -> Level: {desiredLevel} -> Direction: {dir[startingDirection][2]}")
     if desiredLevel == 10:
          #print(f"Found valid path ending at ({startingRow}, {startingCol})")
          return [(startingRow, startingCol)]
     validDirections = checkRadius(grid, startingRow, startingCol, startingDirection, desiredLevel)
     if(not validDirections):
          return []
     totalPaths = []
     #if(len(validDirections) >1):
          #print("Branch! going to look at ", dir[validDirections[0]][2], "and", dir[validDirections[1]][2])
     for direction in validDirections:
          newDirection = dir[direction][3]
          totalPaths.extend(explorePath(grid, startingRow+dir[direction][0], startingCol+dir[direction][1], newDirection))
        
     return totalPaths
          




def checkRadius(grid, startingRow, startingCol, originDir, desiredLevel):
    validDirections = []
    for directionIndex in range(0, len(dir)):
        newDirection = dir[directionIndex]
        newRow = startingRow+newDirection[0]
        newCol = startingCol+newDirection[1]
        if(newRow < len(grid) and newRow >= 0 and newCol >= 0 and newCol <len(grid[0])):             
            #print((newRow, newCol), grid[newRow][newCol])
            if(grid[newRow][newCol] == desiredLevel):
                    validDirections.append(directionIndex % len(dir))
    return validDirections



currentPos = [0,0]
#pos3 is the "next direction"
down = [1,0,"down", 0]
up = [-1,0, "up", 2]
left = [0, -1, "left", 1]
right = [0, 1, "right", 3]
dir = [up, right, down, left]
currentDir = 0
grid = []

for row, line in enumerate(f):
     grid.append(list(line.strip()))
     for col in range(0, len(grid[row])):
        if(grid[row][col] == '.'):
            grid[row][col] = -1
        else:
             grid[row][col] = int(grid[row][col])



for row, line in enumerate(grid):
     for col, spot in enumerate(line):
          if(spot == 0):
            paths = explorePath(grid, row, col, 0)
            answer1 += len(set(paths))
            answer2 += len(paths)

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)