Number_of_days = int(input("How many days do you have? "))
print(Number_of_days)
Number_of_hours = int(input("How many hours do you have? "))
print(Number_of_hours)
Number_of_minutes = int(input("How many minutes do you have? "))
print(Number_of_minutes)
Number_of_seconds = int(input("How many seconds do you have? "))
print(Number_of_seconds)

Seconds_in_days = int(Number_of_days * 864s00)
Seconds_in_hours = int(Number_of_hours * 3600)
Seconds_in_minutes = int(Number_of_minutes * 60)
Total = Seconds_in_days + Seconds_in_hours + Seconds_in_minutes + Number_of_seconds

print(Number_of_days, 'Days' , Number_of_hours, 'Hours', Number_of_minutes, 'Minutes', Number_of_seconds, 'Seconds results in a total of', Total, 'Seconds')  

