def map(f, lst):
    
    result = [f(it_lst) for it_lst in lst]

    return result

# Mapping the abs function
start_list = [-2, 4, -6, 8]
mapped_list = map(abs, start_list)
print(mapped_list)

# Mapping the len function
start_list = [[], [2, 3, 4], [3, 2, 5, 5, 1]]
mapped_list = map(len, start_list)
print(mapped_list)

# Mapping a user-defined function
def cube(x):
    return x**3
start_list = [1, 2, 3, 4, 5]
mapped_list = map(cube, start_list)
print(mapped_list)

# Mapping a lambda function
start_list = [1, 2, 3, 4, 5]
mapped_list = map(lambda x: x**4, start_list)
print(mapped_list)

