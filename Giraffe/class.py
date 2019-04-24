class Employee:
     def __init__(self,first,last,pay):

         self.first=first
         self.last=last
         self.pay=pay
         self.email=first + '.'+ last + '@gmail.com'

     def full_name(self):
         return '{} {}'.format(self.first,self.last)

emp_1=Employee('Arun','Sahu',100000)
emp_2=Employee('Test','User',50000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)
# print(emp_2.first)
# print(emp_2.last)
# print(emp_2.pay)
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.full_name())
# print(Employee.full_name(emp_2))