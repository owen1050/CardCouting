def createDeck(n):
    ret = {}
    for i in range(1,11):
        if i == 10:
            ret[i] = n * 16
        else:
            ret[i] = n * 4
    return ret

def totalDeck(d):
    ret = 0
    for i in d:
        ret = ret + d[i]
    return ret

def removeCard(c, d2):
    d = d2.copy()
    d[c] = d[c] - 1
    return d

def getDistribution(d):
    t = totalDeck(d)
    ret = {}
    for i in d:
        ret[i] = d[i] / t
    return ret

def getHandOdds(h, d, o):
    ret = {}
    dist = getDistribution(d)
    for c in dist: 
        t = list(h)
        t.append(c)
        ret[tuple(t)] = dist[c] * o
    return ret

def handsToPoints(h):
    ret = {}
    for i in h:
        possPts = [0]
        for j in i:
            if(j == 1):
                for k in range(len(possPts)):
                    possPts.append(possPts[k] + 11)
                    possPts[k] = possPts[k] + 1
            else:
                for k in range(len(possPts)):
                    possPts[k] = possPts[k] + j
        ret[tuple(possPts)] = h[i]
    return ret

def handToPoints(h):
    ret = 0
    possPts = [0]
    for j in h:
        if(j == 1):
            for k in range(len(possPts)):
                possPts.append(possPts[k] + 11)
                possPts[k] = possPts[k] + 1
        else:
            for k in range(len(possPts)):
                possPts[k] = possPts[k] + j

    return possPts

def genDealerOds(c, thisDeck):
    ods = getHandOdds(c, thisDeck, 1)

    while(allHandsStay(ods) == False):
        #print(ods)
        toRem = []
        toAdd = []
        for od in ods:
            if(dealerStays(od) == False and ods[od] > 0):
                deck = thisDeck
                for d in od:
                    deck = removeCard(d, deck)
                newOds = getHandOdds(od, deck, ods[od])
                toRem.append(od)
                toAdd.append(newOds)
        for odD in toAdd:
            for od in odD:
                ods[od] = odD[od]
        for od in toRem:
            del ods[od]

    
    ret = {}
    for od in ods:
        score = handToBestScore(od)
        if(score in ret):
            ret[score] = ods[od] + ret[score]
        else:
            if(ods[od] > 0):
                ret[score] = ods[od]

    return ret

def allHandsStay(h):
    AllStay = True
    for hand in h:
        if(dealerStays(hand) == False and h[hand] > 0):
            AllStay = False
    return AllStay

def handToBestScore(h):
    ns = handToPoints(h)
    best = -1
    for i in ns:
        if i > best and i < 22:
            best = i
    return best

def dealerStays(h):
    H = list(h)
    if(1 in H):
        bs = handToBestScore(h)
        if( bs > 17 or  bs == -1):
            return True
        else:
            return False
    else:
        if sum(H) >= 17:
            return True
        else:
            return False

def genPlayerOds(h, d):
    ods = getHandOdds(h, d, 1)
    ret = {}
    for od in ods:
        ret[handToBestScore(od)] = ods[od]
    return ret

numDecks = 1
deck = createDeck(numDecks)


playerHand = (10,4)
deck = removeCard(5, deck)
deck = removeCard(6, deck)
dealerHand = (10,)
deck = removeCard(10, deck)

dealerOds = genDealerOds(dealerHand, deck)
playerOds = genPlayerOds(playerHand, deck)

print(dealerOds)
print(playerOds)

