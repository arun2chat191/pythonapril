def fib():
    a,b=0,1
    while True:
        yield(a)
        a,b=b,a+b


for n in fib():
    if n > 10:
     break
print(n)

#Generators
#------------
#1.to generate first n numbers
#2.to implement countdown
#3.to generate fibonacci numbers


#to generate first n numbers



# def firstn(num):
#     n=1
#     while n<=num:
#         yield(n)
#         n+=1
#
# number=firstn(10)
# for x in number:
#     print(x)

# import time
#
# def countdown(num):
#     print("and now the countdown begins.....")
#     while num>0:
#         yield (num)
#         num-=1
#
# value=countdown(5)
# for x in value:
#     print(x)
#     time.sleep(1)














# def my_gen():
#     yield "a"
#     yield "b"
#     yield "c"
#
# g=my_gen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))


# g=(x*x for x in range(100))
# while True:
#     print(next(g))