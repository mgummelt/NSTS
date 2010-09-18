import random
import fraction
from fraction import Fraction

isPrime = [True] * 10000
primes = [] 
nouns = ["penguins", "cans", "donuts", "pens", "pencils", "tires", "rolls", "loaves of bread", 
         "computers", "widgets", "folders", "backpacks", "notebooks", "pieces of paper",
         "laptops", "CDs", "cards", "eggs", "gallons of milk", "dogs", "toothbrushes", 
         "gallons of gas", "books"]
singNouns = ["penguin", "can", "donut", "pen", "pencil", "tire", "roll", "loaf of bread", 
             "computer", "widget", "folder", "backpack", "notebook", "piece of paper", "laptop", 
             "CD", "card", "egg", "gallon of milk", "dog", "toothbrush", "gallon of gas","book"]
        

class Category:
    categories = []
    def __init__(self, func, name, data):
        self.func = func
        self.name = name
        self.data = data

class Polygon:
    names = ['point', 'line', 'triangle', 'quadrilateral', 'pentagon', \
             'hexagon', 'septagon', 'octagon', 'nonagon', 'decagon', 
             'undecagon', 'dodecagon']
    def __init__(self, numsides=1):
        self.name = Polygon.names[numsides-1]
        self.numsides = numsides
    def __str__(self):
        return self.name
    
class PrimeFact:
    def __init__(self, x):
        self.powers, self.divisors = [], []
        if len(utility.primes) == 0:
            utility.initPrimes()
        for i in utility.primes:
            if i > x: break
            if x%i!=0: continue
            temp, pow = i, 1
            while True:
                if x % (temp*i) != 0:
                    break
                temp*=i
                pow+=1
            pow-=1
            divisors.append(i)
            powers.append(pow)
            
class Cubic:
    def __init__(self, A=0, B=0, C=0, D=0):
        self.A, self.B, self.C, self.D = A, B, C, D
    def __str__(self):
        p = Polynomial(4)
        p.coeff = [self.A,self.B,self.C,self.D]
        return str(p)
    def Evaluate(self, num):
        return self.A*(num**3) + self.B*(num**2) + self.C*num + self.D
    def Derivative(self):
        return Quadratic(self.A*3, self.B*2, self.C)

class Quadratic:
    def __init__(self, A=0, B=0, C=0):
        self.A, self.B, self.C = A, B, C
    def __str__(self):
        p = Polynomial(3)
        p.coeff = [self.A,self.B,self.C]
        return str(p)
    def Evaluate(self, num):
        return self.A * num * num + self.B * num + self.C
    def Derivative(self):
        return Linear(2*self.A, self.B)

class Linear:
    def __init__(self, A = 0, B = 0):
        self.A, self.B = A, B
    def __str__(self):
        return self.ToString('x')
    def ToString(self, diffVar):
        p = Polynomial(2)
        p.coeff[0], p.coeff[1] = self.A, self.B
        return p.ToString(diffVar)
    def Evaluate(self, num):
        return self.A*num + self.B
    
class Polynomial:
    def __init__(self, x = 0):
        self.coeff = [0] * x
    def __str__(self):
        return self.ToString('x')
    def ToString(self, diffVar):
        ret = ''
        if len(self.coeff) == 0: return ret
        
        for i in range(len(self.coeff)):
            if self.coeff[i] == 0: continue
            b = False
            for j in range(i):
                if self.coeff[j] != 0: b = True
            if not b:
                if self.coeff[i] < 0: ret += '-'
            else:
                ret += ' - ' if self.coeff[i] < 0 else ' + '
            if abs(self.coeff[i]) != 1 or i == len(self.coeff) - 1: ret += str(abs(self.coeff[i]))
            if i == len(self.coeff) - 2: ret += diffVar
            elif i < len(self.coeff) - 2: ret += str(diffVar) + '^' + str(len(self.coeff) - i - 1)
            
        return ret
    def Evaluate(self, eval):
        ret = 0
        for i in range(len(self.coeff)):
            ret += (eval**(len(self.coeff)-i-1)) * self.coeff[i]
        return ret

class PrimeFact:
    def __init__(self, x = 0):
        self.divisors = []
        self.powers = []
        if len(primes) == 0:
            InitPrimes()
        for j in range(len(primes)):
            i = primes[j]
            if i > x:
                break
            if x%i != 0:
                break
            temp, pow = i, i
            while True:
                if x % (temp * i) != 0:
                    break
                temp *= i
                pow += 1
            pow -= 1
            self.divisors.append(i)
            self.powers.append(pow)

class Line:
    def __init__(self, s, y):
        self.slope = s
        self.yInter = y
    def __str__(self):
        type = random.randint(0, 4)
        if type == 0:
            yInter2 = Fraction(abs(self.yInter.numerator), self.yInter.denominator)
            return 'y = ' + ('' if self.slope.numerator == 0 else self.slope.ToStringAddNum('x')) + \
                   ('' if self.yInter.numerator == 0 else ((' - ' + str(yInter2)) if self.yInter.numerator < 0 else (' + ' + str(yInter2))))
        elif type < 3:
            lcm = LCM(self.slope.denominator, self.yInter.denominator)
            A = self.slope.numerator * lcm / self.slope.denominator
            B = lcm
            C = self.yInter.numerator * lcm / self.yInter.denominator
            A *= -1
            if A < 0:
                A *= -1
                B *= -1
                C *= -1
            if random.randint(0, 1):
                return ('-' if A == -1 else ('' if A == 1 else str(A))) + 'x' + (' - ' if B < 0 else ' + ') + \
                       ('' if abs(B) == 1 else str(abs(B))) + 'y = ' + str(C)
            else:
                return str(C) + ' = ' + ('-' if A == -1 else ('' if A == 1 else str(A))) + 'x' + (' - ' if B < 0 else ' + ') + \
                       ('' if abs(B) == 1 else str(abs(B))) + 'y'
        elif type < 5:
            multDen = random.randint(2, 8)
            multNum = random.randint(1, multDen - 1)
            mult = Fraction(multNum, multDen)
            X = fraction.Multiply(mult, self.slope)
            con = fraction.Multiply(mult, self.yInter)
            
            if random.randint(0, 1):
                return mult.ToStringAddNum('y') + ' = ' + ('' if X.numerator == 0 else X.ToStringAddNum('x')) + \
                       ('' if con.numerator == 0 else ((' - ' + str(Fraction(-con.numerator, con.denominator))) if con.numerator < 0 else (' + ' + str(con))))
            else:
                X.numerator *= -1
                return ('' if X.numerator == 0 else X.ToStringAddNum('x')) + ' + ' + mult.ToStringAddNum('y') + ' = ' + str(con)
        return '-1'

