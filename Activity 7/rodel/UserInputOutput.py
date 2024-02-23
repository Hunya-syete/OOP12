import GrossSalary
import SalaryDeduction
import NetSalary

print(" <({}>) Hi, I was programmed to help compute your NetSalary!")
Name = input("What is your name?: ")
Hours = int(input("How many hours do you work per day?: "))
Loan = int(input("How much do you pay for loans?: "))
Insurance = int(input("How much do you pay for insurance?: "))

GrossSalary = GrossSalary.Calc_GrossSalary(Hours)
Tax = SalaryDeduction.Calc_Tax(GrossSalary)
SalaryDeduction = SalaryDeduction.Calc_SalaryDeduction(Tax, Loan, Insurance)
NetSalary = NetSalary.Calc_NetSalary(GrossSalary, SalaryDeduction)

print("")
print(")( ;[•-•];  Okay!, " + str(Name) + " doing " + str(Hours) + " Hour(s) of work per day.")
print("")
print("GrossSalary: Php " + str(GrossSalary))
print("Tax: Php " + str(Tax))
print("Loans: Php " + str(Loan))
print("Insurance: Php " + str(Insurance))
print("")
print("Your TotalDeduction is Php " + str(SalaryDeduction))
print("")
print("Your NetSalary is: Php " + str(NetSalary) + " (<['_']>)")