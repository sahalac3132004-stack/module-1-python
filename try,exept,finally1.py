n1=int(input("enter marks for subject 1:"))
n2=int(input("enter mark for subject 2:"))
n3=int(input("enter mark for subject3:"))
n4=int(input("enter mark for subject 4:"))
n5=int(input("enter mark for subject 5:"))

def sum(n1,n2,n3,n4,n5):
    total=n1+n2+n3+n4+n5
    print("totalmark",total)
    average=total/5
    print("averagemark",average)

try:
    sum(n1,n2,n3,n4,n5)

except ZeroDivisionError:
    print("invalid input")


finally:
    print("mark processing completed")












