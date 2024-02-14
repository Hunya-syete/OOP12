from NetSalary import net
from SalaryDeductions import tax, rate, TotalDeductions

name = input("Enter your Name: ")
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
print("Net Salary: ", net(gross, deductions))

