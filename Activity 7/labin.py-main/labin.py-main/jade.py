# imports
import GrossSalary
import SalaryDeduction
import NetSalary

# introduction
print(" Hello, User Im your assistant for today's Video XD")

# inputs
Name = input("Dear User. what is your name?: ")

Hours = int(input("how many hours do Grind in your work per day?: "))

Insurance = int(input("How much do you pay for Insurance User?: "))

Loan = int(input("How much do you pay for Loan?: "))

# Calc
GrossSalary = GrossSalary.Calc_GrossSalary (Hours)
Tax = SalaryDeduction.Calc_Tax (GrossSalary)
SalaryDeduction = SalaryDeduction.Calc_SalaryDeduction (Tax, Loan, Insurance)
NetSalary = NetSalary.Calc_NetSalary (GrossSalary, SalaryDeduction)

print("")
print(" Okay User, " + str(Name) + " doing " + str(Hours) + " Hour(s) of Grind per day.")
print("")
print("GrossSalary: Php " + str(GrossSalary))
print("Tax: Php " + str(Tax))
print("Loans: Php " + str(Loan))
print("Insurance: Php " + str(Insurance))
print("")
print("Your TotalDeduction is Php " + str(SalaryDeduction))
print("")
print("Your NetSalary is: Php " + str(NetSalary) + " XD ")