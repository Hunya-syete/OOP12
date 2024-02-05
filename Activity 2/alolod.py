
name = input("Enter your name: ")
Math = int(input("Math: "))
Science = int(input("Science: "))
English = int(input("English: "))
Average = int(Math + Science + English)/3
print(Average)

if Math < 75 <= Average <= Science and English >= 75:
    print("Congratulations! You passed the semester. But you need  to re-enroll Math Subject")

if Math >= 75 > Science and Average >= 75 and English >= 75:
    print("Congratulations! You passed the semester. But you need  to re-enroll Science Subject")

if Math >= 75 and Average >= 75 and Science >= 75 and English < 75:
    print("Congratulations! You passed the semester. But you need  to re-enroll English Subject")

if Math >= 75 and Average >= 75 and English >= 75 and Science >= 75:
    print("Congratulations! You passed the semester.")

if Math < 75 and Average < 75 and English <= 75 and Science < 75:
    print("you have failed the semester")




