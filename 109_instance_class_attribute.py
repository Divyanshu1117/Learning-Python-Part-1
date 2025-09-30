class Employee:
    company = "Google"
    salary = 100

divyanshu = Employee()
aman = Employee()

# Creating Instance Attribute Salary For Both The Objects
# divyanshu.salary = 400
# aman.salary = 300

divyanshu.salary = 500

print(divyanshu.salary)
print(aman.salary)
# print(aman.address) # Throws an error as address is not present in instance/class.