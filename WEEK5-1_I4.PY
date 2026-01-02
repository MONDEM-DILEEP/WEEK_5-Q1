#with recursion
def prime(n,i=2) :
    if n<=1 :
        return 0
    if i*i>n :
        return 1
    if n%i==0 : 
        return 0
    return prime(n,i+1)
n=int(input("enter a number to check prime or not(with recursion)"))
if(prime(n) == 1) :
    print("it is prime")
else :
    print("not prime ")

#without recursion 
def prime_WR(n) :
    if n<=1 :
        return 0
    for i in range(2,int(n**0.5)+1) :
        if n%1 ==0 :
            return 0
        return 1
n=int(input("enter a number to check prime or not(without recursion)"))
if(prime(n) == 1) :
    print("it is prime")
else :
    print("not prime ")
