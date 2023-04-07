def add(x: float) -> float:
    """Exponentiation of a number"""
    def exponentiate(y: float) -> float:
        exp = pow(x, y)
        if str(exp).endswith('.0'):
            return int(exp)
        else:
            return exp
    return exponentiate


print("A program for exponentiation of a number")

pow_number = add(float(input("Write the number: ")))
result = pow_number((float(input("Write the degree: "))))

print(f"The result is: {result}")