from collections import defaultdict, Counter

events = []

SLEEP, WAKE = 0, 1

with open('input.txt') as f:
    for line in f:
        split = line.split()

        year, month, day = map(int, split[0][1:].split('-'))
        hour, minute = map(int, split[1][:-1].split(':'))
        number, type = None, None

        if split[2] == "Guard":
            number = int(split[3][1:])
        elif split[2] == "falls":
            type = SLEEP
        else:
            type = WAKE

        events.append((year, month, day, hour, minute, number, type))

events.sort()

sleepTimes = defaultdict(Counter)
currentGuard, startOfSleep = None, None

for event in events:
    _, _, _, _, minute, number, type = event

    if number is not None:
        currentGuard = number
    elif type == SLEEP:
        startOfSleep = minute
    elif type == WAKE:
        sleepTimes[currentGuard].update(range(startOfSleep, minute))
    else:
        raise ValueError("Improper data")

##########
# Part 1 #
##########

guard = max(sleepTimes, key = lambda k: sum(sleepTimes[k].values()))
minute = sleepTimes[guard].most_common(1)[0][0]

print("Part 1:", guard * minute)


##########
# Part 2 #
##########

guard = max(sleepTimes, key = lambda k: sleepTimes[k].most_common(1)[0][1])
minute = sleepTimes[guard].most_common(1)[0][0]

print("Part 2:", minute * guard)
