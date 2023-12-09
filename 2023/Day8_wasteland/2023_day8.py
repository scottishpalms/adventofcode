import math
import re

def recursiveSolve1(data, count, instructions, start, part2):
 
    for i, step in enumerate(instructions):
        if(i == 0):
            key = data[start][step]
            #print(count, key, "first step")
        else: 
            key = data[key][step]
            #print(count, key, i)
        count+=1
        
        if(not part2):
            if key == 'ZZZ':
                return [count, key]
        elif re.findall('\w\wZ', key):
            #print("stopping here for now!")
            return [count, key]
        
            
        
        
    start = key#start from where we left off in the next level down 
    return recursiveSolve1(data, count, instructions, start, part2)




answer1, answer2, i, j, game = 0,0,1,0, 1
data = {}
instructions = []
answers2 = []
starts = []
f = open("input.txt", "r")
for i, line in enumerate(f):#read the input file
    if(i == 0):
        for step in line.strip():
            if(step == 'L'):
                instructions.append(0)
            else: instructions.append(1)
        #print(instructions)
    elif(i != 1):
        line = line.strip()
        line = line.split("=")
        key = line[0].strip()
        matches = re.findall('\w\wA', key)#part2: check if this step ends in an A
        if(matches):
            starts.append(key)
            answers2.append(0)
        matches = re.findall('\w\w\w', line[1])
        value = [0,0]
        value[0] = matches[0]
        value[1] = matches[1]
        #print(key, value)
        data[key] = value

    
count = 0
#print("Part 1 Answer: ", recursiveSolve1(data, count, instructions, "AAA", False))
print(starts)
highAnswer = 1
firstTime = True
round = 0
multiplied = 1
for i, path in enumerate(answers2):
    retVal = recursiveSolve1(data, answers2[i], instructions, starts[i], True)
    answers2[i] = retVal[0]
    print(answers2[i], i)
    #starts[i] = retVal[1]
    multiplied *= answers2[i]

answer2 = math.lcm(*answers2)

print("Part 2 Answer: ", answer2)


