list1 = []
#for i in range(5):
entity1 = input('Input name: ')
list1.append(entity1)
entity2 = input('Input name: ')
index1 = int(input('Where do you want this name? '))
list1.insert((index1-1), entity1)
delete = int(input('Which string do you want to delete? '))
del list1[(delete-1)]

print(list1)