def rotate_k_times(arr,k):
    k = k % 5

    if k == 0:
        return arr
    for i in range(k):
        first_element = arr[0]
        for j in range(1,len(arr)):
            arr[j - 1] = arr[j]
        arr[-1] = first_element
        
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rotate_k_times(arr,2))
