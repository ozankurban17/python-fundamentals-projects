#Ozan Kurban
#This program calculates the final amount in a bank account using compound interest.
P = float(input("Enter the starting principal: "))
r = float(input("Enter the annual interest rate: "))
n = int(input("How many times per year is the interest compounded? "))
t = int(input("For how many years will the account earn interest? "))
r = r/100
A = P*(1+r/n)**(n*t)
print(f"at the end of {t} years you will have $ {A:,.2f} ")


