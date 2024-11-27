def get_longest_prefix(strings):
    strings.sort()
    ptr1 = 0
    ptr2 = 0
    first = strings[0]
    last = strings[-1]

    while ptr1 < len(first) and ptr2 < len(last):
        if first[ptr1] != last[ptr2]:
            return first[:ptr1]
        ptr1 += 1
        ptr2 += 1
    return "empty string"

if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]
    print(get_longest_prefix(strings))
