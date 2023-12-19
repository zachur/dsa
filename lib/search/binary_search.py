def binarySearch(file_path, target_element):
    with open(file_path, 'r') as file:
        input_list = [int(line.strip()) for line in file]

    left = 0
    right = len(input_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == target_element:
            return mid
        elif input_list[mid] < target_element:
            left = mid + 1
        else:
            right = mid - 1

    return -1
