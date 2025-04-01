def increasing(n,curr=1):
    if curr>n :
        return n
    print(curr,"\n")
    increasing(n,curr+1)
n=int(input("Enter a number"))
increasing(n)