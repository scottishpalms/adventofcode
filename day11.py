class Monkey:
   def  __init__(self):    
        self.startItems = []
        self.operation = ['','']
        self.test = 0
        self.t = 0
        self.f = 0
        self.inspectionCounter = 0

answer1, answer2, i, j = 0,0,0,0
instructions = []
mbuisness = []
product = 1
monkeyIndex = -1
monks = []

f = open("input11.txt", "r")
for line in f:#read the file
    row = [0,0]
    numString = ''
    text = line.strip().split(":")
    #print(text)
    if len(text)>1:
        if text[0][0]=='M':
            monks.append(Monkey())
            monkeyIndex +=1
        elif text[0] == "Starting items":
            text[1] = text[1].replace(" ", '')
            text[1] = text[1].split(",")
            startingItems = []
            for item in text[1]:
                if(item!=''):                    
                    startingItems.append(int(item))
            monks[monkeyIndex].startItems += startingItems
        elif text[0] == "Operation":
            # text[1] = text[1].replace(" ", '')
            text[1] = text[1].split(" ")
            monks[monkeyIndex].operation = text[1][4:]
        elif text[0] == "Test":
            text[1] = text[1].split(" ")
            monks[monkeyIndex].test = int(text[1][3])
            product *= monks[monkeyIndex].test
        elif text[0] == "If true":
            text[1] = text[1].split(" ")
            monks[monkeyIndex].t = int(text[1][4])            
        elif text[0] == "If false":
            text[1] = text[1].split(" ")
            monks[monkeyIndex].f = int(text[1][4])           


numRounds = 10000
for rounds in range(0, numRounds):    
    for monkey in monks:
        numItems = len(monkey.startItems)
        for j in range(0,numItems):
            item = monkey.startItems.pop(0)
            #print(item)
            monkey.inspectionCounter += 1
            operand = monkey.operation[1]
            if operand == "old":
                operand = item
            else: 
                operand = int(monkey.operation[1])            
            if monkey.operation[0] == "+":
                item += operand
            if monkey.operation[0] == "*":
                # print("\nMultiplying:", item, "by", operand)
                item = operand * item
                # print("result is: ", item,"\n")

            #Part1 only: 
            # item = int(item/3)            
            item = (item % product) + product #keep "worry levels manageable"
            if (item % monkey.test):#If false test
                monks[monkey.f].startItems.append(item)

            else:#true test
                monks[monkey.t].startItems.append(item)
        
    # print("Done with round:",rounds)

           
for monkey in monks:
    mbuisness.append(monkey.inspectionCounter)
mbuisness.sort(reverse=True)
answer2 = mbuisness[0]*mbuisness[1]
print("Part 1 Answer: ", answer1)
print("Part 2 Answer: ", answer2)





