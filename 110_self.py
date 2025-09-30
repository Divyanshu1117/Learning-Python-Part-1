class Employee:
    company = "Google"

    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

divyanshu = Employee()
divyanshu.salary = 100000
divyanshu.getSalary()  # Employee.getSalary(divyanshu)