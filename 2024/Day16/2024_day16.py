### General setup: ###
USE_TEST_INPUT = 1
DAY_NAME = "Day16"
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
   (row, col)=(y, x): 
    0123456 right x
   0
   1  
   2
   down y
"""
maze = []

from collections import deque
from heapq import heappop, heappush

def bfs_maze(maze):
    rows, cols = len(maze), len(maze[0])
    directions = {  # (dr, dc, symbol)
        'R': (0, 1, '>'), 
        'D': (1, 0, 'v'), 
        'L': (0, -1, '<'), 
        'U': (-1, 0, '^')
    }
    turn_cost = {  # Cost of turning based on the direction change
        ('R', 'R'): 1, ('R', 'D'): 1000, ('R', 'U'): 1000, ('R', 'L'): 2000,
        ('D', 'D'): 1, ('D', 'R'): 1000, ('D', 'L'): 1000, ('D', 'U'): 2000,
        ('L', 'L'): 1, ('L', 'U'): 1000, ('L', 'D'): 1000, ('L', 'R'): 2000,
        ('U', 'U'): 1, ('U', 'R'): 1000, ('U', 'L'): 1000, ('U', 'D'): 2000,
    }

    # Locate start (S) and end (E)
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    if not start or not end:
        print("Start or End position missing in the maze.")
        return None

    # Priority Queue: (cost, row, col, direction, parent)
    heap = []
    for d in directions:  # Try all initial directions
        heappush(heap, (0, start[0], start[1], d, None))  # Start cost is 0

    visited = {}  # To track the minimum cost for each (row, col, direction)
    parent = {}   # To reconstruct the path

    while heap:
        cost, r, c, direction, prev = heappop(heap)

        # Stop when we reach the exit
        if (r, c) == end:
            parent[(r, c)] = (prev, direction)
            break

        # Skip if we've already visited with a lower cost
        if (r, c, direction) in visited and visited[(r, c, direction)] <= cost:
            continue
        visited[(r, c, direction)] = cost
        parent[(r, c)] = (prev, direction)

        # Explore all directions
        for new_dir, (dr, dc, symbol) in directions.items():
            nr, nc = r + dr, c + dc  # New position
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                new_cost = cost + turn_cost[(direction, new_dir)]
                heappush(heap, (new_cost, nr, nc, new_dir, (r, c)))

    # If no path was found
    if end not in parent:
        print("No path to the exit was found.")
        return None

    # Reconstruct the path
    path_maze = [list(row) for row in maze]  # Copy maze to modify
    current = end
    total_steps = 0

    while current != start:
        if current not in parent:
            print("Error: Path reconstruction failed. Missing parent for:", current)
            return None
        prev, direction = parent[current]
        pr, pc = prev
        path_maze[pr][pc] = directions[direction][2]  # Use symbol for direction
        current = prev
        total_steps += 1


    # Replace start and end positions
    path_maze[start[0]][start[1]] = 'S'
    path_maze[end[0]][end[1]] = 'E'

    # Print the maze with the path
    print("\nMaze with the optimized path:")
    for row in path_maze:
        print("".join(row))

    return total_steps

for row, line in enumerate(f):
    maze.append(list(line.strip()))
for row in maze:
    blankStr = ""
    print(blankStr.join(row))


print(bfs_maze(maze))


     

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)