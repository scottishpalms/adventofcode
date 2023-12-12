import math

def getAnswer1(data, seeds):
    for j, round in enumerate(data):
        #print(round)
        for i, seed in enumerate(seeds):
            for line in round: 
                #print("start value =", seed)
                if(seed>=line[1] and seed<(line[1]+line[2])):
                    seeds[i] = line[0]+(seed-line[1])
                    #print ("mapped value:",seeds[i], " destination range")
    return min(seeds)


def getAnswer(data, seed):
    for j, round in enumerate(data):
        #print(round)
            for line in round: 
                #print("start value =", seed)
                if(seed>=line[1] and seed<(line[1]+line[2])):
                    seed = line[0]+(seed-line[1])
                    #print ("mapped value:",seeds[i], " destination range")
    return seed
def computeStep(start, length, data, location):
    startAnswer = getAnswer(data, start)
    if length == 0:
        return startAnswer
    endAnswer = getAnswer(data, (start+length))
    #print(length)
    answer2 = min(startAnswer, endAnswer)
    #print(startAnswer, endAnswer)
    inSameGroup = False
    for locale in location:
        if(((startAnswer in range(locale[0], locale[0]+locale[2]+1)) and (endAnswer in range(locale[0], locale[0]+locale[2]+1)))):
            inSameGroup = True
            print("Moving on!")
            break
    if inSameGroup == False:
        lowHalf = computeStep(start, int(length/2), data, location)
        highHalf = computeStep(int(start+length/2), int(length/2), data, location)
        answer2 = min(lowHalf, highHalf, answer2)
    print("Start:", start, "length", length, [startAnswer, endAnswer])
    
    return answer2


answer1, answer2, i, j, game = 0,0,1,0, 1

seeds = []
soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []

with open('1input.txt', 'r') as file:
    lines = file.readlines()

# Extract seeds data
seeds_line = lines[0].strip().split(': ')[1]
seeds = list(map(int, seeds_line.split()))

# Extract soil data
soil_line_start = lines.index('seed-to-soil map:\n') + 1
soil_line_end = lines.index('\n', soil_line_start)
soil_lines = lines[soil_line_start:soil_line_end]
soil = [list(map(int, line.split())) for line in soil_lines]

# Extract fertilizer data
fertilizer_line_start = lines.index('soil-to-fertilizer map:\n') + 1
fertilizer_line_end = lines.index('\n', fertilizer_line_start)
fertilizer_lines = lines[fertilizer_line_start:fertilizer_line_end]
fertilizer = [list(map(int, line.split())) for line in fertilizer_lines]

# Extract water data
water_line_start = lines.index('fertilizer-to-water map:\n') + 1
water_line_end = lines.index('\n', water_line_start)
water_lines = lines[water_line_start:water_line_end]
water = [list(map(int, line.split())) for line in water_lines]

# Extract light data
light_line_start = lines.index('water-to-light map:\n') + 1
light_line_end = lines.index('\n', light_line_start)
light_lines = lines[light_line_start:light_line_end]
light = [list(map(int, line.split())) for line in light_lines]

# Extract temperature data
temperature_line_start = lines.index('light-to-temperature map:\n') + 1
temperature_line_end = lines.index('\n', temperature_line_start)
temperature_lines = lines[temperature_line_start:temperature_line_end]
temperature = [list(map(int, line.split())) for line in temperature_lines]

# Extract humidity data
humidity_line_start = lines.index('temperature-to-humidity map:\n') + 1
humidity_line_end = lines.index('\n', humidity_line_start)
humidity_lines = lines[humidity_line_start:humidity_line_end]
humidity = [list(map(int, line.split())) for line in humidity_lines]

# Extract location data
humidity_line_start = lines.index('humidity-to-location map:\n') + 1
humidity_line_end = lines.index('\n', humidity_line_start)
humidity_lines = lines[humidity_line_start:humidity_line_end]
location = [list(map(int, line.split())) for line in humidity_lines]

locationMap = 1000000000000
data = []
data.append(soil)
data.append(fertilizer)
data.append(water)
data.append(light)
data.append(temperature)
data.append(humidity)
data.append(location)

#print(data)
seedsPart2 = seeds.copy()
answer2 = 10000000000000000000000000000
for i in range(0, len(seedsPart2), 2):
    answer2 = min(computeStep(seedsPart2[i], seedsPart2[i+1], data, location), answer2)
    print(i/len(seedsPart2)*100,"%")

answer1 = getAnswer1(data, seeds)

#answer2 = getAnswer(data, seedsPart2)

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)



