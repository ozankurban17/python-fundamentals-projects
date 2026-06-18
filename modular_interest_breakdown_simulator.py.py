# Ozan Kurban

# This program calculates the final amount in a bank account using compound interest.

# It now runs in a loop and shows a yearly breakdown of the balance using functions.

def adjust_rate(P, r):

    if P >= 5100 and P <= 11000:

        r = r + 0.005

    elif P >= 11001 and P <= 60000:

        r = r + 0.0075

    elif P > 60000:

        r = r + 0.0125

    return r



def calculate_amount(P, r, n, t):

    A = P * (1 + r/n)**(n * t)

    return A

# Returns the amount to be added if term is 12+ and rate is at least 6%

def incentive_one(t, r, P):

    if t >= 12 and r >= .06:

        return P * 0.01 * t

    return 0

# Returns 75 if r is greater than 11%, otherwise returns 0

def incentive_two(r):

    if r > 0.11:

        return 75

    return 0



def main():

    repeat = 'y'

    while repeat.lower() == 'y':

        P = float(input("Enter the principal balance: "))

        r = float(input("Enter the interest rate as a percent: "))

        n = int(input("How many times per year is the interest compounded? "))

        t = int(input("How many years will the account earn interest? "))

        

        r_orig = r / 100

        r_decimal = r / 100



        # Calling adjust_rate to get the new r

        r_adjusted = adjust_rate(P, r_decimal)



        # Loop to print the yearly listing of the amount        

        print(f"{'Year':<10} Amount")

        for year in range(1, t + 1):

            A_yearly = calculate_amount(P, r_adjusted, n, year)

            print(f"{year:<10} ${A_yearly:,.2f}")



        # Final A calculation using function

        A = calculate_amount(P, r_adjusted, n, t)



        # Adding incentives via functions

        A = A + incentive_one(t, r_orig, P)

        A = A + incentive_two(r_orig)



        print(f"\nAt the end of {float(t)} years, you will have ${A:,.2f}\n")



        # Ask the user if they want to run again and validate their response

        repeat = input("Would you like to run this again on another set of data? (y/n) ")

        while repeat.lower() not in ['y', 'n']:

            repeat = input("Would you like to run this again on another set of data? (y/n) ")



# Calling main function to execute

if __name__ == "__main__":

    main()
