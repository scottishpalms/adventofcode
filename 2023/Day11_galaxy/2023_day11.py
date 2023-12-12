answer1, answer2 = 0,0

def wholeProgram(EXPANSION_RATE):
    f = open("input.txt", "r")
    answer1 = 0
    emptyRows = []
    universe = []
    for i, line in enumerate(f):#read the input file
        universe.append(list(line.strip()))
        if(len(set(universe[-1]))==1):#handle empty rows
            #universe.append(list(line.strip()))
            emptyRows.append(i)

    emptyCols = []
    galaxyCoord = []
    for j in range(0, len(universe[0])):#identify the empty colummns
        containsGalaxy = False
        for i in range(0, len(universe)):
            if universe[i][j] =='#':
                containsGalaxy = True
        if(not containsGalaxy):
            emptyCols.append(j)

    for j in range(0, len(universe[0])):#get the coordinates of the galaxies
        for i in range(0, len(universe)):
            if universe[i][j] =='#':
                galaxyCoord.append([])#the first row of galaxyCoord has every galaxy, the 2nd one has everything but the first, and so on. each row is a partial list of pairs
                for k in range(0, len(galaxyCoord)):
                    galaxyCoord[k].append((i, j))

### run through the list of list of galaxies pairs
    for i, line in enumerate(galaxyCoord):
        for j, galaxy in enumerate(line):
      
            #find the distance between two galaxies
            if line[0][0] < galaxy[0]:
                start = line[0][0]
                end = galaxy[0]
            else:
                start = galaxy[0]
                end =  line[0][0]             
            for k in range(start, end):
                if(abs(k) in emptyRows):#check if we traverse and empty row
                    answer1+=EXPANSION_RATE
                else: answer1+=1

            if line[0][1] < galaxy[1]:
                start = line[0][1]
                end = galaxy[1]
            else:
                start = galaxy[1]
                end =  line[0][1]           
            for k in range(start, end):
                if(abs(k) in emptyCols):
                    answer1+=EXPANSION_RATE
                else: answer1+=1

    return answer1


print("Part 1 Answer: ", wholeProgram(2))
print("Part 2 Answer: ", wholeProgram(1000000))


