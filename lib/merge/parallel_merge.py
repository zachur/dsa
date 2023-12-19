def mergeSortedLists(lists):
    def mergeTwoLists(list1, list2):
        result = []
        i = j = 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])
        return result

    def mergeListsParallel(lists):
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            left_half = lists[:mid]
            right_half = lists[mid:]

            left_result = mergeListsParallel(left_half)
            right_result = mergeListsParallel(right_half)

            return mergeTwoLists(left_result, right_result)

    if not lists:
        return []

    return mergeListsParallel(lists)
