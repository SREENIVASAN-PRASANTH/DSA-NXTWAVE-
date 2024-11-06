def add_zeroes_to_end(arr):
    position = 0

    for num in arr:
        if num!= 0:
            arr[position] = num
            position += 1
        
    for j in range(position,len(arr)):
        arr[j] = 0
    
    return arr

if __name__ == "__main__":
    arr = [1,2,0,0,3,4,0,5,6]
    print(add_zeroes_to_end(arr))