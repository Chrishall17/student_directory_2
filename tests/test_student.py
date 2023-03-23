from lib.student import Student

"""
Student constructs with an id, name and cohort id
"""
def test_student_constructs():
    student = Student(1, "Test Student", 1)
    assert student.id == 1
    assert student.name == "Test Student"
    assert student.cohort_id == 1

"""
We can format students to strings nicely
"""
def test_students_format_nicely():
    student = Student(1, "Test Student", 1)
    assert str(student) == "Student(1, Test Student, 1)"

"""
We can compare two identical students
And have them be equal
"""
def test_cohorts_are_equal():
    student1 = Student(1, "Test Student", 1)
    student2 = Student(1, "Test Student", 1)
    assert student1 == student2