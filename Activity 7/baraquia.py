class GrossSalary(object):
    pass


GrossSalary.py


def compute_gross(hour, rate=500):
     return hour * rate

class SalaryDeductions(object):
    pass


SalaryDeductions.py


def compute_deductions(loan, health_insurance, tax_rate, gross_salary):
    tax = tax_rate * gross_salary
    return loan + health_insurance + tax


class NetSalary(object):
    pass


NetSalary.py

class GrossSalary (object): ("{gross_salary}")
class SalaryDeductions(object): ("SalaryDeductions")


def compute_net(name, hour, loan, health_insurance, tax_rate=0.12):
    gross_salary = compute_gross(hour)
    deductions = compute_deductions(loan, health_insurance, tax_rate, gross_salary)
    net_salary = gross_salary - deductions

    print(f"Employee: {name}")
    print(f"Gross Salary: {gross_salary}")
    print(f"Deductions: {deductions}")
    print(f"Net Salary: {net_salary}")


name = input("Enter Name: ")
hour = int(input("Enter Hours Worked: "))
loan = float(input("Enter Loan: "))
health_insurance = float(input("Enter Health Insurance: "))

compute_net(name, hour, loan, health_insurance)

