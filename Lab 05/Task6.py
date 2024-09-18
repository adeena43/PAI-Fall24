from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
       
    @abstractmethod
    def calculateBonus(self):
        pass
    
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculateBonus(self):
        self.salary += self.salary * 0.2
        print(f"Salary with bonus of Manager is {self.salary}")
    
    def hire(self):
        print('manager is hiring someone')
        
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculateBonus(self):
        self.salary += self.salary * 0.1
        print(f"Salary with bonus of Developer is {self.salary}")
    
    def writeCode(self):
        print('developer is writing code')
        
class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculateBonus(self):
        self.salary += self.salary * 0.3
        print(f"Salary with bonus of Senior Manager is {self.salary}")

m = Manager('Raghib',1000)
d = Developer('Rizwan',1000)
s = SeniorManager('Rabani',1000)

m.calculateBonus()
m.hire()
d.calculateBonus()
d.writeCode()
s.calculateBonus()
