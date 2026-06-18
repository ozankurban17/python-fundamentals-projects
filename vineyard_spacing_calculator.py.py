#Ozan Kurban
# This program calculates the number of grapevines that will fit in a vineyard row, 
# dynamically adjusting post and vine spacing based on the total row length.
keep_going='y'
# Main application loop for continuous calculations
while keep_going == 'y':
    R = float(input("Enter the length of the row in feet "))
    E = float(input("Enter the amount of space in feet used by an end-post assembly "))
    S = float(input("Enter the space between the vines in feet "))
# Preserve original inputs for the final summary print
    E_orig = E
    S_orig = S
# Adjust end-post assembly spacing based on specific row length thresholds
    E_adj = E 
    if R <= 55 :
        E_adj = E/2
    elif R >= 120 :
        E_adj = E*1.5
# Adjust individual vine spacing based on specific row length thresholds       
    S_adj = S
    if R < 50 :
        S_adj = S*2
    elif R > 125 :
        S_adj = S/2
# Apply the standard vineyard capacity formula with adjusted variables        
    V = (R - 2*E_adj)/S_adj
    # Output the calculated results with precise float formatting
    print(f" A row {R:.2f} ft long, with {E_orig:.2f} ft end-posts and vines {S_orig:.2f} ft apart has been adjusted to {E_adj:.2f} ft end-posts and vines {S_adj:.2f} ft apart and requires {V:.2f} vines ")
# Generate a visual text representation of the row structure (e.g., EVVVVVE)
    print('E',end="")
    for count in range(int(V)):
        print("V",end="")
    print("E")
# Check if the user wants to perform another simulation
    keep_going = input('Would you like to run the program again? (y/n) ')



