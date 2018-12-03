from collections import defaultdict

d = defaultdict(int)
count = 0

with open("input.txt") as f:
    for line in f:
        p = line.split()
        n = int(p[0][1:])
        l = int(p[2].split(",")[0])
        t = int(p[2].split(",")[1][:-1])
        w = int(p[3].split("x")[0])
        h = int(p[3].split("x")[1])

        for i in range(w):
            for j in range(h):
                d[l + i, t + j] += 1
                if d[l + i, t + j] == 2:
                    count += 1

print("part 1", count)

with open("input.txt") as f:
    for line in f:
        p = line.split()
        n = int(p[0][1:])
        l = int(p[2].split(",")[0])
        t = int(p[2].split(",")[1][:-1])
        w = int(p[3].split("x")[0])
        h = int(p[3].split("x")[1])
        Good = True

        for i in range(w):
            for j in range(h):
                if d[l + i, t + j] > 1:
                    Good = False

        if Good:
            print("part 2", n)
