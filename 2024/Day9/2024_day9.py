### General setup: ###
USE_TEST_INPUT = 1
DAY_NAME = "Day9"
answer1, answer2 = 0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

filesys = f[0].strip()
disk = ""
diskList = []
diskList2 = []
id = 0

def getMemoryChunk(diskList2, blankSize, blankLoc):
    for m, chunk in enumerate(reversed(diskList2)):
        #print("chunk:",chunk, i, blankSize)
        if(chunk[1]<=blankSize and chunk[0]!= "."):
            #print("fit found!")
            return -1*(m+1)
        if(m>(len(diskList2)-blankLoc)):
            break
    #print("can't find a fit!")
    return 1


for i, num in enumerate(str(filesys)):
    if(i%2==0):
        for j in range(0, int(num)):
            diskList.append(id)
        diskList2.append([id, int(num)])
        id += 1
    else:
        for j in range(0, int(num)):
            diskList.append(".")
        if(diskList2[-1][0] =="."):
            diskList2[-1][1] += int(num)#stitch together adjoining blank spaces. not sure this is needed
        else: diskList2.append([".", int(num)])
print("original: ", disk)
print(diskList)
print(diskList2)
#diskList2 = diskList.copy()
#part1:
for i in range(0, len(diskList)):
    if(i<len(diskList)):
        if(diskList[i] == "."):
            lastBit = diskList.pop()
            diskList[i] = lastBit
            while(lastBit == "."):
                lastBit = diskList.pop()
                diskList[i] = lastBit
print(diskList)

#part2:
for i in range(0, len(diskList2)-7):
    for j in range(0, len(diskList2)):
        if(diskList2[i][0] == "."):
            blockIndex = getMemoryChunk(diskList2, diskList2[i][1], i)
            # print("index", blockIndex, diskList2[blockIndex])
            if(blockIndex != 1):
                if(diskList2[i][1] == diskList2[blockIndex][1]): #perfectly fits the block, so just swap the positions
                    diskList2[i], diskList2[blockIndex] = diskList2[blockIndex], diskList2[i]
                    # print("swapping", diskList2[i], diskList2[blockIndex], "at", i)                    
                    
                else:
                    diskList2[i][1] -=diskList2[blockIndex][1]
                    # if(diskList2[i+1][0] =="."):#is there blank space right next to this?
                    #     diskList2[i][1]+=diskList2[i+1][1]
                    #     diskList2.pop(i+1)
                    diskList2.insert(i, diskList2.pop(blockIndex))
                    diskList2.insert(blockIndex, [".", diskList2[i][1]])
                    # print("inserting", diskList2[i], diskList2[blockIndex], "at", i)
                #combine adjecent blank sections
                if(diskList2[blockIndex+1] =="."):
                        diskList2[blockIndex][1]+=diskList2[blockIndex+1][1]
                        diskList2.pop(blockIndex+1)
                if(diskList2[blockIndex-1] =="."):
                    diskList2[blockIndex-1][1]+=diskList2[blockIndex-1][1]
                    diskList2.pop(blockIndex)
            # print(diskList2)

prettydisk2=""
# for item in diskList2:
#     for times in range(0, item[1]):
#         prettydisk2+=str(item[0])

for i, num in enumerate(diskList):
    answer1 += i*num
j = 0
print(diskList2)
print(prettydisk2)
k=0
for i, num in enumerate(diskList2):
    for j in range(0, num[1]):
        if(num[0]!= "."):
            answer2+= (k)*num[0]
            # print((i+j), num[0])
        k+=1
            



print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)