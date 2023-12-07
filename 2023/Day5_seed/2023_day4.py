import math
import re
answer1, answer2, i, j, game = 0,0,1,0, 1
winningNumbers = []
myNumbers = []
queue = []
f = open("input.txt", "r")
for i, line in enumerate(f):#read the input file
    line = line.strip()
    line = line.split(":")[1].split("|")
    winningNumbers = list(filter(None,line[0].strip().split(" ")))
    myNumbers = list(filter(None, line[1].strip().split(" ")))
    #print(winningNumbers, "My numbers: ", myNumbers)
    winningNumbers = set(winningNumbers)#filter out any duplicates. don't know if this is needed or not
    matches = -1
    for myNumber in myNumbers:
        if(myNumber in winningNumbers):
            matches += 1    
    answer1+= math.floor(2**matches)#floor filters out 2^-1 = 0.5
    matches+=1 #get true number of matches
    multiplier=1
    if(queue):
        multiplier+=queue.pop(0)
    #print("Card:", i+1, "copies: ",multiplier)
    answer2+=multiplier
    for j in range(0, multiplier):
        for k in range(0, matches):
            if(k>=len(queue)):
                queue.append(1)
            else:
                queue[k]+=1
            #print("Card", i+1, "added 1 to card", k+i+2, queue)    



print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)


