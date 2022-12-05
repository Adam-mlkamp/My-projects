import csv
from datetime import datetime

current_date_and_time = datetime.now()

def main():
    print("Inkom Emporium")
    print()
    request_dict = read_request(0)
    product_dict = Read_products(0)

    Subtotal = 0
    Item_total = 0

    for i in request_dict:
       info = request_dict[i]
       quantity = info[1]
       info2 = product_dict[i]
       item = info2[1]
       price = info2[2]
       print(f"{item}: {quantity} @ ${price}")
       total_price = int(quantity) * float(price)
       Subtotal = total_price + Subtotal
       Item_total = int(quantity) + Item_total
    print()
    sales_tax = Subtotal * .06
    print(f"Number of Items: {Item_total}")
    print(f"Subtotal: ${Subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${Subtotal + sales_tax:.2f}")
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%A %I:%M %p}")


def Read_products(key_column_index):
    dictionary = {}
    with open("products.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]            
            dictionary[key] = row_list

    return dictionary

def read_request(key_column_index):
    dictionary = {}
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]            
            dictionary[key] = row_list

    return dictionary
try:
    main()
except
    