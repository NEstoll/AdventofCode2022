import sys
from typing import Any

def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(input) -> Any:
    for l in input:

        pass
    return None

def part2(input) -> Any:
    count = 0
    for l in input:
        s1 = int(l.split(",")[0].split("-")[0])
        s2 = int(l.split(",")[1].split("-")[0])
        e1 = int(l.split(",")[0].split("-")[1])
        e2 = int(l.split(",")[1].split("-")[1])
        if (s1 <= s2 and e1 >= s2) or (s1 <= e2 and e1 >= e2) or (s2 <= s1 and e2 >= s1) or (s2 <= e1 and e2 >= e1):
            count += 1

        pass
    return count
