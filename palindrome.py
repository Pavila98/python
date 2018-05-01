y=int(input())
temp=y
rev=0
while(y>0):
    a=y%10
    rev=rev*10+a
    y=int(y/10)
if temp==rev:
    print("it is a palindrome")
else:
    print("not a palindrome")
