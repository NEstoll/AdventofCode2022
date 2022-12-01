import sys

with open("day1/input.txt", "r") as file:
    each = []
    sum = 0
    for line in file:
        if line == "\n":
            each.append(sum)
            sum = 0
        else:
            sum += int(line)
    each.sort()
    print(each[-3] + each[-2] + each[-1])
