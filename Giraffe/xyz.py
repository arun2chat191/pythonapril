
num=int(input("Enter a number:"))
rev=0
a=num

while num>0:
    dg=num%10
    num=num//10
    rev=rev*10+dg
print(rev)
if a==rev:
    print(a,"number is a palindrome")

else :

    print(a,"number is not a palindrome number")

