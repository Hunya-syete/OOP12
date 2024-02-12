from GrossSalary import gross
from GrossSalary import hours
from GrossSalary import rate

tax = (int(gross(hours,rate) * .12))
loan = int(input("Enter Loan Amount: "))
insurance = int(input("Enter Health Insurance Amount: "))



def deduction(tax,loan,insurance):
    return int(tax) + int(loan) + int(insurance)

if deduction(tax,loan,insurance) >= 1:
    print("Tax: Php " + str(tax))
    print("Total deduction: Php " + str(deduction(tax, loan, insurance)))
