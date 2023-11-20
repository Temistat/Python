current_max = -1

value = int(input("How many: "))

for x in range(value):
 entry = float(input())
 if entry > current_max:
  current_max = entry

print("The largest of these values is:", current_max)  
 
