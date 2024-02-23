from GrossSalary import cal_gross_salary
from SalaryDeduction import cal_deductions
from NetSalary import cal_net_salary

# User input
name = input("Enter your name: ")
hourly_rate = 500
hours_worked = float(input("Enter hours work: "))
loan = float(input("Enter loan amount: "))
health_insurance = float(input("Enter health insurance: "))

# Calculations
gross_salary = cal_gross_salary(hourly_rate, hours_worked)
total_deductions = cal_deductions(gross_salary, loan, health_insurance)
net_salary = cal_net_salary(gross_salary, total_deductions)

# Display results
print("\nSalary Details:")
print(f"Name: {name}")
print(f"Gross Salary: ${gross_salary}")
print(f"Total Deductions: ${total_deductions}")
print(f"Net Salary: ${net_salary}")