
import GrossSalary
import SalaryDeduction

def main():

    name =input("Enter your name:")
    hourly_rate = 500
    hours_worked = int(input("Enter your hours worked:"))
    tax_rate = 0.12
    hourly_loan_rate = int(input("Enter your Loan amount:"))
    health_insurance_rate = int(input("Enter your Insurance:"))


    gross_salary = GrossSalary.cal_gross_salary(hourly_rate, hours_worked)
    tax = SalaryDeduction.cal_tax(gross_salary, tax_rate)
    loans = SalaryDeduction.cal_loans(hourly_loan_rate, hours_worked)
    insurance = SalaryDeduction.cal_insurance(health_insurance_rate)
    total_deductions = SalaryDeduction.cal_total_deductions(tax, loans, insurance)
    net_salary = gross_salary - total_deductions

    # Output results
    print(f"Name: {name}")
    print(f"Hour: {hours_worked}")
    print(f"Gross Salary: Php {gross_salary:,.2f}")
    print(f"Tax: Php {tax:,.2f}")
    print(f"Loan: Php {loans:,.2f}")
    print(f"Insurance: Php {insurance:,.2f}")
    print(f"Total Deductions: Php {total_deductions:,.2f}")
    print(f"Net Salary: Php {net_salary:,.2f}")

if __name__ == "__main__":
    main()