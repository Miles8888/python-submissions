class Employee():
    """A class representing the information on an employee."""

    def __init__(self, f_name, l_name, salary):
        """Run through basic employee information."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount