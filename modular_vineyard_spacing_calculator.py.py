# Name: Ozan Kurban
# This function calculates the number of vines based on the row length and adjusted values
def calculate_vines(R, E_adj, S_adj):
    V = (R - 2 * E_adj) / S_adj
    return V

# This function prints the E-V-E visual representation based on vine count
def print_visual(V):
    print('E', end="")
    for count in range(int(V)):
        print("V", end="")
    print("E")

def main():
    keep_going = 'y'
    
    while keep_going == 'y':
        R = float(input("Enter the length of the row in feet: "))
        E = float(input("Enter the amount of space in feet used by an end-post assembly: "))
        S = float(input("Enter the space between the vines in feet: "))

        # Store original values for the output message
        E_orig = E
        S_orig = S

        # Adjust E based on row length
        E_adj = E 
        if R <= 55:
            E_adj = E / 2
        elif R >= 120:
            E_adj = E * 1.5
            
        # Adjust S based on row length
        S_adj = S
        if R < 50:
            S_adj = S * 2
        elif R > 125:
            S_adj = S / 2
            
        # Call the value-returning function to calculate V
        V = calculate_vines(R, E_adj, S_adj)

        # Print formatted output with 2 decimal places
        print(f"\nA row {R:.2f} ft long with {E_orig:.2f} ft end-posts and vines {S_orig:.2f} ft apart")
        print(f"has been adjusted to {E_adj:.2f} ft end-posts {S_adj:.2f} ft apart and requires {V:.2f} vines")
        
        # Call the non-value returning function to print the visual
        print_visual(V)
        
        # Loop control with validation for y/n
        keep_going = input('\nWould you like to run the program again? (y/n): ').lower()
        while keep_going not in ['y', 'n']:
            keep_going = input('Please enter "y" or "n": ').lower()

# Execute the main function
if __name__ == "__main__":
    main()
