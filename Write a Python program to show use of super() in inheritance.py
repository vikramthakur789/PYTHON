class employee:
    def __init__(self, role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role =", self.role) 
        print("dept =", self.dept)
        print("salary =", self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(). __init__("emginer","IT","800000")

engg1 = engineer('vikram thakur',21)
engg1.showdetails()
