import re

rom_num = input("What is the number in Roman numerals? ").upper()

single_roman_dict = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

double_roman_dict = {
    "IV":single_roman_dict["V"]-single_roman_dict["I"],
    "IX":single_roman_dict["X"]-single_roman_dict["I"],
    "XL":single_roman_dict["L"]-single_roman_dict["X"],
    "XC":single_roman_dict["C"]-single_roman_dict["X"],
    "CD":single_roman_dict["D"]-single_roman_dict["C"],
    "CM":single_roman_dict["M"]-single_roman_dict["C"],
}

romans = re.findall(r"CM|CD|XC|XL|IX|IV|[MDCLXVI]", rom_num)

rom_sum = 0

for roman_index, roman in enumerate(romans):
    if roman in single_roman_dict.keys():
        rom_sum += single_roman_dict[roman]
    else:
        rom_sum += double_roman_dict[roman]
    

print(f"that's {rom_sum} as a decimal")

