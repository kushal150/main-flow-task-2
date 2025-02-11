import math

def lcm_and_gcd(a, b):
   
    gcd = math.gcd(a, b)
    

    if gcd == 0:
        lcm = 0
    else:
        lcm = abs(a * b) // gcd
    
    return lcm, gcd

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm, gcd = lcm_and_gcd(a, b)
print(f"LCM of {a} and {b}: {lcm}")
print(f"GCD of {a} and {b}: {gcd}")