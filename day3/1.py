def byteToInt(byte: str):
    nr = 0
    for i in range(0,len(byte)):
        nr += int(byte[i]) * (2**(11-i))
    return nr

def findPower(byte):
    gammaString = ""
    epsiString = ""
    for i in range(0,12):
        zero = 0
        one = 0
        for bit in byte:
            if bit[i] == '0':
                zero += 1
            else:
                one += 1
        if zero > one:
            gammaString = gammaString + '0'
            epsiString = epsiString + '1'
        else:
            gammaString = gammaString + '1'
            epsiString = epsiString + '0'
    print(gammaString)
    gamma = 0
    epsi = 0
    for i in range(0,12):
        gamma += int(gammaString[i]) *(2**(11-i))
        epsi += int(epsiString[i]) * (2**(11-i))
    return byteToInt(gammaString) * byteToInt(epsiString)

def findOxygen(byte, index = 0):
    zero = 0
    one = 0
    zeros = []
    ones = []
    if len(byte) > 1:
        for bit in byte:
            if bit[index] == '0':
                zero += 1
                zeros.append(bit)
            else:
                one += 1
                ones.append(bit)
        if zero > one:
            return findOxygen(zeros, index+1)
        else:
            return findOxygen(ones, index+1)
    else:
        nrString = byte[0]
        nr = 0
        for i in range(0,12):
            nr += int(nrString[i]) * (2**(11-i))
        return nr

def findCO2(byte, index = 0):
    zero = 0
    one = 0
    zeros = []
    ones = []
    if len(byte) > 1:
        for bit in byte:
            if bit[index] == '0':
                zero += 1
                zeros.append(bit)
            else:
                one += 1
                ones.append(bit)
        if one < zero:
            return findCO2(ones, index+1)
        else:
            return findCO2(zeros, index+1)
    else:
        nrString = byte[0]
        nr = 0
        for i in range(0,12):
            nr += int(nrString[i]) * (2**(11-i))
        return nr

if __name__ == '__main__':
    with open("day3\\input.txt") as f:
        byte = []
        for line in f:
            byte.append(line)
        print("PART1: " + str(findPower(byte)))
        print("PART2: " + str(findOxygen(byte)*findCO2(byte)))

        #931 and 3618