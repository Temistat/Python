"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW6 - Q2 
Date due: 2022-03-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_decimal_time(hour, minute, second):
    number = (hour * 3600) + (minute * 60) + second
    hour = number // 10000
    minute = (number % 10000) // 100
    second = (number % 100) 
    line = "{}:{}:{}".format(hour,minute,second)
    return line

def get_decimal_date(month, date, year):
    if month == 1:
       month = 'Nivôse'
    elif month == 2:
       month = 'Pluviôse'
    elif month == 3:
       month = 'Ventôse'
    elif month == 4:
       month = 'Germinal '  
    elif month == 5:
       month = 'Floréal'
    elif month == 6:
       month = 'Prairial'
    elif month == 7:
       month = 'Messidor'
    elif month == 8:
       month = 'Thermidor'
    elif month == 9:
       month = 'Fructidor'
    elif month == 10:
       month = 'Vendémiaire'
    elif month == 11:
       month = 'Brumaire'
    elif month == 12:
       month = 'Frimaire'
    year -= 1792
    decade = (year // 100) + 1
    line = "{} {} Year {}, Decade {}".format(date,month,year,decade)
    return line

def get_french_datetime(gregorian_datetime):
    space = gregorian_datetime.find(" ")
    time = gregorian_datetime[:space]
    date = gregorian_datetime[space + 1:]
    colon = time.find(":")
    remaining_time = time[colon + 1:]
    hour = int(time[:colon])
    minute = int(remaining_time[:colon])
    second = int(remaining_time[colon + 1:])              
    slash = date.find("/")
    remaining_date = date[slash + 1:]           
    month = int(date[:slash])
    date = int(remaining_date[:slash])
    year = int(remaining_date[slash + 1:])
    decimal_time = get_decimal_time(hour, minute, second)
    decimal_date = get_decimal_date(month, date, year)
    print(decimal_time)
    print(decimal_date)
    
def main():
    gregorian_datetime = input("Enter gregorian_datetime: ")
    french_datetime = get_french_datetime(gregorian_datetime)
    
main()

