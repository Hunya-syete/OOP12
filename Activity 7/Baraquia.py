#GrossSalary.py module:
 
 
def calculate_gross_salary(hour, rate):
    gross_salary = hour * rate
    return gross_salary
   
 #SalaryDeductions.py module:
 
 
def calculate_deductions(gross_salary, loan, health_insurance, tax):
    deduction = loan + health_insurance + (gross_salary * (tax / 100))
    return deduction
 
 
 #NetSalary.py module:
 
 
def calculate_net_salary(gross_salary, deductions):
    net_salary = gross_salary - deductions
    return net_salary
 
 
 #Salary computation app:
 


# Get inputs
name = input("Enter your name: ")
hour = float(input("Enter the number of hours worked: "))
loan = float(input("Enter the loan amount: "))
health_insurance = float(input("Enter the health insurance amount: "))
tax = 12
rate = 500

# Calculate gross salary
gross_salary = calculate_gross_salary(hour, rate)

# Calculate deductions
deductions = calculate_deductions(gross_salary, loan, health_insurance, tax)

# Calculate net salary
net_salary = calculate_net_salary(gross_salary, deductions)

# Print results
print("Name:", name)
print("Gross Salary: $", gross_salary)
print("Deductions: $", deductions)
print("Net Salary: $", net_salary)
