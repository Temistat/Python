base = float(input("Please enter a positive integer to serve as the base: "))
highest_power = float(input("Please enter a positive integer to serve as the highest power: "))

base_check = base % 1
highest_power_check = highest_power % 1

if (base_check == 0 and highest_power_check == 0) and (base > 0 and highest_power > 0):
 highest_power =  int(highest_power)   
 for n in range(highest_power+1):
  answer = base ** n
  print(base, "^", n, "=", answer)
else:  
 print("ERROR: Both values must be POSITIVE INTEGERS.")  
