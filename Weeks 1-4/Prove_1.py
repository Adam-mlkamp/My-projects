import math
from datetime import datetime

current_time_and_date = datetime.now()

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
v = (math.pi*w*w*a*(w*a+2540*d))/10000000000
print(f"The approximate volume is {v:.2f} liters")
New_tires = input(f"Do you want to buy new tires with {w} width {a} aspect and {d} diameter? ")
if New_tires.capitalize() == "Yes" or New_tires.capitalize() == "Sure" or New_tires.capitalize() == "Y":
    number = input("What is your phone number? ")
    with open("volumes.txt", "at") as tire_file:
        print(f"{current_time_and_date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {number}", file=tire_file )
else:
    print("Okay have a great day!")
    with open("volumes.txt", "at") as tire_file:
        print(f"{current_time_and_date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}", file=tire_file )


