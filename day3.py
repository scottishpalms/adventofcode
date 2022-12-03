ASCII_UPPER_OFFSET = 38
ASCII_LOWER_OFFSET = 96
f = open("input.txt", "r")
answer = 0
for line in f:
    length = len(line)
    length = (int)((length-1)/2)
    ruck2 = line[length:]
    ruck1 = line[:length]
    for letter in ruck1:
        for comp in ruck2:
            if letter == comp:
                match = letter
    if match.isupper():
        answer += ord(match) - ASCII_UPPER_OFFSET
    else: answer += ord(match) - ASCII_LOWER_OFFSET
print("Part 1 Answer: ",answer)
i=0
elf1 = "x"
elf2 = "x"
elf3 = "x"
answer = 0
f.seek(0)
for line2 in f:
    line2 = line2.strip()
    if i%3 == 0:
        elf1 = line2
    elif (i%3 == 1):
        elf2 = line2       
    else:
        elf3 = line2
        #print(elf1, elf2, elf3)
        for letter1 in elf1:
            for letter2 in elf2:
                for letter3 in elf3:
                    if(letter1 == letter2 and letter2 == letter3):
                        match = letter1 
        if match.isupper():
            answer += ord(match) - ASCII_UPPER_OFFSET
        else: answer += ord(match) - ASCII_LOWER_OFFSET
    i+=1
print("Part 2 Answer: ", answer)