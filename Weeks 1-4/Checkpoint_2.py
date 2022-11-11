import math
items = input("Enter the number of items: ")
boxes = input("Enter the number of items per box: ")
print(f"For {items} items, packing {boxes} items in each box, you will need {math.ceil(int(items)/int(boxes))} boxes.")