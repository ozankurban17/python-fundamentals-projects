# Ozan Kurban
# This program calculates the final amount in a bank account using compound interest.
# It now runs in a loop and shows a yearly breakdown of the balance.
# Start of the main loop to run the program multiple times
repeat = 'y'
while repeat.lower() == 'y':
    P = float(input("Enter the principal balance: "))
    r = float(input("Enter the interest rate as a percent: "))
    n = int(input("How many times per year is the interest compounded? "))
    t = int(input("How many years will the account earn interest? "))
    
    r_orig = r / 100
    r = r / 100

    if P >= 5100 and P <= 11000:
        r = r + 0.005
    elif P >= 11001 and P <=60000:
        r = r + 0.0075
    elif P > 60000:
        r = r + 0.0125
# Loop to print the yearly listing of the amount        
    print(f"{'Year':<10} Amount")
    for year in range(1, t + 1):
        A_yearly = P * (1 + r/n)**(n * year)
        print(f"{year:<10} ${A_yearly:,.2f}")

    A = P*(1+r/n)**(n*t)

    if t >= 12 and r_orig >= .06:
        A = A + P*0.01*t
        
    if r_orig > 0.11:
        A = A + 75

    print(f"\nAt the end of {float(t)} years, you will have ${A:,.2f}\n")
# Ask the user if they want to run again and validate their response
    repeat = input("Would you like to run this again on another set of data? (y/n) ")
    while repeat.lower() not in ['y', 'n']:
        repeat = input("Would you like to run this again on another set of data? (y/n) ")
