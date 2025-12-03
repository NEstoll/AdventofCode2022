from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    total = 0
    grid = []
    for line in lines:
        grid.append([(int(digit), False) for digit in line])
    for i, row in enumerate(grid):
        highest = 0
        for j, tuple in enumerate(row):
            if highest<tuple[0] or j == 0:
                grid[i][j] = (grid[i][j][0], True)
                highest = tuple[0]
    for i, row in enumerate(grid):
        highest = 0
        for j, tuple in reversed(list(enumerate(row))):
            if highest<tuple[0] or j == len(grid[i])-1:
                grid[i][j] = (grid[i][j][0], True)
                highest = tuple[0]
    for i in range(len(grid[0])):
        highest = 0
        for j, tuple in enumerate([row[i] for row in grid]):
            if highest<tuple[0] or j == 0:
                grid[j][i] = (grid[j][i][0], True)
                highest = tuple[0]
    for i in range(len(grid[0])):
        highest = 0
        for j, tuple in reversed(list(enumerate([row[i] for row in grid]))):
            if highest<tuple[0] or j == len(grid)-1:
                grid[j][i] = (grid[j][i][0], True)
                highest = tuple[0]
    for row in grid:
        for tree, visible in row:
            if visible:
                # print("\033[92m", tree, "\033[0m", sep="", end="",)
                total += 1
            else:
                # print("\033[91m", tree, "\033[0m", sep="", end="",)
                pass
        # print()
                



    return total

def part2(lines) -> Any:
    best = 0
    grid = []
    for line in lines:
        grid.append([int(digit) for digit in line])
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            up = 0
            for y in range(j-1, -1, -1):
                up += 1
                if (grid[i][y]>=tree):
                    break
            down = 0
            for y in range(j+1, len(grid)):
                down += 1
                if (grid[i][y]>=tree):
                    break
            left = 0
            for x in range(i-1, -1, -1):
                left += 1
                if (grid[x][j]>=tree):
                    break
            right = 0
            for x in range(i+1, len(grid[i])):
                right += 1
                if (grid[x][j]>=tree):
                    break
            score = up*down*left*right
            if score>best:
                best = score
                print("The tree at", i, j, "has a score of", score, "with", up, down, left, right, "(up, down, left, right)")



    return best