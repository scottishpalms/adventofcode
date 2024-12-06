### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day5"
import re
import random
answer1, answer2, i, j, k = 0,0,0,0,0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()


def isSorted(pageNum, rules): #return sort status and the indices of the rule breakers if not sorted
    for rule in rules:
        try:
            if(pageNum.index(rule[0]) > pageNum.index(rule[1])):
                return False, pageNum.index(rule[0]), pageNum.index(rule[1])
        except ValueError:
            pass
    return True, 0, 0


rules, pages = [], []
instructionPattern = r'(\d+)\|(\d+)' #taking any excuse to use regex 3 days in a row

for lineNumber, line in enumerate(f):
    instructions = re.match(instructionPattern, line.strip())
    if(instructions != None):#found a rule! add to the list
        rules.append((int(instructions.group(1)), int(instructions.group(2))))
    elif(line[0]!='\n'):#handle the blank lines
        pageNum = [int(num) for num in line.strip().split(',')]
            
        alreadySorted = True #for seperating the part 1 vs part 2 lines
        sortStatus = isSorted(pageNum, rules)
        while(not sortStatus[0]):
            alreadySorted = False
            pageNum.insert(sortStatus[1]+1, pageNum.pop(sortStatus[2]))#move the offending page just after the one it's supposed to go past
            sortStatus = isSorted(pageNum, rules) #check again!
        
        if(alreadySorted): #part1: page was already sorted so this one goes towards part1
            answer1 += pageNum[len(pageNum)//2]#get the value of the middle index
        else:
            answer2 += pageNum[len(pageNum)//2]


print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)