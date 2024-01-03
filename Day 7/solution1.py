filename = "input.txt"

hands = []
res = 0

cardValues = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "T": 10,
    "J" : 11,
    "Q": 12,
    "K": 13,
    "A" : 14
}

with open(filename) as text:
    for i,row in enumerate(text):
        hand, bid = row.strip().split(" ")
        hands.append([hand, int(bid)])        


def pokerScores(hand):
    handMap = {}
    for ch in hand:
        handMap[ch] = handMap.get(ch,0) + 1
    case = sorted(list(handMap.values()))

    if case  == [1,1,1,1,1]:
        return 1
    
    elif case == [1,1,1,2]:
        return 2
    
    elif case == [1,2,2]: 
        return 3
    
    elif case == [1,1,3]: 
        return 4
    
    elif case == [2,3]: 
        return 5
    
    elif case == [1,4]: 
        return 6
    
    elif case == [5]: 
        return 7
    
print(hands)


hands.sort(key = lambda x: (pokerScores(x[0]), cardValues[x[0][0]], cardValues[x[0][1]], cardValues[x[0][2]], cardValues[x[0][3]], cardValues[x[0][4]]))
        
for i, (_, bid) in enumerate(hands):
    res += (i+1) * bid

print(hands)
print(res)