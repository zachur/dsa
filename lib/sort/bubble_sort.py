def bubbleSort(arr):
    with open(arr, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return numbers
