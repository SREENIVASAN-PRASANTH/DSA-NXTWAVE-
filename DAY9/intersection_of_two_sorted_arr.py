def get_intersection2(arr1,arr2): #two_pointer approach
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        elif(arr1[i] < arr2[j]):
            i += 1
        else:
            j += 1
    print(*res)

def get_intersection(arr1,arr2):#brute force
    res = []
    for i in arr1:
        if i in arr2:
            res.append(i)
            arr2.remove(i)
    print(*res)

if __name__ == "__main__":
    arr1 = [1,1,2,3,4,4]
    arr2 = [1,2,3,4,4]
    get_intersection2(arr1,arr2)