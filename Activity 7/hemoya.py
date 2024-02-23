calculate_salary(hourly_rate, hours_worked):
    """
    Calculate an employee's salary based on their hourly rate and hours worked.

    :param hourly_rate: The employee's hourly rate.
    :param hours_worked: The number of hours the employee worked.
    :return: The employee's salary.
    """
    # Calculate the employee's gross pay
    gross_pay = ("hourly_rate * hours_worked")

    # Calculate the employee's federal income tax withholding
    federal_income_tax = gross_pay * 0.2

    # Calculate the employee's state income tax withholding
    state_income_tax = gross_pay * 0.05

    # Calculate the employee's social security tax withholding
    social_security_tax = gross_pay * 0.062

    # Calculate the employee's Medicare tax withholding
    medicare_tax = gross_pay * 0.0145

    # Calculate the employee's total deductions
    total_deductions = federal_income_tax + state_income_tax + social_security_tax + medicare_tax

    # Calculate the employee's net pay
    net_pay = gross_pay - total_deductions

    # Return the employee's salary
    return {}
        "employee_name": "Jay Sever",
        "job_title": "Python Developer",
        "gross_pay": gross_pay,
        "deductions": {
            "federal_income_tax": federal_income_tax,
            "state_income_tax": state_income_tax,
            "social_security_tax": social_security_tax,
            "medicare_tax": medicare_tax,
            "total": total_deductions
        },
        "net_pay": net_pay
    }

# Example usage
salary = calculate_salary(25, 40)
print(salary)
