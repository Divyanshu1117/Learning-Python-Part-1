class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")
        # return super().takebreadth()

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am a Programmer so I am breathing breathing++...")

p = Person()
p.takeBreath()
# print(p.company) # Throws an error

e = Employee()
e.salary = 40000
e.getSalary()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.getSalary()
pr.takeBreath()
print(pr.company)
print(pr.country)