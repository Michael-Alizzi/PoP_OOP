fib = int(input("How many Fibonacci numbers would you like? "))

counter = 0

a, b = 0, 1

fib_list = []

while counter < fib:

    fib_list.append(str(a))

    a, b = b, a + b

    counter += 1

fib_list_final = ', '.join(fib_list)

print(fib_list_final)
