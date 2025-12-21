class EmployeeRepository:
    """ Handles database operations for employees. """

    def save(self, employee: Employee) -> None:
        print(f"Saving employee {employee.get_id()} to database")
