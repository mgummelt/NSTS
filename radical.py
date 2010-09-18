from fraction import Fraction

class Radical:
    def __init__(self, num=1, den=1, rad=1):
        self.co = Fraction(num, den)
        self.rad = 1
        self.Reduce()
    def Reduce(self):
        b = False
        self.co.Reduce()
        while True:
            b = False
            i = 2
            while i*i <= self.rad:
                if self.rad % (i*i) == 0:
                    self.co.numerator *= i
                    self.rad /= (i*i)
                    b = True
                i+=1
            if not b: break
            
    def __eq__(self, obj):
        return str(self) == str(obj)
    
    def __str__(self):
        self.Reduce()
        sRad = "" if self.rad == 1 else '\\sqrt{' + str(self.rad) + '}'
        if self.co.numerator == 0 or self.rad == 0:
            return '0'
        if self.co.denominator == 1:
            if self.co.numerator == 1 and self.rad == 1:
                return '1'
            if self.co.numerator == -1 and self.rad == 1:
                return '-1'
            if self.co.numerator == 1:
                return sRad
            if self.co.numerator == -1:
                return '-' + sRad
            return str(self.co.numerator) + sRad
        else:
            if abs(self.co.numerator) == 1 and self.rad == 1:
                return str(self.co)
            if self.co.numerator == 1:
                return '\\displaystyle\\frac{' + sRad + '}{' + str(self.co.denominator) + '}'
            if self.co.numerator == -1:
                return '\\displaystyle\\frac{-' + str(self.co.numerator) + sRad + '}{' + str(self.co.denominator) + '}'
            return '\\displaystyle\\frac{' + str(self.co.numerator) + sRad + '}{' + str(self.co.denominator) + '}'
    
    def ToStringNoDisp(self):
        self.Reduce()
        sRad = "" if self.rad == 1 else '\\sqrt{' + str(self.rad) + '}'
        if self.co.numerator == 0 or self.rad == 0:
            return '0'
        if self.co.denominator == 1:
            if self.co.numerator == 1 and self.rad == 1:
                return '1'
            if self.co.numerator == -1 and self.rad == 1:
                return '-1'
            if self.co.numerator == 1:
                return sRad
            if self.co.numerator == -1:
                return '-' + sRad
            return self.co.numerator + sRad
        else:
            if abs(self.co.numerator) == 1 and self.rad == 1:
                return str(self.co)
            if self.co.numerator == 1:
                return '\\frac{' + sRad + '}{' + str(self.co.denominator) + '}'
            if self.co.numerator == -1:
                return '\\frac{-' + sRad + '}{' + str(self.co.denominator) + '}'
            return '\\frac{' + str(self.co.numerator) + sRad + '}{' + str(self.co.denominator) + '}'
        

def Divide(r1, r2):
    return Radical(r1.co.numerator * r2.co.denominator, r1.co.denominator * r2.co.numerator * r2.rad, r1.rad * r2.rad)

def Multiply(r1, r2):
    return Radical(r1.co.numerator * r2.co.numerator, r1.co.denominator * r2.co.denominator, r1.rad * r2.rad)   
    