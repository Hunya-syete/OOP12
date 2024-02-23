def cal_tax(gross_salary, tax_rate):
    tax = gross_salary * tax_rate
    return tax

def cal_loans(hourly_loan_rate, hours_worked):
    loans = hourly_loan_rate * hours_worked
    return loans

def cal_insurance(health_insurance_rate):
    insurance = health_insurance_rate
    return insurance

def cal_total_deductions(tax, loans, insurance):
    total_deductions = tax + loans + insurance
    return total_deductions
