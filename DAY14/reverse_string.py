def reverse_words(string):
    string = string.split()[::-1]
    print(*string)

if __name__ == "__main__":
    string = "The quick brown fox"
    reverse_words(string)