def initPrimes():
    isPrime[0] = isPrime[1] = False
    for i in range(2, len(isPrime)):
        if not isPrime[i]: 
            continue
        for j in range(i*2, len(isPrime), i): 
            isPrime[j] = False
    primes.extend(x for x in range(len(isPrime)) if isPrime[x])

def GCD(x, y):
    if x == 0 or y == 0: return 1
    x, y = abs(x), abs(y)
    
    if x < y:
        temp = y
        y = x
        x = temp
    
    while x%y!=0:
        temp = x%y
        x = y
        y = temp
        
    return y

def LCM(x, y):
    return x * y / GCD(x, y)

def DoubleToAns(d):
    ans = str(d)
    if ans.find('.') >= 0: ans = ans.lstrip('0')
    return ans 

def Factors(x):
    ret = []
    if x < 0:
        ret = map(lambda x : -x, Factors(-x))
    else:
        for i in range(1, x+1):
            if x % i == 0:
                ret.append(i)
    return ret

def Decimalize(a):
    l = len(str(a))
    div = 10**random.randint(1, l+1)
    return float(a) / div

def Rearrange(b):
    ret, s = 0, str(b)
    l = len(s)
    used = [False] * l
    for i in range(l):
        index = random.randint(0, l - 1)
        while used[index]:
            index = random.randint(0, l-1)
        if not used[index]:
            ret = ret * 10 + int(s[index])
            used[index] = True
    return ret

def ChangeToBase(num, fromBase, toBase):
    neg = False
    if num < 0:
        num *= -1
        neg = True
    base10, pow = 0, 0
    while num!=0:
        base10 += (num%10) * (fromBase**pow)
        pow+=1
        num /= 10
    pow, ret = 0, 0
    while base10 != 0:
        ret = (10**pow) * (base10%toBase)
        base10/=toBase
    if neg:ret*=-1
    return ret

def Comb(big, small):
    return Factorial(big) / (Factorial(small) * Factorial(big-small))

def Perm(big, small):
    return Factorial(big) / Factorial(big-small)

def Factorial(num):
    ret = 1
    for i in range(2, num+1): ret *= i
    return ret

def ChangeToRoman(num):
    one = num%10
    num/=10
    ten = num%10
    num/=10
    hun = num%10
    num/=10
    tho = num%10
    strTho = ['', 'M', 'MM', 'MMM'][tho]
    strHun = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'][hun]
    strTen = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'][ten]
    strOne = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][one]
    return strTho + strHun + strTen + strOne

def SquareRoot(num):
    if num == 1: return '1'
    coeff, inThere = 1, num
    b = False
    while True:
        b = False
        i = 2
        while i*i <= num:
            if num%(i*i) == 0:
                coeff *= i
                num /= (i*i)
                b = True
            i+=1
        if not b : break
    return ("" if coeff == 1 else str(coeff)) + ("" if num == 1 else '\\sqrt{' + str(num) + '}')

def RefAngle(theta):
    while theta < 0: theta += 360
    while theta > 180: theta -= 180
    if theta > 90: theta = 180 - theta
    return theta

def DegToPolar(num):
    return Fraction(num, 180).ToStringAddNum('\\pi')

def CommonDecimal():
    d = [.5, .25, .2, .125, .1]
    return d[random.randint(0, len(d)-1)]

def ToFraction(d):
    for i in range(1, 20):
        for j in range(1, 20):
            if abs(float(i) / j - d) < 1e-7:
                return Fraction(i, j)
    return Fraction(-1, 1)

def rationalDen():
    ret = [2, 4, 5, 8, 10, 16]
    return ret[random.randint(0, len(ret)-1)]

def isPowerOf10(num):
    for i in range(10):
        if 10**i==num:
            return True
    return False

def nextIntLess(num, min, prob):
    if num <= min:
        return min
    if random.random() < prob:
        return num
    return nextIntLess(num-1, min, prob)

def nextIntGreater(num, max, prob):
    for i in range(100000):pass
    if num >= max:
        return max
    r = random.random()
    if r < prob:
        return num
    return nextIntGreater(num+1, max, prob)

def triangular(num):
    ret = 0
    for i in range(1, num + 1):
        ret += i
    return ret

def fracNum(maxDigs):
    den = random.randint(2, 10)
    num = random.randint(1, den-1)
    return int(float(num) / den * (10 ** random.randint(1, maxDigs)))

def goodTrigFrac():
    validDen = range(1, 7)
    den = validDen[random.randint(0, len(validDen)-1)]
    num = random.randint(-den * 3, den * 3)
    if random.randint(0, 1):
        num = random.randint(-den * 2, den * 2)
    else:
        num = random.randint(-den, den)
    return Fraction(num, den)