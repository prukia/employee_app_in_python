# Creating and instantiating classes
# data and function (attributes and methods)

# creating an application for Employees
# using Class to represent a list of employees (each employee will have specific attributes and methods)

# class is basically a blueprint for creating instances
# instance of class: each unique employee we create in the class is an instance of the class

# instance variables: creates data that is unique to each instance

# def __init__(self) is to initialize/ the constructor
# receives the first instance  as param as self


class Employee:
    # pass  # pass means skip that for now

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # creating method: each method within a class takes the instance as the first arguement
    # using self instead of 'emp_1' so it could work with all instances
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# create instances of employee class
# instance is passed by automatically so we can leave out 'self'
# example: emp_1 is being passed as self
emp_1 = Employee('Rukia', 'Sheikh-Mohamed', 50000)
emp_2 = Employee('Test', 'User', 600000)

print(emp_1)
print(emp_2)

# no longer need manual assignments
# emp_1.first = 'Rukia'
# emp_1.last = 'Sheikh-Mohamed'
# emp_1.email = 'rukia.sheikhmohamed@buzzfeed.com'
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test.user@company.com'

print(emp_1.email)
print(emp_2.pay)

# non-dynamic way
print ('{} {}'.format(emp_1.first, emp_1.last))

# perform some kind of action by adding METHODS example adding full name of employee
# needs () because it's a method
print(emp_1.fullname())

# we can run this method using the class name(Employee) it's self
# we have to mainly pass in the instance
# does the same thing as line 57
print(Employee.fullname(emp_1))