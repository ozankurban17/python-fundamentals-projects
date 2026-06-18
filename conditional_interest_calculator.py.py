#Ozan Kurban
#This program calculates the final amount in a bank account using compound interest.
P = float(input("Enter the starting principal: "))
r = float(input("Enter the annual interest rate: "))
n = int(input("How many times per year is the interest compounded? "))
t = int(input("For how many years will the account earn interest? "))
r = r / 100

r_orig = r

if P >= 5100 and P <= 11000:
    r = r + 0.005
elif P >= 11001 and P <=60000:
    r = r + 0.0075
elif P > 60000:
    r = r + 0.0125
    
A = P*(1+r/n)**(n*t)


if t  >= 12 and r_orig >= .06:
    A = A + P*0.01*t
    
if r_orig > 0.11:
    
    A = A + 75

print(f"at the end of {t} years you will have $ {A:,.2f} ")


