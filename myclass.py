
class Jic:
    students = 25
    teacher = 'Abylaikhan'

    def __init__(self, students=25, teacher='Abylaikhan'):
        self.students = students
        self.teacher = teacher


    def setTeacher(self, teacher):
        self.teacher = teacher

    def E_group(self):
        print("Number of students in 1E group is",self.students)

    def monkeys(self):
        print("Teacher of monkeys is", self.teacher)
