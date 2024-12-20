### General setup: ###
USE_TEST_INPUT = 0
DAY_NAME = "Day19"
answer1, answer2 = 0, 0
if(USE_TEST_INPUT):
    f = open(DAY_NAME + "/test_input.txt", "r").readlines()
    GRID_WIDTH = 11
    GRID_HEIGHT = 7
else:
     f = open(DAY_NAME + "/input.txt", "r").readlines()
     GRID_WIDTH = 101
     GRID_HEIGHT = 103
import re
# bruteforce bookmark 1843300000
pattern = r'[a-z]+'
towels = []
p1answerset = []

for i, line in enumerate(f):
    if(not i):
        towels = re.findall(pattern, line)
        print(towels)
    elif(i>1):
        banner = line.strip()
        indexSet = set(range(0, len(banner)))

        #part1
        for towel in towels:
            pattern = re.compile(towel)
            for match in pattern.finditer(banner):
                for index in range(match.start(), match.end()):
                    indexSet.discard(index)
        if(not indexSet):
            answer1+=1 #you can make this banner from the available towels
            print(banner, "POSSIBLE", answer1)
            p1answerset.append(i)
        else:
            print(banner, "NOT POSSIBLE")

        #part2
        banner = line.strip()
        n = len(banner)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to construct an empty banner

        # Process each position in the banner
        for j in range(n):
            if dp[j] > 0:  # Only proceed if there's a valid way to reach index `j`
                for towel in towels:
                    if banner.startswith(towel, j):
                        k = j + len(towel)  # End of the towel match
                        dp[k] += dp[j]  # Add ways to reach `j` to `k`

        print(f"Banner: {banner}, Total Ways: {dp[n]}")
        answer2 += dp[n]  # Count total ways to construct the banner
            

print(p1answerset)

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)