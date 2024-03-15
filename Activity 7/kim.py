def compute_tax(gross_salary):
   return gross_salary * 5000.00

def compute_total_deductions(gross_salary, loan, insurance):
    return compute_tax(gross_salary) + loan + insurance
