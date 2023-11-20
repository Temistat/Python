def decode_caesar(encoded_message,key):
    word = ''
    for i in encoded_message:
        number = 0
        if 97 <= ord(i) <= 122:
           number = ord(i) - ord('a') - key
           number %= 26
           number += ord('a') 
           word += chr(number)
        elif 65 <= ord(i) <= 90:
           number = ord(i) - ord('A') - key
           number %= 26
           number += ord('A') 
           word += chr(number)
        else:
            word += i
    return(word)

def main():
    """
    Just some sample behavior
    """
    decryption_key = 3
    line = input("Enter the encoded line: ")
    decrytion = decode_caesar(line,decryption_key)
    print(decrytion)

main()


