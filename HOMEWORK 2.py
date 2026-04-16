class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # --- НОВЫЙ МЕТОД ДЛЯ ВЫСТАВЛЕНИЯ ОЦЕНОК ЛЕКТОРАМ ---
    def rate_lecture(self, lecturer, course, grade):
        # Проверяем, что это лектор, что он ведет этот курс, и что студент на нем учится
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# --- НОВЫЙ КЛАСС LECTURER ---
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} # Словарь для хранения оценок от студентов


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# --- ПРОВЕРКА РАБОТЫ КОДА (как в задании) ---

# Создаем объекты
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'ж')

# Закрепляем курсы
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# Тестируем метод rate_lecture
print(student.rate_lecture(lecturer, 'Python', 7))  # Должно быть None (оценка успешно выставлена)
print(student.rate_lecture(lecturer, 'Java', 8))    # Должна быть 'Ошибка' (лектор не ведет Java)
print(student.rate_lecture(lecturer, 'C++', 8))     # Должна быть 'Ошибка' (студент не учится на C++)
print(student.rate_lecture(reviewer, 'Python', 6))  # Должна быть 'Ошибка' (нельзя оценить ревьюера этим методом)

# Проверяем итоговые оценки лектора
print(lecturer.grades) # Должно вывести: {'Python': [7]}



