### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day1"
answer1, answer2, lazy = 0, 0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
""" grid directions:
   (row, col)
    0123456 right
   0
   1  
   2
   down
"""
pos = 50 #starting location is 50 per instructions
DIAL_SIZE = 100

def lazyMethod(dir, turns, pos):
    lazyAns = 0
    for step in range(turns):
        if(dir =="R"):
            pos+= 1
        else:
            pos-=1
        pos %= DIAL_SIZE
        if(pos ==0 ):
            lazyAns+=1
    return lazyAns


lineNumber = 0
for lineNumber, line in enumerate(f):
    line.strip()
    dir = line[0]
    turns = int(line[1:])
    #print(dir, turns)
    lazy += lazyMethod(dir, turns, pos)
    if(dir == "R"):
        pos += turns
        if(pos//DIAL_SIZE > 0):
            answer2+= pos//DIAL_SIZE 
    else:
        dist_to_zero = pos if pos > 0 else DIAL_SIZE     
        if turns >= dist_to_zero:
            answer2 += 1 + (turns - dist_to_zero) // DIAL_SIZE
        adjTurns =  turns % DIAL_SIZE
        pos += (DIAL_SIZE - adjTurns)


    pos %= DIAL_SIZE
    if(pos == 0):
        answer1 +=1
        



print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)
print("Lazy part 2 answer", lazy)#works, keeping this in for posterity