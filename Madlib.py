print ('                   Please Enter the Following\n')
adjective = input('Adjective: ')
animal = input('Animal: ')
verb1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('Verb: ')
fruit = input('Fruit: ')
print('')
print('                         Your story is: \n')
firstletter = fruit[0]
if (firstletter == 'a' or firstletter == 'A' or firstletter == 'e' or firstletter == 'E' or firstletter == 'i' or firstletter == 'I' or firstletter == 'o' or firstletter == 'O' or firstletter == 'u' or firstletter == 'U'):
    print (f'The other day, I was really in trouble. It all started when I saw a very\n{adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclamation.lower()}!" I yelled. But all \nI could think to do was to {verb2.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3.lower()}\nright in front of my family. Then an {fruit.lower()} fell and hit the {animal.lower()}.\nThat {animal.lower()} then got scared and ran away')
else:
    print (f'The other day, I was really in trouble. It all started when I saw a very\n{adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclamation.lower()}!" I yelled. But all \nI could think to do was to {verb2.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3.lower()}\nright in front of my family. Then a {fruit.lower()} fell and hit the {animal.lower()}.\nThat {animal.lower()} then got embarressed and ran away')
