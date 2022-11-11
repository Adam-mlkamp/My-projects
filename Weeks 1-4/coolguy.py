print("Hey you're pretty cute!")
date = input("Do you want to go on a date? ")
if date.capitalize() == "Yes":
    print("Awesome!")
    time = input("What day are you free? ")
    print(f"Sweet I'll pick you up {time.capitalize()} at 8:00 pm! can't wait to see you then!")
else:
    print("I didn't want to go on the date anyways so its cool.")