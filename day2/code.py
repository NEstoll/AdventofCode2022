from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    for l in lines:


        pass
    return None

def part2(lines) -> Any:
    score = 0
    for line in lines:
        opp = line.split()[0]
        me = line.split()[1]
        score += (ord('X')-ord(me))*-3
        if me=="Y":
            score += (ord(opp)-ord('A')+1)
        elif me=="Z":
            score += (ord(opp)-ord('A')+1)%3+1
        else:
            score += (2+ord(opp)-ord('A'))%3+1
    return score
    
