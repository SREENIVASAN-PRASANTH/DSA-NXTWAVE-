def find_missing(arr,n):    #brute force approach
    for i in range(1,n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break
        
        if found == False:
            return i

def find_missing2(arr,n):   #optimized approach
    total_sum = (n*(n+1))//2
    arr_sum = 0
    for i in arr:
        arr_sum += i
    
    missing_num = total_sum - arr_sum
    return missing_num


if __name__ == "__main__":
    N = 5
    arr = [1,2,3,4]
    missing_num = find_missing2(arr,N)
    print(missing_num)