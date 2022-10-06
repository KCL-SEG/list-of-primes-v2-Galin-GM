"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True

def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError("Cannot be 0 or negative number");
    else:
        list = []
        j = 2;
        numberOfPrimes = 0

        while (numberOfPrimes < number_of_primes):
            if(isPrime(j)):
                list.append(j);
                numberOfPrimes += 1;
                j += 1;
            else:
                j += 1;
        print (list);


        return list

#i = int(input("enter integer: "));
#primes(i);
