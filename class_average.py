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
    elif average >= 80:
        return 'B', 'Passed'
    elif average >= 70:
        return 'C', 'Passed'
    elif average >= 60:
        return 'D', 'Passed'
    else:
        return 'F', 'Failed'
    
# main function
def main():
    # input student name and grade
    name = input('Enter the student\'s name: ')
    
    # input the grades scored in a grade list
    grades = []
    while grade != '':
        grades.append(int(grade))
        grade = input('Enter the student\'s grade: ')
        
    # find the average of the grades
    average = average(grades)
    
    # print the student's name 
    print('The student\'s name is', name)
    
    
    # output the average of the grades
    print('The average of the grades is: ', average)
    
    # find the appropriate letter grade
    # output the letter grade
    # indicate if the student passed or failed
    letter_grade, pass_fail = letter_grade(average)
    print('The letter grade is: ', letter_grade)
    print('The student', pass_fail)