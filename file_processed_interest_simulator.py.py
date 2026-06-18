# Ozan Kurban
# This program calculates the final amount in a bank account using compound interest.
# It now runs in a loop and shows a yearly breakdown of the balance using functions.


#FUNCTIONS
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

#MAIN FUNCTION
def main():
    try:
        #open the files instead of using manual input
        infile = open(r"C:\Users\ozank\Downloads\input.txt", "r")
        outfile = open("output.txt", "w")

        # This replaces 'while repeat == y' loop
        for line in infile:
            line = line.strip()
            if not line:
                continue

            try:
                # Splitting the line into P, r, n, t
                parts = line.split(',')
                P = float(parts[0])
                r = float(parts[1])
                n = int(parts[2])
                t = int(parts[3])

                #This is logic
                r_orig = r / 100
                r_decimal = r / 100

                # Calling adjust_rate to get the new r
                r_adjusted = adjust_rate(P, r_decimal)

                # Loop to print the yearly listing
                header = f"{'Year':<10} Amount\n"
                print(header, end='')
                outfile.write(header) # Writing to file as required

                for year in range(1, t + 1):
                    A_yearly = calculate_amount(P, r_adjusted, n, year)
                    yearly_row = f"{year:<10} ${A_yearly:,.2f}\n"
                    print(yearly_row, end='')
                    outfile.write(yearly_row) # Writing to file

                # Final A calculation using function
                A = calculate_amount(P, r_adjusted, n, t)

                # Adding incentives via functions
                A = A + incentive_one(t, r_orig, P)
                A = A + incentive_two(r_orig)

                final_text = f"\nAt the end of {float(t)} years, you will have ${A:,.2f}\n\n"
                print(final_text, end='')
                outfile.write(final_text) # Writing to file
                #logic is perfectly preserved

            except (ValueError, IndexError):
                # This is the new requirement for invalid data
                error_msg = f"Invalid Numeric Data was Entered: {line}\n"
                print(error_msg, end='')
                outfile.write(error_msg)

        infile.close()
        outfile.close()

    except FileNotFoundError:
        print("The file 'input.txt' was not found.")

if __name__ == "__main__":
    main()
