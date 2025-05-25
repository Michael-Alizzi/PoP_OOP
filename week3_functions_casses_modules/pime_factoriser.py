import math

def prime_check(num):

    if num < 2:

        prime_f = False

    else:

        number = 2

        prime_f = True

        while number < num:
        
            if num % number == 0:

                prime_f = False

                break

            number += 1

    return prime_f

def prime_factors(num):

    divisor = 1
    
    prim_lst = []
    
    if prime_check(num) or num < 2:
        
        return f"{num} = {num}"
    
    else:
        
        while divisor < num:
    
            divisor += 1
    
            if prime_check(divisor) and num % divisor == 0:

                prim_lst.append(divisor)

    prim_lst_str = [str(num) for num in prim_lst]

    if math.prod(prim_lst) == num:

        return f"{num} = {' x '.join(prim_lst_str)}"
    
    else:

        for index, number in enumerate(prim_lst):
                    
                prim_lst.insert(index+2, number)

                if math.prod(prim_lst) == num:

                    prim_lst.sort()

                    prim_lst_str = [str(num) for num in prim_lst]

                    return f"{num} = {' x '.join(prim_lst_str)}"

num = int(input("Enter a number: "))

print(prime_factors(num))