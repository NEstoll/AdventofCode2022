import sys

with open(sys.argv[1]) as file:
    lines = [line.removesuffix("\n") for line in file]
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
    print(char, add)
    sum += add
print(sum)