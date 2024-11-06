def rotate_array(arr):
    first_element = arr[0]
    for i in range(1,len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first_element
    return arr

def rotate_array_using_slicing(arr):
    first_half = arr[1:]
    second_half = [arr[0]]
    return first_half + second_half

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rotate_array(arr))
    print(rotate_array_using_slicing(arr))

