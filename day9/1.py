import numpy as np

def findLowPoints(heightMap):
    lowPoints = []
    for i in range(len(heightMap)):
        for j in range(len(heightMap[i])):
            #4 corners
            if i == 0 and j == 0:
                if heightMap[i+1][j] > heightMap[i][j] and heightMap[i][j+1] > heightMap[i][j]:
                    lowPoints.append((i,j))
            
            elif i == 0 and j == len(heightMap[i]) - 1:
                if heightMap[i+1][j] > heightMap[i][j] and heightMap[i][j-1] > heightMap[i][j]:
                    lowPoints.append((i,j))

            elif i == len(heightMap) - 1 and j == 0:
                if heightMap[i-1][j] > heightMap[i][j] and heightMap[i][j+1] > heightMap[i][j]:
                    lowPoints.append((i,j))
            
            elif i == len(heightMap) - 1 and j == len(heightMap[i]) - 1:
                if heightMap[i-1][j] > heightMap[i][j] and heightMap[i][j-1] > heightMap[i][j]:
                    lowPoints.append((i,j))
            
            #Edges
            elif i == 0:
                if heightMap[i+1][j] > heightMap[i][j] and heightMap[i][j+1] > heightMap[i][j] and heightMap[i][j-1] > heightMap[i][j]:
                    lowPoints.append((i,j))
            
            elif i == len(heightMap) - 1:
                if heightMap[i-1][j] > heightMap[i][j] and heightMap[i][j+1] > heightMap[i][j] and heightMap[i][j-1] > heightMap[i][j]:
                    lowPoints.append((i,j))
            
            elif j == 0:
                if heightMap[i+1][j] > heightMap[i][j] and heightMap[i-1][j] > heightMap[i][j] and heightMap[i][j+1] > heightMap[i][j]:
                    lowPoints.append((i,j))
            
            elif j == len(heightMap[i]) - 1:
                if heightMap[i+1][j] > heightMap[i][j] and heightMap[i-1][j] > heightMap[i][j] and heightMap[i][j-1] > heightMap[i][j]:
                    lowPoints.append((i,j))

            #The rest
            else:
                if heightMap[i+1][j] > heightMap[i][j] and heightMap[i-1][j] > heightMap[i][j] and heightMap[i][j+1] > heightMap[i][j] and heightMap[i][j-1] > heightMap[i][j]:
                    lowPoints.append((i,j))
    
    return lowPoints

def fill(heightMap, point):
    queue = [point]
    length = 1
    i = 0
    size = 0
    while i < length:
        y = queue[i][0]
        x = queue[i][1]
        if y != 0 and heightMap[y-1][x] != 9 and (y-1,x) not in queue:
            queue.append((y-1,x))
            length +=1

        if y != len(heightMap) -1 and heightMap[y+1][x] != 9 and (y+1,x) not in queue:
            queue.append((y+1,x))
            length +=1

        if x != 0 and heightMap[y][x-1] != 9 and (y,x-1) not in queue:
            queue.append((y,x-1))
            length +=1

        if x != len(heightMap[y]) -1 and heightMap[y][x+1] != 9 and (y,x+1) not in queue:
            queue.append((y,x+1))
            length +=1
        
        i += 1

    return len(queue)

with open("day9\\input.txt") as f:
    heightMap = np.array([[int(n) for n in line] for line in f.read().split('\n')])

points = findLowPoints(heightMap)

top3 = [0,0,0]

for point in points:
    size = fill(heightMap, point)
    if size > top3[0]:
        top3[0] = size
        top3.sort()
    
print(top3[0]*top3[1]*top3[2])