def mult(nr):
    i = 0
    found = False
    multi = 0
    while i < len(nr) and not found:
        j = i+1
        while j < len(nr) and not found:
            if (nr[i] + nr[j]) == 2020:
                multi = nr[i] * nr[j]
                found = True
            else:
                j += 1
        i += 1
    return multi

def mult2(nr):
    i = 0
    found = False
    multi = 0
    while i < len(nr) and not found:
        j = i+1
        while j < len(nr) and not found:
            k = j + 1
            while k < len(nr) and not found:
                if(nr[i]+nr[k]+nr[j]) == 2020:
                    return nr[i]*nr[k]*nr[j]
                k += 1
            j += 1
        i += 1
    return 0

if __name__ == '__main__':
    with open("2020\\day1\\input1.txt") as f:
        nr = []
        for line in f:
            nr.append(int(line))
        print(mult2(nr))