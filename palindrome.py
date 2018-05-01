x=int(input())
temp=x
rev=0
while(x>0):
    a=x%10
    rev=rev*10+a
    x=int(x/10)
if temp==rev:
    print("it is a palindrome")
else:
    print("not a palindrome")
