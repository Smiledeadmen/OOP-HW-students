class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lst_avg = 0
        Student.all_students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avr_value(self):
        lst_in_dict = sum(self.grades.values(), [])
        sum_lst = sum(lst_in_dict)
        self.lst_avg = round(sum_lst / len(lst_in_dict), 1)
        return self.lst_avg

    def __str__(self):
        text = f'''
            Имя: {self.name},
            Фамилия: {self.surname}
            Средняя отценка за домашние задания: {self.avr_value()}
            Курсы в процессе изучения: {",".join(self.courses_in_progress)}
            Завершенные курсы: {",".join(self.finished_courses)}'''
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.lst_avg < other.lst_avg


class Mentor:
    all_lectors = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.lst_avg = 0
        if isinstance(self, Lecturer):
            Mentor.all_lectors.append(self)

    def avr_value(self):
        lst_in_dict = sum(self.grades.values(), [])
        sum_lst = sum(lst_in_dict)
        self.lst_avg = round(sum_lst / len(lst_in_dict))
        return self.lst_avg


class Lecturer(Mentor):
    def __str__(self):
        text = f'''
            Имя: {self.name}
            Фамилия: {self.surname}
            Средняя отценка за лекции: {self.avr_value()}'''
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.lst_avg < other.lst_avg


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'''
            Имя: {self.name}
            Фамилия: {self.surname}'''
        return text


print('НАЧАЛО ПРОГРАММЫ!')
# создание 4 студентов
student1 = Student('Ruoy', 'Eman', 'Male')
student1.courses_in_progress += ['Python']

student2 = Student('Ruby', 'Fisher', 'Female')
student2.courses_in_progress += ['Python']

student3 = Student('Bob', 'Copson', 'Male')
student3.courses_in_progress += ['Git']

student4 = Student('Mary', 'Thander', 'Female')
student4.courses_in_progress += ['Git']

# создание 2 лекторов
lector1 = Lecturer('Jone', 'Gasby')
lector1.courses_attached += ['Python']
lector2 = Lecturer('Ashly', 'Williams')
lector2.courses_attached += ['Git']

# создание 2 проверяющих
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Ada', 'Wong')
reviewer2.courses_attached += ['Git']

# Оценивание домашних заданий студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 3)
reviewer1.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student2, 'Python', 6)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student3, 'Git', 9)
reviewer2.rate_hw(student3, 'Git', 8)
reviewer2.rate_hw(student3, 'Git', 1)
reviewer2.rate_hw(student4, 'Git', 9)
reviewer2.rate_hw(student4, 'Git', 9)
reviewer2.rate_hw(student4, 'Git', 10)

# Оценивание студентами леций
student1.rate_lector(lector1, 'Python', 5)
student1.rate_lector(lector1, 'Python', 8)
student1.rate_lector(lector1, 'Python', 2)
student1.rate_lector(lector1, 'Python', 4)
student2.rate_lector(lector1, 'Python', 8)
student2.rate_lector(lector1, 'Python', 7)
student2.rate_lector(lector1, 'Python', 3)
student2.rate_lector(lector1, 'Python', 3)
student3.rate_lector(lector2, 'Git', 5)
student3.rate_lector(lector2, 'Git', 4)
student3.rate_lector(lector2, 'Git', 8)
student3.rate_lector(lector2, 'Git', 8)
student4.rate_lector(lector2, 'Git', 8)
student4.rate_lector(lector2, 'Git', 8)
student4.rate_lector(lector2, 'Git', 8)
student4.rate_lector(lector2, 'Git', 9)

# Вывод отценок студентов и леторов
print(lector1.grades)
print(lector2.grades)
print(student1.grades)
print(student2.grades)
print(student3.grades)
print(student4.grades)
print('----------------')

# Вывод данных проверяющих
print(reviewer1)
print(reviewer2)
print('----------------')

# Вывод данных лекторов
print(lector1)
print(lector2)
print('----------------')

# добавление законченных курсов
student1.add_courses('Git')
student2.add_courses('Git')
student3.add_courses('Python')
student4.add_courses('Python')

# Вывод данных студентов
print(student1)
print(student2)
print(student3)
print(student4)
print('----------------')

# Сравнивание лекторов
print(lector1 < lector2)
print(lector1 > lector2)
print('----------------')

# Сравнивание студентов
print(student1 < student2)
print(student3 > student4)
print(student4 > student1)

# Вызов списка всех студентов как объекты
print(Student.all_students)

# Функция подсчета среднего значения по всем студентам
def avr_all_students(all_students, course):
        value = 0
        for student in all_students:
            if course in student.courses_in_progress:
                value += student.lst_avg
        return f'Средняя отценка по всем студентам изучающих {course}: {value}'

print(avr_all_students(Student.all_students, 'Python'))
print(avr_all_students(Student.all_students, 'Git'))

# Вызов списка всех лекторов как объекты
print(Mentor.all_lectors)

# Функция подсчета среднего значения по всем лекторам
def avr_all_lectors(all_lectors, course):
    value = 0
    for lector in all_lectors:
        if course in lector.courses_attached:
            value += lector.lst_avg
    return f'Средняя отценка по всем лекторам читаютщим курс {course}: {value}'

print(avr_all_lectors(Mentor.all_lectors, 'Python'))
print(avr_all_lectors(Mentor.all_lectors, 'Git'))