import math


'''Create a program that allows the users's to use two finance calculators
 an investment calculator and a home loan repayment calculator'''

# Interest formulas 

# calculate simple interest
def calculate_simple_interest(P, r, t):
    return P * (1 + (r/100) * t)

# calculate compound interest
def calculate_compound_interest(P, r, t):
    return P * math.pow ((1 + (r/100)), t)

# calculate bond repayment
def calculate_bond_repayment(P, i, n):
    monthly_interest_rate = (i/100) / 12
    return (monthly_interest_rate * P) / (1 - (1 + monthly_interest_rate)**(-n))





# Give the user the option of an investment or bond calculation
print("investment  - to calculate the amount of interest you'll earn on your investment")
print("bond        - to calculate the amount you'll have to pay on home loan")
print(" ")

# Get the calculation choice from the user
calculation_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n").lower()

if calculation_choice == "investment":
    P = float(input("How much money are you depositing?: \n"))
    r = float(input("What is the interest rate? (percentage): \n"))
    t = int(input("How many years are you investing for?: \n"))
    intrest_choice = input("Would you like Simple or Compound interest?: \n").lower()

    # Intrest calculations
    if intrest_choice == "simple":
        result = calculate_simple_interest
        # Print the result
        print(f"Based on the information given your investment return after {t} years will be: \n{round(P * (1 + (r/100) * t), 2)}")
    
    elif intrest_choice == "compound":
        result = calculate_compound_interest
        print(f"Based on the information given your investment return after {t} will be: \n{round(P * math.pow ((1 + (r/100)), t), 2)}")
    else:
        print("Error invalid interest option chosen")

elif calculation_choice == "bond":
    # Get the information required for bond calculation
    P = float(input("What is the current value of your house?: \n"))  
    i = float(input("What is the interest rate? (percentage): \n"))
    n = int(input("How many months do you plan on taking to repay the loan?: \n")) 
    
    result = calculate_bond_repayment(P, i, n,)
    
    # Print repayment result
    print(f"Based on the information you have provided your monthly repayments will be: \n£{round(result, 2)}")
    
    
else:
    print("Error you have entered an invalid response")


