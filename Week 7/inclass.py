student2 = {
    "age": 30,
    "name": 'fred',
    "phone number": "720-678-8008"
}

student3 = {
    "age": 20,
    "name": 'Max',
    "phone number": "358-678-8108"
}

print('the name of the student is ' + student2['name'])

student_list = [student2,student3]

print(student_list)

i=0
while(i<len(student_list)):
    print(student_list[i])
    i+= 1

total_age = 0
for student in student_list:
    total_age += student['age']

average_age = total_age/len(student_list)
print(average_age)

student_names =["Joel",'Jed','Sandy']

for student_name in student_names:
    print(student_name)

for i in range(5):
    student_names.append('emily')

print(student_names)