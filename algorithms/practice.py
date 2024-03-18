def binarySearch(arr, low, high, item):
    if low <= high:
        middle = (low + high) // 2
        if arr[middle] == item:
            return middle
        elif item < arr[middle]:
            binarySearch(arr, low, middle - 1, item)
        elif item > arr[middle]:
            binarySearch(arr, middle + 1, high, item)
        else:
            return -1
        return arr[middle]


testing = [1, 3, 2, 4, 5, 10, 7]
testing.sort()

binarySearch(testing, 0, len(testing) - 1, 3)
