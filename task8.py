def is_armstrong(n):
    digits = str(n)
    num_digits = len(digits)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == n
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
