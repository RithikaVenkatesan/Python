def factorial(N):
    fact=1
    while(N>=1):
        fact=fact*N
        N=N-1
    return fact

N=int(input("enter"))
fact=factorial(N)
print("fatct is:",fact)
