from importlib import import_module
import sys
day = sys.argv[1]
mycode = import_module(day + ".code")

input = ["test.txt", "input.txt"]
output = []
output = []
try:
    expected = [[s.strip() for s in l.removesuffix("\n").strip().split(",")] for l in open(day + "/expected.txt")]
except FileNotFoundError:
    print("Expected file not found")
    expected = []
print("Advent of Code: " + day)
for i in range(0, len(input)):
    try:
        print("\nTest " + str(i) + " (" + input[i] + "):")
        with open(day + "/" + input[i], "r") as file:
            codeInput = mycode.parseInput(file)
            codeOutput = []
            part1 = mycode.part1(codeInput)
            print("\tPart 1: " + str(part1))
        with open(day + "/" + input[i], "r") as file:
            codeInput = mycode.parseInput(file)
            codeOutput = []
            part2 = mycode.part2(codeInput)
            print("\tPart 2: " + str(part2))
            output.append([part1, part2])
    except FileNotFoundError:
        print(input[i] + " not found")
        output.append([None, None])
print()
bad = 0
for i in range(0, len(output)):
    print(input[i] + ": ")
    for o in range(0, len(output[i])):
        if output[i][o] == None:
            print("\tpart " + str(o+1) + ": No Answer")
            continue
        if (i < len(expected) and o < len(expected[i])):
            if (str(output[i][o]) != expected[i][o]):
                bad += 1
                print("\tpart " + str(o+1) + ": " + '\033[91m' + str(output[i][o]) + " != " + expected[i][o] + '\033[0m')
            else:
                print("\tpart " + str(o+1) + ": " + '\033[92m' + str(output[i][o]) + " == " + expected[i][o] + '\033[0m')
        else:
            print("\tpart " + str(o+1) + ": \n" + str(output[i][o]))
if bad == 0:
    print("\n" + '\033[92m' + "Provided outputs match the test cases" + '\033[0m')
else:
    print("\n" + '\033[91m' + str(bad) + " provided outputs DO NOT match the test cases" + '\033[0m')

