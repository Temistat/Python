phrase = input("Enter a phrase: ")
separator = ' '
start = 0
new_word = ''

phrase += separator
for i in range(len(phrase)):
    if phrase[i] == separator:
       word = phrase[start:i]
       start = i + 1
       if word[0].isdigit():
          for x in range(len(word)):
              y = word.replace(word[x],"x")
              new_word += y
              print(new_word)
              
           
    
