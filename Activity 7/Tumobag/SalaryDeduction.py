TAX_RATE = 0.12

def cal_deductions(gross_salary, loan, health_insurance):
    tax = gross_salary * TAX_RATE
    total_deductions = loan + health_insurance + tax
    return total_deductions