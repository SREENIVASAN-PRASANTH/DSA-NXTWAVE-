def get_single_digit(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if(arr[i] == arr[j]):
                count += 1
        
        if (count == 1):
            print(i)
            break

if __name__ == "__main__":
    arr = [1,1,2,3,3]
    get_single_digit(arr)
    

