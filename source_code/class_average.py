"""CHECKLIST"""
# Program to calculate the average of a set of grades
# input student name and grade
# input the grades scored in a grade list
# calculate the average of the grades
# output the average of the grades
# find the appropriate letter grade
# output the letter grade
# indicate if the student passed or failed
# print the student's name and letter grade



# function to calculate the average of the grades
def average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

# function to find the letter grade and indicate if the student passed or failed
def letter_grade(average):
    if average >= 90:
        return 'A', 'Passed'
    elif average >= 80 and average < 90:
        return 'B+', 'Passed'
    elif average >= 70 and average < 80:
        return 'B', 'Passed'
    elif average >= 60 and average < 70:
        return 'C+', 'Passed'
    elif average >= 50 and average < 60:
        return 'C', 'Passed'
    else:
        return 'F', 'Failed'
    
# main function
def main():
    # input student name and grade
    name = input('Enter the student\'s name: ')
      
# new line
    print()
    
# five subjects are entered
    grades = []
    for i in range(4):
        grade = int(input('Enter the grade: '))
        grades.append(grade)

    # calculate the average of the grades
    average_grade = average(grades)
    
    print()    
    # print the student's name 
    print('The student\'s name is: ', name.upper())
    # output the average of the grades
    print('The average of the grades is: ', average_grade)
    # output the letter grade and indicate if the student passed or failed
    alphabet_grade, pass_fail = letter_grade(average_grade)
    print('The letter grade is: ', alphabet_grade)
    print(pass_fail.upper())
    
    
# call the main function
if __name__ == '__main__':
    main()