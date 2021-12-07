
with open("day6\\input.txt") as f:
    fish = [int(n) for n in f.readline().split(',')]

#A more elegant way to do it
nr = []
for i in range(9):
    nr.append(0)

for x in fish:
    nr[x] += 1

for day in range(256):
    f = nr[0]

    for i in range(len(nr)-1):
        nr[i] = nr[i+1]
    nr[6] += f
    nr[8] = f

print("PART2: " + str(sum(nr)))