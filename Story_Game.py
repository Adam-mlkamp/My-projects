name = input('Enter your name: ')
print('')
personcap = input(f'Hello {name.capitalize()}, Welcome to Buffalo Wild Wings I will be your host Jeffery will you be dining with another person? (YES/NO) ')

person = personcap.lower()
if person == 'yes':
    print('')
    print('Sounds good!')
    print('')
    where = input('Would you like to sit close to the FRONT of the builing or in the BACK? ')
    if where.lower() == 'front':
        print('\nThat sounds good wait here one second and I will be back to get your order.')
        print('')
        what1 = input('A man in dark clothing comes to the front of the Buffalo Wild Wings and sits right next to you.\nHe says "I am here with the Cia will you help me with something?" (YES/NO/MAYBE) ')
        if what1.lower() == 'yes':
            print('')
            print('He pulls out a picture of person in the store and says this is the target he has to eliminate. You look at the picture and realize it is your uncle that has been missing for the pass couple months. You heard he was on the sketchy side of things but did not know he was that bad. \n \nRight then the police come in and have a shoot out with the guy who claims to be a CIA agent. He was a cartel member that was hired to\neliminate your uncle. You wake up and realize it was just a dream that would have been to crazy to be real. \n')

        if what1.lower() == 'no':
            print('')
            print('The man gets up and leaves you never see him again but you wonder what could of happened. Maybe it was better that you did not help him\nbecause your date just came in. Hopefully everything goes as you planned, but it probably will not :(.\n')
        elif what1.lower() == 'maybe':
            print('')
            print('The CIA agent is frustrated with you, because you are indecisive. He marches out of the store saying something about his ex-wife.\nThen you realize Jeffery has been gone for too long and you need some water for your dry mouth. Hopefully he will be back soon.\n')
        else:
            print('Your answer was wrong!!')
    if where.lower() == 'back':
        print('')
        what2 = input('Your friend comes into the restuarant and talks to someone in the front of the restuarant. You wonder if he mixed up who\nhe was talking too with you. After all it has been awhile since you have seen him.\nWill you go to the FRONT to see him or STAY where you are? ')
        if what2.lower() == 'front':
            print('')
            print(f'You go up to the front to talk to your friend and he is confused. He thought he was talking to you already, it turns out someone with the same name as {name.capitalize()} was sitting in the front too. You make an akward situation but it is alright because you really just came to try the\nreally spicy wings.\n')
        if what2.lower() == 'stay':
            print('')
            print(f'You stay there for awhile and realized that the person in the front that you though was your friend is not actually him.\nYou feel relieved, then your friend comes in and yells {name.capitalize()}!!!! He sits down and you have a good time it is always good to see old friends.\n')
        else:
            print('That was the wrong answer!!!')
    else:
        print('That was wrong.')
else:
    print('You entered the wrong answer!!')


if person == "no":
    print('')
    print(f'It is okay to be alone {name.capitalize()} (Jeffery sheds a single tear then contuines walking)')
    print('')
    where2 = input('Okay would you like to sit by the BAR or next to the big TV? ')
    if where2.lower() == 'bar':
        print('')
        drink = input('This crazy looking guy with a mowhawk and tatoos everywhere is the bartender. You are a little scared to have him take your order since the\naccident. You do not look him in the eyes because you are scared it will trigger some kind of reaction from him.\nHe asks you if you want COKE or SPRITE? ')
        if drink.lower() == 'coke':
            print('')
            print('You take a sip of your coke and realize you should not be afraid of mowhawks anymore. You have a great conversation with the bartender and he becomes your new best friend. Great job overcoming your fear.\n\nThanks for playing!')

        if drink.lower() == 'sprite':
            print('')
            print('You take a long sip of your sprite and it tastes a little watery. It tastes more like water than it tastes like sprite you are disapointed and\nstart to cry because you are all alone. You run out of the restuarant and you did not even try the wings.\n\nThanks for playing.')
        else:
            print('Wrong Answer!')
    if where2.lower() == 'tv':
        print('')
        wings = input('You sit down all alone but it is okay because the only reason you are there is for the wings. Jeffery comes by and asks you about what wings\nyou want. You have always gone with the USUAL but he says the SPICY wings are amazing. Which will you pick? ')
        if wings.lower() == 'spicy':
            print('')
            print(f'You eat them then your stomach start to growl but you got it under control. Jeffery gives you an award because you ate them so quickly and you\nwin $500. You did it you made it to the end as a winner. Congratulations {name.capitalize()}!!!\n\nThanks for playing.')

        if wings.lower() == 'usual':
            print('')
            print('You get the usual but it turns out Jeffery mixed up the order and you got the really spicy wings. You were not prepared for that and you start\nto cry because they are so spicy. You wonder if Jeffery did that on purose because you did not take his suggestion. You do not leave a tip\nfor Jeffery. When Jeffery sees no tip he regrets giving you those wings on purpose. You go your separate ways and never talk to\neach other again.\n\nThanks for playing.')
        else:
            print('Do not type that again')
    else:
        print('That was the wrong answer!!!')

else:
    print('Thanks for playing.\nTry again.\n')