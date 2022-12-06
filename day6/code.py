from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    l = lines[0]
    count = 0
    recent4 = []
    for c in l:
        if len(recent4) < 4:
            recent4.append(c)
        else:
            if len(set(recent4)) == len(recent4):
                print(recent4)
                break
            recent4.pop(0)
            recent4.append(c)
        count += 1
        
    return count

def part2(lines) -> Any:
    l = lines[0]
    count = 0
    recent14 = []
    for c in l:
        if len(recent14) < 14:
            recent14.append(c)
        else:
            if len(set(recent14)) == len(recent14):
                print(recent14)
                break
            recent14.pop(0)
            recent14.append(c)
        count += 1
        
    return count