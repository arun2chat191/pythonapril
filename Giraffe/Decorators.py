









# def div_decorator(func):
#     def inner(*args):
#         list1=[]
#         list1=args[1:]
#         for i in list1:
#             if i==0:
#                 return"Please provide proper input"
#         return func(*args)
#     return inner
#
#
# @div_decorator
# def div1(a,b):
#     return a/b
# @div_decorator
# def div2(a,b,c):
#     return a/b/c

# print(div1(10,5))
# print(div2(0,1,5))


















# def outer(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner
#
# @outer
# def print_str():
#     return "good morning"
# print(print_str())








# def div_decorator(func):
#     def inner(x,y):
#         if y==0:
#             return "give proper input"
#         return func(x,y)
#     return inner
#
#
#
#
# @div_decorator
# def div(a,b):
#     return a/b
#
# print(div(4,0))
#
#
#
#







# def div(a,b):
#     print(a/b)
#
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
#
# div=smart_div(div)
# div(2,4)
