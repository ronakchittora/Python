from math import sqrt

def check_prime(num):
    a = int(sqrt(num))
    if num != 1:
        for i in range(2,a+1):
            if num%i == 0:
                return 1
            else:
                return 0
    else:
        return 1

num_in = int(input("Enter a number: "))
prime_fl = check_prime(num_in)

if prime_fl == 1:
    print("Not Prime")
else:
    print("It is Prime")


"""
List Comprehension

if sum([ True if a%factor == 0 else False for factor in ( [2] + list(range(3,int(math.sqrt(a)),2) )) ]): 
  print("Number is composite")
else: 
  print("Number is prime")

"""
