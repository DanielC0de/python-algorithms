def LinearSearch(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1


def LinearSearch2(list, element):
    for i in enumerate(list):
        if i[1] == element:
            return i[0]
    return None


def BinarySearch(list, val):
    first = 0
    last = len(list)-1
    index = None
    while (first <= last) and (index is None):
        mid = (first+last)//2
        if list[mid] == val:
            index = mid
        else:
            if val < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


my_list = [1, 3, 5, 7, 9]
print("линейный поиск:")
print(LinearSearch(my_list, 3))
print(LinearSearch(my_list, -1))
print("линейный поиск: ")
print(LinearSearch(my_list, 3))
print(LinearSearch(my_list, -1))
print("бинарный поиск:")
print(BinarySearch(my_list, 3))
print(BinarySearch(my_list, -1))
