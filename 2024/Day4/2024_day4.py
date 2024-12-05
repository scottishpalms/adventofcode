### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day4"
import re
answer1, answer2, i, j, k = 0,0,0,0,0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

#part1
pattern = r'(?=(XMAS|SAMX))'
firstTime = True
horizontal, vertical, diagL, diagR = [], [], [''], ['']
horizontalString = ""
width = 0
startingIndex = 0

for lineNumber, line in enumerate(f):
    horizontal.append(line.strip())#the easy one
    width = len(line.strip())
    #horizontalString += " " + line.strip()
    if(not firstTime):
        startingIndex+=1#do this first so we skip over the first row
        diagR.append('')
        diagL.append('')
    j = 0
    k = 0
    for i, letter in enumerate(line.strip()):
        if(firstTime):
            vertical.append('')
            diagR.append('')
            diagL.append('')
            diagR[startingIndex] += letter
            diagL[startingIndex] += letter
            startingIndex += 1 #keeping this seperate from i so that we know where we left off
        else:
            if((startingIndex - i) > width):
                diagL[startingIndex - i] += letter
            else: 
                diagL[j] += letter
                j+= 1            
            diagR[lineNumber + i] += letter
        vertical[i] += letter    
    firstTime = False
combinedList = [horizontal, vertical, diagL, diagR]
for direction in combinedList:
    answer1 +=  sum([len(re.findall(pattern, xmas)) for xmas in direction])


print (horizontal)
print (vertical)
print(diagL)
print(diagR)
          
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)

