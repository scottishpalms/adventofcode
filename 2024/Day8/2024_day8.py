### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day8"
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
antennas = {}
antinodes = set()
antinodes2 = set()
grid = []

#get the grid pulled in
lineNumber = 0
for lineNumber, line in enumerate(f):
    grid.append(list(line.strip()))
    for cell, pos in enumerate(line.strip()):
        if(pos != '.'):
            if(pos not in antennas):
                antennas[pos] = []
            antennas[pos].append([lineNumber, cell])
width = len(line.strip())
height = lineNumber+1

for antenna, locations in antennas.items():#antenna by antenna
    for i in range(0, len(locations)):
        for j in range (0, len(locations)): #need to iterate through the entire list for each value
            if(i==j):
                continue #avoid comparing the same antenna against itself
            rowDiff = locations[i][0] - locations[j][0]
            colDiff = locations[i][1] - locations[j][1]
            newRow = locations[i][0] + rowDiff
            newCol = locations[i][1] + colDiff
            
            #part1:
            if(newCol < 0 or newRow < 0 or newCol >= width or newRow >= height):
                pass
            else: 
                antinodes.add((newRow, newCol))
                antinodes2.add((newRow, newCol))
            
            #part2:
            while(not(newCol < 0 or newRow < 0 or newCol >= width or newRow >= height)):
                antinodes2.add((newRow, newCol))
                grid[newRow][newCol] = '#' #mark the antinodes in the grid (for debugging purposes)
                newRow+=rowDiff
                newCol += colDiff
        if(len(locations)>1):
            antinodes2.add(tuple(locations[i]))#all antennas are now also antinodes, as long as there are at least two of them

for line in grid:
    print("".join(line))
answer1 = len(antinodes)
answer2 = len(antinodes2)

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)