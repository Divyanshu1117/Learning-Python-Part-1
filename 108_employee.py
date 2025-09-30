class Employee:
    company = "Google"
    salary = 100

divyanshu = Employee()
aman = Employee()

divyanshu.salary = 300
aman.salary = 300

print(divyanshu.company)
print(aman.company)

Employee.company = "YouTube"
print(divyanshu.company)
print(aman.company)

print(divyanshu.salary)
print(aman.salary)