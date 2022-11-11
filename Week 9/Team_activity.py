import csv
filename = "students.csv"

def main():
    list_stu = read_dict(filename)
    print(list_stu)

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    list_stu = []
    with open(filename, "r") as student_filename:
        readers = csv.reader(student_filename)

        for list_student in readers:
            list_stu.append(list_student)

    return list_stu


main()