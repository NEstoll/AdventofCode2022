from typing import Any
from math import copysign


def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    head=(0, 0)
    tail=(0, 0)
    locations = {(0, 0)}
    for l in lines:
        match l[0]:
            case "R":
                for i in range(int(l[2:])):
                    head = (head[0], head[1]+1)
                    tail = updateTail(head, tail)
                    locations.add(tail)
            case "L":
                for i in range(int(l[2:])):
                    head = (head[0], head[1]-1)
                    tail = updateTail(head, tail)
                    locations.add(tail)
            case "U":
                for i in range(int(l[2:])):
                    head = (head[0]+1, head[1])
                    tail = updateTail(head, tail)
                    locations.add(tail)
            case "D":
                for i in range(int(l[2:])):
                    head = (head[0]-1, head[1])
                    tail = updateTail(head, tail)
                    locations.add(tail)
    maxY = max([loc[0] for loc in locations])
    minY = min([loc[0] for loc in locations])
    maxX = max([loc[1] for loc in locations])
    minX = min([loc[1] for loc in locations])
    for i in reversed(range(minY, maxY+1)):
        for j in range(minX, maxX+1):
            if i == 0 and j == 0:
                print("s", sep="", end="")
                pass
            elif (i, j) in locations:
                print("#", sep="", end="")
                pass
            else:
                print(".", sep="", end="")
                pass
        print()

    return len(locations)

def part2(lines) -> Any:
    rope=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    locations = {(0, 0)}
    for l in lines:
        match l[0]:
            case "R":
                for i in range(int(l[2:])):
                    rope[0] = (rope[0][0], rope[0][1]+1)
                    for j in range(1, len(rope)):
                        rope[j] = updateTail(rope[j-1], rope[j])
                    locations.add(rope[9])
            case "L":
                for i in range(int(l[2:])):
                    rope[0] = (rope[0][0], rope[0][1]-1)
                    for j in range(1, len(rope)):
                        rope[j] = updateTail(rope[j-1], rope[j])
                    locations.add(rope[9])
            case "U":
                for i in range(int(l[2:])):
                    rope[0] = (rope[0][0]+1, rope[0][1])
                    for j in range(1, len(rope)):
                        rope[j] = updateTail(rope[j-1], rope[j])
                    locations.add(rope[9])
            case "D":
                for i in range(int(l[2:])):
                    rope[0] = (rope[0][0]-1, rope[0][1])
                    for j in range(1, len(rope)):
                        rope[j] = updateTail(rope[j-1], rope[j])
                    locations.add(rope[9])
    maxY = max([loc[0] for loc in locations])
    minY = min([loc[0] for loc in locations])
    maxX = max([loc[1] for loc in locations])
    minX = min([loc[1] for loc in locations])
    for i in reversed(range(minY, maxY+1)):
        for j in range(minX, maxX+1):
            if i == 0 and j == 0:
                # print("s", sep="", end="")
                pass
            elif (i, j) in locations:
                # print("#", sep="", end="")
                pass
            else:
                # print(".", sep="", end="")
                pass
        # print()

    return len(locations)

def updateTail(head, old):
    diff = tuple(x-y for x, y in zip(head, old))
    move = (0, 0)
    if (abs(diff[0]) == 2):
        move = (int(copysign(1, diff[0])), 0 if diff[1]==0 else int(copysign(1, diff[1])))
    elif (abs(diff[1]) == 2):
        move = (0 if diff[0]==0 else int(copysign(1, diff[0])), int(copysign(1, diff[1])))
    return tuple(x+y for x, y in zip(old, move))