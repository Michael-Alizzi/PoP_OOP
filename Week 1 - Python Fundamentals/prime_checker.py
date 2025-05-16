prime = int(input("What number would you like to check? "))

if prime < 2:

    prime_f = False

else:

    number = 2

    prime_f = True

    while number < prime:
        
        if prime % number == 0:

            prime_f = False

            break

        number += 1

if prime_f:

    print(f"{prime} is prime")

else:

    print(f"{prime} is not prime")