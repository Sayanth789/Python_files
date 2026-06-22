import math 

def check_prime(number: int) -> str:
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return f'No {number} is not a prime it can be divided by {i}' 
        return f'yes {number} is a prime ....!' 
    
print(f"check_prime(10,000,000) = {check_prime(10_000_000)}")
print(f"check_prime(10,000,019) = {check_prime(10_000_019)}")
