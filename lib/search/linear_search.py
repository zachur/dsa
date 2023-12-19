def linearSearch(file_path, target_element):
    with open(file_path, 'r') as file:
        input_list = [int(line.strip()) for line in file]
    
    for index, element in enumerate(input_list):
        if element == target_element:
            return index
    return -1
