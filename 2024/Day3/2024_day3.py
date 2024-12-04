### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day3"
import re
answer1, answer2, i, j = 0,0,0,0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

#part1:
enabled = True
for line in f:
     pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
     allMatches = re.finditer(pattern, line)
     for match in allMatches:
        if(match.group(0) == "don't()"):
            enabled = False
        elif (match.group(0) == "do()"):
            enabled = True
        else:
            answer1+= int(match.group(1)) * int(match.group(2))
            if(enabled):
                answer2+= int(match.group(1)) * int(match.group(2))
          
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)

