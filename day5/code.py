import re
from typing import Any



def parseInput(inputFile) -> list[Any]:
    moves = False
    stacks = []
    move = []
    for line in inputFile:
        if line == "\n":
            moves = True
            continue
        if not moves:
            s = []
            l = int((len(line)/4))
            for i in range(0, l):
                s.append(line[1+i*4])
            stacks.append(s)
            # print(l, s, len(line))
        else:
            m = re.findall('\\d+', line)
            move.append(m)
    stacks.pop()
    stacks2 = [[] for s in stacks[0]]
    for j in range(0, len(stacks)):
        for i in range(0, len(stacks[j])):
            stacks2[i].append(stacks[j][i])
    stacks2 = [[c for c in s if c != ' '] for s in stacks2]
    print(stacks2)



    return [stacks2, move]

def part1(lines: list[list[Any]]) -> Any:
    stacks = lines[0]
    moves = lines[1]
    for m in moves:
        if (int(m[1]) == 8) or int(m[2])==8:
            stop = True
        for i in range(0, int(m[0])):
            stacks[int(m[2])-1].insert(0, stacks[int(m[1])-1].pop(0))
            

        pass
    r = ""
    for s in stacks:
        r += s[0]
    return r

def part2(lines) -> Any:
    stacks = lines[0]
    moves = lines[1]
    for m in moves:
        if (int(m[1]) == 8) or int(m[2])==8:
            stop = True
        temp = []
        for i in range(0, int(m[0])):
            temp.insert(0, stacks[int(m[1])-1].pop(0))
        for i in range(0, int(m[0])):
            stacks[int(m[2])-1].insert(0, temp.pop(0))

        pass
    r = ""
    for s in stacks:
        if len(s) > 0:
            r += s[0]
    return r
