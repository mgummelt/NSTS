import fraction

class MixedNumber:
    def __init__(self, co=0, num=1, den=1):
        self.co = co
        self.f = fraction.Fraction(num, den)
    
    def DecValue(self):
        return self.ToFraction().DecValue()
    
    def ToFraction(self):
        if self.co < 0:
            return fraction.Fraction(self.co * self.f.denominator - self.f.numerator, self.f.denominator)
        else:
            return fraction.Fraction(self.co * self.f.denominator + self.f.numerator, self.f.denominator)
    
    def __eq__(self, m):
        return str(self) == str(m)
    
    def __str__(self):
        return ("" if self.co == 0 else str(self.co)) + ("" if str(self.f) == '0' else str(self.f))
    
def Subtract(m1, m2):
    return fraction.Subtract(m1.ToFraction(), m2.ToFraction()).ToMixedNumber()
 
def Add(m1, m2):
    return fraction.Add(m1.ToFraction(), m2.ToFraction()).ToMixedNumber()

def Multiply(m1, m2):
    return fraction.Multiply(m1.ToFraction(), m2.ToFraction()).ToMixedNumber()

def Divide(m1, m2):
    return fraction.Divide(m1.ToFraction(), m2.ToFraction()).ToMixedNumber()