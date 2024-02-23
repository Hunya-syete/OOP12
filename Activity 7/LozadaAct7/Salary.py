from GrossSalary import compute_gross_salary
from SalaryDeduction import compute_deductions
from NetSalary import compute_net_salary

name = input("Enter your name: ")
hours_worked = float(input("Enter hours worked: "))
loan = float(input("Enter loan amount: "))
health_insurance = float(input("Enter health insurance amount: "))

tax_rate = 0.12
hourly_rate = 500

gross_salary = compute_gross_salary(hours_worked, hourly_rate)
tax = gross_salary*tax_rate
deductions = compute_deductions(loan, health_insurance, gross_salary, tax_rate)

net_salary = compute_net_salary(gross_salary, deductions)

# Display the results
print("\nSalary Computation Summary")
print("Hour: ",hours_worked)
print("Name:", name)
print("\nGross Salary: Php", gross_salary)
print("\nTax: Php",tax)
print("Loan: Php",loan)
print("Insurance: Php",health_insurance)
print("\nDeductions: Php", deductions)
print("Net Salary: Php", net_salary)
