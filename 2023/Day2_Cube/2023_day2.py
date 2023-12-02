import os
import re
answer1, answer2, i, j, game = 0,0,1,0, 1
redCubes = 12#not making this a #def feels very wrong
greenCubes = 13
blueCubes = 14
pattern = re.compile('\d+')

class Bag:#this is only a class because I thought round 2 was going to be way more complicated
    red, blue, green = 0, 0, 0
f = open("input.txt", "r")
for line in f:#read the file
    rounds=((line.strip()).split(':'))[1].split(';')#get a list of each bag pull
    roundEliminated = False
    maxBag = Bag()#holds the highest numbers in each game
    for round in rounds:#iterate through each set (bag pull)
        bag = Bag() #just holds the results from each bag pull 
        cubes = round.split(',')
        for cube in cubes:#now get the rgb values for each bag pull and add them up
            numCubes = int(pattern.search(cube).group())
            if(cube[-1]=='d'):#red (yes this is a dumb way to match this but it's midnight and I'm tired)
                bag.red = numCubes
                if(bag.red>maxBag.red):#part 2
                    maxBag.red = bag.red
            if (cube[-1] == 'e'):
                bag.blue = numCubes
                if(bag.blue>maxBag.blue):#part2
                    maxBag.blue = bag.blue
            if(cube[-1] == 'n'): 
                bag.green = numCubes
                if(bag.green>maxBag.green):#part2
                    maxBag.green = bag.green
            if(bag.blue > blueCubes or bag.red>redCubes or bag.green>greenCubes):#checking if it's a valid round or not for round 1
                roundEliminated = True
        
    answer2 += maxBag.blue*maxBag.green*maxBag.red
    if(not roundEliminated):
        answer1+=game    
    game+=1

print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)