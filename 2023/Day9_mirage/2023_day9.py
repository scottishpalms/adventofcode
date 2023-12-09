import math
import re

answer1, answer2, i, j, game = 0,0,0,0,0


f = open("input.txt", "r")
for i, line in enumerate(f):#read the input file
    data = [[0]]
    data[0] = [int(x) for x in line.strip().split(" ")]
    print(data[0])
    i=-1
    while(len(set(data[i])) != 1 or i == -1):#drill down
        
        i+=1
        
        data.append([])
        for j, num in enumerate(data[i]):
            if (j >= (len(data[i])-1)):
                break
            data[i+1].append(data[i][j+1]-data[i][j])
        #print(data[i+1])
        #print(set(data[i]), len(set(data[i])))
    print("\n\n")
    data.reverse()
    for i in range (1, len(data)):
         data[i].append(data[i-1][-1]+data[i][-1])
         data[i].insert(0, data[i][0]-data[i-1][0])
    print(data)
    answer1+=data[-1][-1]
    answer2+=data[-1][0]
    
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)


