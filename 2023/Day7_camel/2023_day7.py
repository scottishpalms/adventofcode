class Game:
    hand = []
    bet = 0
    tier = 0
    rank = 0
    value = 0
    winnings = 0
    hexHand = 0
    originalHand = 0

def fullProgram(part2):#part 1 and part 2 only differ by how the joker is treated
    answer1 = 0
    games=[[],[],[],[],[],[],[]]
    f = open("input.txt", "r")
    for i, line in enumerate(f):#read the input file
        game = Game()
        line = line.strip()
        line = line.split(" ")
        game.hand = list(line[0])
        game.originalHand = list(line[0])
        #convert face cards to hex numbers for easier ranking
        for j, card in enumerate(game.hand):
            if card == 'T':
                game.hand[j] = 'A'
            elif card == 'J':
                if(part2):
                    game.hand[j] = '1'#joker is low/wild card for part2
                else: game.hand[j] = 'B'
            elif card == 'Q':
                game.hand[j] = 'C'
            elif card == 'K':
                game.hand[j] = 'D'
            elif card == 'A':
                game.hand[j] = 'E'
        game.bet =(int(line[1]))
        tempSet = set(game.hand)#figure out how many unique cards are in the set   
        #now figure out the value of the hand is (pair, full house, etc) 
        if(len(tempSet) == 5):#why does python not have switch statements??
            if '1' in tempSet:
                game.tier = 1#joker makes a pair, and there wasn't already a pair of jokers here
            else: game.tier = 0#high card
        elif(len(tempSet)==4): 
                if '1' in tempSet:
                    game.tier = 3 #joker turns the pair into three of a kind (or two jokers merge with another card)
                else: game.tier = 1#pair
        elif(len(tempSet)==3): #three of a kind or two pair
            isTwoPair = False
            for card in game.hand:
                if (game.hand.count(card) == 2):
                    isTwoPair = True
                    break
            if(isTwoPair):
                if '1' in tempSet:
                    if(game.hand.count('1') == 1):
                        game.tier = 4 #two pair goes to full house (example: 22J33 becomes 22233)
                    else: game.tier = 5 #there must be 2 jokers, so two pair goes to four of a kind (example: 223JJ becomes 22322)
                else: game.tier = 2
            else: 
                if '1' in tempSet:
                    game.tier = 5 #joker turns this to 4 of a kind
                else: game.tier = 3 #three of a kind
        elif(len(tempSet)==2): 
            if(game.hand.count(game.hand[0]) == 4 or game.hand.count(game.hand[0]) == 1):#how many of the first character do we have?
                if '1' in tempSet:
                    game.tier = 6 #joker turns this to 5 of a kind
                else:   game.tier = 5#four of a kind
            else: 
                if '1' in tempSet:
                    game.tier = 6 # joker turns full house into 5 of a kind
                else: game.tier =  4#full house
        else:
                game.tier = 6#five of a kind
        game.hexHand= int(("".join(game.hand)), 16)#reverse the hand then convert to a hex number
        games[game.tier].append(game)#make 7 different lists broken out by tier
        #print(game.tier)
    
    currentRank = 0    
    for i, tierGroup in enumerate(games):#run through each tier and sort
        games[i] = sorted(games[i], key=lambda x: x.hexHand, reverse = False)
        for j, round in enumerate(tierGroup):
            currentRank += 1
            games[i][j].rank = currentRank #only recording this for debugging purposes
            games[i][j].winnings = currentRank * games[i][j].bet
            answer1 += games[i][j].winnings
            
    return answer1

print("Part 1 Answer: ", fullProgram(False))
print("Part 2 Answer: ", fullProgram(True))


