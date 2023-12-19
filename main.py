from lib import *

def exampleUsage_01():
    sorted_lists = [
        [12, 41, 73],
        [27, 54, 83],
        [90, 32, 68],
    ]
    list_file = mergeSortedLists(sorted_lists)
    """
    print("Parallel Merge List:", list_file)
    file_path = "./dataset/example_list.txt"
    with open(file_path, "w") as file:
        for item in list_file:
            file.write(str(item) + "\n")
    """

def exampleUsage_02():
    target_element = 290000
    result = linearSearch(list_file, target_element)
    if result != -1:
        print(f"Linear Search Result: Element {target_element} found at index {result}.")
    else:
        print(f"Linear Search Result: Element {target_element} not found in the list.")

def exampleUsage_03():
    target_element = 112000
    result = binarySearch(list_file, target_element)
    if result != -1:
        print(f"Binary Search Result: Element {target_element} found at index {result}.")
    else:
        print(f"Binary Search Result: Element {target_element} not found in the list.")

def exampleUsage_04():
    bubble_sorted_list = bubbleSort(list_file)
    # print("Bubble Sort List:", bubble_sorted_list)

def exampleUsage_05():
    insertion_sorted_list = insertionSort(list_file)
    # print("Insertion Sort List:", insertion_sorted_list)

def exampleUsage_06():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    quickSort(numbers)
    # print("Quick Sort List:", numbers)

def exampleUsage_07():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    merge_sorted_list = mergeSort(numbers)
    # print("Merge Sort List:", merge_sorted_list)

def exampleUsage_08():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    selectionSort(numbers)
    # print("Selection Sort List:", numbers)

def exampleUsage_09():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    heapSort(numbers)
    # print("Heap Sort List:", numbers)

def exampleUsage_10():
    list1 = [13, 71, 39]
    list2 = [42, 54, 85]
    merged_list = iterativeMerge(list1, list2)
    # print("Iterative Merge List:", merged_list)

def exampleUsage_11():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    
    for node, distance in distances.items():
        print(f'Shortest distance from {start_node} to {node}: {distance}')

if __name__ == "__main__":
    logMessage("START")
    list_file = './dataset/output.txt'
    exampleUsage_01()
    exampleUsage_02()
    exampleUsage_03()
    exampleUsage_04()
    exampleUsage_05()
    exampleUsage_06()
    exampleUsage_07()
    exampleUsage_08()
    exampleUsage_09()
    exampleUsage_10()
    exampleUsage_11()
    logMessage("STOP")