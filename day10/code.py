from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    cycle = 0
    x = 1
    total = 0
    for l in lines:
        opp = l.split(" ")
        match opp[0]:
            case "noop":
                cycle += 1
                total += testSignal(cycle, x)
            case addx:
                cycle += 1
                total += testSignal(cycle, x)
                cycle += 1
                total += testSignal(cycle, x)
                x += int(opp[1])

        pass
    return total

def part2(lines) -> Any:
    cycle = 0
    x = 1
    total = ""
    for l in lines:
        opp = l.split(" ")
        match opp[0]:
            case "noop":
                total += pixel(cycle, x)
                cycle += 1
            case addx:
                total += pixel(cycle, x)
                cycle += 1
                total += pixel(cycle, x)
                x += int(opp[1])
                cycle += 1

        pass
    return total

def testSignal(cycle, x):
    if cycle%40 == 20:
        print(x, cycle, x*cycle)
        return x*cycle
    return 0
def pixel(cycle, x):
    pixel = ""
    if cycle%40>=x-1 and cycle%40 <= x+1:
        pixel += "#"
    else:
        pixel += "."
    if cycle%40 == 39 and cycle != 0:
        pixel += "\n"
    return pixel