from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        return cohorts

    def find(self, cohort_id):
        rows = self._connection.execute(
            'SELECT * from cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])

    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)', [
                                cohort.name, cohort.starting_date])
        return None

    def delete(self, cohort_id):
        self._connection.execute(
            'DELETE FROM cohorts WHERE id = %s', [cohort_id])
        return None
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            "SELECT cohorts.id AS cohort_id, cohorts.name, cohorts.starting_date, students.id AS student_id, students.name " \
            "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
            "WHERE cohorts.id = %s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["name"], row["cohort_id"])
            students.append(student)

        # Each row has the same id, name, and genre, so we just use the first
        return Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students)

