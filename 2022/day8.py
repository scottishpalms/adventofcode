def viewDistance(grove, tree):
    viewDistance = 0
    for shrub in grove: 
        if (shrub<tree):
            viewDistance+=1
        else: 
            viewDistance +=1
            break
    return viewDistance

answer1, answer2, i, j = 0,0,0,0
forest1 = []
forest2 = list()
transposedForest = []
intForest = []
flatTF = []

f = open("input8.txt", "r")
for line in f:#read the file
    line=line.strip()
    forest1.append(list(line))#get it into a list of lines
    forest2+=line.strip()#get it as a long string
rowLen = len(line)
forest2 = list(forest2)#convert to list of characters
    
for tree in forest2:
    intForest.append(int(tree))
    
forest2 = intForest    
for column in zip(*forest1):
    transposedForest.append(list(column))
tranposedForest = [j for sub in transposedForest for j in sub]

while(i<rowLen):
    while(j<rowLen):
        flatTF.append(int(transposedForest[i][j]))
        j+=1
    j = 0
    i += 1
    
i,j=0,0  
while(i<rowLen):
    while(j<rowLen):
        if(i==0 or j==0 or i==rowLen-1 or j==rowLen-1):
            answer1+=1
            j+=1
            continue
        if(forest2[i*rowLen+j]!=flatTF[j*rowLen+i]):#kill the program if something went wrong with input
            raise Exception("Transpose Error")
        
        tree = (forest2[i*rowLen+j])
        treeScore = 1
        
        #get a list of trees looking outward in each direction
        left = forest2[i*rowLen:i*rowLen+j]
        right = forest2[(i*rowLen+j+1):((i+1)*rowLen)]
        down = flatTF[(j*rowLen+i+1):((j+1)*rowLen)]
        up = flatTF[j*rowLen:j*rowLen+(i)]        
        
        #solve part 1. check if tree can see all the way to the edge
        if  all(shrubs < tree for shrubs in left) or\
            all(shrubs < tree for shrubs in right) or\
            all(shrubs < tree for shrubs in down) or\
            all(shrubs < tree for shrubs in up):
            answer1+=1
        #solve part 2. looking directly outward, how far can the tree see out
        treeScore *= viewDistance(reversed(left),tree)
        treeScore *= viewDistance(right,tree)
        treeScore *= viewDistance(down,tree)
        treeScore *= viewDistance(reversed(up),tree)
       
        if(answer2<treeScore):
            answer2 = treeScore
        
        j+=1
    j = 0
    i += 1

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)