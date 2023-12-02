import os
import re
#given lines of text, combine the first and last digit in each line together then add to a running sum. 
#part 1 only looks at digits, part 2 considers written numbers to be digits too
current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, ("input.txt"))

answer1, answer2, i, j = 0,0,1,0
numberList = ['0','1','2','3','4','5','6','7','8','9']
textNumList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

f = open(input_file_path, "r")
for line in f:#read the file
    line=line.strip()        
    #part 1
    partialAnswer1 = re.compile(r'\d').search(line).group()#grab the first digit in the line
    match2 = re.compile(r'([^\d]*$)').search(line)#match everything after the last digit
    if(match2):
        partialAnswer2 = line[match2.start()-1]
    else:#this happens when a digit is the last character in a line
        partialAnswer2 = line[-1]
    answer1 += int(partialAnswer1 + partialAnswer2)
    
    #part2
    partialAnswer1, backMatchIndex, partialAnswer2 = -1,-1,-1
    forwardMatchIndex = len(line)+1
    for index in range(10):
        matchNum = re.compile(numberList[index]).finditer(line)#get all matches
        for match in matchNum: 
            if(match.start()<forwardMatchIndex):#new front match?
                forwardMatchIndex = match.start()
                partialAnswer1 = numberList[index]
            if(match.start()>backMatchIndex):#new back match?
                backMatchIndex = match.start()
                partialAnswer2 = numberList[index]
        
        matchText = re.compile(textNumList[index]).finditer(line)#now look for the written out numbers
        for match in matchText:
             if(match.start()<forwardMatchIndex):#new front match?
                forwardMatchIndex = match.start()
                partialAnswer1 = numberList[index]
             if(match.start()>backMatchIndex):#new back match?
                backMatchIndex = match.start()
                partialAnswer2 = numberList[index]
    print(partialAnswer1, partialAnswer2, "Line #", i)    
    answer2 += int(partialAnswer1 + partialAnswer2)
    i+=1

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)