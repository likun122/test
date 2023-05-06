class Employee(object):
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
    try:
        def printclass(self):
            print(f"'{self.name}‘s salary is {self.salary}, and his age is {self.age}'")
    except:
        print("Error! No age")
name = input()
salary = input()
age = input()
Employee(name,salary,age)