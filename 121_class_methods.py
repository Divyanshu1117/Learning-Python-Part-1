class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, salary1):
    #     # self.salary = salary1
    #     self.__class__.salary = salary1

    @classmethod
    def changeSalary(cls, salary1):
        cls.salary = salary1

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)