class Employee:
    MIN_SALARY = 30000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.readline()
        return cls(name)


emp1 = Employee.from_file("employee_data.txt")
print(type(emp1))
print(emp1.name, str(emp1.salary))

emp2 = Employee("fernando", 500000)
print(type(emp2))
print(emp2.name, str(emp2.salary))