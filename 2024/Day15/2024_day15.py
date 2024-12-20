### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day15"
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


print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)