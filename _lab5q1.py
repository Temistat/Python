user_input = input("Enter your phrase: ")
length = len(user_input)
word = ''

for i in range(length - 1,-1,-1):
    word += user_input[i]
print(word)


