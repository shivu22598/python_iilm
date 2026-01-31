a=10
try:
    b=int(input("Enter a number:"))
    c=a/b
except ValueError:
    print("Value error")   
finally:
    print("c:",c)