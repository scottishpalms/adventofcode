### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day17"
answer1, answer2 = "", ""
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
    GRID_WIDTH = 11
    GRID_HEIGHT = 7
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
     GRID_WIDTH = 101
     GRID_HEIGHT = 103
import re
# bruteforce bookmark 1843300000
regAPattern = r'Register A: (\d+)'
regBPattern = r'Register B: (\d+)'
regCPattern = r'Register C: (\d+)'
numPattern = r'\d+'
program = []

regA, regB, regC = 0,0,0

for i, line in enumerate(f):
    nums = re.findall(numPattern, line)
    print(nums)
    if(i == 0):
        regA = int(nums[0])
    if(i == 1):
        regB = int(nums[0])
    if(i == 2):
        regC = int(nums[0])
    if(i ==4):
        program  = list(map(int, nums))
def runProgram(part1, regAVal, progLen, targetOutput):
    HALT_LEVEL = 100
    regA = regAVal
    regB = 0
    regC = 0
  
    
    j = 0
    answer1 = ""
    answer2 = []
    programOutput = []
    haltCount = 0
    outIndex = 0
    while(j<len(program) and haltCount < HALT_LEVEL):
        opcode = program[j]
        literalOperand = program[j+1]
        comboOperand = literalOperand
        
        if(comboOperand == 4):
            comboOperand = regA
        elif(comboOperand == 5):
            comboOperand = regB
        elif(comboOperand == 6):
            comboOperand = regC
        #print("code:",opcode,"Litoperand", literalOperand, "combo", comboOperand, "A",regA, "B",regB, "C",regC)
        if(opcode == 0):#adv
            regA = regA//pow(2,comboOperand)
        elif(opcode == 1):#bxl
            regB = literalOperand ^ regB
        elif(opcode == 2):#bst
            regB = comboOperand % 8
        elif(opcode == 3):#jnz
            if(regA):
                j = literalOperand
                #print("jumping to", j)
                j-=2 # to counter the += 2 later on. we don't want to increment the instruction pointer when jumping
        elif(opcode == 4):#bxc
            regB = regB ^ regC
        elif(opcode == 5):#out
            if(part1):
                answer1 += str((comboOperand % 8))+","
            else:
                outVal =  comboOperand % 8
                
                if(outVal == targetOutput[outIndex]):
                # if(program[outIndex] == outVal):
                     outIndex += 1
                     if(outIndex == len(targetOutput)):
                         return 1
                else:
                    return 0
            haltCount = 0
        elif(opcode == 6):#bdv
            regB = regA//pow(2,comboOperand)
        elif(opcode == 7):#cdv
            regC = regA//pow(2,comboOperand)
        haltCount += 1
        j+=2
    if(part1):
        return answer1
    if(outIndex < progLen):
        return 0
    return 1


progLen = len(program)
answer1 = runProgram(True, regA, progLen, list())
print("final:", regA, regB, regC)
print(answer1)
answer1 = answer1[:-1]
regA = 0

outputCount = -1
targetOutput = [program[outputCount]]
while((outputCount *-1)<progLen):
    regA +=1
    if(runProgram(False, regA, progLen, targetOutput)):
        outputCount -=1
        if(outputCount *-1 <= progLen):
            regA = regA<<3
            targetOutput.insert(0, program[outputCount])
            print("Found digit!", targetOutput[0], outputCount, regA)
        else:
            break
    else: regA+=1
    if( not regA % 100000):
        print("Trying:", regA)
    answer2 = regA

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)