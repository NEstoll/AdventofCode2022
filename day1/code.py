from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line for line in inputFile]



    return lines

def part1(lines) -> Any:
    for l in lines:


        pass
    return None

def part2(lines) -> Any:
    each = []
    sum = 0
    for line in lines:
        if line == "\n":
            each.append(sum)
            sum = 0
        else:
            sum += int(line)
    each.sort()
    return (each[-3] + each[-2] + each[-1])
