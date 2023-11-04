from fractions import Fraction


class Rational:

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return int(self.__numerator)

    @property
    def denominator(self):
        return int(self.__denominator)

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __add__(self, otherfraction):
        if self.denominator == otherfraction.denominator:
            newnum = self.numerator + otherfraction.numerator
            newden = self.denominator

        else:
            newnum = (self.numerator * otherfraction.denominator) + (self.denominator * otherfraction.numerator)
            newden = self.denominator * otherfraction.denominator
        return Rational(newnum, newden)

    def __sub__(self, other):
        return Fraction(self.numerator, self.denominator) - Fraction(other.numerator, other.denominator)

    def __truediv__(self, other):
        # a / b: c / d = (a * d) / (b * c)
        return Rational(other.denominator * self.numerator, self.denominator * other.numerator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return Fraction(self.numerator, self.denominator) < Fraction(other.numerator, other.denominator)

    def __gt__(self, other):
        return Fraction(self.numerator, self.denominator) > Fraction(other.numerator, other.denominator)

    def __le__(self, other):
        return Fraction(self.numerator, self.denominator) <= Fraction(other.numerator, other.denominator)

    def __ge__(self, other):
        return Fraction(self.numerator, self.denominator) >= Fraction(other.numerator, other.denominator)

    def __ne__(self, other):
        return Fraction(self.numerator, self.denominator) != Fraction(other.numerator, other.denominator)


if __name__ == '__main__':
    r = Rational(1, 2)

    assert r.numerator == 1
    assert r.denominator == 2
    assert r.__str__() == '1 / 2'
    assert r == Rational(1, 2)
    assert Rational(1, 4) - Rational(1, 2) == -1 / 4
    assert Rational(2, 5) < Rational(3, 7)
    assert Rational(3, 5) != Rational(1, 9)
    assert Rational(1, 2) > Rational(1, 5)
    assert Rational(3, 5) / Rational(4, 9) == Rational(27,20)
    print(Rational(4,20) + Rational(3,10))