### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day2"
import bisect 
answer1, answer2, i, j, multipliers = 0,0,0,0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

#part1:
list1 = []
list2 = []
for i, line in enumerate(f):
    leftNum = int((line.split()[0]))
    rightNum= int((line.split()[1]))
    bisect.insort(list1, leftNum)
    bisect.insort(list2, rightNum)
    
for i, item in enumerate(list1):
    answer1 += (abs(list1[i] - list2[i]))
    occurances = list2.count(item)
    answer2 += item * occurances
#part 2:
      

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)

