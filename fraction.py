import mixedNumber
import random
import utility

class Fraction:
    def __init__(self, num=1, den=1, reduce=True):
        self.numerator   = num
        self.denominator = den
        if reduce: self.Reduce()
    
    def isReduced(self):
        return utility.GCD(self.numerator, self.denominator) == 1
    
    def Reduce(self):
        gcd = utility.GCD(self.numerator, self.denominator)
        self.numerator   /= gcd
        self.denominator /= gcd
        if self.denominator < 0:
            self.numerator   *= -1
            self.denominator *= -1
    
    def canBeDecimal(self):
        self.Reduce()
        return len(str(self.DecValue())) <= 5
    
    def __str__(self):
        self.Reduce()
        if self.numerator   == 0 : return '0'
        if self.denominator == 1 : return str(self.numerator)
        if self.numerator == self.denominator : return '1'
        return '\\displaystyle\\frac{%d}{%d}' % (self.numerator, self.denominator)
        
    def ToStringNoDisp(self):
        self.Reduce()
        if self.numerator   == 0 : return '0'
        if self.denominator == 1 : return str(self.numerator)
        if self.numerator == self.denominator : return '1'
        return '\\frac{%d}{%d}' % (self.numerator, self.denominator)
    
    def ToStringPossDec(self, d):
        if (len(str(float(self.numerator) / self.denominator)) < 5 and random.random() < d):
            return str(float(self.numerator) / self.denominator)
        return str(self)
    
    def DecValue(self):
        return float(self.numerator) / self.denominator
    
    def ToStringAddNum(self, num):
        self.Reduce()
        if self.numerator == 0 : return '0'
        if self.numerator == -1 and self.denominator == 1 : return '-' + num
        if self.numerator == self.denominator : return num
        if self.denominator == 1 : return str(self.numerator) + num
        if self.numerator == -1 : return '\\displaystyle\\frac{-%s}{%d}' % (num, self.denominator)
        if self.numerator == 1 : return '\\displaystyle\\frac{%s}{%d}' % (num, self.denominator)
        return '\\displaystyle\\frac{%d%s}{%d}' % (self.numerator, num, self.denominator)
    
    def ToStringAns(self):
        ret = str(self)
        if (abs(self.numerator) > self.denominator) and (str(self.ToMixedNumber()) != str(self)) :
            ret += '$ or $%s' % (self.ToMixedNumber())
        if (str(self.DecValue()).find('.') < 0 or \
            len(str(self.DecValue())[str(self.DecValue()).find('.'):]) <= 5) and \
           (str(self.DecValue()) != str(self)):
            ret += '$ or $%s' % (utility.DoubleToAns(self.DecValue()))
        return ret  
    
    def __eq__(self, f):
        return str(self) == str(f)
    
    def ToMixedNumber(self):
        tempNum, tempDen = abs(self.numerator), abs(self.denominator)
        ret = mixedNumber.MixedNumber(tempNum / tempDen, tempNum % tempDen, tempDen)
        if self.numerator * self.denominator < 0:
            ret.co *= -1
        if (self.numerator * self.denominator < 0) and (abs(self.numerator) < abs(self.denominator)):
            ret.f.numerator *= -1
        return ret
    
    def ToPercent(self):
        f = Fraction(self.numerator * 100, self.denominator)
        return '%s\\%%' % (str(f.ToMixedNumber()))
        
    
    
def Subtract(f1, f2):
    return Fraction(f2.denominator*f1.numerator - f1.denominator*f2.numerator, f1.denominator * f2.denominator)
            
def Multiply(f1, f2):
    return Fraction(f1.numerator * f2.numerator, f1.denominator * f2.denominator)
    
def Divide(f1, f2):
    return Multiply(f1, Fraction(f2.denominator, f2.numerator))

def Add(f1, f2):
    return Fraction(f2.denominator * f1.numerator + f1.denominator * f2.numerator, f1.denominator * f2.denominator)

def LessThan1Fraction(numMax, denMax):
    num, den = random.randint(1, numMax-1), random.randint(1, denMax-1)
    while num >= den:
        num, den = random.randint(1, numMax-1), random.randint(1, denMax-1)
    return Fraction(num, den)
        
    