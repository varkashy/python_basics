class Employee:

    emp_count = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def displayMe(self) :
        print("name: %s , salary : %s" % (self.name,self.salary))

    def giveRaise(self, percent):
        self.salary += self.salary * percent

    def displayCount() :
        print(" count : %d" % Employee.emp_count)


    
    
