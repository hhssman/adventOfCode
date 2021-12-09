with open("day8\\input.txt") as f:
    output = []
    for line in f:
        out = line.split(' | ')
        for x in out[1].split():
            output.append(x)
    
count = 0
for nr in output:
    length = len(nr)
    if length == 2:
        count += 1
    elif length == 4:
        count += 1
    elif length == 3:
        count += 1
    elif length == 7:
        count += 1

print(count)