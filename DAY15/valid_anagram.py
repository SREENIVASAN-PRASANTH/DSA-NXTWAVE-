def check_valid_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False

if __name__ == "__main__":
    str1 = "anagram"
    str2 = "nagaram"

    print(check_valid_anagram(str1, str2))