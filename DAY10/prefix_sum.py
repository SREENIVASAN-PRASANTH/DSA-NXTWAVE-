def prefix_sum(k,arr):
    res_arr = []
    max_len = 0

    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len,j-i+1)
                res_arr = arr[i:j + 1]
                break
    
    print(max_len)
    print(res_arr)

if __name__ == "__main__":
    k = 15
    arr = [10,5,2,7,1,9]
    prefix_sum(k,arr)