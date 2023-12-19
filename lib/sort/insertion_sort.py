def insertionSort(arr):
    with open(arr, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    return numbers
