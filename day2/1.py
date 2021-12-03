from typing import Match


def nav(place):
    x = 0
    y = 0
    commands = []
    for i in range(0, len(place)-1):
        aux = place[i].split(' ')
        commands.append((aux[0], int(aux[1])))
    for command in commands:
        match command[0]:
            case 'forward':
                x += command[1]
            case 'down':
                y += command[1]
            case  'up':
                y -= command[1]
    return x*y
    
def nav2(place):
    x = 0
    y = 0
    aim = 0
    commands = []
    for i in range(0, len(place)-1):
        aux = place[i].split(' ')
        commands.append((aux[0], int(aux[1])))
    for command in commands:
        match command[0]:
            case 'forward':
                x += command[1]
                y += (command[1]*aim)
            case 'down':
                aim += command[1]
            case  'up':
                aim -= command[1]
    return x*y

if __name__ == '__main__':
    with open("day2\\input1.txt") as f:
        place = f.read().split("\n")
        print("PART1: "+ str(nav(place)))
        print("PART2: "+ str(nav2(place)))