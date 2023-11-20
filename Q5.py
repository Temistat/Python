

Semi_days = int(input("Please enter the number of days Semi has worked: "))
Semi_hours = int(input("Please enter the number of hours Semi has worked: "))
Semi_minutes = int(input("Please enter the number of minutes Semi has worked: "))
Ollie_days = int(input("Please enter the number of days Ollie has worked: "))
Ollie_hours = int(input("Please enter the number of hours Ollie has worked: "))
Ollie_minutes = int(input("Please enter the number of minutes Ollie has worked: "))

Semi_days = Semi_days * 1440
Semi_hours = Semi_hours * 60
Semi_minutes = Semi_days + Semi_hours + Semi_minutes

Ollie_days = Ollie_days * 1440
Ollie_hours = Ollie_hours * 60
Ollie_minutes = Ollie_days + Ollie_hours + Ollie_minutes

Minutes = int(Semi_minutes + Ollie_minutes)

Days = Minutes // 1440
Hours = (Minutes % 1440) // 60
Minutes = Minutes - ((Days * 1440) + (Hours * 60))

print("The total time both of them worked together is:", Days, "days", Hours, "hours and", Minutes, "minutes.")
