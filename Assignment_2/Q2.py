def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
x=int(input("Enter the 1st integer"))
y=int(input("Enter the 2nd integer"))
print(gcd(x,y))
print()
