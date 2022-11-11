"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
age = input('Please enter your age: ')
print('')
print(f'When you exercise to strengthen your heart, you should') 
print(f'keep your heart rate between {int((220 - int(age))*.65)} and {int((220 - int(age)) * .85)} beats per minute.')
print('')
Heartrate = input('What is your current heart rate? ')
print('')
if int(Heartrate) > int((220 - int(age)) * .85):
    print("Your heart is going super fast, you might want to calm it down!")
elif int(Heartrate) < int((220 - int(age)) *.65):
        print("Pick up the work!")
else:
    print("Great Work, you're in the target range!")