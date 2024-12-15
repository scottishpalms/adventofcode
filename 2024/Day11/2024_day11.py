### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day11"
answer1, answer2 = 0, 0
from functools import cache
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
stones = list(map(int, f[0].split()))


@cache
def recursiveStoneCount(stone, iterations, maxIterations):
    # Base case: If we reach the max iterations, return 1 (this stone counts as one)
    if iterations >= maxIterations:
        return 1

    if len(str(stone)) % 2 == 0:  # Stone has an even number of digits
        stoneString = str(stone)
        stoneMiddle = len(stoneString) // 2
        # Split the stone into two parts
        stone1 = int(stoneString[:stoneMiddle])
        stone2 = int(stoneString[stoneMiddle:])
        # Recurse on the two parts
        return (
            recursiveStoneCount(stone1, iterations + 1, maxIterations) +
            recursiveStoneCount(stone2, iterations + 1, maxIterations)
        )
    else:  # Stone has an odd number of digits
        # Handle 0 stones
        if stone == 0:
            stone = 1
        else:
            stone *= 2024
        # Recurse on the modified stone
        return recursiveStoneCount(stone, iterations + 1, maxIterations)
    
#does the same thing as above function, but without needing to import cache
def recursiveStoneCount2(stone, iterations, maxIterations, memo):
    if iterations >= maxIterations:
        return 1  # Base case: count this stone

    # Memoization key
    memo_key = (stone, iterations)
    if memo_key in memo:
        return memo[memo_key]

    if len(str(stone)) % 2 == 0:  # Stone has an even number of digits
        stoneString = str(stone)
        stoneMiddle = len(stoneString) // 2
        stone1 = int(stoneString[:stoneMiddle])
        stone2 = int(stoneString[stoneMiddle:])
        result = recursiveStoneCount2(stone1, iterations + 1, maxIterations, memo)
        result += recursiveStoneCount2(stone2, iterations + 1, maxIterations, memo)
    else:
        if stone == 0:
            stone = 1
        else:
            stone *= 2024
        result = recursiveStoneCount2(stone, iterations + 1, maxIterations, memo)

    # Store in memo
    memo[memo_key] = result
    return result




ITERATIONS1 = 25
ITERATIONS2 = 75
#part 1
zeros = 0
for singleStone in stones:
     stoneList = [singleStone]
     for i in range(0, ITERATIONS1):
          #print(i, len(stoneList), stoneList)
          j = 0
          #print()
          while  j < len(stoneList):
               if(not stoneList[j]):
                    stoneList[j] = 1
               elif ((len(str(stoneList[j])) % 2) == 0): #stone has even number of digits
                    
                    stone = str(stoneList[j])
                    stoneMiddle = len(stone)//2
                    stoneList[j] = int(stone[stoneMiddle:])
                    stoneList.insert(j, int(stone[:stoneMiddle]))
                    j += 1
                    #print(stone, int(stone[:stoneMiddle]),int(stone[stoneMiddle:] ))
                    #print(stones)
               else:
                    stoneList[j] *= 2024
               j+=1
     answer1+= len(stoneList)
     zeros += stoneList.count(0)
print(stones)
memo = {}
for stone in stones:
     answer2+= recursiveStoneCount(stone, 0, ITERATIONS2)
     #answer2+= recursiveStoneCount2(stone, 0, ITERATIONS2, memo)
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)