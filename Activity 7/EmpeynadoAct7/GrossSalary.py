hours = int(input("Enter hour/s rendered: "))
rate = 500

def gross(hours, rate):
    return int(hours) * int(rate)

if hours >=1:
    print("Gross Salary: Php " + str(gross(hours, rate)))