def linear_search(arr, target):
    # Your code here
    #create a loop that searches arr for target
    for x in range(len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    
    # Your code here
    #find middle point of ordered list
    #compare target to middle value and repeat
    #until middle = target
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
    
        if arr[mid] > target:
            high = mid - 1
    
        elif arr[mid] < target:
            low = mid + 1
    
        else:
            return mid

    return -1  # not found
