from typing import Any
import ast
from functools import cmp_to_key


def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    total = 0
    for i, l1, l2 in zip(range(len(lines)), lines[::3], lines[1::3]):
        left = ast.literal_eval(l1)
        right = ast.literal_eval(l2)
        if compare(left, right) < 0:
            total += i+1
            # print(i)
    return total

def part2(lines) -> Any:
    all = [ast.literal_eval(l) for l in lines if l.strip() != ""]
    dividers = [[[2]], [[6]]]
    all += dividers
    all = sorted(all, key=cmp_to_key(compare))
    print(all)
    return (all.index(dividers[0])+1)*(all.index(dividers[1])+1)

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left-right
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])
    for l, r in zip(left, right):
        value = compare(l, r)
        if value != 0:
            return value
    return len(left)-len(right)
        

        