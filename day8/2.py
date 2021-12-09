import itertools as iter

with open("day8\\input.txt") as f:
    lines = []
    for line in f:
        out = line.split(' | ')
        for x in out[0].split():
            lines.append(x)
        for x in out[1].split():
            lines.append(x)


for line in lines:
    sol = [[] for n in range(10)]
    