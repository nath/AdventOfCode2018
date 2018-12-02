from collections import Counter

two = 0
three = 0

with open('input.txt') as f:
    for line in f:
        c = Counter(line)
        twoD = 1
        threeD = 1
        for d in c:
            if c[d] == 2:
                two += twoD
                twoD = 0
            if c[d] == 3:
                three += threeD
                threeD = 0

print(two * three)

with open('input.txt') as f:
    lines = [line for line in f]

def matches(a, b):
    mismatch = 0
    for c, d in zip(a,b):
        if c != d:
            mismatch += 1

    return mismatch == 1 and len(a) == len(b)

for line1 in lines:
    for line2 in lines:
        if matches(line1, line2):
            print(line1)
            print(line2)
