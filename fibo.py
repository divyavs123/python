def fibo(n):
        if n<=1:
                return 1
        else:
                return(fibo(n-1)+fibo(n-2))
n=int(input("Enter the elements:"))
if n<=0:
    print("Value cannot be negative")
else:
    print("Fibonic sequenc:")
    for i in range(0,n):
        print(fibo(i))
