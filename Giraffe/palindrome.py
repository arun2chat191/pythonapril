num=int(input("Enter a  number"))
rev=0
a=num

while num>0:
    dg=num%10
    num=num//10
    rev=rev*10+dg
print(rev)

if a==rev:
    print(a,"is a palindrome number")
else:
    print(a,"is not  a palindrome number")

