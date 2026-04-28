from typing import Any



def parseInput(inputFile) -> list[Any]:
    lines = [line.removesuffix("\n") for line in inputFile]
    


    return lines

def part1(lines:list[str]) -> Any:
    monkies = {}
    for i in range(7, len(lines)+1, 7):
        monkey = lines[i-7:i]
        id = int(monkey[0][7:-1])
        items = [int(s) for s in monkey[1][17:].split(",")]
        operation = monkey[2][18:].strip().split(" ")
        match operation[1]:
            case "*":
                func = mult(int(operation[2]) if operation[2] != "old" else None)
            case "+":
                func = add(int(operation[2]) if operation[2] != "old" else None)
        test = (int(monkey[3][20:]), int(monkey[4][28:]), int(monkey[5][29:]))
        monkies[id] = (items, func, test)
        pass
    activity = [0 for x in monkies]
    allItems = []
    for id in monkies:
        allItems += [(id, item) for item in monkies[id][0]]
    for item in allItems:
        start = item[0]
        current = item[0]
        worry = item[1]
        tracking = [0 for x in activity]
        # print("tracking item", item, "starting at monkey", start)
        i = 0
        while i < 20:
            tracking[current] += 1
            last = current
            worry = monkies[current][1](worry)
            worry = worry//3
            current = monkies[current][2][1] if worry%monkies[current][2][0]==0 else monkies[current][2][2]
            if (current == start) and False:
                print("shortcut after", i, "trips", tracking)
                tracking = [x*(20//(i+1)) for x in tracking]
                i += (i+1)*((20//(i+1))-1)
            if last > current:
                i += 1
        activity = [x+y for x,y in zip(activity, tracking)]
    print(activity)
    activity.sort(reverse=True)
    return activity[0]*activity[1]

def mult(value):
    if value is None:
        return lambda x: x*x
    else:
        return lambda x: x*value

def add(value):
    if value is None:
        return lambda x: x+x
    else:
        return lambda x: x+value

def part2(lines) -> Any:
    monkies = {}
    bigFactor = 1
    for i in range(7, len(lines)+1, 7):
        monkey = lines[i-7:i]
        id = int(monkey[0][7:-1])
        items = [int(s) for s in monkey[1][17:].split(",")]
        operation = monkey[2][18:].strip().split(" ")
        match operation[1]:
            case "*":
                func = mult(int(operation[2]) if operation[2] != "old" else None)
            case "+":
                func = add(int(operation[2]) if operation[2] != "old" else None)
        test = (int(monkey[3][20:]), int(monkey[4][28:]), int(monkey[5][29:]))
        bigFactor *= int(monkey[3][20:])
        monkies[id] = (items, func, test)
        pass
    activity = [0 for x in monkies]
    allItems = []
    for id in monkies:
        allItems += [(id, item) for item in monkies[id][0]]
    for item in allItems:
        start = item[0]
        current = item[0]
        worry = item[1]
        tracking = [0 for x in activity]
        print("tracking item", item, "starting at monkey", start)
        i = 0
        while i < 10000:
            tracking[current] += 1
            last = current
            worry = monkies[current][1](worry)
            worry = worry%bigFactor
            current = monkies[current][2][1] if worry%monkies[current][2][0]==0 else monkies[current][2][2]
            if (current == start) and False:
                print("shortcut after", i, "trips", tracking)
                tracking = [x*(10000//(i+1)) for x in tracking]
                i += (i+1)*((10000//(i+1))-1)
            if last > current:
                i += 1
        activity = [x+y for x,y in zip(activity, tracking)]
    print(activity)
    activity.sort(reverse=True)
    return activity[0]*activity[1]