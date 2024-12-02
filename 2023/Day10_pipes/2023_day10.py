answer1, answer2 = 0,0
maze = []
f = open("1input.txt", "r")
for j, line in enumerate(f):#read the input file
    
    maze.append([int(x) for x in line.strip().split(" ")])
    print(maze)

    
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)


