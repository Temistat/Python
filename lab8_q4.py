def encoder(word):
    num = 1
    count = 0
    for i in range(len(word)):
        if word[i] == word[i + num]:
           lettter = i 
           count += 1 
