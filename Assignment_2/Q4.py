
def fib(n):
    if n==1 :
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter a number"))
print(fib(n))

'''Time complexity of the recursive solution is (O(2^n))
0 1 1 2 3 5'''