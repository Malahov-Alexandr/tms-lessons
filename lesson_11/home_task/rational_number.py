class Rational:

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator, self.__denominator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'


    # TODO
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

r = Rational(1,2)
print(r)