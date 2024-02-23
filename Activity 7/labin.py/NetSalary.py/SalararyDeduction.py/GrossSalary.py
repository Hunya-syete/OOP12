def Calc_Tax(GrossSalary: int):
    return 0.12 * GrossSalary

def Calc_SalaryDeduction(Tax: int, Loan: int, Insurance: int):
    return Tax + Loan + Insurance
