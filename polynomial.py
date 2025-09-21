import math

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        result = 0

        for i, coeff in enumerate(reversed(self.coefficients)):
            result += coeff * (x ** i)
        
        return result
    
    def add(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len

        for i in range(len(self.coefficients)):
            new_coeffs[max_len - len(self.coefficients) + i] += self.coefficients[i]

        for i in range(len(other.coefficients)):
            new_coeffs[max_len - len(other.coefficients) + i] += other.coefficients[i]

        return Polynomial(new_coeffs)
    
    def subtract(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len

        for i in range(len(self.coefficients)):
            new_coeffs[max_len - len(self.coefficients) + i] += self.coefficients[i]

        for i in range(len(other.coefficients)):
            new_coeffs[max_len - len(other.coefficients) + i] -= other.coefficients[i]

        return Polynomial(new_coeffs)
    
    def __str__(self):
        terms = []
        for i, coeff in enumerate(reversed(self.coefficients)):
            if coeff != 0:  # Skip if coefficient is zero
                term = f"{coeff}" if i == 0 else (f"{coeff}x^{i}" if i > 1 else f"{coeff}x")
                terms.append(term)
        return " + ".join(terms[::-1]) if terms else "0"
