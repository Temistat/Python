price_of_item_1 = float(input("Price of Item 1: "))
price_of_item_2 = float(input("Price of Item 2: "))
club_card_member = input("Club Card Member (Y/N): ")
tax_rate = float(input("Tax: "))

if  price_of_item_1 < price_of_item_2:
    price_of_item_1 = price_of_item_1 / 2

else:
    price_of_item_2 / 2    

total_price_of_items = price_of_item_1 + price_of_item_2

if  club_card_member == "Y":
    club_card_member = total_price_of_items * (10 / 100)
    total_price_of_items = total_price_of_items - club_card_member
   
tax_rate = total_price_of_items * (tax_rate / 100)
total_price_of_items = round((total_price_of_items + tax_rate), 2)
total_price_of_items = str(total_price_of_items)
print("Total Price: $" + total_price_of_items)
   

