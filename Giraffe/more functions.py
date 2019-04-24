## def my_functions(fname):
#     full_name= fname + "Sahu"
#     print(full_name)
#
# my_functions('arun')
# my_functions('ajay')

def is_leap(year):

    return year %4==0 and (year %100!=0 or year %400==0)


print(is_leap(2100))
