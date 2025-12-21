class EmployeeStatusService:
    """ Handles employee status changes. """

    def terminate_employee(self, employee: Employee) -> None:
        employee.mark_as_terminated()
