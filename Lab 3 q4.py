first_number = float(input("Enter your first number: "))
operation = input("Enter the operation (+, -, *, /): ")
second_number = float(input("Enter your second number: "))

if first_number == 0 or second_number == 0 and operation == "/":
   print(first_number, operation, second_number, "is an invalid operation.")
elif operation == "+":
   answer = first_number + second_number
   print(first_number, operation, second_number, "=", answer)
elif operation == "-":
   answer = first_number - second_number
   print(first_number, operation, second_number, "=", answer)
elif operation == "*":
   answer = first_number * second_number
   print(first_number, operation, second_number, "=", answer)
else:
   answer = first_number / second_number
   print(first_number, operation, second_number, "=", answer)      
