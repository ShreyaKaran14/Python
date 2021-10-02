class Employee:
    def __init__(self, emp_id, emp_name, salary, emp_dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        self.emp_dept = emp_dept
    def display(self):
        print('Name:', self.emp_name)
        print('Empid: ', self.emp_id)
        print('Empsal: ', self.salary)
        print('Empdept : ', self.emp_dept)
    def createtimesheet(self):
        date = input("enter date: ")
        no_of_hrs = input("enter no_of_hrs : ")
        activity = input("enter activity: ")
        description = input("enter description: ")
        status = input("enter status: ")


#TimeSheet - date, hours , activity, description, status
class Timesheet(Employee):
    def __init__(self, date, no_of_hrs, activity, description, status):
        Employee.__init__(self, self.emp_id, self.emp_name, self.salary, self.emp_dept)
        self.date = date
        self.hours = hours
        self.activity = activity
        self.description = description
        self.status = status


e1=Employee('20861','Shreya Karan','30000','do')
e1.createtimesheet()