import math

class Employee:

    """
    Class variables are shared across all instances of that class.
    Instance variables, however, are unique to each instance.
    """

    base_salary = 38000
    raise_amount = 1.00
    n_employees = 0

    def __init__(self, firtname: str, lastname: str, additional_amount: int) -> None:

        """
        Increment the n_employees variable upon creation of each employee instance
        Using the class name, since it will not be modified by any instance
        """

        self.firtname = firtname
        self.lastname = lastname
        self.additional_amount = additional_amount
        Employee.n_employees += 1

    @classmethod
    def from_string(cls, string):
        firstname, lastname, additional_amount = string.split("-")
        return cls(firstname, lastname, int(additional_amount))

    @classmethod
    def set_base_salary(cls, amount):
        cls.base_salary = amount

    def set_raise_amount(self, amount):
        """
        This methid only modify the variable for a specific instance of the Employee class;
        not for all instance.
         """
        self.raise_amount = amount

    def GetSalary(self):

        """
        using self.annual_raise allows us to modify this variable outside the class.
        It will also also subclasses of this class to modify that variable if they wanted to.
        """
        self.salary = int((Employee.base_salary + self.additional_amount) * self.raise_amount)
        return self.salary


if __name__ == "__main__":

    moein = Employee("Moein", "Torabi", 4000)
    Employee.set_base_salary(42000)
    print(moein.GetSalary())
    moein.set_raise_amount(1.01)
    print(moein.GetSalary())
    print(moein.raise_amount)
    print(Employee.raise_amount)



    thomas = Employee("Thomas", "Lin", 5000)
    # print(thomas.raise_amount)
    # kamil = Employee.from_string("Kamil-something-4000")
    # print(kamil.GetSalary())