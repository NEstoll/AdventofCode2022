from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines: list[str]) -> Any:
    grid = []
    start = ()
    end = ()
    for l in lines:
        row = [ord(c)-ord('a') for c in l]
        if 'S' in l:
            start = (len(grid), l.index('S'))
            row[start[1]] = 0
        if 'E' in l:
            end = (len(grid), l.index('E'))
            row[end[1]] = 25
        grid.append(row)
        pass
    best = {}
    heights = {0: {}}
    heights[0][start] = [start]
    while len(heights) > 0:
        paths = heights.pop(max(heights.keys()))
        while len(paths) > 0:
            current = min(paths.keys(), key=lambda p: (end[0]-p[0])**2+(end[1]-p[1])**2)
            path = paths.pop(current)
            if best.get(str(current)) is None or len(best[str(current)]) > len(path):
                best[str(current)] = path
            else:
                continue
            if current == end:
                continue
            for r, c in zip([1, -1, 0, 0], [0, 0, -1, 1]):
                if 0 <= current[0]+r < len(grid) and 0 <= current[1]+c < len(grid[current[0]+r]) and (current[0]+r, current[1]+c) not in path:
                    next = (current[0]+r, current[1]+c)
                    diff = grid[current[0]+r][current[1]+c]-grid[current[0]][current[1]]
                    if diff <= 1:
                        if heights.get(grid[current[0]+r][current[1]+c]) is None:
                            heights[grid[current[0]+r][current[1]+c]] = {}
                        if heights[grid[current[0]+r][current[1]+c]].get(next) is None or len(heights[grid[current[0]+r][current[1]+c]].get(next)) > len(path)+1:
                            heights[grid[current[0]+r][current[1]+c]][next] = path+[next]
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if best.get(str((r, c))) is not None:
                print("\033[92m" + chr(char+ord('a'))+ '\033[0m', end="")
            else:
                print("\033[91m" + chr(char+ord('a'))+ '\033[0m', end="")
        print()

    return len(best[str(end)])-1


def part2(lines) -> Any:
    grid = []
    start = []
    end = ()
    for l in lines:
        row = [ord(c)-ord('a') for c in l]
        if 'S' in l:
            row[l.index('S')] = 0
        if 'E' in l:
            end = (len(grid), l.index('E'))
            row[end[1]] = 25
        start += [(len(grid), i) for i, c in enumerate(row) if c == 0]
        grid.append(row)
        pass
    best = {}
    heights = {0: {s:[s] for s in start}}
    while len(heights) > 0:
        paths = heights.pop(max(heights.keys()))
        while len(paths) > 0:
            current = min(paths.keys(), key=lambda p: (end[0]-p[0])**2+(end[1]-p[1])**2)
            path = paths.pop(current)
            if best.get(str(current)) is None or len(best[str(current)]) > len(path):
                best[str(current)] = path
            else:
                continue
            if current == end:
                continue
            for r, c in zip([1, -1, 0, 0], [0, 0, -1, 1]):
                if 0 <= current[0]+r < len(grid) and 0 <= current[1]+c < len(grid[current[0]+r]) and (current[0]+r, current[1]+c) not in path:
                    next = (current[0]+r, current[1]+c)
                    diff = grid[current[0]+r][current[1]+c]-grid[current[0]][current[1]]
                    if diff <= 1:
                        if heights.get(grid[current[0]+r][current[1]+c]) is None:
                            heights[grid[current[0]+r][current[1]+c]] = {}
                        if heights[grid[current[0]+r][current[1]+c]].get(next) is None or len(heights[grid[current[0]+r][current[1]+c]].get(next)) > len(path)+1:
                            heights[grid[current[0]+r][current[1]+c]][next] = path+[next]
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if best.get(str((r, c))) is not None:
                print("\033[92m" + chr(char+ord('a'))+ '\033[0m', end="")
            else:
                print("\033[91m" + chr(char+ord('a'))+ '\033[0m', end="")
        print()

    return len(best[str(end)])-1