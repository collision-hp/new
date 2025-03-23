class ML:
    var1="Welcome to ML"
class DL:
    var2="We;come to DL"
class AI(ML,DL):
    var3="Welcome to AI"

deepseek=AI()
print(deepseek.var1)
print(deepseek.var2)
print(deepseek.var3)