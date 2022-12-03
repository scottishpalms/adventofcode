ASCII_UPPER_OFFSET = 38
ASCII_LOWER_OFFSET = 96
f = open("input.txt", "r")
answer1 = 0
answer2 = 0
i=0
for line in f:
    length = len(line)
    length = (int)((length-1)/2)
    ruck2 = line[length:]
    ruck1 = line[:length]
    for letter in ruck1:
        for comp in ruck2:
            if letter == comp:
                match1 = letter
    if match1.isupper():
        answer1 += ord(match1) - ASCII_UPPER_OFFSET
    else: answer1 += ord(match1) - ASCII_LOWER_OFFSET
    #start part 2:
    line = line.strip()
    if i%3 == 0:
        elf1 = line
    elif (i%3 == 1):
        elf2 = line       
    else:
        elf3 = line
        for letter1 in elf1:
            for letter2 in elf2:
                for letter3 in elf3:
                    if(letter1 == letter2 and letter2 == letter3):
                        match2 = letter1 
        if match2.isupper():
            answer2 += ord(match2) - ASCII_UPPER_OFFSET
        else: answer2 += ord(match2) - ASCII_LOWER_OFFSET
    i+=1
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)
