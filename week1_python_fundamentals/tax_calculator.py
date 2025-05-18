# Name: Michael Alizzi
# Student Id: 5651718

### Tax Calculator ###

income = int(input("What was your income in 2022-23? "))

# Define the upper threshold for each tax bracket.
TAX_BRACKET_THRESHOLD1 = 18200

TAX_BRACKET_THRESHOLD2 = 45000

TAX_BRACKET_THRESHOLD3 = 120000

TAX_BRACKET_THRESHOLD4 = 180000

# Note 
# The upper threshold for the final tax bracket (TAX_BRACKET_THRESHOLD5) isn't required 
# because if the user is not in the 1-4 tax brackets then they must be in the final tax bracket.

### Tax Bracket One ###

# Less than $18,201
if income < TAX_BRACKET_THRESHOLD1+1:

    # No tax
    tax_amount = 0

### Tax Bracket Two ###

# Less than $45,001
elif income < TAX_BRACKET_THRESHOLD2+1:

    # Logic
    # 19c for each $1 over $18,200

    # Code
    # The difference between the user's income and the upper threshold for the 1st tax bracket ($18,200) multiplied by 0.19 (19c).
    tax_amount = (income-TAX_BRACKET_THRESHOLD1)*0.19

### Tax Bracket Three ###

# Less than $120,001
elif income < TAX_BRACKET_THRESHOLD3+1:

    # Logic
    # $5,092 plus 32.5c for each $1 over $45,000

    # Code
    # The difference between the user's income and the upper threshold for the 2nd tax bracket ($45,000) multiplied by 0.325 (32.5c), 
    # plus 5092. 
    tax_amount = 5092+(income-TAX_BRACKET_THRESHOLD2)*0.325

### Tax Bracket Four ###

# Less than $180,001
elif income < TAX_BRACKET_THRESHOLD4+1:

    # Logic
    # $29,467 plus 37c for each $1 over $120,000

    # Code
    # The difference between the user's income and the upper threshold for the 3nd tax bracket ($120,000) multiplied by 0.37 (37c), 
    # plus 29467.
    tax_amount = 29467+(income-TAX_BRACKET_THRESHOLD3)*0.37

### Tax Bracket Five ###

# Greater than $180,000
else:
    
    # Logic
    # $51,667 plus 45c for each $1 over $180,000

    # Code
    # The difference between the user's income and the upper threshold for the 4th tax bracket ($180,000) multiplied by 0.45 (45c), 
    # plus 51667.
    tax_amount = 51667+(income-TAX_BRACKET_THRESHOLD4)*0.45

print(f"The estimated tax on your income is ${round(tax_amount)}")