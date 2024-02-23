def compute_deductions(loan, health_insurance,gross_salary, tax_rate):
    tax_deduction = gross_salary *tax_rate
    total_deductions =  tax_deduction + loan + health_insurance
    return total_deductions