answer1, answer2, i, j, multipliers = 1,1,0,0, 0

f = open("1input.txt", "r").readlines()
times = [int(x) for x in list(filter(None, f[0].strip().split(":")[1].split(" ")))]
record = [int(x) for x in list(filter(None, f[1].strip().split(":")[1].split(" ")))]
#part1:
for i, time in enumerate(times):
    wins = 0
    for buttonTime in range(0, time):
        distance = buttonTime * (time - buttonTime)
        if distance > record[i]:
            wins += 1
    answer1 *= wins
    
#part 2:
wins = 0
combinedTime = list(filter(None, f[0].strip().split(":")[1].split(" "))) #we want it in strings now so it can get added together
combinedRecord = list(filter(None, f[1].strip().split(":")[1].split(" ")))

time = int(''.join(x for x in combinedTime))
record = int(''.join(y for y in combinedRecord))
for buttonTime in range(0, time):
    distance = buttonTime * (time - buttonTime)
    if distance > record:
        wins += 1
    answer2 = wins

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)


