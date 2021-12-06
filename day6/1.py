
if __name__ == '__main__':
    with open("day6\\example.txt") as f:
        fish = [int(n) for n in f.readline().split(',')]
    
    for i in range(0,256):
        newFish = 0
        for j in range(0, len(fish)):
            if fish[j] == 0:
                fish[j] = 6
                newFish += 1
            else:
                fish[j] -= 1
        if newFish > 0:
            for k in range(0, newFish):
                fish.append(8)
    
    print(len(fish))
    