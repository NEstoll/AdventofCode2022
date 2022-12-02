import sys

with open(sys.argv[1]) as file:
    score = 0
    for line in file:
        opp = line.split()[0]
        me = line.split()[1]
        score += (ord('X')-ord(me))*-3
        if me=="Y":
            score += (ord(opp)-ord('A')+1)
        elif me=="Z":
            score += (ord(opp)-ord('A')+1)%3+1
        else:
            score += (2+ord(opp)-ord('A'))%3+1
    print (score)
