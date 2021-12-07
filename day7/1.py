def part1(crap):
    fuel = float("inf")

    for i in range(min(crap), max(crap) + 1):
        t = sum(abs(x-i) for x in crap) #Calculate the fuel needed to get to postition i
        fuel = min(fuel, t)

    return fuel

def part2(crap):
    fuel = float("inf")

    g = lambda x: x * (x + 1) // 2

    for i in range(min(crap), max(crap) + 1):
        t = sum(g(abs(x-i)) for x in crap) #Calculate the fuel needed to get to postition i
        fuel = min(fuel, t)

    return fuel


with open("day7\\input.txt") as f:
    crap = [int(n) for n in f.read().split(',')]

print("PART1: " + str(part1(crap)))
print("PART2: " + str(part2(crap)))
