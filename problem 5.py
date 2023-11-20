Num = int(input("Enter an interger less than 100: "))
          
String_L = "L" * (Num // 50)
String_X = "X" * ((Num % 50) // 10)
String_V = "V" * ((Num % 10) // 5)
String_I = "I" * ((Num % 5) // 1)

print(Num, 'in Roman numerals is', String_L, String_X, String_V, String_I)
