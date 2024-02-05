Table = 1

print("Hello, I can provide you a multiplication table for any given number!")
UserInput = int(input("Input your desired number: "))

while Table <= 10:
    print(str(UserInput) + " x " + str(Table) + " = " + str((UserInput * Table)))
    Table += 1
