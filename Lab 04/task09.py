class Student:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")


class Marks(Student):
    def __init__(self,name, id, marks_algo,marks_dataScience, marks_calculus):
        super().__init__(name, id)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

        

    def display_marks(self):
        print(f"Marks in Algorithms: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_dataScience}")
        print(f"Marks in Calculus: {self.marks_calculus}")

class Result(Marks):
    def __init__(self, name, id, marks_algo,marks_dataScience, marks_calculus):
        super().__init__( name, id, marks_algo,marks_dataScience, marks_calculus)
        self.total_marks = 0
        self.avg_marks = 0

    def total_and_avg_marks(self):
        total = self.marks_algo + self.marks_dataScience + self.marks_calculus
        avg = total/3
        self.total_marks = total
        self.avg_marks= avg
        print(f"Total marks are: {self.total_marks}")
        print(f"Average marks are: {self.avg_marks}")

s1 = Result("Adina", "23k-0008", 75, 80, 91)
s1.display_info()
s1.display_marks()
s1.total_and_avg_marks()
