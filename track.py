# Base or Super class


class Track:

    # Constructor
    def __init__(self, id, start, end):
        self.id = id
        self.cnx_start = start
        self.cnx_end = end

    # Track identifier
    def get_id(self):
        return self.id

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
