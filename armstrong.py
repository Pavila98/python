y=int(input())
temp=y
num=0
while(y>0):
    rem=y%10
    num+=rem**3
    y=y//10
if(temp==num):
    print("yes")
else:
    print("no")
