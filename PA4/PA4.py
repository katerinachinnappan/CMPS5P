#Katerina Chinnappan
#kachinna@ucsc.edu
#PA4
#Compute n prime numbers entered by user
import string
 #start of isPrime
def isPrime(primeNumber, L):
    divisor = 2
    #while divisor is <= than the primeNumber
    while divisor <= primeNumber:
        #if the primeNumber is 2, return 2 because 2 is prime
        if primeNumber == 2:
            return True
        #if the remainder is 0, return false, so not prime number
        if primeNumber % divisor == 0:
            return False
        #while the remainder is not 0, check if primeNumber - divisor is > 1 then
        #increment divisor
        #otherwise return true
        while primeNumber % divisor != 0:
            change = primeNumber - divisor
            if change > 1:
                divisor += 1
            else:
                return True
    #end of isPrime
            
#main program starts here
numprimes = int(input('Enter the number of Primes to compute: '))
count = 0
primeNumber = 2
#start with empty list
L = []

#loop through the primer numbers for n times and append to List, then increment
#to the next prime number
while count < int(numprimes):
    if isPrime(primeNumber, L) == True:#proceed if true
        count += 1
        L.append(primeNumber)#append to List
        numbers = str(count)     
    primeNumber +=1#increment to the next primeNumber found

print("\n")
print("The first "+numbers+" primes are:")
#print 10 numbers per line looping through each element in List
for i in range(0, len(L), 10):
    print(*L[i:i+10])



