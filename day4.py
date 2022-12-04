f = open("input.txt", "r")
answer1 = 0
answer2 = 0
for line in f:
    line = line.strip()
    length = len(line)
    length = (int)((length-1)/2)
    elves = line.split(",")
    elves = [(i.split("-")) for i in elves]
    elf1 = [int(i) for i in elves[0]]
    elf2 = [int(i) for i in elves[1]]

    if (elf1[0]>=elf2[0] and elf1[1]<=elf2[1]) or (elf2[0]>=elf1[0] and elf2[1]<=elf1[1]):
        answer1+=1        
    if (elf1[0]>=elf2[0] and elf1[0]<=elf2[1]) or (elf2[0]>=elf1[0] and elf2[0]<=elf1[1]):
        answer2+=1    
print("Part 1 answer: ", answer1)
print("Part 2 answer: ", answer2)
