temp = input("Enter a temperature (e.g. 24C, 78F): ")

temp_upper = temp.upper()

if temp_upper[-1] == "C":

    # Celsius to Fahrenheit
    temp_converted = (float(temp_upper.replace('C', '')) * 1.8) + 32

    T = "F"

else: 

    # Fahrenheit to Celsius
    temp_converted = (float(temp_upper.replace('F', '')) - 32) / 1.8

    T = "C"

print(f"{temp_upper} is {str(round(temp_converted, 1))+T}")