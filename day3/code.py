import sys
from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    sum = 0
    for l in lines:
        first = l[:int(len(l)/2)]
        second = l[int(len(l)/2):]
        char = set(first).intersection(second).pop()
        if (char.capitalize() == char):
            add = 26+ord(char)-ord('A')+1
        else:
            add = ord(char)-ord('a')+1
        sum += add
    return sum

def part2(lines) -> Any:
    sum = 0
    for i in range(0, len(lines), 3):
        s1 = set(lines[i])
        s2 = set(lines[i+1])
        s3 = set(lines[i+2])
        print(s1.intersection(s2))
        print(s1.intersection(s2).intersection(s3))
        char = s1.intersection(s2).intersection(s3).pop()
        
        if (char.capitalize() == char):
            add = 26+ord(char)-ord('A')+1
        else:
            add = ord(char)-ord('a')+1
        sum += add
    return sum


