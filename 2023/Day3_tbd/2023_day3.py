import os
import re
answer1, answer2, i, j, game = 0,0,1,0, 1

f = open("input.txt", "r")
for line in f:#read the file
   line = line.strip()
    game+=1

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)