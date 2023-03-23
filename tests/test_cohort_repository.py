from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
import datetime

"""
When we call CohortRepository#all
Need to note date entered is datetime.date type
We get a list of Cohort objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = CohortRepository(db_connection) # Create a new CohortRepository

    cohorts = repository.all() 

    assert cohorts == [
        Cohort(1, "Feb 23", datetime.date(2023, 2, 23), [])
    ]

"""
When we call CohortRepository#find
We get a single Cohort object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.find(1)
    assert cohort == Cohort(1, "Feb 23", datetime.date(2023, 2, 23))

"""
When we call CohortRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    repository.create(Cohort(None, "Mar 23", datetime.date(2023, 2, 23)))

    result = repository.all()
    assert result == [
        Cohort(1, 'Feb 23', datetime.date(2023, 2, 23)),
        Cohort(2, "Mar 23", datetime.date(2023, 2, 23))
    ]

"""
When we call CohortRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [

    ]

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, "Feb 23", datetime.date(2023, 2, 23), [
        Student(1, "Chris", 1)
    ])
