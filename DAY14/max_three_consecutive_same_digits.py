def get_max_three_consecutive(string):
    res = ""
    for i in range(len(string) - 2):
        if (string[i] == string[i+1] and string[i] == string[i + 2]):
            res = max(res, string[i:i+ 3])
    
    print(res)

if __name__ == "__main__":
    string = "6777133388"
    get_max_three_consecutive(string)