#Ozan Kurban
R = float(input("Enter the length of the row in feet "))
E = float(input("Enter the amount of space in feet used by an end-post assembly "))
S = float(input("Enter the space between the vines in feet "))
E_orig = E
S_orig = S

E_adj = E 
if R <= 55 :
    E_adj = E/2
elif R >= 120 :
    E_adj = E*1.5
    
S_adj = S
if R < 50 :
    S_adj = S*2
elif R > 125 :
    S_adj = S/2
    
V = (R - 2*E_adj)/S_adj

print(f" A row {R:.1f} ft long, with {E_orig:.1f} ft end-posts and vines {S_orig:.1f} ft apart has been adjusted to {E_adj:.1f} ft end-posts and vines {S_adj:.1f} ft apart and requires {V:.1f} vines ")



