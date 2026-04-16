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

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def _get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count > 0 else 0


    def __str__(self):
        avg_grade = self._get_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"


    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов со студентами")
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов со студентами")
        return self._get_average_grade() == other._get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def _get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count > 0 else 0


    def __str__(self):
        avg_grade = self._get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов с лекторами")
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов с лекторами")
        return self._get_average_grade() == other._get_average_grade()


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"



def average_student_grade(students_list, course_name):
    total_grades = []
    for student in students_list:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])
    if not total_grades:
        return 0
    return round(sum(total_grades) / len(total_grades), 1)



def average_lecturer_grade(lecturers_list, course_name):
    total_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])
    if not total_grades:
        return 0
    return round(sum(total_grades) / len(total_grades), 1)



student1 = Student('Алёхина', 'Ольга', 'ж')
student2 = Student('Иванов', 'Иван', 'м')

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Сергей', 'Сергеев')

reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Мария', 'Сидорова')


student1.courses_in_progress += ['Python', 'Java']
student2.courses_in_progress += ['Python', 'Git']

lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'Git']

reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'Git']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 10)

student1.rate_lecture(lecturer1, 'Python', 7)
student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 10)

student1.add_courses('Введение в программирование')
student2.add_courses('Основы алгоритмов')

print(reviewer1)
print()
print(reviewer2)
print()

print(lecturer1)
print()
print(lecturer2)
print()

print(student1)
print()
print(student2)
print()

print(f"student1 > student2: {student1 > student2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print()

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка студентов по курсу Python: {average_student_grade(students_list, 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {average_lecturer_grade(lecturers_list, 'Python')}")