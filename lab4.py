##This is a four operation calculator

quit_option = input("Hit enter to continue and Q to quit calculator: ")
first_number = float(input("Enter your first number: "))
operation = input("Enter the operation (+, -, *, /): ")
second_number = float(input("Enter your second number: "))

while quit_option == Q
       print("Goodbye")
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

