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
    d2 = (f"{current_date_and_time:%a}")

    if d2 == "Tue" or d2 == "Wed":
        discount = .9
    else:
        discount = 1

    for i in request_dict:
       info = i[0]
       quantity = i[1]
       info2 = product_dict[info]
       item = info2[1]
       price = (float(info2[2]) * discount)
       print(f"{item}: {quantity} @ ${price:.2f}")
       total_price = int(quantity) * float(price)
       Subtotal = total_price + Subtotal
       Item_total = int(quantity) + Item_total
    print()
    sales_tax = Subtotal * .06
    if d2 == "Tue" or d2 == "Wed":
        print(f"You received a discount because today is {current_date_and_time:%A}!")
        print(f"Discount amount was ${(Subtotal/discount)-Subtotal:.2f}")
        print()
    else:
        pass
    print(f"Number of Items: {Item_total}")
    print(f"Subtotal: ${Subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${Subtotal + sales_tax:.2f}")
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%a %b  %d %I:%M:%S %Y}")


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
    dictionary = []
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader: 
            if row_list == []:
                return dictionary
            else:        
                dictionary.append(row_list)  
    return dictionary
try:
    main()
except FileNotFoundError as not_found_err:
    print()
    print(f"Error: missing file")
    print( not_found_err, sep=": ")
except PermissionError as perm_err:
        print()
        print(f"Error: you do not have permission to access this file")
        print(perm_err, sep=": ")
except KeyError as key_err:
    print()
    print('Error: unknown product ID in the request.csv file',key_err)


