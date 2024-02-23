# Define the student's grades
# name = "mr pogi"
# math = 80
# science = 70
# english = 85
#
# # Calculate the student's average grade
# total_grades = math + science + english + python
# num_subjects = 3
# average_grade = total_grades / num_subjects
#
# # Print the student's average grade
# print(f"{name}'s average grade is {average_grade:.2f}")
#
# # Determine if the student has failed the semester
# if average_grade < 75:
#     print("The student has failed the semester.")
# else:
#     print("The student has passed the semester.")

def compute_average():
    # Input for student details
    name = input("Enter student name: ")
    math_grade = float(input("Enter math grade: "))
    science_grade = float(input("Enter science grade: "))
    english_grade = float(input("Enter English grade: "))

    # Calculate average
    average = (math_grade + science_grade + english_grade) / 3

    # Display the average
    print(f"Average for {name}: {average}")

    # Check if the student failed
    if average < 75:
        print(f"{name} failed the semester.")
    else:
        print(f"{name} passed the semester.")

# Call the function to compute average
compute_average()
