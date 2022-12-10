def checkCycle(cycle, regVal, crt):
    crtCol = cycle%40
    #print("During Cycle,",cycle, "regVal is", regVal,"So the signal strength is ", regVal*cycle)
    if regVal in range(crtCol-2, crtCol+1):
        crt[cycle-1] = '#'
        #print("Found")
    if((cycle+20)%40) == 0:
        
        return regVal*cycle
    else: return 0

answer1, answer2, i, j = 0,0,0,0
instructions = []
outputString = ''
w,h =40, 6
numPixels = w*h
crt = ["."]*numPixels

lastCharWasNumber = False
noop = 'noop'
addx = 'addx'

cycle = 0
regVal = 1

f = open("input10.txt", "r")
for line in f:#read the file
    row = [0,0]
    numString = ''
    line=line.strip()
    if(line[0].isalpha()):
        if(line[0] =='a'):           
            row[0] = 'addx'
        else: row[0] = 'noop'
    for char in line:
        if char.isnumeric() or char =='-':
            numString+=(char)
    if(row[0] == addx):
        row[1] = int(numString)
    
    instructions.append(row)

for instruction in instructions:
    op = instruction[0]
    adder = instruction[1]
    
    if op == noop:
        cycle+=1
        answer1+= checkCycle(cycle, regVal, crt)
        
    elif op == addx:
        cycle+=1
        answer1+= checkCycle(cycle, regVal, crt)
        cycle+=1
        answer1+= checkCycle(cycle, regVal, crt)
        regVal += adder

print("Part 1 Answer: ", answer1)
#print("Part 2 Answer: ", answer2)
for i in range(0,h):#pretty print answer2
    crtRow = crt[i*w:(i+1)*w]
    outputString2 = ''
    for char in crtRow:
        outputString2 += char
    print(outputString2)




