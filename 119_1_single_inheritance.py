class Employee:
    company = "Google"

    def showDetails(Self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "YouTube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(Self):
        print("This is an Programmer")

e = Employee()
e.showDetails()
# print(e.company)
p = Programmer()
p.showDetails()
print(p.company)