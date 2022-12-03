import sys

with open(sys.argv[1]) as file:
    lines = [line for line in file]
sum = 0
for l in lines:
    first = l[:int(len(l)/2)]
    second = l[int(len(l)/2):]
    char = set(first).intersection(second).pop()
    if (char.capitalize() == char):
        add = 26+ord(char)-ord('A')+1
    else:
        add = ord(char)-ord('a')+1
    print(char, add)
    sum += add
print(sum)


