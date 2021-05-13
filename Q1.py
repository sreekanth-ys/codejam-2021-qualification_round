cases = int(input())
for counter in range(cases):
    N = int(input())
    numbers = []
    numbers = list(map(int,input().split()))
    length = len(numbers);

    cost = 0
    for i in range(0, length-1):
        minimum = numbers.index(min(numbers[i:length+1]))
        mini = minimum + 1
        numbers[i:mini] = reversed(numbers[i:mini])
        cost += (minimum - i +1)

    print("Case #%d:"%(counter+1),cost)
