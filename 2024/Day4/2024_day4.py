### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day4"
import re
answer1, answer2, i, j, k = 0,0,0,0,0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

#part1: find all cases of "XMAS", horizontal, vertical, and diagonal (forwards and backwards)
firstTime = True
horizontal, vertical, diagL, diagR = [], [], [''], ['']
horizontalString = ""
width = 0
startingIndex = 0
#extract horizontal, vertical both diagonal strings:
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
#now put all the strings together and find all the matches
combinedList = [horizontal, vertical, diagL, diagR]
pattern = r'(?=(XMAS|SAMX))'
for direction in combinedList:
    answer1 +=  sum([len(re.findall(pattern, xmas)) for xmas in direction])

#part2
#you can't take my regex from me
msPattern = r'M.S'
smPattern = r'S.M'
mmPattern = r'S.S'
ssPattern = r'M.M'
aPattern  = r'.A.'
patterns = [
    (ssPattern, aPattern, mmPattern),  # Match SS_MM
    (mmPattern, aPattern, ssPattern),  # Match MM_SS
    (msPattern, aPattern, msPattern),  # Match MS_MS
    (smPattern, aPattern, smPattern),  # Match SM_SM
]

for i in range(width-2):
    for j in range(width-2): #input is a "square"
        for pattern1, pattern2, pattern3 in patterns:
            if (re.match(pattern1, horizontal[i][j:j+3]) and
                re.match(pattern2, horizontal[i+1][j:j+3]) and
                re.match(pattern3, horizontal[i+2][j:j+3])):
                answer2 += 1

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)