def cube(n):
    
    if n not in cube.dictionary.keys():
        cube.dictionary[n] = n**3
        return cube.dictionary[n]
    
    else:
        return cube.dictionary[n]

cube.dictionary = {}

print(cube(10))
print(cube(10))
print(cube(5))
print(cube(5))
print(cube(10))
print(cube(5))
print(cube.dictionary)