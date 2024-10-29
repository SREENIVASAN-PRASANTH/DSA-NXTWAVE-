def generate_matrix(key):
    matrix = []
    seen = set()
    key = key.upper().replace("J","I")
    
    for char in key:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
            
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    return [matrix[i:i + 5] for i in range(0,25,5)]

def find_position(matrix,char):
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j] == char:
                return i,j
    return None

def encrypt_digraph(matrix,a,b):
    row1, col1 = find_position(matrix,a)
    row2, col2 = find_position(matrix,b)
    
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2+ 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
        
def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J","I")
    prepared = ""
    
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
        
    if len(prepared) % 2 != 0:
        prepared += 'X'
    
    return prepared

def playfair_cipher(plaintext,key):
    matrix = generate_matrix(key)
    prepared_text = prepare_text(plaintext)
    cipher_text = ""
    
    for i in range(0,len(prepared_text), 2):
        a,b = prepared_text[i] + prepared_text[i + 1]
        cipher_text += encrypt_digraph(matrix,a,b)
    
    return cipher_text

if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = input("Enter the plaintext: ")
    cipher_text = playfair_cipher(plaintext,key)
    print(cipher_text)
    
    