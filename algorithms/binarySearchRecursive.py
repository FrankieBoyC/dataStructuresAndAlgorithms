def binary_search_recursive(arr, low, high, item):
    if low <= high:
        middle = (low + high) // 2
        # Base Case
        if arr[middle] == item:
            return middle
        # Recursive Case
        elif item < arr[middle]:
            binary_search_recursive(arr, low, middle - 1, item)
        elif item > arr[middle]:
            binary_search_recursive(arr, middle + 1, high, item)
        else:
            return -1
