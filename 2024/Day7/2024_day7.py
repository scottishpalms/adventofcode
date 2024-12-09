### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day7"
answer1, answer2, i, j, k = 0,0,0,0,0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

for lineNumber, line in enumerate(f):
    value = int(line.split()[0][:-1])
    stringEq =  line.split()[1:]
    equation = list(map(int,stringEq))
    testCases = pow(2,len(equation)-1)
    
    for i in range(0, testCases):
        total = equation[0]
        for j in range(1, len(equation)):
            if ((i >> (j-1)) & 1):  #alternate */+ based on the binary representation
                total += equation[j]
            else:
                total *= equation[j]   
            if(total > value):
                break#just to speed things up a bit 
                    
        if(total == value):
            answer1 += value
            break #found a good one, don't need to keep trying
#part 2:
    testCases = pow(3,len(equation)-1)#this is basically base 3 now instead of base2
    print("Line:", lineNumber, "Value:",value, "tc:", testCases, equation)#, end="")

    for i in range(0, testCases):
        total = equation[0]
        for j in range(1, len(equation)):
            operation = (i // (3**(j-1))) % 3  #base 3ish way of doing what was done in binary for part 1
            if (operation == 0):  
                total += equation[j]
            elif (operation == 1):
                total = int(str(total)+str(equation[j]))                
            else:
                total *= equation[j]
            if(total > value):
                break#just to speed things up a bit      
        
        if(total == value):
            answer2 += value
            break #found a good one, don't need to keep trying


print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)