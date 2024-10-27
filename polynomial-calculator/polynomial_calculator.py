def find_factors(n):
    # Find factors of n, including both positive and negative factors
    factors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(-i)
    return factors

def possible_roots(coef):
    # Determine possible rational roots of the polynomial using the Rational Root Theorem
    poss_roots = []
    p = int(coef[-1]) # Constant term
    q = int(coef[0]) # Leading coefficient

    p_factors = find_factors(p)
    q_factors = find_factors(q)

    # Calculate all possible p/q values
    for p_factor in p_factors:
        for q_factor in q_factors:
            if q_factor != 0:
                poss_roots.append(p_factor / q_factor)
    
    # Remove duplicates
    poss_roots = list(set(poss_roots))
    print(f"\nThe possible roots are: {poss_roots}")
    return poss_roots

def newton(coef, power, guess):
    # Use Newton's method to find a root starting from an initial guess
    tolerance = 1e-10
    max_iterations = 1000
    x = guess
    
    for iteration in range(max_iterations):
        result1, result2 = 0, 0

        # Calculate p(x) and p'(x)
        for j in range(power + 1):
            result1 += coef[j] * (x ** (power - j)) # p(x)
        
            if power - j > 0:
                result2 += (coef[j] * (power - j)) * (x ** ((power - j) - 1)) # p'(x)
        
        if result2 == 0:
            print(f"Derivative is zero at x = {x}. Newton's method failed.")
            return None

        # Newton's formula: x_next = x - p(x) / p'(x)
        x_next = x - (result1 / result2)

        # Check the precision of the result
        if abs(x_next - x) < tolerance:
            return x_next
            
        x = x_next
        
    print("Maximum iterations reached.")
    return None  # If a solution is not found

def find_all_roots(coef, power):
    # Find all roots of the polynomial using possible rational roots and Newton's method
    possible_roots_list = possible_roots(coef)
    found_roots = []
    
    for guess in possible_roots_list:
        root = newton(coef, power, guess)
        if root is not None:
            root = round(root, 3)
            if root not in found_roots:
                found_roots.append(root)
    
    # Sort the found roots
    found_roots.sort()
    if found_roots:
        print(f"\nAll found roots: {found_roots}")
    else:
        print("\nNo roots found.")

def check_root(coef, power, root):
    # Check if a given value is a root of the polynomial
    result = 0

    # Calculate P(root)
    for j in range(power + 1):
        result += coef[j] * (root ** (power - j))

    print("\nTrue") if result == 0 else print("\nFalse")

def polynomial():
    # Main function to interact with the user and perform polynomial operations
    while True:
        power = int(input("Power: "))
        coef = []

        print("Enter coefficients starting from the highest power:")
        for i in range(power + 1):
            coef.append(float(input(f"Coefficient for x^{power - i}: ")))

        while True:
            # Display menu options to the user
            print("\n1. Check if value is a root.")
            print("2. Find all roots.")
            print("3. Enter a new polynomial")
            print("4. Exit")
            option = int(input("Choose an option:"))
            
            if option == 1:
                root = int(input("\nEnter value to check if it is a root: "))
                check_root(coef, power, root)
            elif option == 2:
                find_all_roots(coef, power)
            elif option == 3:
                break
            elif option == 4:
                return
            else:
                print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    polynomial()