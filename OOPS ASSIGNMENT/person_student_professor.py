class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age


class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__major = major

    # Getter for student_id
    def get_student_id(self):
        return self.__student_id

    # Setter for student_id
    def set_student_id(self, student_id):
        self.__student_id = student_id

    # Getter for major
    def get_major(self):
        return self.__major

    # Setter for major
    def set_major(self, major):
        self.__major = major


class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__department = department

    # Getter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee_id
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for department
    def get_department(self):
        return self.__department

    # Setter for department
    def set_department(self, department):
        self.__department = department


class University:
    def __init__(self):
        self.students = []
        self.professors = []

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def display_students(self):
        for student in self.students:
            print(
                f"Name: {student.get_name()}, Age: {student.get_age()}, ID: {student.get_student_id()}, Major: {student.get_major()}")

    def display_professors(self):
        for professor in self.professors:
            print(
                f"Name: {professor.get_name()}, Age: {professor.get_age()}, ID: {professor.get_employee_id()}, Department: {professor.get_department()}")

# Example usage:
university = University()
student1 = Student("Alice", 20, "S123", "Computer Science")
professor1 = Professor("Dr. Smith", 45, "P456", "Mathematics")
university.add_student(student1)
university.add_professor(professor1)
university.display_students()
university.display_professors()
