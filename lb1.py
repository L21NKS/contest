def sh(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1
        
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == x:
        while mid > 0 and arr[mid-1] == x:
            mid -= 1
        return mid
    elif arr[mid] < x:
        return sh(arr, x, mid + 1, high)
    else:
        return sh(arr, x, low, mid - 1)
    
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    while True:
        try:
            line = input().split()
            if line[0] == "search":
                x = int(line[1])
                result = sh(arr, x)
                print(result)
        except EOFError:
            break