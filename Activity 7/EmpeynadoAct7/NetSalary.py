from GrossSalary import hours
from GrossSalary import rate
from GrossSalary import gross
from SalaryDeduction import tax
from SalaryDeduction import loan
from SalaryDeduction import insurance
from SalaryDeduction import deduction

salary = gross(hours,rate) - deduction(tax,loan,insurance)

print("Net salary: Php " + str(salary))

