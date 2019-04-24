# def greet_customer(name,num_apples):
#     print("hello !" + name +'!')
#     print("we have " + str(num_apples) + "apples in stock")
#
# greet_customer('mark',4)
# greet_customer('brooke',5)
# greet_customer('Greg',6)
# def greet(first_name,last_name):
#
#     print(f"Hi! {first_name} {last_name}")
#     print("Welcome abroad")
#
# greet('Josh','Hamedani')
# greet('John','Smith')
# greet('Arun','Sahu')
''' functions that performs a task
and functions that returns a value'''
# def increment(number,by=1):
#     return number + by
#
# print(increment(2,5))


# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total*=number
#     return total
# print(multiply(2,3,4,5))

# def fizz_buzz(input):
#
#     if (input%3==0 and input %5==0):
#         return "fizzbuzz"
#     if input%3==0:
#           return "fizz"
#     if input % 5==0:
#          return "buzz"
#     return input
#
# print(fizz_buzz(20))
# name1="Arun"
# height_h1=1.8
# weight_kg1=60
# def bmi_calculator(name,height_m,weight_kg):
#
#         bmi=weight_kg/(height_m**2)
#         print('bmi:')
#         print(bmi)
#         if (bmi)<=25:
#             return( name + " not overweight")
#
#         else:
#             return( name + " overweight ")
#
#
# result1 = bmi_calculator(name1, height_h1, weight_kg1)
#
# print(result1)
# def max_num(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num3 and num2>num1:
#         return num2
#     else:
#         return num3
#
# print(max_num(1,2,3))
# num1=float(input("Enter a number:"))
# op=input("Enter a operator:")
# num2=float(input("Enter another number"))
#
# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("Invalid operator")

secret_word="Giraffe"
guess=""
guess_count=0
guess_limit=3
out_of_guesses= False

while guess != secret_word and not(out_of_guesses):

    if  guess_count<guess_limit:

      guess=input("Enter Guess:")
      guess_count += 1

    else:
     out_of_guesses = True
if out_of_guesses:
          print("Out of guesses, You  Lose!")
else:
    print("You Win!")




