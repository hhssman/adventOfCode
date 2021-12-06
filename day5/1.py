import numpy as np
from numpy.core.arrayprint import get_printoptions

def plotStraightLine(graph, line):
    mask = line[0] == line[1]
    if mask[0]:
        for y in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
            graph[line[0][0]][y] += 1
    elif mask[1]:
        for x in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
            graph[x][line[0][1]] += 1

def plotLine(graph, line):
    if line[0][0] == line[1][0]:
        for y in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
            graph[line[0][0]][y] += 1
    elif line[0][1] == line[1][1]:
        for x in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
            graph[x][line[0][1]] += 1
    else:
        if line[0][0] < line[1][0]:
            if line[0][1] < line[1][1]:
                for x in range(0, line[1][0] - line[0][0]+1):
                    graph[line[0][0]+x][line[0][1]+x] += 1
            else:
                for x in range(0, line[1][0] - line[0][0]+1):
                    graph[line[0][0]+x][line[0][1]-x] += 1  
        else:
            if line[0][1] < line[1][1]:
                for x in range(line[0][0] - line[1][0]+1):
                    graph[line[0][0]-x][line[0][1]+x] += 1
            else:
                for x in range(line[0][0] - line[1][0]+1):
                    graph[line[0][0]-x][line[0][1]-x] += 1
        

if __name__ == '__main__':
    with open("day5\\input.txt") as f:
        cordinates = np.array([[[int(n) for n in cord.split(',')] for cord in row.split(' -> ')] for row in f.read().split('\n')])
        graph1 = np.array([[0 for i in range(0,1000)] for row in range(0,1000)])
        graph2 = np.array([[0 for i in range(0,1000)] for row in range(0,1000)])

        for line in cordinates:
            plotStraightLine(graph1, line)
            plotLine(graph2, line)

        count = 0
        #print(graph1)
        for line in graph1:
            for x in line:
                if x > 1:
                    count += 1
        #print(count)
        #graph290 = np.flip(np.rot90(graph2, 3),1)
        #print(graph290)
        count2 = 0
        for line in graph2:
            for x in line:
                if x > 1:
                    count2 += 1
        print(count2)