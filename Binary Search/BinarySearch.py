
def binarySearch(arr,target):
    left = 0
    right = len(arr) - 1

    while(left <= right):

        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1

arr = [-1,0,5,9,2]
target = 9
print(binarySearch(arr, 9))