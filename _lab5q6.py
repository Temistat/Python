phrase = input("Enter a phrase: ")
separator = ' '
start = 0
words = 0

phrase += separator
for i in range(len(phrase)):
    if phrase[i] == separator:
       word = phrase[start:i]
       start = i + 1
       word += 1
if word % 2 == 0:
    
