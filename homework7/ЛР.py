class Polynomial:
    def __init__(self, coefficients):
        self._coefficients = coefficients[::-1]

    @property
    def degree(self):
        return len(self._coefficients) - 1

    def __repr__(self):
        terms = []
        for i, coeff in enumerate(self._coefficients):
            if coeff == 0:
                continue
            power = self.degree - i
            term = f"{coeff}*x^{power}" if power != 0 else f"{coeff}"
            terms.append(term)
        return " + ".join(terms) if terms else "0"

    def __call__(self, x):
        return self.evaluate(x)

    def __add__(self, other):
        max_len = max(len(self._coefficients), len(other._coefficients))
        result_coeffs = [0] * max_len
        for i in range(max_len):
            coeff1 = self._coefficients[i] if i < len(self._coefficients) else 0
            coeff2 = other._coefficients[i] if i < len(other._coefficients) else 0
            result_coeffs[i] = coeff1 + coeff2
        return Polynomial(result_coeffs[::-1])

    def __sub__(self, other):
        max_len = max(len(self._coefficients), len(other._coefficients))
        result_coeffs = [0] * max_len
        for i in range(max_len):
            coeff1 = self._coefficients[i] if i < len(self._coefficients) else 0
            coeff2 = other._coefficients[i] if i < len(other._coefficients) else 0
            result_coeffs[i] = coeff1 - coeff2
        return Polynomial(result_coeffs[::-1])

    def __mul__(self, other):
        result_coeffs = [0] * (len(self._coefficients) + len(other._coefficients) - 1)
        for i, coeff1 in enumerate(self._coefficients):
            for j, coeff2 in enumerate(other._coefficients):
                result_coeffs[i + j] += coeff1 * coeff2
        return Polynomial(result_coeffs[::-1])

    def derivative(self):
        if self.degree == 0:
            return Polynomial([0])
        deriv_coeffs = [self._coefficients[i] * (self.degree - i) for i in range(self.degree)]
        return Polynomial(deriv_coeffs[::-1])

    def evaluate(self, x):
        result = 0
        for coeff in self._coefficients:
            result = result * x + coeff
        return result

class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        super().__init__(coefficients)

    def discriminant(self):
        a, b, c = self._coefficients
        return b ** 2 - 4 * a * c

    def find_roots(self):
        a, b, c = self._coefficients
        disc = self.discriminant()
        root1 = (-b + disc ** 0.5) / (2 * a)
        root2 = (-b - disc ** 0.5) / (2 * a)
        return root1, root2

