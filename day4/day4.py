from collections import defaultdict, Counter

events = []

with open('input.txt') as f:
    for line in f:
        split = line.split()
        date = split[0][1:].split('-')
        time = split[1][:-1].split(':')

        if split[2] == "Guard":
            number = int(split[3][1:])
            type = 0
        elif split[2] == "falls":
            number = -1
            type = 1
        else:
            number = -1
            type = 2

        events.append((int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), number, type))

events.sort()

sleepTimes = defaultdict(Counter)

# Part 1

currentGuard = -1
lastAsleep = 0

for i, event in enumerate(events):
    _, _, _, _, minute, number, type = event

    if type == 0:
        currentGuard = number
        continue

    if type == 1:
        lastAsleep = minute
        continue

    sleepTimes[currentGuard].update(range(lastAsleep, minute))

sleepiestGuard = max(sleepTimes, key = lambda k: sum(sleepTimes[k].values()))
sleepiestMinute = sleepTimes[sleepiestGuard].most_common(1)[0][0]

print("Part 1:", sleepiestGuard * sleepiestMinute)

# Part 2

guard = max(sleepTimes, key = lambda k: sleepTimes[k].most_common(1)[0][1])
minute = sleepTimes[guard].most_common(1)[0][0]

print("Part 2:", minute * guard)
