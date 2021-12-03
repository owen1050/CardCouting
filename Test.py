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

def genAllOds(thisDeck)

def allOdsToBestHands(allOds):
    for od in allOds:
        print(od)


numDecks = 1
playerHand = (2,3)
dealer = (1,)

deck = createDeck(numDecks)
cards = totalDeck(deck)
newDeck = removeCard(1, deck)
dist = getDistribution(newDeck)
ods = getHandOdds(dealer, newDeck, 1)
pts = handsToPoints(ods)
allOds = []
for od in ods:
    thisDeck = newDeck
    for c in od:
        thisDeck = removeCard(c, thisDeck)
    newOds = getHandOdds(od, thisDeck, ods[od])
    t = handsToPoints(newOds)
    allOds.append(t)



