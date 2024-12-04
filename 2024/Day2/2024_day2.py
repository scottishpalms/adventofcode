### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day2"
answer1, answer2, i, j, multipliers = 0,0,0,0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()

#part1:
def isLineSafe(report):
    increasing, decreasing, unsafe = False, False, False
    for num, nextNum in zip(report, report[1:]):
        if(nextNum < num):
            decreasing = True
        elif(nextNum > num):
            increasing = True
        else: 
            unsafe = True
        if((nextNum == num) or abs(nextNum - num) > 3):
            unsafe = True
    if(not(increasing and decreasing or unsafe)):
        return True
    else: return False


for i, line in enumerate(f):
    report = list(map(int, line.split()))
    if(isLineSafe(report)):
       answer1+= 1
       answer2+=1
    else:
        for j, level in enumerate(report):
            dampenedReport = report[:j] + report[j+1:]#make a new list without one of the elements
            if(isLineSafe(dampenedReport)):#this is slower than figuring out what the bad entry is specifically, but it works
                answer2+=1
                break

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)

