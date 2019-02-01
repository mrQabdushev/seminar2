class Jic:
    students = 25
    teacher = 'Abylaikhan'
    def E_group(self):
        print("Number of students in 1E group is",self.students)

    def monkeys(self):
        self.teacher = "Yerdaulet"
        print("Teacher of monkeys is",self.teacher)

if __name__ == "__main__":
    p = Jic()
    p.E_group()
    p.monkeys()