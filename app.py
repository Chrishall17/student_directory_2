from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")

repository = CohortRepository(connection)

cohort = repository.find_with_students(1)

print(cohort)


