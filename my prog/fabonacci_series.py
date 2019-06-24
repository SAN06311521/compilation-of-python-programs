def Fabonacci(num):
        if num==1:
            return 1
        elif num==2:
            return 1
        elif num>2:
            return Fabonacci(num-1) + Fabonacci(num-2)

print("number of terms : fabonacci series -" )
for num in range(1 , 11):
    print(num , ":" , Fabonacci(num))
