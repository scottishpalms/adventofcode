### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day11"
answer1, answer2 = 0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
stones = list(map(int, f[0].split()))
    

def recursiveStoneCount(stone, iterations, maxIterations, memo):
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
        result = recursiveStoneCount(stone1, iterations + 1, maxIterations, memo)
        result += recursiveStoneCount(stone2, iterations + 1, maxIterations, memo)
    else:
        if (stone == 0):
            stone = 1
        else:
            stone *= 2024
        result = recursiveStoneCount(stone, iterations + 1, maxIterations, memo)

    # Store in memo
    memo[memo_key] = result
    return result


ITERATIONS1 = 25
ITERATIONS2 = 75
#part 1, could replace this with recursiveStoneCount, but I'm keeping it here for posterity
for singleStone in stones:
     stoneList = [singleStone]
     for i in range(0, ITERATIONS1):
          j = 0
          while  j < len(stoneList):
               if(not stoneList[j]):
                    stoneList[j] = 1
               elif ((len(str(stoneList[j])) % 2) == 0): #stone has even number of digits
                    
                    stone = str(stoneList[j])
                    stoneMiddle = len(stone)//2
                    stoneList[j] = int(stone[stoneMiddle:])
                    stoneList.insert(j, int(stone[:stoneMiddle]))
                    j += 1
               else:
                    stoneList[j] *= 2024
               j+=1
     answer1+= len(stoneList)
memo = {}
for stone in stones:
     answer2+= recursiveStoneCount(stone, 0, ITERATIONS2, memo)
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)