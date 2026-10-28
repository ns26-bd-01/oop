class Student:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show_info(self):
        print('men o\'quvchimana')


students: list[Student] = [
    Student('Ali', 'Valiyev', 19),
    Student('Bob', 'Samiyev', 21),
    Student('Gani', 'Samiyev', 21),
    Student('John', 'Doe', 12),
]

max_age = students[0].age
for student in students:
    if student.age > max_age:
        max_age = student.age

max_students = []
for student in students:
    if student.age == max_age:
        max_students.append(student)

print(max_age)
for s in max_students:
    print(s.first_name, s.age)
