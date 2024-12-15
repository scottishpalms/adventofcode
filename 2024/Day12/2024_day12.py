### General setup: ###
USE_TEST_INPUT = 1
DAY_NAME = "Day12"
answer1, answer2 = 0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
from functools import cache
""" grid directions:
   (row, col)
    0123456 right
   0
   1  
   2
   down
"""

def explorePath(grid, startingRow, startingCol, startingDirection, visited=None):
    # Initialize visited set if not provided
    if visited is None:
        visited = set()
    fences = 4
    # Mark the current position as visited
    visited.add((startingRow, startingCol))
    
    veggie = grid[startingRow][startingCol]
    validDirections = checkRadius(grid, startingRow, startingCol, veggie)
    
    if not validDirections:
        coord = (startingRow, startingCol)
        return {coord}, fences  # No valid directions, end recursion
    
    totalPaths = set()
    #deadEnd = True

    for direction in validDirections:
        newRow = startingRow + dir[direction][0]
        newCol = startingCol + dir[direction][1]
        newDirection = dir[direction][3]
        fences -= 1

        
        # Only explore if the position has not already been visited
        if (newRow, newCol) not in visited:
            paths = explorePath(grid, newRow, newCol, newDirection, visited)
            totalPaths.update(paths[0])
            fences+=paths[1]
            #deadEnd = False
    
    # Add the current position to the path
    totalPaths.add((startingRow, startingCol))
    return [totalPaths, fences]

def checkRadius(grid, startingRow, startingCol, veggie):
    validDirections = set()
    for directionIndex in range(0, len(dir)):
        newDirection = dir[directionIndex]
        newRow = startingRow+newDirection[0]
        newCol = startingCol+newDirection[1]
        if(newRow < len(grid) and newRow >= 0 and newCol >= 0 and newCol <len(grid[0])):             
            #print((newRow, newCol), grid[newRow][newCol])
            if(grid[newRow][newCol] == veggie):
                    validDirections.add(directionIndex % len(dir))
    return validDirections

def getAdjacentCells(cell):
    row = cell[0]
    col = cell[1]
    cells = set()
    for direction in extendedDir:
        cells.add((row+direction[0], col+direction[1]))
    return cells

def vertexCount(edges): #DEBUG THIS
    vertices = 0
    #ideally i want to count number of vertices and then double count any exterior facing ones. working out how to do that still
    for tile in edges:
        nearbyCells = getAdjacentCells(tile)
        #print(nearbyCells)
        adjoiningEdges = nearbyCells.intersection(edges)
        rows = 0
        cols = 0
        for cell in adjoiningEdges:
            rows += abs(cell[0]-tile[0])
            cols += abs(cell[1]-tile[1])
        if(rows and cols):
            vertices +=1
    return vertices

def getNextEdge(cell, lastCell, edges):
    #edges.remove(lastCell)
    for direction in dir:
        newRow = cell[0] + direction[0]
        newCol = cell[1] + direction[1]
        newCell = (newRow, newCol)
        print(cell, newCell)
        if(newCell != lastCell and newCell in edges):
            print("RETURNING", newCell)
            return newCell


currentPos = [0,0]
#pos3 is the "next direction"
down = [1,0,"down", 0]
up = [-1,0, "up", 2]
left = [0, -1, "left", 1]
right = [0, 1, "right", 3]
upRight =       [-1, 1]
upLeft =        [-1, -1]
downLeft =      [1, -1]
downRight =     [1, 1]
dir = [up, right, down, left]
extendedDir = [up, right, down, left, upRight, upLeft, downRight, downLeft]
currentDir = 0
grid = []
plots = {}
for row, line in enumerate(f):
     grid.append(list(line.strip()))

perimeterCount = 0
plotCount = 0
for row, line in enumerate(grid):
     for col, spot in enumerate(line):
        cellVisited = False
        
        plotIndex = 0
        if grid[row][col] not in plots:
            plots[grid[row][col]] = []

        else:
            for group in plots[grid[row][col]]:
                if((row, col) in group):
                    cellVisited = True
                    break
                plotIndex +=1
                
    
        if(not cellVisited):#if we have been to the cell before, then we don't need to explore it again, we already know what touches it. 
            #plots[grid[row][col]].append(set())
            currentPlot = explorePath(grid, row, col, 0)
            plots[grid[row][col]].append(currentPlot[0])#finds the entire plot 
            perimeterCount += currentPlot[1]
            #print(grid[row][col], currentPlot[1], len(currentPlot[0]))
            answer1 += currentPlot[1] * len(currentPlot[0])

print(plots)

for key, in plots:
    for plot in plots[key]:
        edges = set()
        for cell in plot:
            edges.update(getAdjacentCells(cell))
        edges.difference_update(plot)
        startingCell =  next(iter(edges))
        cell = startingCell
        lastCell = (-10, -10)#something that can't be on the grid
        nextCell = lastCell
        while(nextCell != startingCell):
            nextCell = getNextEdge(cell, lastCell, edges)
            lastCell = cell
            cell = nextCell
            print(nextCell, lastCell, cell)
            
        if(key =='D'):
            sides = vertexCount(edges)
            print(plot, sides)
            answer2 += sides
        
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)