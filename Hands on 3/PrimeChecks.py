def getNum():
    num=int(input("Please enter an integer between 1 and 5000: "))
    while num<2 and num>4999:
        print("Invalid integer. Please try again.")
        num=int(input("Please enter an integer between 1 and 5000:"))
    checkPrime(num=num)

def checkPrime(num):
    factorCount=0
    factors=[]
    for i in range(1,num):
        if num%i==0 and num!=i and i!=1:
            factorCount+=1
            factors.append(i)
    
    if factorCount==0:
        print(num,"is a prime number.")
    else:
        print(num,"is NOT a prime number, it has",factorCount,"factors aside from 1 and",num,"those are")
        for i in range(factorCount/2):
            print(factors[i],"and",factors[-i-1])
        
        #print(factors)