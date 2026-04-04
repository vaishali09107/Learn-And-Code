class Employee:
    """ Represents an employee. """

    def __init__(self, employee_id: int, name: str, department: str):
        self._employee_id = employee_id
        self._name = name
        self._department = department
        self._is_working = True

    def get_id(self) -> int:
        return self._employee_id

    def get_name(self) -> str:
        return self._name

    def get_department(self) -> str:
        return self._department

    def is_working(self) -> bool:
        return self._is_working

    def mark_as_terminated(self) -> None:
        self._is_working = False
