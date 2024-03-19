def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Test array
test_unsorted = [2, 4, 3, 20, 10]
test = quick_sort(test_unsorted)
x = 10

# Function call
result = binary_search(test, 0, len(test) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
