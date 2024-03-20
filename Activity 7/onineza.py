from NetSalary import cal_net_salary
from SalaryDeduction import tax, rate, TotalDeductions

name = input("Enter your full Name: ")
hour = int(input("How Many Hours of Work Per Day: "))
gross = rate(hour)

print()
print("Gross Salary:", gross)

print()
print("Tax:", tax(gross))
loan = float(input("Loan: "))
insurance = float(input("Insurance: "))
deductions = TotalDeductions(tax(gross), insurance, loan)
print()

print("Total Deduction: ", deductions)
print()
print("Net Salary: ", cal_net_salary(gross, deductions))