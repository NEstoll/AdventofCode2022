from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]



    return lines

def part1(lines) -> Any:
    files = {"/":[0, []]}
    curr = "/"
    for l in lines:
        if l[0] == "$":
            if l[2:4] == "cd":
                if l[5:] == "..":
                    curr = curr[:-1]
                    while curr[len(curr)-1] != "/":
                        curr = curr[:-1]
                elif l[5:] == "/":
                    curr = "/"
                else:
                    curr = curr  + l[5:]+ "/"
                    files[curr] = [0, []]
                print(curr)
            else:
                pass
        else:
            if l[0:3] == "dir":
                files[curr][1].append(curr + l[4:]+ "/")
                if files.get(curr + l[4:]+ "/", 0) == 0:
                    files[curr + l[4:]+ "/"] = [0, []]
            else:
                files[curr][0] += int(l.split(" ")[0])
        pass
    ans = 0
    print(files)
    for f in files.values():
        s = sum(f, files)
        if s <= 100000:
            ans += s




    return ans

def sum(dir, all) -> int:
    if len(dir[1]) == 0:
        return dir[0]
    s = dir[0]
    for r in dir[1]:
        s += sum(all[r], all)
    return s

def part2(lines) -> Any:
    files = {"/":[0, []]}
    curr = "/"
    for l in lines:
        if l[0] == "$":
            if l[2:4] == "cd":
                if l[5:] == "..":
                    curr = curr[:-1]
                    while curr[len(curr)-1] != "/":
                        curr = curr[:-1]
                elif l[5:] == "/":
                    curr = "/"
                else:
                    curr = curr  + l[5:]+ "/"
                    files[curr] = [0, []]
                print(curr)
            else:
                pass
        else:
            if l[0:3] == "dir":
                files[curr][1].append(curr + l[4:]+ "/")
                if files.get(curr + l[4:]+ "/", 0) == 0:
                    files[curr + l[4:]+ "/"] = [0, []]
            else:
                files[curr][0] += int(l.split(" ")[0])
        pass
    ans = 0
    unused = 70000000-sum(files["/"], files)
    possible = []
    print(files)
    for f in files.values():
        s = sum(f, files)
        if s+unused >= 30000000:
            possible.append(s)
    possible.sort()
    return possible[0]