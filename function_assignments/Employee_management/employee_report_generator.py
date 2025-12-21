from abc import ABC, abstractmethod

class EmployeeReportGenerator(ABC):
    """ Report generator abstraction. """

    @abstractmethod
    def generate(self, employee: Employee) -> str:
        pass

class CsvEmployeeReportGenerator(EmployeeReportGenerator):
    def generate(self, employee: Employee) -> str:
        return (
            f"{employee.get_id()},"
            f"{employee.get_name()},"
            f"{employee.get_department()},"
            f"{employee.is_working()}"
        )

class XmlEmployeeReportGenerator(EmployeeReportGenerator):
    def generate(self, employee: Employee) -> str:
        return (
            "<employee>"
            f"<id>{employee.get_id()}</id>"
            f"<name>{employee.get_name()}</name>"
            f"<department>{employee.get_department()}</department>"
            f"<working>{employee.is_working()}</working>"
            "</employee>"
        )
