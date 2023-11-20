phrase = input("Enter a phrase: ")
length = len(phrase)
right = 0
word = ''

for x in range(length - 1, -1, -1):
    word += phrase[x]
if word == phrase:
   print(phrase, "is a sentence length palindrome")
else:
    print(phrase, "is NOT a sentence length palindrome")
 




