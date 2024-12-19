class Polynomial:
    def __init__(self, coefficients):
        self._coefficients = coefficients

    @property
    def degree(self):
        return len(self._coefficients) - 1

    def __repr__(self):
        term = []
        for i, coef in enumerate(reversed(self._coefficients)):
            if coef == 0:
                continue
            pow = self.degree - i
            if pow == 0:
                term.append(f"{coef}")
            elif pow == 1:
                term.append(f"{coef}x")
            else:
                term.append(f"{coef}x^{pow}")
        return " + ".join(term) if term else "0"

    def __call__(self, x):
        return self.evaluate(x)

    def __add__(self, other):
        max_l = max(self.degree, other.degree) + 1
        n_coef = [0] * max_l
        for i in range(len(self._coefficients)):
            n_coef[i] += self._coefficients[i]
        for i in range(len(other._coefficients)):
            n_coef[i] += other._coefficients[i]
        return Polynomial(n_coef)

    def __sub__(self, other):
        max_l = max(self.degree, other.degree) + 1
        new_coef = [0] * max_l
        for i in range(len(self._coefficients)):
            new_coef[i] += self._coefficients[i]
        for i in range(len(other._coefficients)):
            new_coef[i] -= other._coefficients[i]
        return Polynomial(new_coef)

    def __mul__(self, other):
        new_coef = [0] * (self.degree + other.degree + 1)
        for i in range(len(self._coefficients)):
            for j in range(len(other._coefficients)):
                new_coef[i + j] += self._coefficients[i] * other._coefficients[j]
        return Polynomial(new_coef)

    def derivative(self):
        if self.degree == 0:
            return Polynomial([0])
        d_coef = [self._coefficients[i] * i for i in range(1, len(self._coefficients))]
        return Polynomial(d_coef)

    def evaluate(self, x):
        result = 0
        for i, cf in enumerate(self._coefficients):
            result += cf * (x ** i)
        return result


class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        super().__init__(coefficients)

    def discriminant(self):
        a, b, c = self._coefficients
        return b ** 2 - 4 * a * c

    def find_roots(self):
        c, b, a = self._coefficients
        disc = self.discriminant()
        root1 = (-b + disc ** 0.5) / (2 * a)
        root2 = (-b - disc ** 0.5) / (2 * a)
        return root1, root2


# Пример использования
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([0, -1, 1])
quadraticpolynom = QuadraticPolynomial([1, -3, 2])
print("P1:", p1) 
print("P2:", p2) 
print("P1 + P2:", p1 + p2)
print("P1 - P2:", p1 - p2)  
print("P1 * P2:", p1 * p2)  
print("P1(2):", p1(2)) 
print("P1 derivative:", p1.derivative())
print('Discriminant:', test.discriminant())
print('Roots:', test.find_roots())
