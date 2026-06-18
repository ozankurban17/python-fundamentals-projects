#Ozan Kurban
#This program calculates how many grapevines fit in a row

R = float(input("Enter the length of the row in feet "))
E = float(input("Enter the amount of space in feet used by an end-post assembly "))
S = float(input("Enter the space between the vines in feet "))
V = (R - 2*E)/S
print(f" A row {R} ft long, with {E} ft end-posts and vines {S} ft apart will require {int(V)} vines ")



