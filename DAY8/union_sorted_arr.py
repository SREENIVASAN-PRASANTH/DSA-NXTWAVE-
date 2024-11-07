def union_sorted_arr(arr1,arr2):
    pt1 = 0
    pt2 = 0

    union_arr = []

    while pt1 < len(arr1) and pt2 < len(arr2):
        if (arr1[pt1] < arr2[pt2]):
            if union_arr == [] or (arr1[pt1] != union_arr[-1]):
                union_arr.append(arr1[pt1])
            pt1 += 1
        
        else:
            if union_arr == [] or (arr2[pt2] != union_arr[-1]):
                union_arr.append(arr2[pt2])
            pt2 += 1

    while pt1 <len(arr1):
        if (arr1[pt1] != union_arr[-1]):
            union_arr.append(arr1[pt1])
        pt1 += 1
    
    while pt2 < len(arr2):
        if (arr2[pt2] != union_arr[-1]):
            union_arr.append(arr2[pt2])
        pt2 += 1
    
    return union_arr
    

if __name__ == "__main__":
    arr1 = [1,2,3,4,4]
    arr2 = [4,5,6,6,7]

    res1 = union_sorted_arr(arr1,arr2)
    print(res1)
