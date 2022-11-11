
print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you tenstatements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the statements by responding with one of these four letters:")
print("")
print('D means you strongly disagree with the statement.')
print('c means you disagree with the statement.')
print('b means you agree with the statement.')
print('A means you strongly agree with the statement.')
print("")
score = 0
print("1. I feel that I am a person of worth, at least on an\n equal plane with others.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 0
elif worth == "d":
    score = score + 1
elif worth == "a":
   score = score + 2 
elif worth == "A":
    score = score + 3
else:
    print("That is not a valid answer!")

print("2. I feel that I have a number of good qualities.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 0
elif worth == "d":
    score = score + 1
elif worth == "a":
   score = score + 2 
elif worth == "A":
    score = score + 3
else:
    print("That is not a valid answer!")

print("3. All in all, I am inclined to feel that I am a failure.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 3
elif worth == "d":
    score = score + 2
elif worth == "a":
   score = score + 1
elif worth == "A":
    score = score + 0
else:
    print("That is not a valid answer!")
print("4. I am able to do things as well as most other people.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 0
elif worth == "d":
    score = score + 1
elif worth == "a":
   score = score + 2 
elif worth == "A":
    score = score + 3
else:
    print("That is not a valid answer!")

print("5. I feel I do not have much to be proud of.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 3
elif worth == "d":
    score = score + 2
elif worth == "a":
   score = score + 1
elif worth == "A":
    score = score + 0
else:
    print("That is not a valid answer!")

print("6. I take a positive attitude toward myself.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 0
elif worth == "d":
    score = score + 1
elif worth == "a":
   score = score + 2 
elif worth == "A":
    score = score + 3
else:
    print("That is not a valid answer!")

print("7. On the whole, I am satisfied with myself.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 0
elif worth == "d":
    score = score + 1
elif worth == "a":
   score = score + 2 
elif worth == "A":
    score = score + 3
else:
    print("That is not a valid answer!")

print("8. I wish I could have more respect for myself.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 3
elif worth == "d":
    score = score + 2
elif worth == "a":
   score = score + 1
elif worth == "A":
    score = score + 0
else:
    print("That is not a valid answer!")

print("9. I certainly feel useless at times.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 3
elif worth == "d":
    score = score + 2
elif worth == "a":
   score = score + 1
elif worth == "A":
    score = score + 0
else:
    print("That is not a valid answer!")

print("10. At times I think I am no good at all.")
worth = input('    Enter D, d, a, or A: ')
if worth == "D":
     score = score + 3
elif worth == "d":
    score = score + 2
elif worth == "a":
   score = score + 1
elif worth == "A":
    score = score + 0
else:
    print("That is not a valid answer!")

print(f"Your score is {score}.")
print("A score below 15 may indicate problematic low self-esteem.")

