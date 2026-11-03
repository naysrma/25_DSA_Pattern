
def binarySearch(arr, target):
    left = 0
    right = len(arr) * len(arr[0]) - 1
    n = len(arr[0])  # Number of columns in the 2D array

    while left <= right:
        mid = left + (right - left) // 2
        col = mid % n
        row = mid // n
        if arr[row][col] == target:
            return mid
        elif arr[row][col] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1

arr = [[1,3,5,7],[10,11,16,20],[23,30,39,66]]
target = 66;

print(binarySearch(arr, target))
