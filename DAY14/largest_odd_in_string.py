def get_largest_odd_num(string):
    for i in range(len(string)-1, -1, -1):
        if (int(string[i]) % 2 != 0):
            return string[:i+1]
    return ""

if __name__ == "__main__":
    string = "234567850"
    print(get_largest_odd_num(string))