def get_max_consecutive_one(arr):
    max_count = 0
    count = 0
    for i in arr:
        if i == 0:
            if (count > max_count):
                max_count = count
            count = 0
        else:
            count += 1
    if count > max_count:
        max_count = count
    print(max_count)

if __name__ == "__main__":
    arr = [0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1]
    get_max_consecutive_one(arr)