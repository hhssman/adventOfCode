def inc(numbers):
    prev = numbers[0]
    count = 0
    for i in range(1,len(numbers)):
        if prev < numbers[i]:
            count+=1
        prev = numbers[i]
    return count

def slideInc(numbers):
    numberSum = []
    for i in range(0, len(numbers)-2):
        numberSum.append(numbers[i] + numbers[i+1] + numbers[i+2])
    return inc(numberSum)

if __name__ == '__main__':
    with open("day1\\input1.txt") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))
        print(slideInc(numbers))
