class Employee:
    def getData(self):
        self.name = input("Enter the name of the employee: ")
        self.salary = int(input("ENter your monthly salary:"))
        self.tax_perc = int(input("Enter the tax percentage you want to deduct: "))

    def Salary_after_tax(self):
        self.salary -= self.salary*(self.tax_perc/100)
        return self.salary

    def update_tax_percentage(self, tax):
        self.salary -= self.salary*(tax/100)
        return self.salary
    
e1 = Employee()
e1.getData()
print(e1.Salary_after_tax())
print(e1.update_tax_percentage(3))
