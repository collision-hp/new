def pow(base,expo):
    if(expo==0):
        return 1
    else:
        return base*pow(base,expo-1)
base=int(input("Enter the base"))
expo=int(input("Enter the exponent"))
print(pow(base,expo))