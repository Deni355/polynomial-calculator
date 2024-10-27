import numpy as np

def find_all_roots(coef):
    # Find the roots of the polynomial with given coefficients
    roots = np.roots(coef)
    found_roots = []
    
    for root in roots:
        # Check if the imaginary part of the root is negligible
        if abs(root.imag) < 1e-10:
            found_root = round(root.real, 3) # Round to 3 d.p.
            # Add the root to the list if it's not already present
            if found_root not in found_roots:
                found_roots.append(found_root)

    # Sort the found roots
    found_roots.sort()
    if found_roots:
        print(f"\nAll found roots: {', '.join(map(str, found_roots))}")
    else:
        print("\nNo roots found.")

def check_root(coef, root):
    # Evaluate the polynomial at the given root
    result = np.polyval(coef, root)
    # Print True if the result is close to zero, otherwise print False
    print("\nTrue") if abs(result) < 1e-10 else print("\nFalse")

def polynomial():
    while True:
        # Get the power of the polynomial from the user
        print("\nWrite the polynomial")
        power = int(input("Power: "))
        coef = []

        print("Enter coefficients starting from the highest power:")
        for i in range(power + 1):
            # Get each coefficient from the user
            coef.append(float(input(f"Coefficient for x^{power - i}: ")))

        # Convert coefficients to numpy array
        coef = np.array(coef)

        while True:
            # Display menu options to the user
            print("\n1. Check if value is a root.")
            print("2. Find all roots.")
            print("3. Enter a new polynomial")
            print("4. Exit")
            option = int(input("Choose an option:"))
            
            if option == 1:
                root = int(input("\nEnter value to check if it is a root: "))
                check_root(coef, root)
            elif option == 2:
                find_all_roots(coef)
            elif option == 3:
                break
            elif option == 4:
                return
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    # Run the polynomial function if the script is executed directly
    polynomial()