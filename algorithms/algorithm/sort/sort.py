import math

def InsertSort(array):
    """
    Insertion sort algorithm O(n^2)

    Args:
    array: the input array

    Out:
    None(the source array which has been sorted)
    """
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


def Merge(array, start, middle, end):
    """
    Merge operation

    Args:
    start: start idx
    middle: middle idx
    end: end idx

    Out:
    None
    """
    tmp = []
    i = start
    j = middle + 1
    while i <= middle and j <= end:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    if i <= middle:
        tmp.extend(array[i: middle + 1])
    else:
        tmp.extend(array[j: end + 1])
    array[start: end + 1] = tmp[:]


def MergeSort(array, start, end):
    """
    Merge sort algorithm

    Args:
    array: the input array
    start: start idx
    end: end idx

    Out:
    None(the source array which has been sorted)
    """
    if start < end:
        middle = (start + end) // 2
        MergeSort(array, start, middle)
        MergeSort(array, middle + 1, end)
        Merge(array, start, middle, end)


if __name__ == '__main__':
    array = [10, 5, 6, 4, 8]
    MergeSort(array, 0, len(array) - 1)
    print(array)


