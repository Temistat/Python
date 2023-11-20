Pi = 3.1416
Number_of_ice_cream_scoops = int(input("What is the number of the ice cream scoops: "))
print(Number_of_ice_cream_scoops)
Radius = float(input("What is the radius of the ice cream cone: "))
print(Radius)
Height =float(input("What is the height of the ice cream cone: "))
print(Height)


Volume_of_scoops = ((4 * Pi * (Radius**3)) / 3) * Number_of_ice_cream_scoops
Volume_of_ice_cream_scoops = (Pi * (Radius**2) * Height) / 3
Total_volume = Volume_of_scoops + Volume_of_ice_cream_scoops 

print('Your' , Number_of_ice_cream_scoops, 'scoop ice cream cone has a total volume of' , Total_volume)





                                   
