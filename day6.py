answer1, answer2 = 0,0
f = open("input.txt", "r")
buf1Len = 4
buf2Len = 14
buffer1 = ['']*buf1Len
buffer2 = ['']*buf2Len
i,j,k=0,0,0
buffer1Found = False
buffer2Found = False 
for line in f:
    for char in line:
        buffer1[j] = char
        buffer2[k] = char
        print(buffer1)
        if (len(set(buffer1))>buf1Len-1 and i > buf1Len-1 and not buffer1Found):
            buffer1Found = True
            answer1 = i+1
        if (len(set(buffer2))>buf2Len-1 and i > buf2Len-1 and not buffer2Found):
            buffer2Found = True
            answer2 = i+1         
        i+=1
        j+=1
        k+=1
        if(j>buf1Len-1): 
            j = 0
        if(k>buf2Len-1):
            k=0
print("Part 1 answer: ", answer1)
print("Part 2 answer: ", answer2)
