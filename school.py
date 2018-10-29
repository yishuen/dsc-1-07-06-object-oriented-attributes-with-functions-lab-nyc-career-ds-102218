class School:

    def __init__(self, name, school_roster = {}):
        self._name = name
        self._roster = school_roster

    def roster(self):
        return self._roster

    def add_student(self, student_name, student_grade):
        if student_grade in self._roster.keys():
            self._roster[student_grade].append(student_name)
        else:
            self._roster[student_grade] = [student_name]

    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        roster = self._roster
        for grade, students in roster.items():
            students = students.sort()

school = School("Middletown High School")
