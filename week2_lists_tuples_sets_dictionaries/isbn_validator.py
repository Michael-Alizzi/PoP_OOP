ISBN = input("What is the ISBN? ")

isbn_list = list(ISBN)

sum_list = []

for num_index, num in enumerate(isbn_list):
    if num_index < 9:
        num_index += 1
        product_index = num_index*int(num)
        sum_list.append(int(product_index))


mod_sum = sum(sum_list) % 11

if ISBN[-1] =='X':
    if mod_sum == 10:
        print(f"{ISBN} is valid")
    else:
        print(f"{ISBN} is invalid")
elif ISBN[-1] !='X':
    if mod_sum == int(ISBN[-1]):
        print(f"{ISBN} is valid")
    else:
        print(f"{ISBN} is invalid")