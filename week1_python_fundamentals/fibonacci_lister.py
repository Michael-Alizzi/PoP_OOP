fib = int(input("How many Fibonacci numbers would you like? "))


prev_count = 0

current_count = 1

final_count = 1

for i in range(fib):

    if i == 0:

        print(prev_count)
    
        print(" ")

    else:

        if i % 2 == 0:

            print(current_count)

            current_count += final_count

            print(" ")

        else:
            
            print(final_count)

            final_count += current_count

            print(" ")