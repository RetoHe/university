def binary_search(list, value):
    first = 0
    last = len(list) - 1
    found = False
    idx = -1

    while (first <= last and not found):
        mid = (first + last) // 2
        if list[mid] == value:
            found = True
            idx = mid
        else:
            if value < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return idx

list = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print(binary_search(list, 6))
print(binary_search(list, 5))
