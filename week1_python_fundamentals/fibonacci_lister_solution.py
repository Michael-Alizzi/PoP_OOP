fib = int(input("How many Fibonacci numbers would you like? "))

counter = 0

a, b = 0, 1

while counter < fib:
    
    print(a)

    a, b = b, a + b

    counter += 1


