import random, math, string, datetime
import utility, fraction, mixedNumber, radical, day, trig, estimations
from utility import Quadratic, Cubic, Linear, PrimeFact, Polynomial, Line
from fraction import Fraction
from mixedNumber import MixedNumber
from radical import Radical
from utility import Polygon
from day import Day

def SumOfPosIntDiv(probNum):
    question, answer, end = '', '', ''
    isProper = False
    rand = random.randint(0, 3)
    
    if probNum < 30:
        if rand == 0 : isProper = True
        else         : isProper = False
    else:
        if rand == 0 : isProper = False
        else         : isProper = True
    
    num = 2
    while(utility.isPrime[num]):
        num = random.randint(20, 99)

    ans = 0
    
    if isProper:
        question = 'The sum of the proper positive integral divisors of $%d$ is ' % (num)
    else:
        question = 'The sum of the positive integral divisors of $%d$ is ' % (num)
    
    for i in range(1, num+1):
        if num % i == 0:
            ans += i
    
    if isProper: ans -= num
    
    answer = '$%d$' % (ans)
    return [question, answer, end]

def XsquaredPlusX(probNum):
    question, answer, end = '', '', ''
    num = random.randint(15, 99)
    while num % 5 != 4: 
        num += 1
    answer = str(num**2 + num)
    question = '$%d ^ 2 + %d = $' % (num, num)
    return [question, answer, end]

def RelativelyPrime(probNum):
    question, answer, end = '', '', ''
    num  = random.randint(10, 49)
    rand = random.randint(0, 3)
    
    if probNum < 40:
        if rand == 0 : isSum = True
        else         : isSum = False
    else:
        if rand == 0 : isSum = False
        else         : isSum = True
    
    if isSum:
        question = 'The sum of the positive integers less than $%d$ and relatively prime to $%d$ is' % (num, num)
    else:
        question = 'How many positive integers less than $%d$ are relatively prime to $%d$?' % (num, num)
    
    relPrime = []
    for i in range(1, num):
        if utility.GCD(num, 1) == 1:
            relPrime.append(i)
    
    ans = 0
    if isSum:
        for x in relPrime:
            ans+=x
    else:
        ans = len(relPrime)
    
    answer = '$%d$' % (ans)
    return [question, answer, end]

def RepeatingDecimalToFraction(probNum):
    question, answer, end = '', '', ''
    numDig = random.randint(1, 3)
    num = 0
    strNum = ''
    
    if numDig == 1:
        num = random.randint(1, 9)
        strNum = str(num)
    elif numDig == 2:
        num = random.randint(1, 99)
        strNum = str(num)
        if num < 10: strNum = '0' + strNum
    elif numDig == 3:
        num = random.randint(1, 999)
        strNum = str(num)
        if num < 100: '0' + strNum
        if num < 10:  '0' + strNum
    
    rep = strNum
    offSet = random.randint(0, 1) == 0
    off = 0
    if offSet and len(strNum) < 3:
        off = random.randint(1, 9)
        strNum = str(off) + strNum
    else: 
        offSet = False
    
    addZero = random.randint(0, 2) == 0
    if addZero and len(strNum) < 3:
        strNum = '0' + strNum
    else: addZero = False
    
    question = '$.%s%s%s... =$' % (strNum, rep, rep)
    end = '(fraction)'
    f = Fraction()
    
    if numDig == 1 and not offSet and not addZero:
        f.numerator = num
        f.denominator = 9
    elif numDig == 1 and not offSet and addZero:
        f.numerator = num
        f.denominator = 90
    elif numDig == 1 and offSet and not addZero:
        f.numerator = off * 10 + num - off
        f.denominator = 99
    elif numDig == 1 and offSet and addZero:
        f.numerator = off * 10 + num - off
        f.denominator = 900
    elif numDig == 2 and offSet and not addZero:
        f.numerator = off * 100 + num - off
        f.denominator = 990
    elif numDig == 2 and not offSet and not addZero:
        f.numerator = num
        f.denominator = 99
    elif numDig == 2 and not offSet and addZero:
        f.numerator = num
        f.denominator = 990
    elif numDig == 3:
        f.numerator = num
        f.denominator = 999
    f.Reduce()
   
    answer = '$%s$' % (str(f))
    return [question, answer, end] 

def Squares(probNum):
    question, answer, end = '', '', ''
    d2 = probNum <= 40
    if probNum > 40: 
        d2 = random.randint(0, 9) == 0
    num = 0
    
    if d2:
        num = random.randint(11, 50)
    else:
        num = random.randint(1, 9) * 100
        b = random.randint(0, 1) == 0
        if b: num += num/100
        else: num += random.randint(1, 24)
    
    bp = random.randint(0, 1) == 0
    if bp:
        question = '$%d ^ 2 =$' % (num)
    else:
        question = '$%d \\times %d = $' % (num, num)
    answer = str(num * num)
    return [question, answer, end]

def SubSets(probNum):
    question, answer, end = '', '', ''
    words = ['MATH', 'NUMBER', 'FOUR', 'FIVE', 'NEWTON', 'TRIANGLE', 'SQUARE',
             'CUBE', 'SHAPE', 'THEORY']
    rand = random.randint(0, 3)
    s = '$\\{'
    
    if rand == 0:
        w = random.randint(0, len(words)-1)
        s += ','.join(words[w])
        l = len(words[w])
    else:
        l = random.randint(3, 7)
        ra = random.randint(0, 1)
        if ra == 0 : start = chr(ord('A') + random.randint(0, 16))
        else : start = chr(ord('a') + random.randint(0, 16))
        for i in range(ord(start), ord(start) + l):
            c = chr(i)
            s += c
            if i != ord(start) + l - 1:
                s += ','
    
    s += '\\}$'
    rand = random.randint(0, 5)
    if rand == 0:
        question = 'How many improper subsets does the set %s have?' % (s)
        answer = '1'
    elif rand >= 1 and rand <= 3:
        question = 'The number of proper subsets of the set %s is' % (s)
        answer = str(2**l - 1)
    else:
        question = 'The number of subsets of the set %s is' % (s)
        answer = str(2**l)
        
    return [question, answer, end]

def SubtractingReverses(probNum):
    question, answer, end = '', '', ''
    num = random.randint(100, 998)
    reverse = ((num%10) * 100) + (((num/10) % 10) * 10) + (num/100)
    while num % 10 == 0 or reverse % 10 == 0 or num == reverse:
        num = random.randint(100, 998)
        reverse = ((num%10) * 100) + (((num/10) % 10) * 10) + (num/100)
    question = '$%d - %d = $' % (num, reverse)
    answer = str(num - reverse)
    return [question, answer, end]

def XSquaredMinusXSquaredSplitUp(probNum):
    question, answer, end = '', '', ''
    num = random.randint(20, 59)
    split = random.randint(2, 7)
    b = random.randint(0, 3) == 0
    if b:
        split = (num-1)/2
    
    sp1, sp2 = num - split, split
    rep = '$'
    
    b = random.randint(0, 1) == 0
    if b : rep += '%d^2 ' % (num)
    else : rep += '(%d + %d)^2 ' % (sp1, sp2)
    
    plus = random.randint(0, 1) == 0
    if plus : rep += '+ '
    else    : rep += '- '
    
    rep += '(%d^2 - %d^2)' % (sp1, sp2)
    
    n1 = num**2
    n2 = sp1**2 - sp2**2
    question = '%s = $' % (rep)
    if plus : answer = str(n1 + n2)
    else    : answer = str(n1 - n2)
    
    return [answer, question, end]

def WhichIsLargerOrSmaller(probNum):
    question, answer, end = '', '', ''
    
    den = random.randint(7, 29)
    num = random.randint(den/3, den*3/4 - 1)
    f1 = Fraction(num, den)
    
    b = random.randint(0, 1) == 0
    larger = random.randint(0, 1) == 0
    
    if larger : question = 'Which is larger, $%s$ or ' % (str(f1))
    else      : question = 'Which is smaller, $%s$ or ' % (str(f1))
    
    if b:
        add = random.randint(-4, 4)
        while add == 0: add = random.randint(-4, 4)
        f2 = Fraction(num+add, den + add)
        question += '$%s$' % (str(f2))
        if f2.numerator == 0: return WhichIsLargerOrSmaller(probNum)
        if f1.DecValue() > f2.DecValue:
            answer = '$%s$' % (str(f1) if larger else str(f2))
        else:
            answer = '$%s$' % (str(f2) if larger else str(f1))
    
    else:
        min, max = float(0), float(100)
        val = f1.DecValue()
        
        while min / 100 < val * .72 : min += 1
        while max / 100 > val * 1.3 : max -= 1
        
        d = random.randint(int(min), int(max))
        bo = random.randint(0, 1) == 0
        
        if bo : question += '$%d\\%%$' % (d)
        else  : question += '$.%d$' % (d)
        sAns = '.%d' % (d)
        if not bo: sAns = '.%d' % (d)
        
        if f1.DecValue() > float(d) / 100:
            answer = '$%s$' % (str(f1) if larger else sAns)
        else:
            answer = '$%s$' % (sAns if larger else str(f1))
        
    question += '?'
    return [question, answer, end]

def SubtractingTwoFractions(probNum):
    question, answer, end = '', '', ''
    den1 = random.randint(3, 17)
    minNum, maxNum = 0, den1*4-1
    while float(minNum)/den1 < .23:
        minNum += 1
    num1 = random.randint(minNum, maxNum)
    f1 = Fraction(num1, den1)
    
    while True:
        minNum = 0
        den2 = random.randint(7, 55)
        maxNum = den2 * 4 - 1
        while abs(f1.DecValue() - float(minNum) / den2) > .3:
            minNum += 1
        while abs(f1.DecValue() - float(maxNum) / den2) > .3:
            maxNum -= 1
        num2 = random.randint(minNum, maxNum -1)
        f2 = Fraction(num2, den2)
        if not f1 == f2: break
    
    if utility.GCD(f1.denominator, f2.denominator) == 1 and \
       f1.denominator * f2.denominator > 40 and \
       random.randint(0, 3) < 3:
        return SubtractingTwoFractions(probNum)
    if utility.GCD(f1.denominator, f2.denominator) == 1 and \
       f1.denominator * f2.denominator > 100:
        return SubtractingTwoFractions(probNum)
    
    question = '$%s - %s = $' % (str(f1), str(f2))
    ans = fraction.Subtract(f1, f2)
    answer = '$%s$' % (str(ans))
    return [question, answer, end]

def InfiniteSequences(probNum):
    question, answer, end = '', '', ''
    b = random.randint(0, 9)
    if b < 6   : num = 1
    elif b < 8 : num = 2
    else       : num = 3
    den = random.randint(num+1, 4)
    mult = Fraction(num, den)
    bo = random.randint(0, 1) == 0
    if bo: 
        start = Fraction(random.randint(1, 6), 1)
    else:
        start = Fraction(random.randint(1, 4), random.randint(2, 5))
    
    bo = random.randint(0, 4) == 0
    origStart = Fraction(start.numerator, start.denominator)
    question = '$%s ' % (str(start))
    if bo : question += '- '
    else  : question += '+ '
    start = fraction.Multiply(start, mult)
    
    question += str(start) + ' + '
    start = fraction.Multiply(start, mult)
    
    question += str(start) + ' '
    if bo : question += '- '
    else  : question += '+ '
    
    question += '... =$'
    if bo: mult.numerator *= -1
    answer = '$%s$' % (fraction.Divide(origStart, fraction.Subtract(Fraction(1, 1), mult)).ToStringAns())
    return [question, answer, end]

def IntegersBetweenXandY(probNum):
    question, answer, end = '', '', ''
    type = random.randint(0, 3)
    neg = random.randint(0, 3) == 0
    if neg : min = random.randint(-60, -1)
    else   : min = random.randint(4, 63)
    max = random.randint(min + 30, min + 129)
    t, notDiv = '', 0
    
    if   type == 0 : t = 'odd '
    elif type == 1 : t = 'even '
    
    if type != 3: 
        question = 'How many %sintegers are between $%d$ and $%d$?' % (t, min, max)
    else:
        notDiv = random.randint(2, 9)
        question = 'How many integers between $%d$ and $%d$ are not divisible by $%d$' % (min, max, notDiv)
    a = 0
    if type == 0:
        for i in range(min+1, max):
            if abs(i) % 2 == 1 : a+=1
    if type == 1:
        for i in range(min+1, max):
            if abs(i) % 2 == 0 : a+=1
    if type == 2:
        for i in range(min+1, max): a+=1
    if type == 3:
        for i in range(min+1, max):
            if i % notDiv != 0: a+=1
    answer = str(a)
    return [question, answer, end]

def Inverse(probNum):
    question, answer, end = '', '', ''
    additive = random.randint(0, 1) == 0
    f1 = fraction.LessThan1Fraction(7, 7)
    if random.randint(0, 1) == 0 : f1.numerator *= -1
    if additive:
        question = 'The additive inverse of $%s$ is' % (str(f1))
        f1.numerator *= -1
        answer = '$%s$' % (str(f1))
    else:
        question = 'The multiplicitive inverse of $%s$ is' % (str(f1))
        temp = f1.numerator
        f1.numerator = f1.denominator
        f1.denominator = temp
        answer = '$%s$' % (str(f1))
    return [question, answer, end]

def SumOfTwoSquares(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    if rand < 2:
        first = random.randint(11, 98)
        second = ((first%10)-1)*10 + (10 - first/10)
    elif rand < 4:
        if random.randint(0, 1):
            if random.randint(0, 1):
                second = random.randint(4, 21)
                first = 2 * second
            else:
                first = 3 * random.randint(4, 21)
                second = first / 3
        else:
            first = random.randint(7, 17)
            second = 2*first if random.randint(0, 1) else 3*first
    else:
        first = 5 * random.randint(5, 17)
        second = first + 1
    question = '$%d^2 + %d^2 =$' % (first, second)
    answer = str(first**2 + second**2)
    return [question, answer, end]

def WhatPercent(probNum):
    question, answer, end = '', '', ''
    secNum = random.randint(5, 149)
    while utility.isPrime[secNum]: 
        secNum = random.randint(5, 149)
    f1 = fraction.LessThan1Fraction(12, 12)
    while (secNum * f1.numerator) % f1.denominator != 0:
        f1 = fraction.LessThan1Fraction(12, 12)
    
    firNumLess = random.randint(0, 1) == 0
    frac = (secNum * f1.numerator) / f1.denominator
    if firNumLess : firNum = secNum - frac
    else          : firNum = secNum + frac
    
    percentOf = random.randint(0, 1) == 0
    if percentOf:
        question = '$%d$ is what percent of $%d$?' % (firNum, secNum)
        ans = Fraction(firNum * 100, secNum)
        answer = '$%s$' % (ans.ToStringAns())
    else:
        if firNumLess:
            question = '$%d$ is what percent less than $%d$?' % (firNum, secNum)
            ans = Fraction(f1.numerator * 100, f1.denominator)
            answer = '$%s$' % (ans.ToStringAns())
        else:
            question = '$%d$ is what percent more than $%d$?' % (firNum, secNum)
            ans = Fraction(f1.numerator * 100, f1.denominator)
            answer = '$%s$' % (ans.ToStringAns())
    return [question, answer, end]

def ProductOfCoefficients(probNum):
    question, answer, end = '', '', ''
    plus1 = random.randint(0, 3) == 0
    first, second, power = 1, 1, 1
    minus = False
    if not plus1:
        minus = random.randint(0, 1) == 0
        first, second, power = random.randint(1, 5), random.randint(1, 5), 2
    if plus1:
        minus, first, second, power = False, 1, 1, random.randint(2, 5)
    var1, var2 = '', ''
    rand = random.randint(0, 2)
    if rand == 0:
        var1, var2 = 'x', 'y'
    elif rand == 1:
        var1, var2 = 'm', 'n'
    elif rand == 2:
        var1, var2 = 'a', 'b'
    sign = ' - ' if minus else ' + '
    question = 'The product of the coefficients of $(%s)^%d$ =' % (("" if first == 1 else str(first)) + var1 + sign + ("" if second == 1 else str(second)) + var2, power)    
    if plus1:
        answer = ['', '', '2', '9', '96', '2500'][power]
    else:
        answer = str((first**3)*(second**3)*2)
    if minus : answer = '-' + answer
    return [question, answer, end]

def Multiply2MixedNumbers(probNum):
    question, answer, end = '', '', ''
    cancel = random.randint(0, 4) == 0
    fTemp = fraction.LessThan1Fraction(9, 9)
    mn1 = MixedNumber(random.randint(2, 9), fTemp.numerator, fTemp.denominator)
    while utility.isPrime[mn1.co * mn1.f.denominator + mn1.f.numerator]:
        fTemp = fraction.LessThan1Fraction(9, 9)
        mn1 = MixedNumber(random.randint(2, 9), fTemp.numerator, fTemp.denominator)
    mn2 = MixedNumber()
    if cancel:
        factors = []
        num = mn1.co * mn1.f.denominator * mn1.f.numerator
        for i in range(2, num+1):
            if num % i == 0 : factors.append(i)
        den = factors[random.randint(0, len(factors) - 1)]
        mn2 = MixedNumber(random.randint(0, 9), random.randint(0, 8), den)
    else:
        rand = random.randint(0, 3)
        if rand < 2:
            mn2 = MixedNumber(random.randint(2, 9), mn1.f.numerator, mn1.f.denominator)
        elif rand == 2:
            f1 = Fraction(mn1.f.denominator - mn1.f.numerator, mn1.f.denominator)
            mn2 = MixedNumber(mn1.co if random.randint(0, 2) == 0 else random.randint(2, 9), f1.numerator, f1.denominator)
        elif rand == 3:
            co = mn1.f.denominator * 3 if mn1.f.denominator < 5 else mn1.f.denominator * 2
            fact = utility.Factors(mn1.co)
            den = fact[random.randint(0, len(fact)-1)]
            while den == 1:
                den = fact[random.randint(0, len(fact)-1)]
            num = random.randint(1, den-1)
            mn2 = MixedNumber(co, num, den)
    
    question = '$%s \\times %s =$' % (str(mn1), str(mn2))
    answer = '$%s$' % (mixedNumber.Multiply(mn1, mn2).ToFraction().ToStringAns())
    return [question, answer, end]

def ATimesBPlusATimesC(probNum):
    question, answer, end = '', '', ''
    plus, fact = random.randint(0, 1) == 0, random.randint(0, 3) == 0
    num = random.randint(8, 72)
    factors = utility.Factors(num)
    if fact : secNum = factors[random.randint(0, len(factors) - 1)]
    else    : secNum = num
    firN, secN = random.randint(8, 73), random.randint(8, 73)
    if random.randint(0, 1) == 0:
        temp = firN
        firN = num
        num = temp
    if random.randint(0, 1) == 0:
        temp = secNum
        secNum = secN
        secN = temp
    op= ' + ' if plus else ' - '
    question = '$%d \\times %d%s%d \\times %d =$' % (num, firN, op, secNum, secN)
    if plus: answer = str(num*firN + secNum*secN)
    else   : answer = str(num*firN - secNum*secN)
    return [question, answer, end]

def ATimesAOverB(probNum):
    question, answer, end = '', '', ''
    whole, dif = random.randint(7, 39), random.randint(2, 4)
    if random.randint(0, 4) == 0: dif *= -1
    f = Fraction(whole, whole + dif, False)
    while (not f.isReduced() and random.randint(0, 2) < 2):
        whole, dif = random.randint(7, 39), random.randint(2, 4)
        if random.randint(0, 4) == 0: dif *= -1
        f = Fraction(whole, whole + dif)
    b = random.randint(0, 4) != 4
    add = 0
    if probNum > 35 and b:
        rand = random.randint(0, 2) != 2
        if rand: add = -1 * whole
        else   : add = random.randint(-5, 5)
        while add == 0: add = random.randint(-5, 5)
        question = '$%d \\times %s %d =$' % (whole, str(f) + (' - ' if add < 0 else ' + '), abs(add))
        answer = '$%s$' % (Fraction(whole * f.numerator + add * f.denominator, f.denominator).ToStringAns())
    else:
        question = '$%d \\times %s = $' % (whole, str(f))
        answer = '$%s$' % (Fraction(whole * f.numerator, f.denominator).ToStringAns())
    return [question, answer, end]

def RegularNGonDegrees(probNum):
    question, answer, end = '', '', ''
    nsides = random.randint(3, 12)
    while nsides == 11 : nsides = random.randint(3, 12)
    p = Polygon(nsides)
    rand = random.randint(0, 2)
    f = Fraction(360, nsides)
    fs = Fraction(180 * (nsides - 2), nsides)
    if rand == 0:
        ind = random.randint(0, 5)
        if ind == 0:
            question = 'If a regular polygon inscribed in a circle contains a central angle of $%s^\\circ$, then the polygon has' % (str(f))
            end = 'sides'
            answer = str(nsides)
        elif ind == 1:
            question = 'If a regular n-gon inscribed in a circle contains a central angle of $%s^\\circ$, then n =' % (str(f))
            answer = str(nsides)
        elif ind == 2:
            question = 'If a regular polygon inscribed in a circle contains a central angle of $%s^\\circ$, then the polygon has an interior angle containing' % (str(f))
            end = 'degrees'
            answer = '$%s$' % (str(fs))
        elif ind == 3:
            question = 'If a regular polygon inscribed in a circle contains a central angle of $%s^\\circ$, then the sum of its interior angles is' % (str(f))
            end = 'degrees'
            answer = str(180 * (nsides - 2))
        elif ind == 4:
            question = 'If the interior angles of a regular n-gon total $%d^\\circ$, then n =' % (180 * (nsides-2))
            answer = str(nsides)
        elif ind == 5:
            question = 'If a regular polygon has an interior angle of $%s^\\circ$ degrees, then it has' % (str(fs))
            end = 'sides'
            answer = str(nsides)
    elif rand == 1:
        question = 'The interior angle of a regular %s contains' % (str(p))
        end = 'degrees.'
        answer = '$%s$' % (fs.ToStringAns())
    elif rand == 2:
        question = 'The sum of the interior angles of a regular %s total' % (str(p))
        end = 'degrees.'
        answer = str(180 * (nsides - 2))
    return [question, answer, end]

def SqrtATimesB(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    if rand < 4:
        num = random.randint(20, 79)**2
        fact = utility.Factors(num)
        fNum = fact[random.randint(0, len(fact)-1)]
        sNum = num / fNum
        while fNum == sNum or abs(fNum - sNum) > 100 or fNum == 1 or sNum == 1:
            num = random.randint(20, 79)**2
            fact = utility.Factors(num)
            fNum = fact[random.randint(0, len(fact)-1)]
            sNum = num / fNum
        if random.randint(0, 1) == 0:
            temp = fNum
            fNum = sNum
            sNum = temp
        question = '$\\sqrt{%s} \\times \\sqrt{%s} =$' % (str(fNum), str(sNum))
        if random.randint(0, 4) < 2:
            question = '$\\sqrt{%s \\times %s} =$' % (str(fNum), str(sNum))
        answer = str(math.sqrt(num))
    else:
        num = random.randint(20, 79)**2
        fact = utility.Factors(num)
        fNum = fact[random.randint(0, len(fact)-1)]
        sNum2 = num / fNum
        fact2 = utility.Factors(sNum2)
        sNum = fact2[random.randint(0, len(fact2)-1)]
        tNum = sNum2 / sNum
        while fNum == sNum or sNum == tNum or fNum == tNum or fNum == 1 or sNum == 1 or tNum == 1:
            num = random.randint(20, 79)**2
            fact = utility.Factors(num)
            fNum = fact[random.randint(0, len(fact)-1)]
            sNum2 = num / fNum
            fact2 = utility.Factors(sNum2)
            sNum = fact2[random.randint(0, len(fact2)-1)]
            tNum = sNum2 / sNum
        question = '$\\sqrt{%s} \\times \\sqrt{%s} \\times \\sqrt{%s} =$' % (str(fNum), str(sNum), str(tNum))
        answer = str(math.sqrt(num))
    return [question, answer, end]

def GCDLCM(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 1) == 0:
        if random.randint(0, 1) == 0:
            n = random.randint(6, 29)
            fNum = n * random.randint(2, 12)
            sNum = n * random.randint(2, 12)
            while utility.GCD(fNum, sNum) != n or fNum > 200 or sNum > 200 or fNum == 1 or sNum == 1 or \
                  ((fNum == n or sNum == n) and random.randint(0, 2) < 2):
                fNum = n * random.randint(1, 12)
                sNum = n * random.randint(1, 12)
            question = 'The GCD of $%d$ and $%d =$' % (fNum, sNum)
            answer = str(n)
        else:
            n = random.randint(6, 29)
            fNum, sNum, tNum = n * random.randint(1, 8), n * random.randint(1, 8), n * random.randint(1, 8)
            while (fNum == sNum or fNum == tNum or sNum == tNum) or utility.GCD(utility.GCD(fNum, sNum), tNum) != n or \
                  fNum > 200 or sNum > 200 or tNum > 200 or fNum == 1 or sNum == 1 or tNum == 1 or \
                  ((fNum == n or sNum == n or tNum == n) and random.randint(0, 2) < 2):
                fNum, sNum, tNum = n * random.randint(1, 8), n * random.randint(1, 8), n * random.randint(1, 8)
            question = 'The GCD of $%d$, $%d$, and $%d =$' % (fNum, sNum, tNum)
            answer = str(n)
    else:
        if random.randint(0, 1) == 0:
            n = random.randint(50, 199)
            fact = utility.Factors(n)
            fNum, sNum = fact[random.randint(0, len(fact)-1)], fact[random.randint(0, len(fact)-1)]
            while fNum == sNum or utility.LCM(fNum, sNum) != n or fNum == 1 or sNum == 1 or \
                  utility.LCM(fNum, sNum) == fNum or utility.LCM(fNum, sNum)==sNum:
                n = random.randint(50, 199)
                fact = utility.Factors(n)
                fNum, sNum = fact[random.randint(0, len(fact)-1)], fact[random.randint(0, len(fact)-1)]
            question = 'The LCM of $%d$ and $%d =$' % (fNum, sNum)
            answer   = str(n)
        else:
            n = random.randint(50, 199)
            fact = utility.Factors(n)
            fNum = fact[random.randint(0, len(fact)-1)]
            sNum = fact[random.randint(0, len(fact)-1)]
            tNum = fact[random.randint(0, len(fact)-1)]
            while fNum == 1 or sNum == 1 or tNum == 1 or \
                  fNum == sNum or fNum == tNum or sNum == tNum or \
                  utility.LCM(utility.LCM(tNum, fNum), sNum) != n or \
                  fNum==n or sNum==n or tNum==n:
                n = random.randint(50, 199)
                fact = utility.Factors(n)
                fNum = fact[random.randint(0, len(fact)-1)]
                sNum = fact[random.randint(0, len(fact)-1)]
                tNum = fact[random.randint(0, len(fact)-1)]
            question = "The LCM of $" + str(fNum) + "," + str(sNum) + "$ and $" + str(tNum) + " =$"
            answer = str(n)         
    return [question, answer, end]

def MultiplyBy11(probNum):
    question, answer, end = '', '', ''
    l  = 0
    sNum = 0
    if probNum < 40:
        rand = random.randint(0, 4)
        if rand==0 : l = 3
        else       : l = 2
        rand = random.randint(0, 4)
        if rand==0 : sNum = random.randint(123, 986)
        else       : sNum = random.randint(11, 98)
    else:
        rand = random.randint(0, 1)
        if rand==0 : l = 3
        else       : l = 4
        rand = random.randint(0, 4)
        if(rand==0) : sNum = random.randint(11, 98)
        else        : sNum = random.randint(11, 98)
    fNum = 0
    for i in range(0, l):
        fNum = fNum*10 + 1
    dsNum, dfNum = -1, -1
    if random.randint(0, 9) == 0 :
        dsNum = utility.Decimalize(sNum)
    if random.randint(0, 9) == 0 :
        dfNum = utility.Decimalize(fNum)
    if random.randint(0, 2) == 0:
        temp = fNum
        fNum = sNum
        sNum = temp
        
        temp = dfNum
        dfNum = dsNum
        dsNum = temp
        
    question = "$" + (str(fNum) if dfNum == -1 else str(dfNum)) + " \\times " + (str(sNum) if dsNum == -1 else str(dsNum)) + " =$"
    answer = str((fNum if dfNum == -1 else dfNum) *  (sNum if dsNum == -1 else dsNum))
    return [question, answer, end]

def MultiplyBy25(probNum):
    question, answer, end = '', '', ''
    fNum = 25 if random.randint(0, 1) == 0 else 75
    sNum = random.randint(11,98) if random.randint(0, 1) == 0 else random.randint(103, 255)
    question = '$%d \\times %d =$' % (fNum, sNum)
    answer = str(fNum * sNum)
    return [question, answer, end]

def MultiplyBy125(probNum):
    question, answer, end = '', '', ''
    fNum = 125 if random.randint(0, 1) == 0 else 125 * random.randint(2, 4) * 2 - 125
    rand = random.randint(0, 4)
    if rand == 0 : sNum = random.randint(11, 99)
    else         : sNum = random.randint(13, 61) * 8
    dfNum, dsNum = -1, -1
    if random.randint(0, 9) == 0:
        dfNum = utility.Decimalize(fNum)
    if random.randint(0, 9) == 0:
        dsNum = utility.Decimalize(sNum)
    question = '$%d \\times %d =$' % (fNum if dfNum == -1 else dfNum, sNum if dsNum == -1 else dsNum)
    answer = str((fNum if dfNum == -1 else dfNum) * (sNum if dsNum == -1 else dsNum))
    return [question, answer, end]

def MultiplyBy429(probNum):
    question, answer, end = '', '', ''
    num1, num2 = 0, 0
    if probNum < 20 : num1 = 429 if random.randint(0, 4) < 4  else 143 * random.randint(1, 6)
    else            : num1 = 429 if random.randint(0, 1) == 0 else 143 * random.randint(1, 6)
    if probNum < 45:
        if random.randint(0, 9) == 0: num2 = 7 * random.randint(15, 104)
        else: num2 = 7 * random.randint(2, 14)
    else:
        num2 = 7 * random.randint(15, 104) if random.randint(0, 1) == 0 else 7 * random.randint(2, 14)
    question = '$%d \\times %d =$' % (num1, num2)
    answer = str(num1*num2)
    if probNum > 60 and random.randint(0, 1) == 0:
        if random.randint(0, 1) == 0:
            question = '$%d \\times %d = 1001 \\times$' % (num1, num2)
            answer = str(num2 * num1 / 1001)
        else:
            mult = random.randint(12, 58)
            while (mult*7) % (num1 / 143) != 0: mult = random.randint(12, 58)
            question = '$1001 \\times %d = %d \\times$' % (mult, num1)
            answer = str(1001 * mult / num1)
    return [question, answer, end]

def MultiplyingPowers(probNum):
    question, answer, end = '', '', ''
    num1, num2, num3 = 0, 0, 0
    num1 = 2**random.randint(1, 3)
    num2 = 5
    if random.randint(0, 2) == 0:
        num3 = 2**random.randint(1, 3) if random.randint(0, 1) == 0 else 3
    pow1, pow2, pow3 = random.randint(2, 6), random.randint(2, 6), random.randint(2, 6)
    
    if pow2 > 4 : pow2 = 4
    if num1 > 4 and pow1 > 2 : pow1 = 3 if random.randint(0, 3) == 0 else 2
    if num3 > 4 and pow3 > 2 : pow3 = 3 if random.randint(0, 3) == 0 else 2
    
    question = "$" + (str(num1) + "^" + str(pow1) + " \\times " + str(num2) + "^" + str(pow2) + " =" if num3 == 0 else \
               str(num1) + "^" + str(pow1) + " \\times " + str(num2) + "^" + str(pow2) + " \\times " + str(num3) + "^" + str(pow3) + " =") + "$"
    answer = str((num1**pow1) * (num2**pow2)) if num3 == 0 else \
             str((num1**pow1) * (num2**pow2) * (num3**pow3))
    return [question, answer, end]

def NumberIntegralDivisors(probNum):
    question, answer, end = '', '', ''
    primefact = random.randint(0, 3)==0
    question, answer = "The number of positive integral divisors of ", ""
    if(primefact):
        p = []
        for i in range(2, 15):
            if utility.isPrime[i]:
              p.append(i)
        numTerms = random.randint(2, 4)
        
        if numTerms == 2:
            term1, term2 = p[random.randint(0, len(p)-1)], p[random.randint(0, len(p)-1)]  
            while(term1 == term2):
                term1, term2 = p[random.randint(0, len(p)-1)], p[random.randint(0, len(p)-1)] 
            pow1, pow2 = random.randint(1, 6), random.randint(1, 6)
            s1, s2 = "" if pow1 == 1 else "^" + str(pow1), \
                     "" if pow2 == 1 else "^" + str(pow2)
                    
            question += "$" + str(term1) + s1 + " \\times " + str(term2) + s2 + "$ is"
            answer = str((pow1 + 1) * (pow2 + 1))
        
        elif numTerms == 3 :
            term1, term2, term3 = p[random.randint(0, len(p)-1)], \
                                  p[random.randint(0, len(p)-1)], \
                                  p[random.randint(0, len(p)-1)]  
            while term1 == term2 or term1==term3 or term2 == term3:
                term1, term2, term3 = p[random.randint(0, len(p)-1)], \
                                      p[random.randint(0, len(p)-1)], \
                                      p[random.randint(0, len(p)-1)]  
            pow1, pow2, pow3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
            s1, s2, s3 = "" if pow1 == 1 else "^" + str(pow1), \
                         "" if pow2 == 1 else "^" + str(pow2), \
                         "" if pow3 == 1 else "^" + str(pow3)
            question += "$" + str(term1) + s1 + " \\times " + str(term2) + s2 + " \\times " + str(term3) + s3 + "$ is"
            answer = str((pow1 + 1) * (pow2 + 1) * (pow3 + 1))
        
        elif numTerms == 4:
            term1, term2, term3, term4 = p[random.randint(0, len(p)-1)], \
                                         p[random.randint(0, len(p)-1)], \
                                         p[random.randint(0, len(p)-1)], \
                                         p[random.randint(0, len(p)-1)]                                         
            while term1 == term2 or term1==term3 or term1==term4 or term2==term3 or term2==term4 or term3==term4:
                term1, term2, term3, term4 = p[random.randint(0, len(p)-1)], \
                                             p[random.randint(0, len(p)-1)], \
                                             p[random.randint(0, len(p)-1)], \
                                             p[random.randint(0, len(p)-1)]   
            pow1, pow2, pow3, pow4 = random.randint(1, 6),random.randint(1, 6),\
                                     random.randint(1, 6),random.randint(1, 6)
            s1 = "" if pow1 == 1 else "^" + str(pow1)
            s2 = "" if pow2 == 1 else "^" + str(pow2)
            s3 = "" if pow3 == 1 else "^" + str(pow3)
            s4 = "" if pow4 == 1 else "^" + str(pow4)
            question += "$" + str(term1) + s1 + " \\times " + str(term2) + s2 + " \\times " + str(term3) + s3 + \
                 " \\times " + str(term4) + s4 + "$ is"
            answer = str((pow1 + 1) * (pow2 + 1) * (pow3 + 1) * (pow4 + 1))
    else:
        num = random.randint(12, 99)
        while utility.isPrime[num]:
            num = random.randint(12, 99)
        question = "The number of positive integral divisors of $" + str(num) + "$ is"
        ans = 0
        for i in range(1, num+1):
            if num%i==0 : ans+=1
        answer = "$" + str(ans) + "$"
    return [question, answer, end]

def Speed(probNum):
    question, answer, end = '', '', ''
    meas      = ['inches', 'feet', 'yards', 'miles']
    measVal   = [1, 12, 36, 5280 * 12]
    metric    = ['centimeters', 'meters', 'decameters', 'kilometers']
    metricVal = [1, 100, 1000, 100000]
    time      = ['second', 'minute', 'hour', 'day']
    timeVal   = [1, 60, 3600, 3600 * 24]
    
    measAbrev = ['in/sec', 'in/min', 'in/hour', 'in/day', \
                 'ft/sec', 'ft/min', 'ft/hour', 'ft/day', \
                 'yards/sec', 'yards/min', 'yards/hour', 'yards/day', \
                 'miles/sec', 'miles/min', 'mph', 'miles/day']
    metricAbrev = ['cm/sec', 'cm/min', 'cm/hour', 'cm/day', \
                   'meters/sec', 'meters/min', 'meters/hour', 'meters/day', \
                   'decameters/sec', 'decameters/min', 'decameters/hour', 'decameters/day', \
                   'km/sec', 'km/min', 'km/hour', 'km/day']
    isMetric = random.randint(0, 2) == 0
    measIndex1 = random.randint(0, 3)
    measIndex2 = random.randint(0, 3)
    timeIndex1 = random.randint(0, 3)
    timeIndex2 = random.randint(0, 3)
    
    if isMetric:
        f1 = fraction.Divide(Fraction(metricVal[measIndex1], timeVal[timeIndex1]), \
                             Fraction(metricVal[measIndex2], timeVal[timeIndex2]))
    else:
        f1 = fraction.Divide(Fraction(measVal[measIndex1], timeVal[timeIndex1]), \
                             Fraction(measVal[measIndex2], timeVal[timeIndex2]))
    
    mult = random.randint(1, 15) * f1.denominator
    
    while (measIndex1 == measIndex2 and timeIndex1 == timeIndex2) or f1.DecValue() < 1.0/3650 or \
           f1.DecValue() > 3650 or mult > 1000:
        measIndex1 = random.randint(0, 3)
        measIndex2 = random.randint(0, 3)
        timeIndex1 = random.randint(0, 3)
        timeIndex2 = random.randint(0, 3)
    
        if isMetric:
            f1 = fraction.Divide(Fraction(metricVal[measIndex1], timeVal[timeIndex1]), \
                                 Fraction(metricVal[measIndex2], timeVal[timeIndex2]))
        else:
            f1 = fraction.Divide(Fraction(measVal[measIndex1], timeVal[timeIndex1]), \
                                 Fraction(measVal[measIndex2], timeVal[timeIndex2]))
    
        mult = random.randint(1, 15) * f1.denominator
    
    dmult = float(-1)
    if random.randint(0, 7) == 0:
        dmult = utility.Decimalize(mult)
    if isMetric:
        question = (str(mult) if dmult == -1 else str(dmult)) + ' ' + \
                   (metric[measIndex1] + " per " + time[timeIndex1] if random.randint(0, 1) else metricAbrev[measIndex1 * 4 + timeIndex1]) + ' ='
        end = (metric[measIndex2] + " per " + time[timeIndex2] if random.randint(0, 1) else metricAbrev[measIndex2 * 4 + timeIndex2])
        answer = str(mult / f1.denominator * f1.numerator if dmult == -1 else dmult / f1.denominator * f1.numerator)
    else:
        question = (str(mult) if dmult == -1 else str(dmult)) + ' ' + \
                   (meas[measIndex1] + " per " + time[timeIndex1] if random.randint(0, 1) else measAbrev[measIndex1 * 4 + timeIndex1]) + ' ='
        end = (meas[measIndex2] + " per " + time[timeIndex2] if random.randint(0, 1) else measAbrev[measIndex2 * 4 + timeIndex2])
        answer = str(mult / f1.denominator * f1.numerator if dmult == -1 else dmult / f1.denominator * f1.numerator)
    return [question, answer, end]
        
def CubeRt(probNum):
    question, answer, end = '', '', ''
    largeNum = random.randint(0, 1) == 0
    num, root = 0, 0
    if largeNum:
        root = random.randint(30, 99)
        num = root**3
    else:
        root = random.randint(4, 15)
        num = root**3
    droot, dnum = -1, -1
    
    if random.randint(0, 6)==0:
        droot = float(root) / 10
        dnum = droot**3
    if random.randint(0, 7) == 0:
        if random.randint(0, 2) == 0: #3 terms
            b1, b2, b3 = random.randint(2, 9), random.randint(2, 9), random.randint(2, 9)
            t1, t2, t3 = b1**3, b2**3, b3**3
            question = "$\\sqrt[3]{" + str(t1) + "} \\times \\sqrt[3]{" + str(t2) + "} \\times \\sqrt[3]{" + str(t3) + "} = $"
            answer = str(b1 * b2 * b3)
        else: #2 terms
            b1, b2 = random.randint(2, 9), random.randint(2, 9)
            t1, t2 = b1**3, b2**3
            question = "$\\sqrt[3]{" + str(t1) + "} \\times \\sqrt[3]{" + str(t2) + "} = $"
            answer = str(b1 * b2)
    else:
        if random.randint(0, 1):
            question = "$\\sqrt[3]{" + (str(num) if dnum == -1 else str(dnum)) + "} = $"
            answer = str(root if dnum == -1 else droot)
        else:
            question = '$' + str(num if dnum == -1 else dnum) + '^{\\frac{1}{3}} = $'
            answer = str(root if dnum == -1 else droot)
    return [question, answer, end]

def CubesAndFourths(probNum):
    question, answer, end = '', '', ''
    num = -1
    if random.randint(0, 4) == 0: #fourth
        num = random.randint(3, 8)
        question = "$" + (str(num) + " \\times " + str(num) + " \\times " + str(num) + " \\times " + str(num) + " =$" if random.randint(0, 4) == 0 else str(num) + "^4 =$")
        answer = str(num * num * num * num)
    else:
        num = random.randint(3, 16)
        question = "$" + (str(num) + " \\times " + str(num) + " \\times " + str(num)  + " =$" if random.randint(0, 4) == 0 else str(num) + "^3 =$")
        answer = str(num * num * num)
    return [question, answer, end]

def DegreeRadian(probNum):
    question, answer, end = '', '', ''
    fact = utility.Factors(360)
    f1 = Fraction(random.randint(0, 64), fact[random.randint(0, 12)])
    while f1.DecValue() > 4:
        f1 = Fraction(random.randint(0, 64), fact[random.randint(0, 12)])
    degValue = 180 / f1.denominator * f1.numerator
    if random.randint(0, 2) == 0:
        question = "If $" + str(degValue) + "^\\circ = k\\pi$ radians, then $k =$"
        answer = "$" + str(f1) + "$"
    else:
        question = "$" + f1.ToStringAddNum("\\pi") + "$ radians $=$"
        end = "degrees"
        answer = "$" + str(degValue) + "$"
    return [question, answer, end]

def DifferenceOfTwoCubes(probNum):
    question, answer, end = '', '', ''
    num1, num2 = random.randint(2, 12), random.randint(2, 12)
    question = "$" + str(num1) + "^3 - " + str(num2) + "^3 =$"
    answer = str(num1*num1*num1 - num2*num2*num2)
    return [question, answer, end]

def DifferenceOfTwoSquares(probNum):
    question, answer, end ='', '', ''
    num1, num2, rand = 0, 0, random.randint(0, 2)
    if rand == 0:
        num1 = random.randint(23, 199)
        num2 = num1 + -1**random.randint(1, 2)
    elif rand == 1:
        bigNum = 10 * random.randint(6, 17)
        num1 = random.randint(0, bigNum-1)
        num2 = bigNum - num1
    elif rand == 2:
        num1 = random.randint(6, 32)
        num2 = num1 * random.randint(2, 3)
    dnum1, dnum2 = -1, -1
    if random.randint(0, 6) == 0:
        dnum1, dnum2 = float(num1)/10, float(num2)/10
    
    question = "$" + str(num1 if dnum1 == -1 else dnum1) + "^2 - " + str(num2 if dnum2 == -1 else dnum2) + "^2 =$"
    if dnum1 == -1:
        answer = "$" + str(num1 * num1 - num2 * num2) + "$"    
    else:
        answer = "$" + str(dnum1 * dnum1 - dnum2 * dnum2) + "$"
    return [question, answer, end]

def DistinctDiagonals(probNum):
    question, anser, end = '', '', ''
    nSides, rand = random.randint(3, 11), random.randint(0, 4)
    p = Polygon(nSides)
    if rand == 0:
        question = "How many distinct diagonals can be drawn from each vertex of a regular " + str(p) + "?"
        answer = str(nSides - 3)
    elif rand == 1 or rand == 2:
        question = "A " + str(p) + " has"
        end = "distinct diagonals."
        answer = str((nSides) * (nSides - 3) / 2)
    else:
        question = "If a regular polygon has $" + str((nSides) * (nSides - 3) / 2) + "$ distinct diagonals, then it has"
        end = "sides."
        answer = str(nSides)
    return [question, answer, end]
    
def TwodigitTimesTwodigit(probNum):
    question, answer, end = '', '', ''
    num1, num2, rand = 0, 0, random.randint(0, 7)
    if rand < 4:
        num1, num2 = random.randint(11, 99), random.randint(11, 99)
    elif rand == 4:
        num1 = random.randint(11, 99)
        while num1 % 10 > 4 : num1 = random.randint(11, 99)
        num2 = (num1/10 * 10) + (5 - num1 % 10)
    elif rand == 5:
        num1 = random.randint(11, 99)
        num2 = (num1/10 * 10) + (10 - num1 % 10)
    elif rand == 6:
        num1 = random.randint(11, 99)
        num2 = (10 - num1/10) + (num1%10)
    elif rand == 7:
        bNum, dif = random.randint(11, 99), random.randint(0, 7)
        num1, num2 = bNum - dif, bNum + dif
    if random.randint(0, 1):
        temp = num1
        num1 = num2
        num1 = temp
    dnum1, dnum2 = -1, -1
    if random.randint(0, 19) == 0:
        dnum1, dnum2 = utility.Decimalize(num1), utility.Decimalize(num2)

    question = "$" + str(num1 if dnum1 == -1 else dnum1) + " \\times " + str(num2 if dnum2 == -1 else dnum2) + " =$"
    answer = str((num1 if dnum1 == -1 else dnum1) * (num2 if dnum2 == -1 else dnum2))
    return [question, answer, end]

def ThreeDigitTimesSomething(probNum):
    question, answer, end = '', '', ''
    num, num2 = random.randint(101, 499), 0
    if random.randint(0, 2) < 2:
         num2 = random.randint(5, 19)
    else:
         num2 = utility.Rearrange(num) if random.randint(0, 1) else random.randint(101, 499)
    dnum, dnum2 = -1, -1
    
    if random.randint(0, 13) == 0:
        dnum, dnum2 = utility.Decimalize(num), utility.Decimalize(num2)
    if num2 == 1 or num == 1 or dnum == 1 or dnum2 == 1:
        return ThreeDigitTimesSomething(probNum)
    question = "$" + str(num if dnum == -1 else dnum) + " \\times " + str(num2 if dnum2 == -1 else dnum2) + " =$"
    answer = "$" + str(num * num2) + "$"
    if dnum != -1:
        answer = "$" + utility.DoubleToAns(dnum * dnum2) + "$"
    return [question, answer, end]

def MultiplyBy3367(probNum):
    question, answer, end = '', '', ''
    num, num2, dnum, dnum2 = 3367, 3 * random.randint(2, 31), -1, -1
    if random.randint(0, 13) == 0: dnum = utility.Decimalize(num)
    if random.randint(0, 13) == 0: dnum2 = utility.Decimalize(num2)
    question = "$" + str(num if dnum == -1 else dnum) + " \\times " + str(num2 if dnum2 == -1 else dnum2) + " =$"
    answer = str((num if dnum == -1 else dnum) * (num2 if dnum2 == -1 else dnum2))
    return [question, answer, end]

def AOverBMinusBOverA(probNum):
    question, answer, end = '', '', ''
    dif, a, b = random.randint(1, 3), random.randint(3, 24), random.randint(3, 24)
    f1, f2 = Fraction(a, b), Fraction(b, a)
    question = "$" + str(f1) + " - " + str(f2) + " =$"
    answer = "$" + fraction.Subtract(f1, f2).ToStringAns() + "$"
    return [question, answer, end]

def AOverBPlusBOverA(probNum):
    question, answer, end = '', '', ''
    while True:
        a = random.randint(3, 19)
        b = a + random.randint(1, 4) * -1**random.randint(0, 1)
        f1, f2 = Fraction(a, b), Fraction(b, a)
        ans = fraction.Add(f1, f2)
        if not (abs(b) > a or b == 0) : break
    
    question = '$' + str(f1) + ' + ' + str(f2)
    answer = '$' + ans.ToStringAns() + '$'
    
    if random.randint(0, 3) == 0:
        if random.randint(0, 1):
            add, sub = random.randint(1, 4), random.randint(0, 1) == 0
            question += (" - " if sub else " + ") + str(add)
            answer = "$" + (fraction.Subtract(ans, Fraction(add, 1)).ToStringAns() if sub else \
                     fraction.Add(ans, Fraction(add, 1)).ToStringAns()) + "$"
        else:
            den = ans.denominator
            f = Fraction(random.randint(0, den-1), den)
            sub = random.randint(0, 1) == 0
            question += (" - " if sub else " + ") + str(f)
            if sub:
                 answer = "$" + fraction.Subtract(ans, f).ToStringAns() + "$"
            else:
                 answer = "$" + fraction.Add(ans, f).ToStringAns() + "$"
    question += ' = $'
    return [question, answer, end]

def ASquaredOverAMinus1(probNum):
    question, answer, end = '', '', ''
    num = random.randint(3, 22)
    num2 = num - 1
    question = "$\\displaystyle\\frac{" + str(num) + "^2}{" + str(num2) + "^2 - 1} =$"
    answer = "$" + Fraction(num*num, num2*num2 - 1).ToStringAns() + "$"
    return [question, answer, end]

def ATimesBPlusDifference(probNum):
    question, answer, end = '', '', ''
    diff, middle = random.randint(1, 4), 0
    if random.randint(0, 1): middle = 5 * random.randint(5, 25)
    else : middle = random.randint(11, 36)
    a, b = middle - diff, middle + diff
    question = "$" + str(a) + " \\times " +  str(b) + " + " + str(diff*diff) + " =$"
    answer = str(a*b + diff*diff)
    return [question, answer, end]

def CelsiusFahrenheitConv(probNum):
    question, answer, end = '', '', ''
    FtoC = random.randint(0, 1) == 0
    num, ans = 0, 0
    if FtoC:
        num = 9 * random.randint(-11, 25) + 32
        ans = (num - 32)*5/9
        question = '$' + str(num) + '^\\circ F ='
        end = '^\\circ C$'
        answer = '$' + str(ans) + '$'
    else:
        if random.randint(0, 2) < 2:
            num = 5 * random.randint(-11, 44)
            ans = (num*9/5) + 32
            question = '$' + str(num) + '^\\circ C ='
            end = '^\\circ F$'
            answer = '$' + str(ans) + '$'
        else:
            num = random.randint(-55, 225)
            ans2 = float(num) * 9 / 5 + 32
            question = '$' + str(num) + '^\\circ C ='
            end = '^\\circ F$'
            answer = str(ans2)
    return [question, answer, end]

def Bases(probNum):
    question, answer, end = '', '', ''
    if probNum > 60 or random.randint(0, 8) == 0:
        if random.randint(0, 1):
            rand = random.randint(0, 9)
            
            if rand == 0:
                num = random.randint(1, 8)
                b = 0
                if random.randint(0, 3): b = num+2
                else: b = random.randint(num+1, 16)
                while b == 10: b = random.randint(num+1, 16)
                ans = fraction.Divide(Fraction(num, b), Fraction(b-1, b))
                question = '$.' + str(num) + str(num) + str(num) + '...$ base $' + str(b) + '$ is equivalent to'
                end = 'base $10$'
                answer = '$' + str(ans) + '$'
                
            elif rand < 5:
                b = random.randint(2, 9)
                pow = random.randint(1, 3)
                toDecimal = random.randint(0, 1) == 0
                while toDecimal and 1000 % b**pow != 0:
                    b = random.randint(2, 9)
                    pow = random.randint(1, 3)
                num = random.randint(10**(pow-1), 10**pow-1)
                while True:
                    b2 = False
                    for i in range(len(str(num))):
                        if num % (10**(i+1)) / 10**i >= b:
                            b2 = True
                    if not b2: break
                    num = random.randint(10**(pow-1), 10**pow-1)
                base10 = utility.ChangeToBase(num, b, 10)
                ans = float(base10) / (b**pow)
                fans = Fraction(base10, b**pow)
                if toDecimal:
                    question = 'Change $.' + str(num) + '$ base $' + str(b) + '$ to a base $10$ fraction.'
                    answer = '$' + str(fans) + '$'
                else:
                    question = 'Change $.' + str(num) + '$ base $' + str(b) + '$ to a base $10$ fraction.'
                    answer = '$' + str(fans) + '$'
            else:
                f1 = Fraction(1, 1)
                b, num, den, pow = -1, -1, -1, -1
                while f1.denominator == 1:
                    b = random.randint(2, 9)
                    pow = random.randint(1, 3)
                    den = b**pow
                    num = random.randint(1, 2*den - 1)
                    f1 = Fraction(num, den-1)
                ans = float(utility.ChangeToBase(num, 10, b)) / (10**pow)
                question = 'Change $' + str(f1) + '$ to a base $' + str(b) + '$ decimal.'
                answer = '$' + utility.DoubleToAns(ans) + '$'
        else:
            b, rand = random.randint(2, 9), random.randint(0, 3)
            if rand == 0:
                num1_10 = random.randint(3, b**5-1)
                num2_10 = random.randint(3, b**5-1)
                num3_10 = random.randint(3, b**5-1)
                num1 = utility.ChangeToBase(num1_10, 10, b)
                num2 = utility.ChangeToBase(num2_10, 10, b)
                num3 = utility.ChangeToBase(num3_10, 10, b)
                ra = random.randint(0, 4)
                question = "$" + str(num1) + "_{" + str(b) + "} + " + str(num2) + "_{" + str(b) + "}" + \
                           (" + " + str(num3) + "_" + str(b) if ra < 2 else "") + " =$"
                end = "$_{" + str(b) + "}$"
                answer = str(utility.ChangeToBase(num1_10 + num2_10 + (num3_10 if ra < 2 else 0), 10, b))      
            elif rand == 1:
                num1_10 = random.randint(3, b**4-1)
                num2_10 = random.randint(3, b**4-1)
                num1 = utility.ChangeToBase(num1_10, 10, b)
                num2 = utility.ChangeToBase(num2_10, 10, b)
                question = '$' + str(num1) + '_{' + str(b) + '} - ' + str(num2) + '_{' + str(b) + '} =$'
                end = '$_{' + str(b) + '}$'
                answer = str(utility.ChangeToBase(num1_10 - num2_10, 10, b))
            elif rand == 2:
                num1_10 = random.randint(3, b**(4 if b < 4 else 3) - 1)
                num2_10 = random.randint(3, b**(4 if b < 4 else 3) - 1)
                num1 = utility.ChangeToBase(num1_10, 10, b)
                num2 = utility.ChangeToBase(num2_10, 10, b)
                question = "$" + str(num1) + "_{" + str(b) + "} \\times " + str(num2) + "_{" + str(b) + "} =$"
                end = "$_{" + str(b) + "}$"
                answer = str(utility.ChangeToBase(num1_10 * num2_10, 10, b))
            elif rand == 3:
                num2_10 = random.randint(3, b**(4 if b < 4 else 3) - 1)
                num1_10 = num2_10 * random.randint(2, 7)
                num1 = utility.ChangeToBase(num1_10, 10, b)
                num2 = utility.ChangeToBase(num2_10, 10, b)
                question = "$" + str(num1) + "_{" + str(b) + "} \\div " + str(num2) + "_{" + str(b) + "} =$"
                end = "$_{" + str(b) + "}$"
                answer = str(utility.ChangeToBase(num1_10 / num2_10, 10, b))
    else:
        if random.randint(0, 2) < 2:
            rand = random.randint(0, 4)
            if rand == 0:
                b = random.randint(2, 8)
                ra = random.randint(2, 5) if b < 6 else random.randint(2, 3)
                num_10 = random.randint(b+1, b**ra-1)
                num = utility.ChangeToBase(num_10, 10, b)
                question = '$' + str(num) + '_{' + str(b) + '} =$'
                end = '$_{10}$'
                answer = str(num_10)
            elif rand == 1:
                b = random.randint(2, 8)
                ra = random.randint(2, 5) if b < 6 else random.randint(2, 3)
                num_10 = random.randint(b+1, b**ra-1)
                num = utility.ChangeToBase(num_10, 10, b)
                question = '$' + str(num_10) + '_{10} =$'
                end = '$_{' + str(b) + '}$'
                answer = str(num)
            elif rand == 2:
                b = 2 if random.randint(0, 1) == 2 else 3
                tob = (4 if random.randint(0, 1) else 8) if b == 2 else 9
                ra = random.randint(2, 9)
                num_10 = random.randint(b+1, b**ra-1)
                numb = utility.ChangeToBase(num_10, 10, b)
                numtob = utility.ChangeToBase(num_10, 10, tob)
                question = '$' + str(numb) + '_{' + str(b) + '} =$'
                end = '$_{' + str(tob) + '}$'
                answer = str(numtob)
            elif rand == 3:
                b = (4 if random.randint(0, 1) else 8) if random.randint(0, 1) else 9
                tob = 2 if (b==4 or b==8) else 3
                ra = random.randint(2, 4)
                num_10 = random.randint(b+1, b**ra-1)
                numb = utility.ChangeToBase(num_10, 10, b)
                numtob = utility.ChangeToBase(num_10, 10, tob)
                question = '$' + str(numb) + '_{' + str(b) + '} =$'
                end = '$_{' + str(tob) + '}$'
                answer = str(numtob)
            elif rand == 4:
                b, c = random.randint(2, 8), random.randint(2, 8)
                while b == c:
                    b, c = random.randint(2, 8), random.randint(2, 8)
                ra = random.randint(2, 4) if b < 6 else random.randint(2, 3)
                num10 = random.randint(b+1, b**ra-1)
                numb = utility.ChangeToBase(num10, 10, b)
                numc = utility.ChangeToBase(num10, 10, c)
                question = '$' + str(numb) + '_{' + str(b) + '} =$'
                end = '$_{' + str(c) + '}$'
                answer = str(numc)
        else:
            b = random.randint(2, 9)
            num = random.randint(b**3, b**4-1)
            origNum = num
            question = ' =$'
            end = '$_{' + str(b) + '}$'
            question = str(num % b) + question
            num/=b
            if num%b != 0: question = str((num%b) * b) + ' + ' + question
            num/=b
            if num%b != 0: question = str((num%b) * (b**2)) + " + " + question
            num/=b
            if num%b != 0: question = str((num%b) * (b**3)) + " + " + question
            question = "$" + question
            answer = str(utility.ChangeToBase(origNum, 10, b))
    return [question, answer, end]
            
def Division(probNum):
    question, answer, end = '', '', ''
    ra = random.randint(0, 4)
    if probNum < 40:
        if ra < 3:
            den = random.randint(4, 14)
            num = den * random.randint(10, 99) if random.randint(0, 1) else random.randint(den*10, den*100-1)
        elif ra == 3:
            den = random.randint(16, 49)
            num = den * random.randint(5, 14) if random.randint(0, 2) < 2 else random.randint(den*5, den*15-1)
        else:
            den = 5 * random.randint(1, 18)
            num = den * random.randint(10, 49)
    else:
        if random.randint(0, 4) == 0:
            den = random.randint(16, 49)
            num = den * random.randint(5, 14) if random.randint(0, 2) < 2 else random.randint(den*5, den*15 -1)
        else:
            den = 101 if random.randint(0, 2) == 0 else (111 if random.randint(0, 2) == 0 else 1111)
            num = den * random.randint(11, 499)
    if random.randint(0, 13) == 0:
        num, den = random.randint(7, 99), random.randint(7, 99)
    if random.randint(0, 13) == 0:
        num, den = random.randint(8, 999), random.randint(8, 999)
    dnum, dden = -1.0, -1.0
    if random.randint(0, 9) == 0:
        dnum, dden = utility.Decimalize(num), utility.Decimalize(den)
    if dnum == -1 and dden == -1 and utility.GCD(num, den) == 1:
        return Division(probNum)
    question = '$' + str(num if dnum == -1 else dnum) + ' \\div ' + str(den if dden == -1 else dden) + ' = $'
    ans = Fraction(num, den)
    changeNum, changeDen = dnum / num, dden / den
    if dnum != -1 and changeNum < 1:
        changeNum = 1 / changeNum
        x = int(round(changeNum))
        ans.denominator *= x
    elif dnum != -1:
        x = round(changeNum)
        ans.numerator *= x
    if dden != -1 and changeDen < 1:
        changeDen = 1 / changeDen
        x = round(changeDen)
        ans.numerator *= x
    elif dden != -1:
        x = round(changeDen)
        ans.denominator *= x
    answer = '$' + ans.ToStringAns() + '$'
    return [question, answer, end]

def Expansions(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    plus = random.randint(0, 1) == 0
    op = ' + ' if plus else ' - '
    if rand < 2:
        a, b = random.randint(1, 2), random.randint(1, 2)
        p = random.randint(3, 9)
        n = random.randint(1, p+1)
        if n == 1: suf = 'st'
        if n == 2: suf = 'nd'
        if n == 3: suf = 'rd'
        if n > 3: suf = 'th'
        question = 'The coefficient of the $' + str(n) + suf + '$ term of the expansion $(' + \
                   ("" if a==1 else str(a)) + 'x' + op + ('' if b==1 else str(b)) + 'y' + \
                   ')^' + str(p) + '$ is'
        k = n - 1
        ans = utility.Comb(p, k) * (a**(p-k)) * (b**k)
        if op == ' - ' and k % 2 == 1: ans *= -1
        answer = '$' + str(ans) + '$'
    elif rand < 4:
        a, b = random.randint(1, 9), random.randint(1, 9)
        total = a + (b if plus else -b)
        pow = random.randint(2, 4) if (total<7 and total>-7) else 2
        question = 'The sum of the coefficients in the expansion of $(' + \
                   ("" if a==1 else str(a)) + 'x' + op + ("" if b==1 else str(b)) + \
                   'y)^' + str(pow) + '$ is'
        answer = str(total**pow)
    else:
        a, b = random.randint(1, 10), random.randint(1, 10)
        pow = random.randint(3, 10)
        question = 'The number of terms in the expansion of $(' + ("" if a==1 else str(a)) + \
                   'x' + op + ("" if b==1 else str(b)) + 'y)^{' + str(pow) + '}$ is'
        answer = str(pow+1)
    return [question, answer, end]

def UnitsDigit(probNum):
    quesiton, answer, end = '', '', ''
    b, pow = random.randint(3, 99), random.randint(4, 10)
    question = 'The units digit of $' + str(b) + '^{' + str(pow) + '}$ is'
    answer = str(((b%10)**pow) % 10)
    return [question, answer, end]

def PolygonalNumbers(probNum):
    question, answer, end = '', '', ''
    names = ['', '', '', 'triangular', '', 'pentagonal', 'hexagonal', 'heptagonal', 'octagonal']
    if random.randint(0, 2) < 2:
        nSides = random.randint(3, 8)
        while nSides == 4:
            nSides = random.randint(3, 8)
        n = random.randint(4, 13)
        question = 'The $' + str(n) + 'th$ ' + names[nSides] + ' number is'
        if nSides == 3: answer = str(n*(n+1)/2)
        if nSides == 5: answer = str(n*(3*n-1)/2)
        if nSides == 6: answer = str(n*(2*n-1))
        if nSides == 7: answer = str(n*(5*n-3)/2)
        if nSides == 8: answer = str(n*(3*n-2))
    else:
        if random.randint(0, 1):
            nSides = random.randint(3, 8)
            while nSides == 4: nSides = random.randint(3, 8)
            n = random.randint(5, 13)
            question = 'The difference of the $' + str(n) + 'th$ and the $' + str(n-1) + 'th$ ' + names[nSides] + 'numbers is'
            answer = str((nSides - 2)*n - (nSides -3))
        else:
            nSides = random.randint(3, 8)
            while nSides == 4:
                nSides = random.randint(3, 8)
            n = random.randint(5, 13)
            question = 'The sum of the $' + str(n-1) + 'th$ and the $' + str(n) + 'th$ ' + names[nSides] + ' numbers is'
            if nSides == 3: answer = str((n*(n+1)/2) + ((n-1)*n/2))
            if nSides == 5: answer = str((n*(3*n-1)/2) + ((n-1)*(3*(n-1)-1)/2))
            if nSides == 6: answer = str((n*(2*n-1)) + ((n-1)*(2*(n-1)-1)))
            if nSides == 7: answer = str((n*(5*n-3)/2) + ((n-1)*(5*(n-1)-3)/2))
            if nSides == 8: answer = str((n*(3*n-2)) + ((n-1)*(3*(n-1)-2)))
    return [question, answer, end]

def SeriesOfIntWithNoDots(probNum):
    question, answer, end = '', '', ''
    neg = random.randint(0, 1) == 0
    six = random.randint(0, 1) == 0
    terms = [0] * 6
    if neg:
        total, start, end = random.randint(20, 119), 0, 5 if six else 4
        if random.randint(0, 1):
            terms[start] = random.randint(4, total-1)
            start+=1
            terms[end] = total - terms[0]
            end-=1
            terms[start] = random.randint(4, total-1)
            start+=1
            terms[end] = total - terms[1]
            end-=1
            if six:
                terms[start] = random.randint(4, total-1)
                start+=1
                terms[end] = total - terms[2]
                end-=1
            else:
                terms[2] = total/2
            start, end = 0, 5 if six else 4
            if random.randint(0, 1):
                terms[start]*=-1
                terms[end]*=-1
            start+=1
            end-=1
            if random.randint(0, 1):
                terms[start] *= -1
                terms[end] *= -1
            start+=1
            end-=1
            if random.randint(0, 1):
                terms[start]*=1
                terms[end]*=1
        else:
            add = random.randint(-15, 14)
            start = random.randint(50, 119) if add < 0 else random.randint(4, 59)
            terms = [start, start+add, start+2*add, start+3*add, start+4*add, start+5*add]
    else:
        total = random.randint(20, 119)
        start, end = 0, 5 if six else 4
        terms[start] = random.randint(4, total-1)
        start+=1
        terms[end] = total - terms[0]
        end-=1
        terms[start] = random.randint(4, total-1)
        start+=1
        terms[end] = random.randint(4, total-1)
        end-=1
        if six:
            terms[start] = random.randint(4, total-1)
            start+=1
            terms[end] = total - terms[2]
            end-=1
        else:
            terms[2] = total/2
    if six:
        question = '$' + str(terms[0]) + \
                   (' - ' if terms[1] < 0 else ' + ') + str(abs(terms[1])) + \
                   (' - ' if terms[2] < 0 else ' + ') + str(abs(terms[2])) + \
                   (' - ' if terms[3] < 0 else ' + ') + str(abs(terms[3])) + \
                   (' - ' if terms[4] < 0 else ' + ') + str(abs(terms[4])) + \
                   (' - ' if terms[5] < 0 else ' + ') + str(abs(terms[5])) + ' = $'
        ans = 0
        for x in terms: ans+=x
        answer = '$' + str(ans) + '$'
    else:
        question = '$' + str(terms[0]) + \
                   (' - ' if terms[1] < 0 else ' + ') + str(abs(terms[1])) + \
                   (' - ' if terms[2] < 0 else ' + ') + str(abs(terms[2])) + \
                   (' - ' if terms[3] < 0 else ' + ') + str(abs(terms[3])) + \
                   (' - ' if terms[4] < 0 else ' + ') + str(abs(terms[4])) + ' = $'
        ans = 0
        for i in range(5): ans+=terms[i]
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def SeriesOfFractions(probNum):
    question, answer, end = '', '', ''
    num1 = num2 = num3 = den1 = den2 = den3 = 1
    if probNum < 40:
        if random.randint(0, 1) :
            den1 = random.randint(2, 6)
            den2 = den1 * random.randint(1, 4)
            den3 = den2 * ((den2/den1) if random.randint(0, 1) else random.randint(1, 4))
        else:
            den1 = random.randint(2, 6)
            den2 = den1**2
            den3 = den1**3
        if random.randint(0, 1): 
            num1 = num2 = num3 = 1
        else:
            num1, num2, num3 = random.randint(1, den1-1), random.randint(1, den2-1), random.randint(1, den3-1)
    else:
        b = random.randint(3, 4)
        den1, den2, den3 = b*(b+1), (b+1)*(b+2), (b+2)*(b+3)
        num1 = num2 = num3 = 1 if random.randint(0, 2) == 0 else random.randint(1, b-1)
    if random.randint(0, 5) == 0: num1*=-1
    if random.randint(0, 5) == 0: num2*=-1
    if random.randint(0, 5) == 0: num3*=-1
    f1, f2, f3 = Fraction(num1, den1), Fraction(abs(num2), den2), Fraction(abs(num3), den3)
    question = '$' + str(f1) + (' - ' if num2 < 0 else ' + ') + \
                     str(f2) + (' - ' if num3 < 0 else ' + ') + \
                     str(f3) + ' =$'
    f1, f2, f3 = Fraction(num1, den1), Fraction(num2, den2), Fraction(num3, den3)
    ans = fraction.Add(fraction.Add(f1, f2), f3)
    answer = '$' + ans.ToStringAns() + '$'
    return [question, answer, end]

def SequencesWithPowersOrFactorials(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 3)
    if rand == 0:
        x = random.randint(20, 99)
        question = '$' + str(x) + '^2 - ' + str(x-1) + '^2 + ' + str(x-2) + '^2 - ' + str(x-3) + '^2 =$'
        answer = str(x**2 - (x-1)**2 + (x-2)**2 - (x-3)**2)
    elif rand == 1:
        x, ra = random.randint(3, 6), random.randint(0, 2)
        if ra == 0:
            question = '$' + str(x) + '(' + str(x) + '!) + '
            for i in range(x-1, 1, -1):
                question += str(i) + '(' + str(i) + '!) + '
            question += '1(1!) =$'
            answer = str(utility.Factorial(x+1)-1)
        elif ra == 1:
            question = '$1(1!) + '
            for i in range(2, x):
                question += str(i) + '(' + str(i) + '!) + '
            question += str(x) + '(' + str(x) + '!) =$'
            answer = str(utility.Factorial(x+1)-1)
        elif ra == 2:
            question += '$'
            for i in range(2, x):
                question += str(i) + '(' + str(i) + '!) + '
            question += str(x) + '(' + str(x) + '!) =$'
            answer = str(utility.Factorial(x+1)-2)
    elif rand == 2:
        x = random.randint(3, 10)
        if x < 6:
            question += '$'
            for i in range(1, x):
                question += str(i) + '^3 '
            question += str(x) + '^3 =$'
            answer = str((x*(x+1)/2) * (x*(x+1)/2))
        else:
            question = '$1^3 + 2^3 + ..... + '
            question += str(x-1) + '^3 + ' + str(x) + '^3 =$'
            answer = str((x*(x+1)/2) * (x*(x+1)/2))
    elif rand == 3:
        n = random.randint(3, 8)
        question = '$' + str(n) + '^3 '
        a = n**3
        for i in range(n-1, 0, -1):
            if -1**i == 1:
                question += ' - ' + str(i) + '^3 '
                a -= i**3
            else:
                question += ' + ' + str(i) + '^3 '
                a += i**3
        question += '=$'
        answer = '$' + str(a) + '$'
    return [question, answer, end]

def Roman(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 19)
    
    if rand == 0:
        num = random.randint(10, 1999)
        question = '$' + str(num) + ' =$'
        end = '(Roman Numeral)'
        answer = utility.ChangeToRoman(num)
        
    elif rand < 10:
        num = random.randint(10, 1999)
        question = str(utility.ChangeToRoman(num)) + ' $=$'
        end = '(Arabic Numeral)'
        answer = str(num)
        
    else:
        ra = random.randint(0, 2)
        
        if ra == 0:
            num = num2 = 0
            if random.randint(0, 1):
                num, num2 = random.randint(1, 14)*10, random.randint(1, 14)*10
            else:
                num, num2 = random.randint(3, 29)*5, random.randint(1, 9)
            question = utility.ChangeToRoman(num) + ' $+$ ' + utility.ChangeToRoman(num2) + ' $=$'
            end = '(Arabic Numeral)'
            answer = str(num+num2)
            
        elif ra == 1:
            num, num2 = random.randint(1, 199), random.randint(1, 199)
            while len(utility.ChangeToRoman(num)) > 4:
                num = random.randint(1, 199)
            while len(utility.ChangeToRoman(num2)) > 4:
                num2 = random.randint(1, 199)
            question = utility.ChangeToRoman(num) + ' $-$ ' + utility.ChangeToRoman(num2) + ' $=$'
            end = '(Arabic Numeral)'
            answer = str(num-num2)
            
        elif ra == 2:
            num = random.randint(1, 199) if random.randint(0, 1) else random.randint(1, 19)
            num2 = random.randint(1, 9)
            while len(utility.ChangeToRoman(num)) > 4:
                num = random.randint(1, 199)
            question = utility.ChangeToRoman(num) + ' $\\times$ ' + utility.ChangeToRoman(num2) + ' $=$'
            answer = str(num*num2)
            
    return [question, answer, end]

def PrimeDivisors(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    
    if rand == 0:
        num = random.randint(10, 69) if random.randint(0, 1) else random.randint(10, 149)
        question = 'The product of the prime factors of $' + str(num) + '$ is'
        pf = PrimeFact(num)
        ans = 1
        for x in pf.divisors:
            ans *= x
        answer = '$' + str(ans) + '$'
    elif rand < 3:
        num = random.randint(10, 79) if random.randint(0, 1) else random.randint(10, 299)
        question = 'The sum of the prime factors of $' + str(num) + '$ is'
        pf = PrimeFact(num)
        ans = 0
        for x in pf.divisors:
            ans += x
        answer = '$' + str(ans) + '$'
    else:
        num = random.randint(10, 79) if random.randint(0, 1) else random.randint(10, 299)
        question = 'The number of prime factors of $' + str(num) + '$ is'
        pf = PrimeFact(num)
        ans = len(pf.divisors)
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def Volume(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 2)
    if rand == 0: #sphere
        rad = random.randint(1, 9)
        vol = Fraction(4*(rad**3), 3)
        attrib = ['volume', 'surface area', 'diameter', 'radius']
        values = [vol.ToStringAddNum('\\pi'), str(4*rad*rad) + '\\pi', str(rad*2), str(rad)]
        f, to = random.randint(0, 3), random.randint(0, 3)
        while f == to:
            f, to = random.randint(0, 3), random.randint(0, 3)
        question = 'A sphere has a ' + attrib[f] + ' of $' + values[f] + '$. The ' + attrib[to] + ' of the sphere is'
        answer = '$' + values[to] + '$'
    elif rand == 1:
        length = random.randint(2, 10)
        attrib = ['volume', 'side length', 'long diagonal length', 'side area', 'total surface area']
        values = [str(length**3), str(length), utility.SquareRoot(3*length*length), str(length*length), str(6*length*length)]
        f, to = random.randint(0, 4), random.randint(0, 4)
        while f == to:
            f, to = random.randint(0, 4), random.randint(0, 4)
        question = 'A cube has a ' + attrib[f] + ' of $' + values[f] + '$. The ' + attrib[to] + ' of the cube is'
        answer = '$' + values[to] + '$'
    else:
        if random.randint(0, 3) < 3:
            height, rad = random.randint(1, 19), random.randint(1, 9)
            volume = str(height*rad*rad) + '\\pi'
            if random.randint(0, 4) < 2:
                question = 'A cylinder with a height of $' + str(height) + '$ and a radius of $' + str(rad) + '$ has a volume of' if random.randint(0, 1) else \
                           'A cylinder with a height of $' + str(height) + '$ and a diameter of $' + str(2*rad) + '$ has a volume of'
                answer = '$' + str(volume) + '$'
            else:
                question = 'A cylinder with a height of $' + str(height) + '$ and a radius of $' + str(rad) + '$ has a volume of $k\\pi$ and $k$ =' if random.randint(0, 1) else \
                           'A cylinder with a height of $' + str(height) + '$ and a diameter of $' + str(rad*2) + '$ has a volume of $k\\pi$ and $k$ ='
                answer = '$' + str(height*rad*rad) + '$'
        else:
            totsurf = random.randint(5, 99)
            circ = random.randint(1, totsurf-1)
            question = 'A cylinder has a total surface area of $' + str(totsurf) + '$ and a circumference of $' + str(circ) + '$. The sum of its radius and height is'
            f1 = Fraction(totsurf, circ)
            answer = '$' + str(f1) + '$'
    return [question, answer, end]

def Vertex(probNum):
    question, answer, end = '', '', ''
    h = random.randint(0, 1) == 0
    if h:
        a, b, c = random.randint(-5, 4), random.randint(-16, 15), random.randint(-10, 9)
        while a == 0: a = random.randint(-5, 4)
        q = Quadratic(a, b, c)
        ans = Fraction(-b, 2*a)
        question = 'The vertex of the parabola $y = ' + str(q) + '$ is $(h, k)$ and $h =$'
        answer = '$' + str(ans) + '$'
    else:
        a = random.randint(-5, 4)
        b, c = 2*a*random.randint(-4, 3), random.randint(-10, 9)
        while a == 0: a = random.randint(-5, 4)
        q = Quadratic(a, b, c)
        eval = -b/(2*a)
        ans = q.Evaluate(eval)
        question = 'The vertex of the parabola $y = ' + str(q) + '$ is $(h, k)$ and $k =$'
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def UnitConversions(probNum):
    question, answer, end = '', '', ''
    meas = ['inches', 'feet', 'yards', 'miles']
    measVal = [1, 12, 36, 12 * 5280]
    measLegal = [[False, True, True, False], \
                 [True, False, True, True], \
                 [True, True, False, True], \
                 [False, True, True, False]]
    rangeMeas = [[[0,0],[12,360],[36,144],[0,0]], \
                 [[1,24],[0,0],[3,81],[5280,10560]], \
                 [[1,4],[1,81],[0,0],[1760,5280]], \
                 [[0,0],[1,2],[1,3],[0,0]]]
    squareMeas = ['square inches', 'square feet', 'square yards']
    squareMeasVal = [1, 144, 144*9]
    squareMeasLegal = [[False, True, False], \
                       [True, False, True], \
                       [False, True, False]]
    rangeSquareMeas = [[[0,0],[144,720],[0,0]], \
                       [[1,5],[0,0],[9,81]], \
                       [[0,0],[1,27],[0,0]]]
    cubicMeas = ['cubic inches', 'cubic feet', 'cubic yards']
    cubicMeasVal = [1, 12**3, 12*12*12*27]
    cubicMeasLegal = [[False, True, False], \
                      [True, False, True], \
                      [False, True, False]]
    rangeCubicMeas = [[[0,0],[1728,1728*6],[0,0]], \
                      [[1,6], [0,0], [27,81]], \
                      [[0,0],[1,3],[0,0]]]
    metric = ['centimeters', 'meters', 'decameters', 'kilometers']
    metricVal = [1, 100, 1000, 100000]
    metricLegal = [[False, True, True, False], \
                   [True, False, True, True], \
                   [True, True, False, True], \
                   [False, True, True, False]]
    rangeMetric = [[[0,0],[100,10000],[10000,20000],[0,0]], \
                   [[1,10],[0,0],[10, 100], [1000,30000]], \
                   [[1, 2],[1,10], [0,0], [100, 2000]], \
                   [[0, 0], [1, 30], [1, 20], [0, 0]]]
    squareMetric = ['square centimeters', 'square meters', 'square decameters']
    squareMetricVal = [1, 10000, 1000000]
    squareMetricLegal = [[False, True, False], \
                         [True, False, True], \
                         [False, True, False]]
    rangeSquareMetric = [[[0,0], [10000,100000], [0,0]], \
                         [[1, 10], [0,0], [100, 30000]], \
                         [[0,0],[1,30], [0,0]]]
    type, f, to = random.randint(0, 4), 0, 0
    if type == 0:
        f, to = random.randint(0, 3), random.randint(0, 3)
        while not measLegal[f][to]: f, to = random.randint(0, 3), random.randint(0, 3)
    if type == 1:
        f, to = random.randint(0, 2), random.randint(0, 2)
        while not squareMeasLegal[f][to]: f, to = random.randint(0, 2), random.randint(0, 2)
    if type == 2:
        f, to = random.randint(0, 2), random.randint(0, 2)
        while not cubicMeasLegal[f][to]: f, to = random.randint(0, 2), random.randint(0, 2)
    if type == 3:
        f, to = random.randint(0, 3), random.randint(0, 3)
        while not metricLegal[f][to]: f, to = random.randint(0, 3), random.randint(0, 3)
    if type == 4:
        f, to = random.randint(0, 2), random.randint(0, 2)
        while not squareMetricLegal[f][to]: f, to = random.randint(0, 2), random.randint(0, 2)
    
    if random.randint(0, 1):
        val = 0.0
        if   type==0: val = float(random.randint(1, rangeMeas[f][to][1] / rangeMeas[f][to][0] - 1) * rangeMeas[f][to][0])
        elif type==1: val = float(random.randint(1, rangeSquareMeas[f][to][1]/rangeSquareMeas[f][to][0] - 1) * rangeSquareMeas[f][to][0])
        elif type==2: val = float(random.randint(1, rangeCubicMeas[f][to][1]/rangeCubicMeas[f][to][0] - 1) * rangeCubicMeas[f][to][0])
        elif type==3: val = float(random.randint(1, rangeMetric[f][to][1]/rangeMetric[f][to][0] - 1) * rangeMetric[f][to][0])
        elif type==4: val = float(random.randint(1, rangeSquareMetric[f][to][1]/rangeSquareMetric[f][to][0] - 1) * rangeSquareMetric[f][to][0])
                
        if   type==0 and random.randint(0, 3)==0: val+=rangeMeas[f][to][0]*.5
        elif type==1 and random.randint(0, 3)==0: val+=rangeSquareMeas[f][to][0]*.5
        elif type==2 and random.randint(0, 3)==0: val+=rangeCubicMeas[f][to][0]*.5
        elif type==3 and random.randint(0, 3)==0: val+=rangeMetric[f][to][0]*.5
        elif type==4 and random.randint(0, 3)==0: val+=rangeSquareMetric[f][to][0]*.5
        
        if type == 0:
            question = '$' + str(val) + '$' + str(meas[f]) + ' $=$'
            end = str(meas[to])
            answer = str(val * (float(measVal[f]) / measVal[to]))
        elif type == 1:
            question = '$' + str(val) + '$ ' + squareMeas[f] + ' $=$'
            end = str(squareMeas[to])
            answer = str(val*(float(squareMeasVal[f]) / squareMeasVal[to]))        
        elif type == 2:
            question = '$' + str(val) + '$ ' + cubicMeas[f] + ' $=$'
            end = str(cubicMeas[to])
            answer = str(val*(float(cubicMeasVal[f]) / cubicMeasVal[to]))
        elif type == 3:
            question = '$' + str(val) + '$ ' + metric[f] + ' $=$'
            end = str(metric[to])
            answer = str(val*(float(metricVal[f]) / metricVal[to]))
        elif type == 4:
            question = '$' + str(val) + '$ ' + squareMetric[f] + ' $=$'
            end = str(squareMetric[to])
            answer = str(val*(float(squareMetricVal[f]) / squareMetricVal[to]))
    
    else:
        if type == 0:
            while (not measLegal[f][to]) or (f < to):
                f, to = random.randint(0, 3), random.randint(0, 3)
        if type == 1:
            while (not squareMeasLegal[f][to]) or (f < to):
                f, to = random.randint(0, 2), random.randint(0, 2)
        if type == 2:
            while (not cubicMeasLegal[f][to]) or (f < to):
                f, to = random.randint(0, 2), random.randint(0, 2)
        if type == 3:
            while (not metricLegal[f][to]) or (f < to):
                f, to = random.randint(0, 3), random.randint(0, 3)
        if type == 4:
            while (not squareMetricLegal[f][to]) or (f < to):
                f, to = random.randint(0, 2), random.randint(0, 2)
        
        val = 0.0
        if   type==0: val = float(random.randint(1, rangeMeas[f][to][1]/rangeMeas[f][to][0]-1) * rangeMeas[f][to][0])
        elif type==1: val = float(random.randint(1, rangeSquareMeas[f][to][1]/rangeSquareMeas[f][to][0]-1) * rangeSquareMeas[f][to][0])
        elif type==2: val = float(random.randint(1, rangeCubicMeas[f][to][1]/rangeCubicMeas[f][to][0]-1) * rangeCubicMeas[f][to][0])
        elif type==3: val = float(random.randint(1, rangeMetric[f][to][1]/rangeMetric[f][to][0]-1) * rangeMetric[f][to][0])
        elif type==4: val = float(random.randint(1, rangeSquareMetric[f][to][1]/rangeSquareMetric[f][to][0]-1) * rangeSquareMetric[f][to][0])
                
        if   type==0 and random.randint(0, 4)==0: val+=rangeMeas[f][to][0]*.5
        elif type==1 and random.randint(0, 4)==0: val+=rangeSquareMeas[f][to][0]*.5
        elif type==2 and random.randint(0, 4)==0: val+=rangeCubicMeas[f][to][0]*.5
        elif type==3 and random.randint(0, 4)==0: val+=rangeMetric[f][to][0]*.5
        elif type==4 and random.randint(0, 4)==0: val+=rangeSquareMetric[f][to][0]*.5

        ans = 0.0
        if   type==0: ans = (val * (float(measVal[f]) / measVal[to]))
        elif type==1: ans = (val * (float(squareMeasVal[f]) / squareMeasVal[to]))
        elif type==2: ans = (val * (float(cubicMeasVal[f]) / cubicMeasVal[to]))
        elif type==3: ans = (val * (float(metricVal[f]) / metricVal[to]))
        elif type==4: ans = (val * (float(squareMetricVal[f]) / squareMetricVal[to]))
        
        if int(ans) != ans:
            return UnitConversions(probNum)
        den = random.randint(3, 16)
        while ans % den != 0:
            den = random.randint(3, 16)
        num = random.randint(1, den-1)
        frac = Fraction(num, den)
        pre = ('$' + frac.ToPercent() + '$ of ') if random.randint(0, 4) == 0 else ('$' + str(frac) + '$ of ')
        post = ''
        if type == 0:
            post = '$' + str(val) + '$ ' + meas[f] + ' $=$'
            end = meas[to]
        elif type == 1:
            post = '$' + str(val) + '$ ' + squareMeas[f] + ' $=$'
            end = squareMeas[to]
        elif type == 2:
            post = '$' + str(val) + '$ ' + cubicMeas[f] + ' $=$'
            end = cubicMeas[to]
        elif type == 3:
            post = '$' + str(val) + '$ ' + metric[f] + ' $=$'
            end = metric[to]
        elif type == 4:
            post = '$' + str(val) + '$ ' + squareMetric[f] + ' $=$'
            end = squareMetric[to]
        question = pre + post
        ans2 = int(ans)
        a = Fraction(frac.numerator*ans2, frac.denominator)
        answer = str(a)
    return [question, answer, end]

def RightTriangles(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 2) < 2:
        rand = random.randint(0, 2)
        if rand == 0:
            fLeg = random.randint(2, 8) * 2 - 1
            ans = fLeg * fLeg / 2
            question = 'The sides of a right triangle are integral.  If one leg is $' + str(fLeg) + '$ then the other leg is'
            answer = '$' + str(ans) + '$'
        elif rand == 1:
            root = random.randint(2, 10) * 2 - 1
            hype = root*root/2 + 1
            if random.randint(0, 2) == 0:
                question = 'The sides of a right triangle are integral.  If the hypotenuse is $' + str(hype) + '$ then the smallest leg is'
                answer = '$' + str(root) + '$'
            else:
                question = 'The sides of a right triangle are integral.  If the hypotenuse is $' + str(hype) + '$ then the largest leg is'
                answer = '$' + str(hype-1) + '$'
        elif rand == 2:
            if random.randint(0, 2) == 0:
                smallest = random.randint(2, 4)*2 - 1
                middle = smallest*smallest/2
                largest = middle+1
                ratio = str(smallest) + ':' + str(middle) + ':' + str(largest)
                
                mult = random.randint(1, 5)
                attrib = ['smallest leg', 'largest leg', 'hypotenuse']
                attribVal = [smallest*mult, middle*mult, largest*mult]
                f, to = random.randint(0, 2), random.randint(0, 2)
                
                while f == to:
                    f = random.randint(0, 2)
                
                question = 'The sides of a right triangle are in the ratio $' + str(ratio) + '$.  If the ' + attrib[f] + ' is $' + str(attribVal[f]) + '$ then the ' + attrib[to] + ' is'
                answer = '$' + str(attribVal[to]) + '$'
            else:
                thirty = random.randint(0, 1)
                if thirty:
                    small = random.randint(1, 4)**2
                    if random.randint(0, 1): small*=3
                    mid, large = small*3, small*4
                    attrib = ['side opposite $30^\\circ$ in a', 'side opposite $60^\\circ$ in a', 'hypotenuse in a $30-60-90$']
                    attrib2 = ['side opposite $30^\\circ$', 'side opposite $60^\\circ$', 'hypotenuse']
                    attribVal = [utility.SquareRoot(small), utility.SquareRoot(mid), utility.SquareRoot(large)]
                    
                    f, to = random.randint(0, 2), random.randint(0, 2)
                    while f == to:
                        f = random.randint(0, 2)
                    question = 'The ' + attrib[f] + ' right triangle is $' + str(attribVal[f]) + '$.  The ' + attrib2[to] + ' is'
                    answer = '$' + str(attribVal[to]) + '$'
                else:
                    small = random.randint(1, 14)**2
                    if random.randint(0, 1): small*=2
                    large = small*2
                    attrib = ['side opposite $45^\\circ$ in a', 'hypotenuse in a $45-45-90$']
                    attrib2 = ['side opposite $45^\\circ$', 'hypotenuse']
                    attribVal = [utility.SquareRoot(small), utility.SquareRoot(large)]
                    f, to = random.randint(0, 1), random.randint(0, 1)
                    while f == to:
                        f = random.randint(0, 1)
                    question = 'The ' + attrib[f] + ' right triangle is $' + str(attribVal[f]) + '$.  The ' + attrib2[to] + ' is'
                    answer = '$' + str(attribVal[to]) + '$'
    else:
        hyp = random.randint(1, 14)
        strHyp = str(hyp)
        question = "The area of an isosceles right triangle with a hypotenuse of $" + strHyp + "$ is"
        answer = "$" + str(Fraction(hyp*hyp, 4)) + "$"
    return [question, answer, end]

def SumAndProductOfRoots(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 3)
    if rand == 0:
        if random.randint(0, 2) == 0:
            q = Quadratic(random.randint(-5, 4), random.randint(-10, 9), random.randint(-15, 14))
            while q.A == 0: q.A = random.randint(-5, 4)
            question = 'The product of the roots of $' + str(q) + '$ is'
            ans = Fraction(q.C, q.A)
            answer = '$' + ans.ToStringAns() + '$'
        else:
            c = Cubic(random.randint(-5, 4), random.randint(-10, 9), random.randint(-10, 9), random.randint(-15, 14))
            while c.A == 0:
                c.A = random.randint(-5, 4)
            question = 'The product of the roots of $' + str(c) + '$ is'
            answer = '$' + Fraction(-c.D, c.A).ToStringAns() + '$'
    elif rand == 1:
        if random.randint(0, 2) == 0:
            q = Quadratic(random.randint(-5, 4), random.randint(-6, 5), random.randint(-10, 9))
            if random.randint(0, 1):
                val = Fraction(-q.B, q.A)
                ret = 'ax^2'
                if q.B != 0:
                    ret += ' - ' if q.B < 0 else ' + '
                    ret += "" if q.B == 1 else str(abs(q.B)) + 'x'
                if q.C != 0:
                    ret += ' - ' if q.C < 0 else ' + '
                    ret += str(abs(q.C))
                question = 'The equation $' + str(ret) + '$ has roots $r$ and $s$.  If $r + s = ' + str(val) + '$ then $a =$'
                answer = '$' + str(q.A) + '$'
            else:
                val = Fraction(q.C, q.A)
                ret = 'ax^2'
                if q.B != 0:
                    ret += ' - ' if q.B < 0 else ' + '
                    ret += "" if q.B == 1 else str(abs(q.B)) + 'x'
                if q.C != 0:
                    ret += ' - ' if q.C < 0 else ' + '
                    ret += str(abs(q.C))
                question = 'The equation $' + str(ret) + '$ has roots $r$ and $s$.  If $rs = ' + str(val) + '$ then $a =$'
                answer = '$' + str(q.A) + '$'
        else:
            c = Cubic(random.randint(-4, 3), random.randint(-4, 3), random.randint(-8, 7), random.randint(-8, 7))
            ra = random.randint(0, 2)
            if ra == 0:
                val = Fraction(-c.B, c.A)
                ret = 'ax^3'
                if c.B != 0:
                    ret += ' - ' if c.B < 0 else ' + '
                    ret += '' if c.B == 1 else str(abs(c.B)) + 'x^2'
                if c.C != 0:
                    ret += ' - ' if c.C < 0 else ' + '
                    ret += '' if c.C == 1 else str(abs(c.C)) + 'x'
                if c.D != 0:
                    ret += ' - ' if c.D < 0 else ' + '
                    ret += str(abs(c.D))
                question = 'The equation $' + str(ret) + '$ has roots $r$, $s$, $t$.  If $r+s+t$ = $' + str(val) + '$ then $a =$'
                answer = '$' + str(c.A) + '$'
            elif ra == 1:
                val = Fraction(-c.D, c.A)
                ret = 'ax^3'
                if c.B != 0:
                    ret += ' - ' if c.B < 0 else ' + '
                    ret += '' if c.B == 1 else str(abs(c.B)) + 'x^2'
                if c.C != 0:
                    ret += ' - ' if c.C < 0 else ' + '
                    ret += '' if c.C==1 else str(abs(c.C)) + 'x'
                if c.D != 0:
                    ret += ' - ' if c.D < 0 else ' + '
                    ret += str(abs(c.D))
                question = 'The equation $' + ret + '$ has roots $r$, $s$, and $t$.  If $rst = ' + str(val) + '$ then $a =$'
                answer = '$' + str(c.A) + '$'
            elif ra == 2:
                val = Fraction(c.C, c.A)
                ret = 'ax^3'
                if c.B != 0:
                    ret += ' - ' if c.B < 0 else ' + '
                    ret += '' if c.B == 1 else str(abs(c.B)) + 'x^2'
                if c.C != 0:
                    ret += ' - ' if c.C < 0 else ' + '
                    ret += '' if c.C == 1 else str(abs(c.C)) + 'x'
                if c.D != 0:
                    ret += ' - ' if c.D < 0 else ' + '
                    ret += str(abs(c.D))
                question = 'The equation $' + str(ret) + '$ has roots $r$, $s$, and $t$.  If $rs+rt+st = ' + str(val) + '$ then $a =$'
                answer = '$' + str(c.A) + '$'
    else:
        if random.randint(0, 2) == 0:
            c = Cubic(random.randint(-4, 3), random.randint(-4, 3), random.randint(-8, 7), random.randint(-8, 7))
            while c.A == 0: c.A = random.randint(-4, 3)
            question = "The sum of the roots of $" + str(c) + " = 0$ is"
            ans = Fraction(-c.B, c.A)
            ans.Reduce()
            answer = '$' + str(ans) + '$'
        else:
            q = Quadratic(random.randint(-5, 4), random.randint(-6, 5), random.randint(-10, 9))
            while q.A == 0: q.A = random.randint(-5, 4)
            question = 'Thum sum of the roots of $' + str(q) + ' = 0$ is'
            ans = Fraction(-q.B, q.A)
            answer = '$' + ans.ToStringAns() + '$'
    return [question, answer, end]

def SquareRootOperations(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    if rand == 0:
        val1, val2 = (random.randint(2, 5)**2) * random.randint(2, 5), (random.randint(2, 5)**2) * random.randint(2, 5)
        question = '$\\sqrt{' + str(val1) + '} \\times \\sqrt{' + str(val2) + '} =$'
        answer = '$' + utility.SquareRoot(val1*val2) + '$'
    elif rand < 3:
        val1, val2 = random.randint(15, 199), random.randint(15, 199)
        question = '$\\sqrt{' + str(val1) + '} \\div \\sqrt{' + str(val2) + '} \\times \\sqrt{' + str(val1) + '} \\div \\sqrt{' +str(val2) + '} =$'
        answer = '$' + str(Fraction(val1, val2)) + '$'
    else:
        val1, val2 = (random.randint(2, 6)**2) * random.randint(1, 5), (random.randint(2, 6)**2) * random.randint(1, 5)
        while val1 == val2: val2 = (random.randint(2, 6)**2) * random.randint(1, 5)
        ans = radical.Divide(Radical(1, 1, val1), Radical(1, 1, val2))
        question = '$\\displaystyle\\frac{\\sqrt{' + str(val1) + '}}{\\sqrt{' + str(val2) + '}}$'
        answer = '$' + str(ans) + '$'
    return [question, answer, end]
                              
def SameResults(probNum):
    question, answer, end = '', '', ''
    rand, num = random.randint(0, 3), random.randint(2, 15)
    times = random.randint(3, 13)
    plus = times*num - num
    minus = times*num + num
    if(rand==0):
        question = 'What number times $' + str(times) + '$ and added to $' + str(plus) + '$ gives the same results?'
    elif(rand==1):
        question = 'What number times $' + str(times) + '$ and subtracted from $' + str(minus) + '$ gives the same results?'
    elif(rand==2):
        question = 'What number added to $' + str(plus) + '$ and times $' + str(times) + '$ gives the same results?'
    elif(rand==3):
        question = 'What number subtracted from $' + str(minus) + '$ and times $' + str(times) + '$ gives the same results?'
    answer = str(num)
    return [question, answer, end]
                  
def Remainders(probNum):
    question, answer, end = '', '', ''
    ans = 0
    if probNum < 60:
        val1 = random.randint(2, 69)
        val2 = random.randint(2, 69)
        val3 = random.randint(2, 69)
        val4 = random.randint(2, 69)
        val5 = random.randint(2, 69)
        pow = random.randint(2, 10)        
        div, rand = random.randint(2, 12), random.randint(0, 9)
        if rand == 0:
            question = '$(' + str(val1) + ' \\times ' + str(val2) + ' - ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1*val2-val3)%div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' \\times ' + str(val2) + ' - ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1*val2-val3)%div
        elif rand == 1:
            question = '$(' + str(val1) + ' \\times ' + str(val2) + ' - ' + str(val3) + '^{' + str(pow) + '}) \\div ' + str(div) + '$ has a remainder of'
            ans = (val1*val2 - val3**pow) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' \\times ' + str(val2) + ' - ' + str(val3) + '^{' + str(pow) + '}) \\div ' + str(div) + '$ has a remainder of'
                ans = (val1*val2 - val3**pow) % div
        elif rand == 2:
            question = '$(' + str(val1) + '^{' + str(pow) + '} + ' + str(val3) + ' \\times ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1**pow + val3*val4) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + '^{' + str(pow) + '} + ' + str(val3) + ' \\times ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1**po2 + val3*val4) % div
        elif rand == 3:
            question = '$(' + str(val1) + ' \\times ' + str(val2) + ' + ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1*val2 + val3) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' \\times ' + str(val2) + ' + ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1*val2 + val3) % div
        elif rand == 4:
            question = '$(' + str(val1) + ' \\times ' + str(val2) + ' - ' + str(val3) + ' \\times ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1*val2 - val3*val4) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' \\times ' + str(val2) + ' - ' + str(val3) + ' \\times ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1*val2 - val3*val4) % div
        elif rand == 5:
            question = '$(' + str(val1) + ' + ' + str(val2) + ' \\times ' + str(val3) + ' + ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1+val2*val3+val4) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' + ' + str(val2) + ' \\times ' + str(val3) + ' + ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1+val2*val3+val4) % div
        elif rand == 6:
            question = '$(' + str(val1) + ' + ' + str(val2) + ' - ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1 + val2 - val3) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' + ' + str(val2) + ' - ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1 + val2 - val3) % div
        elif rand == 7:
            question = '$(' + str(val1) + ' + ' + str(val2) + ' \\times ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1 + val2*val3) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + ' + ' + str(val2) + ' \\times ' + str(val3) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1 + val2*val3) % div
        elif rand == 8:
            question = '$(' + str(val1) + '^{' + str(pow) + '} - ' + str(val3) + ' \\times ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = (val1**pow - val3*val4) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + '^{' + str(pow) + '} - ' + str(val3) + ' \\times ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = (val1**pow - val3*val4) % div
        elif rand == 9:
            question = '$(' + str(val1) + '^{' + str(pow) + '} \\times ' + str(val3) + ' - ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
            ans = ((val1**pow) * val3 - val4) % div
            while ans < 0:
                val1 = random.randint(2, 69)
                val2 = random.randint(2, 69)
                val3 = random.randint(2, 69)
                val4 = random.randint(2, 69)
                val5 = random.randint(2, 69)
                pow = random.randint(2, 10)
                question = '$(' + str(val1) + '^{' + str(pow) + '} \\times ' + str(val3) + ' - ' + str(val4) + ') \\div ' + str(div) + '$ has a remainder of'
                ans = ((val1**pow) * val3 - val4) % div
        answer = '$' + str(ans) + '$'
    else:
        if random.randint(0, 1):
            ans = -1
            while ans < 0:
                num1, pow, num2 = random.randint(2, 9), random.randint(2, 11), random.randint(2, 13)
                while num1 == num2: num1 = random.randint(2, 9)
                question = '$' + str(num1) + '^{' + str(pow) + '} \\div ' + str(num2) + '$ has a remainder of'
                ans = (num1**pow) % num2
        else:
            ans = -1
            while ans < 0:
                bigNum, rand = 0, random.randint(0, 3)
                if rand == 0: bigNum = random.randint(100000, 999999)
                elif rand == 1: bigNum = random.randint(10000, 99999)
                elif rand == 2: bigNum = random.randint(1000000, 9999999)
                elif rand == 3: bigNum = random.randint(10000000, 99999999)
                div = random.randint(3, 11)
                question = '$' + str(bigNum) + ' \\div ' + str(div) + '$ has a remainder of'
                ans = bigNum % div
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def QuadraticWithK(probNum):
    question, answer, end = '', '', ''
    q = Quadratic(random.randint(-3, 3), random.randint(-3, 3), 1)
    while q.A == 0: q.A = random.randint(-3, 3)
    ret = ''
    if q.A != 0:
        ret += "" if q.A == 1 else ("-" if q.A==-1 else str(q.A)) + 'x^2'
    if q.B != 0:
        ret += ' - ' if q.B < 0 else ' + '
        ret += ('' if abs(q.B) == 1 else str(abs(q.B))) + 'x'
    minus = random.randint(0, 1) == 0
    ret += ' - ' if minus else ' + '
    if random.randint(0, 1) == 0:
        ret += 'k'
        question = 'For what value of $k$ does $' + str(ret) + '$ have equal roots?'
        ans = Fraction(q.B**2, 4*q.A)
        if minus: ans.numerator *= -1
        answer = '$' + str(ans) + '$'
    else:
        coeff = random.randint(2, 4)
        ret += str(coeff) + 'k'
        question = 'For what value of $k$ does $' + str(ret) + '$ have equal roots?'
        ans = Fraction(q.B**2, 4*q.A*coeff)
        if minus: ans.numerator *= -1
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def Polar(probNum):
    question, answer, end = '', '', ''
    num = random.randint(1, 4)
    if random.randint(0, 4) == 0:
        num*=-1
    deg, rand = 0, random.randint(0, 36)
    if rand < 4: deg = 30
    elif rand < 8: deg = 45
    elif rand < 12: deg = 60
    elif rand < 16: deg = 90
    elif rand < 18: deg = 120
    elif rand < 20: deg = 135
    elif rand < 22: deg = 150
    elif rand < 24: deg = 180
    elif rand == 25: deg = 210
    elif rand == 26: deg = 225
    elif rand == 27: deg = 240
    elif rand == 28: deg = 270
    elif rand == 29: deg = 300
    elif rand == 30: deg = 315
    elif rand == 31: deg = 330
    elif rand < 36: deg = 0
    refAngle = utility.RefAngle(deg)
    
    if refAngle == 0:
        if deg <= 90 or deg >=270:
            rectx = str(num)
        else:
            rectx = str(-num)
        recty = '0'
    elif refAngle == 30:
        f = Fraction(num, 2)
        if deg <= 90 or deg >= 270:
            rectx = str(Radical(f.numerator, f.denominator, 3))
        else:
            rectx = str(Radical(-f.numerator, f.denominator, 3))
        if deg <= 180:
            recty = str(f)
        else: recty = str(Fraction(-f.numerator, f.denominator))
    
    elif refAngle == 45:
        f = Fraction(num, 2)
        if deg <= 90 or deg >= 270:
            rectx = str(Radical(f.numerator, f.denominator, 2))
        else:
            rectx = str(Radical(-f.numerator, f.denominator, 2))
        if deg <= 180:
            recty = str(Radical(f.numerator, f.denominator, 2))
        else:
            recty = str(Radical(-f.numerator, f.denominator, 2))
    elif refAngle == 60:
        f = Fraction(num, 2)
        if deg <= 90 or deg >= 270:
            rectx = str(f)
        else:
            rectx = str(Fraction(-f.numerator, f.denominator))
        if deg <= 180:
            recty = str(Radical(f.numerator, f.denominator, 3))
        else:
            recty = str(Radical(-f.numerator, f.denominator, 3))
    elif refAngle == 90:
        rectx = '0'
        if deg <= 180:
            recty = str(num)
        else:
            recty = str(-num)
    
    rect = '($' + str(rectx) + '$,$' + str(recty) + '$)'
    polTheta = utility.DegToPolar(deg)
    polR = str(num)
    pol = '($' + str(polR) + '$,$' + str(polTheta) + '$)'
    if random.randint(0, 2) == 0:
        if random.randint(0, 1):
            question = str(rect) + ' are rectangular coordinates for the polar coordinates $(r, \\theta)$.  Find $\\theta$.'
            answer = '$' + str(polTheta) + '$'
        else:
            question = str(rect) + ' are rectangular coordinates for the polar coordinates $(r, \\theta)$.  Find $\\theta$.'
            answer = '$' + str(polTheta) + '$'
    else:
        if random.randint(0, 1):
            question = str(pol) + ' are polar coordinates for $(x, y)$.  Find $x$.'
            answer = '$' + str(rectx) + '$'
        else:
            question = str(pol) + ' are polar coordinates for $(x, y)$.  Find $y$.'
            answer = '$' + str(recty) + '$'
    return [question, answer, end]

def PermComb(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 7)
    if rand < 4:
        big = random.randint(4, 9)
        small = random.randint(2, big)
        C = random.randint(0, 1) == 0
        question = '$_' + str(big) + ('C' if C else 'P') + '_' + str(small) + ' =$'
        answer = str(utility.Comb(big, small)) if C else str(utility.Perm(big, small))
    elif rand < 7:
        if random.randint(0, 3) == 0:
            big1, big2 = random.randint(3, 5), random.randint(3, 5)
            small1, small2 = random.randint(big1-2, big1), random.randint(big2-2, big2)
            C1, C2 = random.randint(0, 1)==0, random.randint(0, 1)==0
            question = '$_' + str(big1) + ('C' if C1 else 'P') + '_' + str(small1) + '\\ \\times\\ _' + str(big2) + ('C' if C2 else 'P') + '_' + str(small2) + ' =$'
            first = utility.Comb(big1, small1) if C1 else utility.Perm(big1, small1)
            second = utility.Comb(big2, small2) if C2 else utility.Perm(big2, small2)
            answer = str(first*second)
        else:
            C1 = random.randint(0, 1) == 0
            C2 = not C1
            big1 = big2 = random.randint(3, 9)
            small1 = random.randint(1, big1)
            small2 = small1 if random.randint(0, 1) else (big1-small1)
            question = '$_' + str(big1) + ('C' if C1 else 'P') + '_' + str(small1) + '\\ \\times\\ _' + str(big2) + ('C' if C2 else 'P') + '_' + str(small2) + ' =$'
            first = utility.Comb(big1, small1) if C1 else utility.Perm(big1, small1)
            second = utility.Comb(big2, small2) if C2 else utility.Perm(big2, small2)
            answer = '$' + str(Fraction(first, second)) + '$'
    elif rand == 7:
        objects = ['objects', 'penguins', 'committee members', 'llamas', 'blocks', \
                   'students', 'compact discs', 'shrubberies', 'tasks']
        big = random.randint(3, 9)
        small = random.randint(2, big-1)
        question = 'In how many ways can you group $' + str(big) + '$ distinct ' + objects[random.randint(0, len(objects)-1)] + ' in groups of $' + str(small) + '$?'
        answer = str(utility.Comb(big, small))
    return [question, answer, end]

def PercentToFraction(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    if rand == 0:
        den = random.randint(6, 16)
        num = 1 if random.randint(0, 1) else random.randint(1, den-1)
        f = Fraction(num, den, False)
        while not f.isReduced():
            num = 1 if random.randint(0, 1) else random.randint(1, den-1)
            f = Fraction(num, den)
        m = MixedNumber(num*100, den)
        question = '$' + str(m) + '\\% =$'
        end = '(fraction)'
        f.Reduce()
        answer = '$' + str(f) + '$'
    elif rand == 1:
        num = random.randint(101, 998)
        question = '$' + str(num) + '\\%' + ' =$'
        end = '(mixed number)'
        m = MixedNumber(num/100, num%100, 100)
        m.f.Reduce()
        answer = '$' + str(m) + '$'
    elif rand == 2:
        num = random.randint(11, 98)
        question = '$' + str(num) + '\\% =$'
        end = '(fraction)'
        f = Fraction(num, 100)
        answer = '$' + str(f) + '$'
    elif rand == 3:
        m = MixedNumber(random.randint(1, 29), random.randint(2, 9))
        question = '$' + str(m) + '\\% =$'
        end = '(fraction)'
        ans = Fraction(m.f.numerator + m.co*m.f.denominator, m.f.denominator*100)
        answer = '$' + str(ans) + '$'
    elif rand == 4:
        co = random.randint(1, 9)
        add = utility.CommonDecimal()
        f = utility.ToFraction(add)
        question = '$' + str(co+add) + '\\% =$'
        end = '(fraction)'
        ans = Fraction(co*f.denominator + f.numerator, f.denominator*100)
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def PercentToDecimal(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 2) == 0:
        den = utility.rationalDen()
        m = MixedNumber(random.randint(0, 4), random.randint(1, den-1), den)
        question = '$' + str(m) + '\\% =$'
        end = '(decimal)'
        answer = utility.DoubleToAns((m.co + m.f.DecValue())/100.0)
    else:
        den = utility.rationalDen()
        m = MixedNumber(random.randint(0, 119), random.randint(1, den-1), den)
        question = '$' + str(m) + '\\% =$'
        end = '(decimal)'
        answer = utility.DoubleToAns((m.co + m.f.DecValue())/100.0)
    return [question, answer, end]

def APercentOfBIsC(probNum):
    question, answer, end = '', '', ''
    if (probNum < 40 and random.randint(0, 4) < 4) or (probNum >= 40 and random.randint(0, 4) == 4):
        rand = random.randint(0, 2)
        if probNum > 30 and random.randint(0, 2) < 2:
            rand = 2
        if rand == 0:
            rationalDen = utility.rationalDen()
            f = Fraction(random.randint(1, rationalDen-1), rationalDen)
            m = MixedNumber(f.numerator*100/f.denominator, f.numerator * 100 % f.denominator, f.denominator)
            while m.f.numerator == 0 and random.randint(0, 4) < 4:
                f = Fraction(random.randint(1, rationalDen-1), rationalDen)
                m = MixedNumber(f.numerator*100/f.denominator, f.numerator * 100 % f.denominator, f.denominator)    
            whole = f.denominator * random.randint(1, 19)
            ans = Fraction(f.numerator * whole, f.denominator)
            question = '$' + str(m) + '$\\% of $' + str(whole) + '$ is'
            answer = '$' + ans.ToStringAns() + '$'
        elif rand == 1:
            perc, whole = random.randint(11, 99), random.randint(5, 99)
            dWhole = -1.0
            if random.randint(0, 4) == 0:
                dWhole = utility.Decimalize(perc)
            question = '$' + str(perc) + '\\%$ of $' + (str(whole) if dWhole==-1 else str(dWhole)) + '$ is'
            answer = '$' + str((float(perc) / 100) * (whole if dWhole == -1 else dWhole)) + '$'
        else:
            first, second = random.randint(5, 99), random.randint(5, 99)
            question = '$' + str(first) + '\\%$ of $' + str(second) + '\\%$ is'
            end = '$\\%$'
            answer = '$' + str(float(first) * second / 100) + '$'
    else:
        repeat = random.randint(11, 98)
        while repeat % 10 == 9 or repeat % 10 == 0:
            repeat = random.randint(11, 98)
        f = Fraction(repeat - repeat / 10, 90)
        while f.denominator > 30:
            repeat = random.randint(11, 98)
            while repeat % 10 == 9 or repeat % 10 == 0:
                repeat = random.randint(11, 98)
            f = Fraction(repeat - repeat / 10, 90)
        m = MixedNumber(repeat / 10 * 100 + repeat % 10 * 11, repeat % 10, 9)
        perc = float(f.denominator) * random.randint(1, 9) / 10
        while perc != int(perc) and random.randint(0, 19) < 19:
            perc = float(f.denominator) * random.randint(1, 9) / 10
        question = '$' + str(perc) + '\\%$ of $' + str(m) + '$ is'
        ans = Fraction(int(f.numerator*10*perc), f.denominator)
        answer = '$' + ans.ToStringAns() + '$'
    return [question, answer, end]

def APercentOfBIsCPercentOfD(probNum):
    question, answer, end = '', '', ''
    numA, numD = random.randint(10, 49), random.randint(10, 49)
    numC = numA * random.randint(2, 4)
    numB = numD * (numC / numA)
    while numC > 100 or (numD > 100 and random.randint(0, 2) < 2):
        numA, numD = random.randint(10, 49), random.randint(10, 49)
        numC = numA * random.randint(2, 4)
        numB = numD * (numC / numA)
    if random.randint(0, 1):
        temp = numA
        numA = numC
        numC = temp
        
        temp = numD
        numD = numB
        numB = temp
    
    question = '$' + str(numA) + '\\%$ of $' + str(numB) + '$ is'
    end = '$\\%$ of $' + str(numD) + '$'
    answer = '$' + str(numC) + '$'
    
    return [question, answer, end]

def AddingSubtractingMixedNumbers(probNum):
    question, answer, end = '', '', ''
    while True:
        num = random.randint(2, 29)
        while utility.isPrime[num] and random.randint(0, 2) < 2:
            num = random.randint(2, 29)
        Factors = utility.Factors(num)
        den1 = Factors[random.randint(1, len(Factors)-1)]
        den2 = Factors[random.randint(1, len(Factors)-1)]
        m1 = MixedNumber(random.randint(1, 9), random.randint(1, den1-1), den1)
        m2 = MixedNumber(random.randint(1, 9), random.randint(1, den2-1), den2)
        if not (den1 == den2 and random.randint(0, 4) < 4):
            break
    
    subtract = random.randint(0, 4) < 2
    if subtract:
        question = '$' + str(m1) + ' - ' + str(m2) + ' = $'
        answer = '$' + mixedNumber.Subtract(m1, m2).ToFraction().ToStringAns() + '$'
    else:
        question = '$' + str(m1) + ' + ' + str(m2) + ' = $'
        answer = '$' + mixedNumber.Add(m1, m2).ToFraction().ToStringAns() + '$'
    return [question, answer, end]

def Adding2Fractions(probNum):
    question, answer, end = '', '', ''
    if (probNum < 60 and random.randint(0, 5) < 5) or (probNum >= 60 and random.randint(0, 5) == 0):
        if random.randint(0, 1):
            f1 = fraction.LessThan1Fraction(20, 20)
            f2 = fraction.LessThan1Fraction(20, 20)
        else:
            f1 = fraction.LessThan1Fraction(10, 10)
            den = f1.denominator * random.randint(2, 5)
            f2 = Fraction(random.randint(1, den-1), den)
    else:
        den1 = random.randint(10, 19)
        num1 = den1 - random.randint(1, 4)
        den2 = num1
        num2 = den1-num1
        f1, f2 = Fraction(num1, den1), Fraction(num2, den2)
    if random.randint(0, 1):
        temp = f1
        f1 = f2
        f2 = temp
    
    question = '$' + str(f1) + ' + ' + str(f2) + ' = $'
    answer = '$' + fraction.Add(f1, f2).ToStringAns() + '$'
    return [question, answer, end]

def AIsBPercentOfC(probNum):
    question, answer, end = '', '', ''
    if (probNum < 40 and random.randint(0, 4) < 4) or (probNum >= 40 and random.randint(0, 4) == 4):
        perc = random.randint(6, 99)
        f = Fraction(perc, 99)
        num = f.numerator * random.randint(1, 9)
        if random.randint(0, 2) < 2:
            question = '$' + str(num) + '$ is $' + str(perc) + '\\%$ of'
            answer = '$' + str(num*100/perc) + '$'
        else:
            question = '$' + str(num) + '$ is'
            end = '$\\%$ of ' + str(num*100 / perc)
            answer = '$' + str(perc) + '$'
    else:
        den = random.randint(6, 50)
        while len(utility.Factors(den)) <= 4:
            den = random.randint(6, 50)
        f = Fraction(1, den-1)
        m = MixedNumber(f.numerator*100/f.denominator, f.numerator*100%f.denominator, f.denominator)
        dec = -1.0
        if len(str(f.DecValue())) < 7 and random.randint(0, 2) < 2:
            dec = f.DecValue() * 100
        num = random.randint(3, 50)
        if random.randint(0, 2) == 0:
            question = '$' + str(num) + '$ is $' + (str(m) if dec==-1 else str(dec)) + ' \\%$ of'
            answer = str(num*den)
        else:
            question = '$' + str(num) + '$ is'
            end = '$\\%$ of ' + str(num*den)
            answer = '$' + (m.ToFraction().ToStringAns() if dec==-1 else str(dec)) + '$'
    return [question, answer, end]

def APercentOfBWithSomeOtherOperation(probNum):
    question, answer, end = '', '', ''
    rand, rand2 = random.randint(0, 2), random.randint(0, 5)
    if rand == 0:
        n = random.randint(1, 12)
        while n == 10:
            n = random.randint(1, 12)
        inum1 = inum2 = inum3 = n*10
        snum1 = snum2 = snum3 = str(inum1)
        snum2 += '\\%'
        
        if rand2 < 2: answer = str(inum2*inum3/100+inum1)
        elif rand2 < 4: answer = str(inum2*inum3/100*inum1)
        elif rand2 == 4: answer = str(inum2*inum3/100-inum1)
        else: answer = str(inum1 - (inum2*inum3/100))
    elif rand == 2:
        inum1 = random.randint(3, 12) * 10
        inum2 = inum1 + (10 if random.randint(0, 1) else -10)
        while inum2 == 100:
            inum2 = inum1 + (10 if random.randint(0,1) else -10)
        inum3 = inum1 + (20 if random.randint(0, 1) else -20)
        snum1 = str(inum1)
        snum2 = str(inum2)
        snum3 = str(inum3)
        snum2 += '\\%'
        if rand2 < 2: answer = str(inum2*inum3 / 100 + inum1)
        elif rand2 < 4: answer = str(inum2*inum3/100*inum1)
        elif rand2==4: answer = str(inum2*inum3 / 100 - inum1)
        else: answer = str(inum1 - (inum2*inum3/100))
    else:
        den = random.randint(2, 16)
        f1 = Fraction(random.randint(1, den-1), den)
        snum2 = f1.ToPercent()
        inum3 = den*random.randint(2, 5)*10
        snum3 = str(inum3)
        inum1 = inum3+10-random.randint(0, 2)*10
        snum1 = str(inum1)
        
        if rand2 < 2: answer = str(f1.numerator*inum3/f1.denominator + inum1)
        elif rand2 < 4: answer = str(f1.numerator*inum3/f1.denominator*inum1)
        elif rand2 == 4: answer = str(f1.numerator*inum3/f1.denominator -inum1)
        else: answer = str(inum1-f1.numerator*inum3/f1.denominator)
        
    if rand2 < 2:
        question = '$' + str(snum2) + '$ of $' + str(snum3) + '$'
        if random.randint(0, 1):
            question += ' plus $' + str(snum1) + '$'
        else:
            question = '$' + str(snum1) + '$ plus ' + question
    elif rand2 < 4:
        question = '$' + str(snum2) + '$ of $' + str(snum3) + '$'
        if random.randint(0, 1) == 0:
            question += ' times $' + str(snum1) + '$'
        else:
            question = '$' + str(snum1) + '$ times ' + question
    else:
        question = '$' + str(snum2) + '$ of $' + str(snum3) + '$'
        st = 'minus' if random.randint(0, 1) else 'less'
        if rand2 == 4:
            question += ' ' + st + ' $' + str(snum1) + '$'
        else:
            question = '$' + str(snum1) + '$ ' + st + ' ' + question
    return [question, answer, end]

def Asymptotes(probNum):
    question, answer, end = '', '', ''
    A = random.randint(1, 12) * (-1 if random.randint(0, 3) == 0 else 1)
    B = random.randint(1, 12) * (-1 if random.randint(0, 3) == 0 else 1)
    if random.randint(0, 1):
        C = B * (-1 if random.randint(0, 1) else 1)
        D = A * (-1 if random.randint(0, 1) else 1)
    else:
        C = random.randint(1, 12) * (-1 if random.randint(0, 3) == 0 else 1)
        D = random.randint(1, 12) * (-1 if random.randint(0, 3) == 0 else 1)
    
    top, bottom = Linear(A, B), Linear(C, D)
    
    if random.randint(0, 1):
        question = 'The horizontal asymptote of $\\displaystyle\\frac{' + str(top) + '}{' + str(bottom) + '}$ is $y = $'
        ans = Fraction(A, C)
        answer = '$' + str(ans) + '$'
    else:
        question = 'The vertical asymptote of $\\displaystyle\\frac{' + str(top) + '}{' + str(bottom) + '}$ is $x = $'
        ans = Fraction(B*-1, A)
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def Integrals(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 8)
    if rand == 0:
        exp = fraction.LessThan1Fraction(5, 5)
        question = '$\\int_0^1x^{' + exp.ToStringNoDisp() + '}\\ dx =$'
        exp2 = Fraction(exp.numerator + exp.denominator, exp.denominator)
        fco = Fraction(exp2.denominator, exp2.numerator)
        answer = '$' + fco.ToStringAns() + '$'
    elif rand < 4:
        A = random.randint(-2, 2)
        if random.randint(0, 1):
            A = random.randint(-2, 2)
        B = random.randint(-2, 2)
        lin = Linear(A, B)
        bottom = 0 if random.randint(0, 1) else random.randint(-2, 2)
        top = random.randint(-2, 2)
        while (top <= bottom and random.randint(0, 4) < 3) or (top == 0 and bottom == 0):
            bottom = 0 if random.randint(0, 1) == 0 else random.randint(-2, 2)
            top = random.randint(-2, 2)
        if bottom == top and random.randint(0, 3) < 3: return Integrals(probNum)
        question = '$\\int_{' + str(bottom) + '}^{' + str(top) + '}' + str(lin) + '\\ dx =$'
        co = Fraction(A, 2)
        valTop = fraction.Add(Fraction(top*top*co.numerator, co.denominator), Fraction(B*top, 1))
        valBot = fraction.Add(Fraction(bottom*bottom*co.numerator, co.denominator), Fraction(B*bottom, 1))
        answer = '$' + fraction.Subtract(valTop, valBot).ToStringAns() + '$'
    elif rand < 6:
        exp = random.randint(1, 2)
        co = Fraction(1, exp)
        bottom = fraction.LessThan1Fraction(4, 4) if random.randint(0, 4) == 0 else Fraction(random.randint(-3, 4), 1)
        top = fraction.LessThan1Fraction(4, 4) if random.randint(0, 4) == 0 else Fraction(random.randint(0, 4), 1)
        while (str(bottom) == str(top)):
            bottom = fraction.LessThan1Fraction(4, 4) if random.randint(0, 4) == 0 else Fraction(random.randint(-3, 4), 1)
            top = fraction.LessThan1Fraction(4, 4) if random.randint(0, 4) == 0 else Fraction(random.randint(0, 4), 1)
        strExp = '' if exp == 1 else ('^{ ' + str(exp) + '}')
        question = '$\\int_{' + bottom.ToStringNoDisp() + '}^{' + top.ToStringNoDisp() + '}x' + strExp + '\\ dx =$'
        valTop = Fraction(top.numerator**(exp+1), (top.denominator**(exp+1)) * (exp+1))
        valBot = Fraction(bottom.numerator**(exp+1), (bottom.denominator**(exp+1)) * (exp+1))
        answer = '$' + fraction.Subtract(valTop, valBot).ToStringAns() + '$'
    elif rand < 8:
        frac = fraction.LessThan1Fraction(5, 5)
        bottom = random.randint(0, 4)
        top = random.randint(bottom, 5)
        if bottom == top and random.randint(0, 3) < 3:
            return Integrals(probNum)
        question = "$\\int_{" + str(bottom) + "}^{" + str(top) + "}" + frac.ToStringNoDisp() + "x\\ dx =$"
        valTop = Fraction(top * top * frac.numerator, frac.denominator * 2)
        valBot = Fraction(bottom * bottom * frac.numerator, frac.denominator * 2)
        answer = "$" + fraction.Subtract(valTop, valBot).ToStringAns() + "$"
    else:
        rand2 = random.randint(0, 1)
        strfx = ""
        if rand2 == 0:
            strfx = "\\sin x"
        elif rand2 == 1:
            strfx = "\\cos x"
        question = "$\\int_0^\\pi" + strfx + "\\ dx =$"
        if rand2 == 0:
            answer = "$-2$"
        elif rand2 == 1:
            answer = "$0$"
    return [question, answer, end]

def Days(probNum):
    question, answer, sEnd = '', '', ''
    d = day.randomDay()
    delta = random.randint(8, 69)
    end = day.nextDay(d, delta)
    
    if random.randint(0, 1):
        question = 'How many days are there from ' + str(d) + ' to ' + str(end) + '?'
        answer = '$' + str(delta) + '$'
    else:
        question = 'If today is ' + str(d) + ' then ' + str(delta) + ' days from now will be ' + Day.months[end.month]
        sEnd = ', ' + str(end.year)
        answer = '$' + str(end.year) + '$'
    return [question, answer, end]

def DecimalToFraction(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 4)
    if rand < 4:
        size = random.randint(1, 4)
        den = 10**size
        num = random.randint(0, den-1)
        while utility.GCD(num, den) == 1:
            num = random.randint(0, den-1)
        f = Fraction(num, den)
        dec = str(num)
        while len(dec) < size:
            dec = '0' + dec
        while dec[len(dec)-1] == '0':
            dec = dec[0:len(dec)-1]
        question = '$.' + dec + ' =$'
        end = '(fraction)'
        answer = '$' + str(f) + '$'
    else:
        while True:
            den = utility.rationalDen()
            num = random.randint(1, den-1)
            f = Fraction(num, den)
            den2 = den
            while not utility.isPowerOf10(den2):
                den2+=den
            num2 = num * den2 / den
            dec = str(num2)
            while len(dec) < (len(str(den2)) - 1):
                dec = '0' + dec
            if dec[len(dec)-1] == '0':
                return DecimalToFraction(probNum)
            if not (random.random() < .6**len(dec)):
                break
        question = '$.' + dec + ' =$'
        end = '(fraction)'
        answer = '$' + str(f) + '$'
    return [question, answer, end]

def DecimalToPercent(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 2) == 0:
        den = utility.rationalDen()
        m = MixedNumber(random.randint(0, 4), random.randint(1, den-1), den)
        question = '$' + str((m.co + m.f.DecValue()) / 100.0) + ' =$'
        end = '$\\%$'
        answer = '$' + str(m) + '$'
    else:
        den = utility.rationalDen()
        m = MixedNumber(random.randint(0, 119), random.randint(1, den-1), den)
        question = '$' + str((m.co + m.f.DecValue()) / 100.0) + ' =$'
        end = '$\\%$'
        answer = '$' + str(m) + '$'
    return [question, answer, end]

def Determinant(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 2)
    if rand == 0:
        if random.randint(0, 1):
            num = random.randint(5, 39)
            num2 = utility.nextIntLess(num-1, 1, 0.3)
            if random.randint(0, 1):
                temp = num
                num = num2
                num2 = temp
            question = '$\\left| \\begin{array}{cc}' + \
                       str(num) + ' & ' + str(num2) + '\\\\' + \
                       str(num2) + ' & ' + str(num) + '\\end{array} \\right| =$'
            answer = '$' + str(num**2 - num2**2) + '$'
        else:
            num = random.randint(-20, 19)
            num2 = random.randint(-20, 19)
            num3 = random.randint(-20, 19)
            num4 = random.randint(-20, 19)
            question = '$\\left| \\begin{array}{cc}' + \
                       str(num) + ' & ' + str(num2) + '\\\\' + \
                       str(num3) + ' & ' + str(num4) + '\\end{array} \\right| =$'
            answer = '$' + str(num*num4 - num3*num2) + '$'
    else:
        while True:
            a, x = random.randint(-10, 9), random.randint(-10, 9)
            while x == 0:
                x = random.randint(-10, 9)
            ans = random.randint(-30, 29)
            firstNumTotal = ans + a*x
            if firstNumTotal != 0:
                break
        factors = utility.Factors(firstNumTotal)
        num1 = factors[random.randint(0, len(factors)-1)]
        num2 = firstNumTotal / num1
        if num1 < 0:
            num2 = -num2
        ans = num1*num2 - a*x
        if random.randint(0, 1):
            ans *= -1
            isUp = random.randint(0, 1) == 0
            question = '$\\left| \\begin{array}{cc}' + \
                       ('a' if isUp else str(x)) + ' & ' + str(num1) + '\\\\' + \
                       str(num2) + ' & ' + (str(x) if isUp else 'a') + '\\end{array} \\right| = ' + str(ans) + '$. Find $a$'
            answer = '$' + str(a) + '$'
        else:
            isUp = random.randint(0, 1) == 0
            question = '$\\left| \\begin{array}{cc}' + \
                       str(num1) + ' & ' + ('a' if isUp else str(x)) + '\\\\' + \
                       (str(x) if isUp else 'a') + ' & ' + str(num2) + '\\end{array} \\right| =' + str(ans) + '$. Find $a$'
            answer = '$' + str(a) + '$'
    return [question, answer, end]

def DividingIntoLengthsOrRatio(probNum):
    question, answer, end = '', '', ''
    noNums = random.randint(2, 3)
    if noNums == 2:
        if random.randint(0, 1):
            num = random.randint(30, 149)
            num1 = random.randint(1, num-1)
            num2 = num - num1
            findLarger = random.randint(0, 1) == 0
            question = 'Divide $' + str(num) + '$ into two parts such that ' + \
                       'the larger number exceeds the smaller number by $' + \
                       str(abs(num2-num1)) + '$. Find the ' + ('larger' if findLarger else 'smaller') + ' number.'
            answer = '$' + str((num2 if num2>num1 else num1) if findLarger else (num2 if num2<num1 else num1)) + '$'
        else:
            num = random.randint(20, 119)
            while utility.isPrime[num]:
                num = random.randint(20, 119)
            factors = utility.Factors(num)
            num1 = factors[random.randint(1, len(factors)-2)]
            ratio1 = random.randint(1, num1-1)
            ratio2 = num1 - ratio1
            while ratio1 == ratio2:
                if random.randint(0, 19)==0:
                    return DividingIntoLengthsOrRatio(probNum)
                ratio1 = random.randint(1, num1-1)
                ratio2 = num1 - ratio1
            f = Fraction(ratio1, ratio2)
            findLarger = random.randint(0, 1) == 0
            question = "Two numbers are in the ratio $" + str(f.numerator) + "$:$" + str(f.denominator) + "$. If their sum is $" + str(num) + "$, find the " + ("larger" if findLarger else "smaller") + " number."
            mult = num/num1
            answer = "$" + str((mult * (f.numerator if f.numerator>f.denominator else f.denominator)) if findLarger else  (mult * (f.numerator if f.numerator<f.denominator else f.denominator))) + "$"
    elif noNums == 3:
        num = random.randint(20, 119)
        while utility.isPrime[num]:
            num = random.randint(20, 119)
        factors = utility.Factors(num)
        num1 = factors[random.randint(1, len(factors)-2)]
        while num1 < 3:
            num1 = factors[random.randint(1, len(factors)-2)]
        ratios = [0] * 3
        ratios[0] = random.randint(1, num1-2)
        ratios[1] = random.randint(1, num1-ratios[0])
        ratios[2] = num - (ratios[0] + ratios[1])
        while ratios[1] == ratios[2] and ratios[2] == ratios[0]:
            if random.randint(0, 19) == 0:
                return DividingIntoLengthsOrRatio(probNum)
            ratios[0] = random.randint(1, num1-2)
            ratios[1] = random.randint(1, num1-ratios[0])
            ratios[2] = num - (ratios[0] + ratios[1])
        ratios.sort()
        findLargest = random.randint(0, 1) == 0
        question = "Divide $" + str(num) + "$ into $3$ parts such that the ratio of the $3$ numbers is $" + str(ratios[0]) + "$:$" + str(ratios[1]) + "$:$" + str(ratios[2]) + "$. Find the " + ("largest" if findLargest else "smallest") + " number."
        mult = num / (ratios[0] + ratios[1] + ratios[2])
        answer = "$" + str((mult * ratios[2]) if findLargest else (mult * ratios[0])) + "$"
    return [question, answer, end]

def DivisionOrFractionToMixedNumber(probNum):
    question, answer, end = '', '', ''
    smallNum = random.randint(2, 9)
    bigNum = utility.nextIntGreater(100, 6000, 1 - 0.95923)
    question = '$' + str(bigNum) + ' / ' + str(smallNum) + ' =$'
    end = '(mixed number)'
    m = MixedNumber(bigNum / smallNum, bigNum % smallNum, smallNum)
    if m.f.numerator == 0 or m.f.numerator == m.f.denominator:
        return DivisionOrFractionToMixedNumber(probNum)
    answer = '$' + str(m) + '$'
    return [question, answer, end]

def Factorials(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 4) < 3:
        den = random.randint(5, 11)
        plus = random.randint(0, 2) == 0
        if plus:
            num1, num2 = den+1, den-1
            question = '$\\displaystyle\\frac{' + str(num1) + '! + ' + str(num2) + '!}{' + str(den) + '!} = $'
            f = fraction.Add(Fraction(num1, 1), Fraction(1, den))
            ans = f.ToMixedNumber()
            answer = '$' + ans.ToFraction().ToStringAns() + '$'
        else:
            num1, num2 = den+1, den-1
            question = '$\\displaystyle\\frac{' + str(num1) + '! - ' + str(num2) + '!}{' + str(den) + '!} = $'
            f = fraction.Subtract(Fraction(num1, 1), Fraction(1, den))
            ans = f.ToMixedNumber()
            answer = '$' + ans.ToFraction().ToStringAns() + '$'
    else:
        den = random.randint(3, 9)
        num = den + random.randint(1, 3)
        ans = 1
        for i in range(den+1, num+1):
            ans *= i
        question = '$\\displaystyle\\frac{' + str(num) + '!}{' + str(den) + '!} = $'
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def MultiplicationAround100or1000(probNum):
    question, answer, end = '', '', ''
    num1, num2 = 0, 0
    if random.randint(0, 5) == 0:
        rand = random.randint(0, 4)
        if rand == 0:
            while True:
                num1, num2 = random.randint(985, 1015), random.randint(985, 1015)
                while (abs(1000-num1) > 10 and random.randint(0, 2) < 2) or num1==1000:
                    num1 = random.randint(985, 1015)
                while (abs(1000-num2) > 10 and random.randint(0, 2) < 2) or num2==1000:
                    num2 = random.randint(985, 1015)
                if not ((num1<1000 and num2<1000) or (num2 > 1000 and num1 > 1000)):
                    break
        elif rand < 3:
            num1, num2 = random.randint(985, 999), random.randint(985, 999)
        elif rand < 5:
            num1, num2 = random.randint(1001, 1014), random.randint(1001, 1014)
    else:
        rand = random.randint(0, 4)
        if rand == 0:
            while True:
                num1, num2 = random.randint(85, 115), random.randint(85, 115)
                while (abs(100 - num1) > 10 and random.randint(0, 2) <  2) or num1 == 100:
                    num1 = random.randint(85, 115)
                while (abs(100 - num2) > 10 and random.randint(0, 2) <  2) or num2 == 100:
                    num2 = random.randint(85, 115)
                if not ((num1 < 100 and num2 < 100) or (num2 > 100 and num1 > 100)):
                    break
        elif rand < 3:
            num1, num2 = random.randint(85, 99), random.randint(85, 99)
        elif rand < 5:
            num1, num2 = random.randint(101, 114), random.randint(101, 114)
    question = '$' + str(num1) + ' \\times ' + str(num2) + ' = $'
    answer = '$' + str(num1*num2) + '$'
    return [question, answer, end]

def MaximumProduct(probNum):
    question, answer, end = '', '', ''
    num = random.randint(5, 29)
    if random.randint(0, 1):
        question = 'Find the maximum product of $x$ and $y$ if $x + y = ' + str(num) + ', x, y > 0$.'
    else:
        question = 'Find the maximum product of $x$ and $y$ if $' + str(num) + ' = x + y, x, y > 0$.'
    if num % 2 == 0:
        answer = '$' + str((num/2)**2) + '$'
    else:
        answer = '$' + str((float(num)/2)**2) + '$'      
    return [question, answer, end]

def HowManyRegionsOrLines(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 9) == 0:
        num = random.randint(4, 12)
        question = 'How many lines in a plane are determined by $' + str(num) + '$ points, no $3$ of which are collinear?'
        answer = '$' + str(utility.triangular(num-1)) + '$'
    else:
        num = random.randint(4, 19)
        if random.randint(0, 2) == 0:
            question = 'How many regions in a plane are determined by $' + str(num) + '$ lines, no $2$ are parallel and only $3$ lines are concurrent?'
            answer = '$' + str(utility.triangular(num)) + '$'
        else:
            question = 'How many regions in a plane are determined by $' + str(num) + '$ lines, no $2$ are parallel and no $3$ lines are concurrent?'
            answer = '$' + str(utility.triangular(num) + 1) + '$'
    return [question, answer, end]

def CostRatios(probNum):
    question, answer, end = '', '', ''
    obj = utility.nouns[random.randint(0, len(utility.nouns)-1)]
    num1 = random.randint(2, 14)
    cost = num1* random.randint(15, 299)
    costPer = cost / num1
    sCost = '\\$' + utility.DoubleToAns(float(cost) / 100.0)
    if sCost.find('.') == -1:
        sCost += '.'
    num2 = random.randint(2, 14)
    while num1 == num2:
        num2 = random.randint(2, 14)
    while len(sCost[sCost.find('.') + 1:]) < 2:
        sCost = sCost + '0'
    question = 'If $' + str(num1) + '$ ' + obj + ' cost $' + sCost + '$, then $' + str(num2) + '$ ' + obj + ' cost \\$'
    totCost = costPer * num2
    cost2 = utility.DoubleToAns(float(totCost) / 100.0)
    if cost2.find('.') == -1:
        cost2 += '.'
    while len(cost2[cost2.find('.') + 1:]) < 2:
        cost2 = cost2 + '0'
    answer = '$' + cost2 + '$'
    return [question, answer, end]

def MeanMedianModeRangeAverage(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 14)
    if rand < 6: # mean and average
        type = 'mean' if random.randint(0, 1) else 'average'
        if random.randint(0, 1):
            nums = [0] * random.randint(5, 8)
            while True:
                center = random.randint(3, 7)
                sum = 0
                for i in range(len(nums)):
                    if random.randint(0, 1): nums[i] = utility.nextIntLess(center, 1, .35)
                    else: nums[i] = utility.nextIntGreater(center, 9, .35)
                snums = ''
                for i in range(len(nums)):
                    sum += nums[i]
                    if i != 0: snums += '$,$ '
                    snums += str(nums[i])
                question = 'The ' + type + ' of $' + snums + '$ is'
                answer = '$' + Fraction(sum, len(nums)).ToStringAns() + '$'
                if not (sum % len(nums) != 0 and random.random() < .8):
                    break
        else:
            nums = [0] * random.randint(3, 6)
            while True:
                sum = 0
                for i in range(len(nums)):
                    nums[i] = random.randint(10, 79)
                snums = ''
                for i in range(len(nums)):
                    sum += nums[i]
                    if i != 0: snums += '$,$ '  
                    snums += str(nums[i])
                question = 'The ' + type + ' of $' + snums + '$ is'
                answer = '$' + Fraction(sum, len(nums)).ToStringAns() + '$'
                if not (sum % len(nums) != 0 and random.random() < .7):
                    break
    elif rand < 11: #median
        type = 'median'
        if random.randint(0, 1):
            nums = [0] * random.randint(5, 8)
            center = random.randint(3, 7)
            for i in range(len(nums)):
                if random.randint(0, 1): nums[i] = utility.nextIntLess(center, 1, .35)
                else: nums[i] = utility.nextIntGreater(center, 9, .35)
            snums = ''
            for i in range(len(nums)):
                if i != 0: snums += '$,$ '
                snums += str(nums[i])
            nums.sort()
            if len(nums) % 2 == 0:
                ans = Fraction(nums[len(nums)/2] + nums[len(nums)/2 - 1], 2)
            else:
                ans = Fraction(nums[len(nums)/2], 1)
            question = 'The ' + type + ' of $' + snums + '$ is'
            answer = '$' + ans.ToStringAns() + '$'
        else:
            nums = [0] * random.randint(4, 7)
            for i in range(len(nums)):
                nums[i] = random.randint(10, 119)
            snums = ''
            for i in range(len(nums)):
                if i != 0: snums += '$,$ '
                snums += str(nums[i])
            nums.sort()
            if len(nums) % 2 == 0:
                ans = Fraction(nums[len(nums) / 2] + nums[len(nums) / 2 - 1], 2)
            else:
                ans = Fraction(nums[len(nums) / 2], 1)
            question = 'The ' + type + ' of $' + snums + '$ is'
            answer = '$' + ans.ToStringAns() + '$'
    elif rand < 13:
        type = 'mode'
        while True:
            nums = [0] * random.randint(5, 8)
            center = random.randint(3, 7)
            for i in range(len(nums)):
                if random.randint(0, 1): nums[i] = utility.nextIntLess(center, 1, .35)
                else: nums[i] = utility.nextIntGreater(center, 9, .35)
            snums = ''
            for i in range(len(nums)):
                if i != 0:
                    snums += '$,$ '
                snums += str(nums[i])
            count = [0] * 10
            for i in range(len(nums)):
                count[nums[i]]+=1
            most = mosti = -1
            for i in range(len(count)):
                if count[i] > most:
                    most = count[i]
                    mosti = i
            flag = False
            for i in range(len(count)):
                if count[i] == most and i != mosti:
                    flag = True
            if flag: continue
            cc = 0
            for i in range(len(nums)):
                if nums[i] == mosti: cc+=1
            if cc > len(nums) / 2: continue
            question = 'The ' + type + ' of $' + snums + '$ is'
            answer = '$' + str(mosti) + '$'
            break
    else:
        nums = [0] * random.randint(3, 7)
        for i in range(len(nums)):
            nums[i] = random.randint(10, 119)
        snums = ''
        for i in range(len(nums)):
            if i != 0: snums += '$,$ '
            snums += str(nums[i])
        nums.sort()
        type = 'range'
        ans = nums[-1] - nums[0]
        question = 'The ' + type + ' of $' + snums + '$ is'
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def Derivative(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 12)
    if rand < 9:
        cos = [0] * 3
        pows = [0] * 3
        usedPows = [False] * 6
        for i in range(len(cos)):
            cos[i] = random.randint(-6, 6)
            while cos[i] == 0:
                cos[i] = random.randint(-6, 6)
        for i in range(len(pows)):
            pows[i] = random.randint(0, 4)
            while usedPows[pows[i]]:
                pows[i] = random.randint(0, 4)
            usedPows[pows[i]] = True
        function = ''
        for i in range(len(pows)):
            if i != 0:
                function += ' - ' if cos[i] < 0 else ' + '
                if abs(cos[i]) and pows[i] == 0: 
                    function += str(abs(cos[i]))
                else: 
                    function += ('' if abs(cos[i]) == 1 else str(abs(cos[i]))) + \
                                ('' if pows[i] == 0 else ('x' + ('' if pows[i] == 1 else ('^' + str(pows[i])))))
            else:
                if pows[i] == 0: function += str(cos[i])
                else:
                    if cos[i] == -1: function += '-'
                    elif cos[i] != 1: function += str(cos[i])
                    function += 'x' + ('' if pows[i] == 1 else ('^' + str(pows[i])))
        num = random.randint(-5, 5)
        while num == 0:
            num = random.randint(-5, 5)
        question = 'If $f(x) = ' + function + "$ then $f^{'}(" + str(num) + ') =$'
        
        cos2 = [0] * 3
        pows2 = [0] * 3
        
        for i in range(len(cos2)):
            cos2[i] = cos[i] * pows[i]
            pows2[i] = pows[i] - 1
        
        tot = 0
        for i in range(len(cos2)):
            tot += cos2[i] * (num**pows2[i])
        answer = '$' + str(tot) + '$'
    elif rand < 10:
        cos = [0] * 3
        pows = [0] * 3
        usedPows = [False] * 6
        for i in range(len(cos)):
            cos[i] = random.randint(-6, 6)
            while cos[i] == 0: cos[i] = random.randint(-6, 6)
        for i in range(len(pows)):
            pows[i] = random.randint(0, 4)
            while usedPows[pows[i]]:
                pows[i] = random.randint(0, 5)
            usedPows[pows[i]] = True
        function = ''
        for i in range(len(pows)):
            if i != 0: function += ' - ' if cos[i] < 0 else ' + '
            if abs(cos[i]) == 1 and pows[i] == 0:
                function += str(abs(cos[i]))
            else:
                function += ('' if abs(cos[i]) == 1 else str(abs(cos[i]))) + \
                            ('' if pows[i] == 0 else ('x' + ('' if pows[i] == 1 else ('^' + str(pows[i])))))
        num = random.randint(-5, 5)
        while num == 0:
            num = random.randint(-5, 5)
        question = 'If $f(x) = ' + function + "$ then $f^{''}(" + str(num) + ') =$'
        
        cos2 = [0] * 3
        pows2 = [0] * 3
        
        for i in range(len(cos2)):
            cos2[i] = cos[i] * pows[i]
            pows2[i] = pows[i] - 1
        
        cos3 = [0] * 3
        pows3 = [0] * 3
        
        for i in range(len(cos3)):
            cos3[i] = cos2[i] * pows2[i]
            pows3[i] = pows2[i] - 1
        
        tot = 0
        for i in range(len(cos3)):
            tot += cos3[i] * (num**pows3[i])
        answer = '$' + str(tot) + '$'
    
    elif rand < 11:
        primeConst = random.randint(1, 8)
        cconst = random.randint(1, 8)
        firstToEval = random.randint(-4, 8)
        numToEval = random.randint(-4, 8)
        while firstToEval == numToEval:
            numToEval = random.randint(-4, 8)
        question = "If $f^{'}(x) = " + str(primeConst) + '$ and $f(' + str(firstToEval) + ') = ' + str(cconst) + '$ then $f(' + str(numToEval) + ') =$'
        c = cconst - primeConst * firstToEval
        ans = numToEval * primeConst + c
        answer = '$' + str(ans) + '$'
    else:
        if random.randint(0, 1):
            c = random.randint(2, 6)
            numDeg = (30 * random.randint(0, 6)) if random.randint(0, 1) else (45 * random.randint(0, 3))
            question = '$f(x) = \\sin' + str(c) + "x$, $f^{'}(" + str(numDeg) + '^\\circ) = $'
            numDeg2 = c * numDeg
            cosine = trig.cos(numDeg2)
            cosine.co.numerator *= c
            answer = '$' + str(cosine) + '$'
        else:
            c = random.randint(2, 6)
            numDeg = (30 * random.randint(0, 6)) if random.randint(0, 1) else (45 * random.randint(0, 3))
            question = '$f(x) = \\cos' + str(c) + "x$, $f^{'}(" + str(numDeg) + '^\\circ) = $'
            numDeg2 = c * numDeg
            sine = trig.sin(numDeg2)
            sine.co.numerator *= -c
            answer = '$' + str(sine) + '$'
    return [question, answer, end]

def IsTo(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 3)
    a = random.randint(3, 17)
    b = random.randint(3, 17)
    c = random.randint(3, 17)
    d = random.randint(3, 17)
    if rand == 0:
        a = Fraction(b*c, d)
        if str(a) == str(b) or str(a) == str(c):
            return IsTo(probNum)
        question = ''
        end = 'is to $' + str(b) + '$ as $' + str(c) + '$ is to $' + str(d) + '$'
        answer = '$' + str(a) + '$'
    if rand == 1:
        b = Fraction(a*d, c)
        if str(a) == str(b) or str(a) == str(c):
            return IsTo(probNum)
        question = '$' + str(a) + '$ is to'
        end = 'as $' + str(c) + '$ is to $' + str(d) + '$'
        answer = '$' + str(b) + '$'
    if rand == 2:
        c = Fraction(a*d, b)
        if str(a) == str(b) or str(a) == str(c):
            return IsTo(probNum)
        question = '$' + str(a) + '$ is to $' + str(b) + '$ as'
        end = 'is to $' + str(d) + '$'
        answer = '$' + str(c) + '$'
    if rand == 2:
        c = Fraction(a*d, b)
        if str(a) == str(b) or str(a) == str(c):
            return IsTo(probNum)
        question = '$' + str(a) + '$ is to $' + str(b) + '$ as'
        end = 'is to $' + str(d) + '$'
        answer = '$' + str(c) + '$'
    if rand == 3:
        a = random.randint(3, 17)
        b = random.randint(3, 17)
        c = random.randint(3, 17)
        d = Fraction(b*c, a)
        if str(a) == str(b) or str(a) == str(c):
            return IsTo(probNum)
        question = '$' + str(a) + '$ is to $' + str(b) + '$ as $' + str(c) + '$ is to'
        answer = '$' + str(d) + '$'
    return [question, answer, end]

def ModulusImaginary(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 2) < 2:
        a = random.randint(1, 7) * 2 + 1
        b = a*a/2
        c = b+1
        m = 1
        while random.randint(0, 4) == 0:
            if a * m < 15:
                m = random.randint(2, 3)
        a *= m
        b *= m
        c *= m
        if random.randint(0, 1):
            temp = a
            a = b
            b = temp
        if random.randint(0, 1):
            question = 'The modulus of $(' + str(a) + ' + ' + str(b) + 'i)^2$ is'
            answer = '$' + str(c**2) + '$'
        else:
            question = 'The modulus of $(' + str(a) + ' + ' + str(b) + 'i)^2$ is'
            answer = '$' + str(c) + '$'
    else:
        a, b = random.randint(3, 13), random.randint(3, 14)
        question = 'The modulus of $(' + str(a) + ' + ' + str(b) + 'i)^2$ is'
        answer = '$' + str(a**2 + b**2) + '$'
    return [question, answer, end]

def Modulo(probNum):
    question, answer, end = '', '', ''
    lin = Linear(random.randint(1, 6), random.randint(-8, 7))
    mod = random.randint(4, 8)
    cons = random.randint(-10, 29)
    mod2 = (cons - lin.B) % mod
    while mod2 < 0:
        mod2 += mod
    ans = 0
    while (lin.A * ans) % mod != mod2:
        if ans > 10: return Modulo(probNum)
        ans += 1
    lowBound, highBound = 0, random.randint(ans, ans + mod - 1)
    for i in range(lowBound, highBound + 1):
        mod3 = cons % mod
        while mod3 < 0: 
            mod3 += mod
        acMod = lin.Evaluate(i) % mod
        while acMod < 0:
            acMod += mod
        if acMod == mod3 and i != ans:
            return Modulo(probNum)
    if random.randint(0, 1):
        question = 'Find $x$, $' + str(lowBound) + ' <= x <= ' + str(highBound) + \
                   '$, if $' + str(lin) + ' = ' + str(cons) + '$ mod $' + str(mod) + '$'
    else:
        question = 'If $' + str(lin) + ' = ' + str(cons) + '$ mod $' + str(mod) + '$, $' + str(lowBound) + ' <= x <= ' + str(highBound) + '$, find $x$'
    answer = '$' + str(ans) + '$'
    return [question, answer, end]

def DivisionOrFractionToDecimal(probNum):
    question, answer, end = '', '', ''
    rand3 = random.randint(0, 18)
    rand = 4
    if rand3 < 7: rand = 0
    elif rand3 < 11: rand = 1
    elif rand3 < 13: rand = 2
    elif rand3 < 16: rand = 3
    else: rand = 4 
    
    if rand == 0:
        num = random.randint(3, 12) if random.randint(0, 1) else random.randint(50, 349)
        den = 0
        den = utility.rationalDen()
        if random.randint(0, 1):
            den *= 2
        if random.randint(0, 1):
            den *= 5
        if num == den:
            return DivisionOrFractionToDecimal(probNum)
        f = Fraction(num, den)
        if f.denominator == 1:
            return DivisionOrFractionToDecimal(probNum)
        question = '$' + str(f) + ' =$'
        end = '(decimal)'
        answer = '$' + utility.DoubleToAns(float(num) / den) + '$'
    elif rand == 1:
        den1 = utility.rationalDen()
        den2 = (den1 * random.randint(1, 4)) if random.randint(0, 1) else utility.rationalDen()
        num1, num2 = random.randint(1, den1-1), random.randint(1, den2-1)
        if random.randint(0, 1):
            temp = num1
            num1 = num2
            num2 = temp
            
            temp = den1
            den1 = den2
            den2 = temp
        rand2 = random.randint(0, 3)
        f1 = Fraction(num1, den1)
        f2 = Fraction(num2, den2)
        if rand2 == 0:
            question = '$' + str(f1) + ' + ' + str(f2) + ' =$'
            if len(str(fraction.Add(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(fraction.Add(f1,f2).DecValue()) + '$'
        elif rand2 == 1:
            question = '$' + str(f1) + ' - ' + str(f2) + ' =$'
            if len(str(fraction.Subtract(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(fraction.Subtract(f1, f2).DecValue()) + '$'
        elif rand2 == 2:
            question = '$' + str(f1) + ' \\div ' + str(f2) + ' =$'
            if len(str(fraction.Divide(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(fraction.Divide(f1, f2).DecValue()) + '$'
        elif rand2 == 3:
            question = '$' + str(f1) + ' \\times ' + str(f2) + ' =$'
            if len(str(fraction.Multiply(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(fraction.Multiply(f1, f2).DecValue()) + '$'
        end = '(decimal)'
    elif rand == 2:
        co = utility.nextIntGreater(1, 1000, 0.01)
        den = utility.rationalDen()
        num = random.randint(1, den-1)
        while utility.GCD(num, den) != 1:
            num = random.randint(1, den-1)
        percent = random.randint(0, 1) == 0
        mn = MixedNumber(co, num, den)
        if num == den:
            return DivisionOrFractionToDecimal(probNum)
        if percent:
            question = '$' + str(mn) + '\\% =$'
            answer = '$' + utility.DoubleToAns(float(co*den + num) / (den*100)) + '$'
        else:
            question = '$' + str(mn) + ' =$'
            answer = '$' + utility.DoubleToAns(float(co*den + num) / den) + '$'
        end = '(decimal)'
    elif rand == 3:
        co1 = utility.nextIntGreater(0, 5, 0.2)
        co2 = utility.nextIntGreater(0, 5, 0.2)
        den1, den2 = utility.rationalDen(), utility.rationalDen()
        num1, num2 = random.randint(1, den1-1), random.randint(1, den2-1)
        while utility.GCD(num1, den1) != 1:
            num1 = random.randint(1, den1-1)
        while utility.GCD(num2, den2) != 1:
            num2 = random.randint(1, den2-1)
        f1 = MixedNumber(co1, num1, den1)
        f2 = MixedNumber(co2, num2, den2)
        rand2 = random.randint(0, 3)
        if rand2 == 0:
            question = '$' + str(f1) + ' + ' + str(f2) + ' =$'
            if len(str(mixedNumber.Add(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(mixedNumber.Add(f1,f2).DecValue()) + '$'
        elif rand2 == 1:
            question = '$' + str(f1) + ' - ' + str(f2) + ' =$'
            if len(str(mixedNumber.Subtract(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(mixedNumber.Subtract(f1, f2).DecValue()) + '$'
        elif rand2 == 2:
            question = '$' + str(f1) + ' \\div ' + str(f2) + ' =$'
            if len(str(mixedNumber.Divide(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(mixedNumber.Divide(f1, f2).DecValue()) + '$'
        elif rand2 == 3:
            question = '$' + str(f1) + ' \\times ' + str(f2) + ' =$'
            if len(str(mixedNumber.Multiply(f1, f2).DecValue())) > 6:
                return DivisionOrFractionToDecimal(probNum)
            answer = '$' + utility.DoubleToAns(mixedNumber.Multiply(f1, f2).DecValue()) + '$'
        end = '(decimal)'
    if rand == 4:
        den = random.randint(6, 19)
        num = 0
        if random.randint(0, 2) == 0:
            num = den * random.randint(11, 399)
        else:
            num = den * 100 * random.randint(2, 6) + den * random.randint(2, 6)
        dden = utility.Decimalize(den)
        dnum = utility.Decimalize(num)
        question = '$ \\displaystyle\\frac{' + str(dnum) + '}{' + str(dden) + '} =$'
        end = '(decimal)'
        answer = '$' + utility.DoubleToAns(dnum / dden) + '$'
    
    if answer.find('.') == -1:
        end = ''
    return [question, answer, end]

def ExpressionsInvolvingRepeatingDecimals(probNum):
    question, answer, end = '', '', ''
    numDig = random.randint(1, 2)
    if numDig == 2: den = 99
    else: den = 9
    num = random.randint(1, den-1)
    while random.randint(0, 4) < 4 and den % num != 0:
        num = random.randint(1, den)
    rep = str(num)
    while len(rep) < numDig:
        rep = '0' + rep
    repdec = '.' + rep + rep + rep + '...'
    f = Fraction(num, den)
    if random.randint(0, 1):
        cons = f.denominator * random.randint(1, 9)
        scons = str(cons)
        if random.randint(0, 1):
            temp = scons
            scons = repdec
            repdec = temp
        question = '$' + str(repdec) + ' \\times ' + str(scons) + ' = $'
        if random.randint(0, 1):
            question = '$' + str(repdec) + ' \\times ' + scons + ' = $'
        answer = '$' + str(Fraction(f.numerator * cons, f.denominator)) + '$'
    else:
        cons = f.numerator * random.randint(1, 9)
        scons = str(cons)
        if random.randint(0, 1):
            temp = scons
            scons = repdec
            repdec = temp
        question = '$' + str(scons) + ' \\div ' + str(repdec) + ' = $'
        answer = '$' + str(Fraction(f.numerator * cons, f.denominator)) + '$'
    return [question, answer, end]

def FindTheTerm(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 29)
    quest = [0] * 5
    ans = 0
    dif = False
    
    if rand < 7:
        if random.randint(0, 1):
            for i in range(1, 6):
                quest[i-1] = i**2
            ans *= 6**2
        else:
            for i in range(1, 6):
                quest[i-1] = i**3
            ans = 6**3
        if random.randint(0, 2) == 0:
            dif = True
        if random.randint(0, 4) < 3:
            cons = random.randint(-3, 3)
            for i in range(5):
                quest[i] += cons
            ans += cons
    
    elif rand < 18:
        diff = random.randint(-8, -2) if random.randint(0, 3) == 0 else random.randint(3, 11)
        start = random.randint(10, 49) if diff < 0 else random.randint(-5, 9)
        quest[0] = start
        for i in range(1, 5):
            quest[i] = quest[i-1] + dif
        ans = quest[i] = quest[i-1] + dif
        if diff > 0 and random.randint(0, 2) < 2 and (start > 0 or random.randint(0, 1)):
            dif = True
        elif (not dif) and random.randint(0, 3) < 3:
            terms = '$'
            for i in range(len(quest)-1):
                terms += str(quest[i]) + ', '
            terms += str(quest[-1]) + '$'
            nth = random.randint(2, 12) * 10
            question = 'The $' + str(nth) + 'th$ term of ' + terms + ' is '
            answer = '$' + str((diff * nth) - (diff - start)) + '$'
    
    elif rand < 20:
        ibase = 2 if random.randint(0, 1) else 3
        for i in range(5):
            quest[i] = ibase**(i+1)
        ans = ibase**6
        if random.randint(0, 4) < 4:
            cons = random.randint(-5, 5)
            for i in range(5):
                quest[i] += cons
            ans += cons
        if random.randint(0, 1):
            dif = True
    
    elif rand < 23:
        quest[0] = random.randint(-2, 4)
        quest[1] = random.randint(-2, 4)
        if quest[0] == 0 or quest[1] == 0:
            quest[0] = random.randint(-2, 4)
            quest[1] = random.randint(-2, 4)
        for i in range(2, 5):
            quest[i] = quest[i-1] + quest[i-2]
        ans = quest[-2] + quest[-1]
    
    elif rand < 25:
        quest[0] = 1
        for i in range(1, 5):
            quest[i] = quest[i-1] * (i+1)
        ans = quest[-1] * 6
        cons = random.randint(-5, 5)
        for i in range(5):
            quest[i] += cons
        ans += cons
    
    elif rand < 30:
        ibase = random.randint(1, 5)
        mult = random.randint(2, 3)
        quest[0] = ibase
        for i in range(1, 5):
            quest[i] = quest[i-1] * mult
        ans = quest[-1] * mult
    
    if dif:
        first = random.randint(-3, 4) if random.randint(0, 1) else random.randint(0, 8)
        temp = list(quest)
        quest[0] = first
        for i in range(1, 5):
            quest[i] = quest[i-1] + temp[i-1]
        ans = quest[-1] + temp[-1]
    
    sterms = '$'
    for i in range(len(quest)-1):
        sterms += str(quest[i]) + ', '
    sterms += str(quest[-1]) + '$'
    if question == '':
        question = 'The next terms of ' + sterms + ' is '
        answer = '$' + str(ans) + '$'
    return [question, answer, end]
    
def FiniteSequences(probNum):
    question, answer, end = '', '', ''
    if (probNum < 40 and random.randint(0, 4) < 4) or (probNum >= 40 and random.randint(0, 4) == 0):
        diff = 0
        rand = random.randint(0, 2)
        if rand == 0: diff = 1
        elif rand == 1: diff = 2
        else: diff = random.randint(1, 9)
        start = diff if random.randint(0, 1) else random.randint(-3, 9)
        numTerms = random.randint(10, 29)
        question = '$' + str(start) + ' + ' + str(start+diff) + ' + ' + str(start + 2*diff) + \
                   ' + ... + ' + str(start + diff * (numTerms - 2)) + ' + ' + \
                   str(start + diff * (numTerms - 1)) + ' = $'
        answer = '$' + str(numTerms * (start + start + diff * (numTerms - 1)) / 2) + '$'
    
    else:
        rand = random.randint(0, 4)
        if rand == 0:
            numTerms = random.randint(7, 20)
            if random.randint(0, 1):
                question = '$1^2 + 2^2 + 3^2 + ... + ' + str(numTerms - 1) + '^2 + ' + str(numTerms) + '^2 = $'
            else:
                question = '$1 + 4 + 9 + ... + ' + str((numTerms-1)**2) + ' + ' + str(numTerms**2) + ' = $'
            answer = '$' + str(numTerms * (numTerms + 1) * (2 * numTerms + 1) / 6) + '$'
        elif rand == 1:
            numTerms = random.randint(5, 15)
            if random.randint(0, 1):
                question = '$1^3 + 2^3 + 3^3 + ... + ' + str(numTerms - 1) + '^3 + ' + str(numTerms) + '^3 = $'
            else:
                question = '$1 + 8 + 27 + ... + ' + str((numTerms-1)**3) + ' + ' + str(numTerms**3) + ' = $'
            answer = '$' + str((numTerms*(numTerms + 1) / 2) ** 2) + '$'
        elif rand == 2:
            b = random.randint(2, 4)
            maxPow = random.randint(5, 10)
            while b**maxPow > 1100:
                maxPow = random.randint(5, 10)
            if b == 2:
                question = '$1 + ' + str(b) + ' + ' + str(b) + '^2 + ' + str(b) + \
                           '^3 + ... + ' + str(b) + '^' + str(maxPow - 1) + ' + ' + str(b) + '^' + str(maxPow) + ' = $'
                answer = '$' + str(b**(maxPow+1) - 1) + '$'
            else:
                question = "$" + str(b - 1) + "(1) + " + str(b - 1) + "(" + str(b) + ") + " + str(b - 1) + \
                           "(" + str(b) + "^2) + " + str(b - 1) + str(b) + "^3) + ... + " + str(b - 1) + \
                           "(" + str(b) + "^" + str(maxPow - 1) + ") + " + str(b - 1) + "(" + str(b) + "^" + str(maxPow) + ") = $"
                answer = "$" + str(b**(maxPow + 1) - 1) + "$"
        elif rand == 3:
            maxTri = random.randint(7, 12)
            totTri = maxTri * (maxTri + 1) / 2
            question = '$1 + 3 + 6 + 10 + ... + ' + str(totTri) + ' = $'
            ans = 0
            for i in range(1, maxTri+1):
                ans += i * (i+1)/2
            answer = '$' + str(ans) + '$'
        
        elif rand == 4:
            first, second = random.randint(1, 4), random.randint(1, 4)
            numNums = random.randint(8, 12)
            fibs = [0] * (numNums + 2)
            fibs[0], fibs[1] = first, second
            for i in range(2, numNums + 2):
                fibs[i] = fibs[i-1] + fibs[i-2]
            question = "$" + str(fibs[0]) + " + " + str(fibs[1]) + " + " + str(fibs[2]) + \
                       " + " + str(fibs[3]) + " + " + str(fibs[4]) + " + ... + " + \
                       str(fibs[numNums - 2]) + " + " + str(fibs[numNums - 1]) + " = $"
            answer = "$" + str(fibs[numNums + 1] - fibs[1]) + "$"
    return [question, answer, end]

def FractionDivision(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 3)
    if rand == 0:
        f1 = fraction.LessThan1Fraction(10, 10)
        f2 = fraction.LessThan1Fraction(10, 10)
        question = '$' + str(f1) + ' \\div ' + str(f2) + ' = $'
        if f1 == f2: return FractionDivision(probNum)
        answer = '$' + fraction.Divide(f1, f2).ToStringAns() + '$'
    
    elif rand == 1:
        whole = random.randint(2, 99)
        while len(utility.Factors(whole)) < 4:
            whole = random.randint(2, 99)
        facts = utility.Factors(whole)
        num = facts[random.randint(1, len(facts)-2)]
        while num <= 2:
            num = facts[random.randint(1, len(facts)-2)]
        den = random.randint(2, num-1)
        while utility.GCD(num, den) != 1:
            den = random.randint(2, num-1)
        
        mn = MixedNumber(num, den)
        if random.randint(0, 1):
            question = '$' + str(whole) + ' \\div ' + str(mn) + ' = $'
            answer = '$' + Fraction(whole * den, num).ToStringAns() + '$'
        else:
            question = '$' + str(mn) + ' \\div ' + str(whole) + ' = $'
            answer = '$' + Fraction(num, whole * den).ToStringAns() + '$'
    
    elif rand == 2:
        f = fraction.LessThan1Fraction(10, 10)
        temp = fraction.LessThan1Fraction(10, 10)
        mn = MixedNumber(random.randint(1, 6), temp.numerator, temp.denominator)
        if random.randint(0, 1):
            question = '$' + str(f) + ' \\div ' + str(mn) + ' = $'
            answer = '$' + fraction.Divide(f, mn.ToFraction()).ToStringAns() + '$'
        else:
            question = '$' + str(mn) + ' \\div ' + str(f) + ' = $'
            answer = '$' + fraction.Divide(mn.ToFraction(), f).ToStringAns() + '$'
    
    elif rand == 3:
        den1 = random.randint(2, 8)
        den2 = random.randint(2, 8) if random.randint(0, 2) == 0 else (den1 * random.randint(1, 2))
        num1 = random.randint(den1 + 1, den1 * 4)
        num2 = random.randint(den2 + 1, den2 * 4)
        mn1, mn2 = MixedNumber(num1, den1), MixedNumber(num2, den2)
        if mn1.f.numerator == mn2.f.numerator and mn1.f.denominator == mn2.f.denominator:
            return FractionDivision(probNum)
        question = '$' + str(mn1) + ' \\div ' + str(mn2) + ' = $'
        if mn1 == mn2: return FractionDivision(probNum)
        answer = '$' + fraction.Divide(mn1.ToFraction(), mn2.ToFraction()).ToStringAns() + '$'
    return [question, answer, end]

def FractionMultiplication(probNum):
    question, answer, end = '', '', ''
    rand = random.randint(0, 3)
    if rand == 0:
        f1 = fraction.LessThan1Fraction(10, 10)
        f2 = fraction.LessThan1Fraction(10, 10)
        question = '$' + str(f1) + ' \\times ' + str(f2) + ' = $'
        answer = '$' + str(fraction.Multiply(f1, f2)) + '$'
    
    elif rand == 1:
        whole = random.randint(2, 99)
        facts = utility.Factors(whole)
        while len(facts) < 4:
            whole = random.randint(2, 99)
            facts = utility.Factors(whole)
        den = facts[random.randint(1, len(facts)-2)]
        while den <= 2:
            den = facts[random.randint(1, len(facts)-2)]
        if random.randint(0, 1):
            den = random.randint(2, 8)
        num = random.randint(den+1, den*5 + 1)
        while utility.GCD(num, den) != 1:
            num = random.randint(den+1, den*5 + 1)
        
        mn = MixedNumber(num, den)
        if random.randint(0, 1):
            question = '$' + str(whole) + ' \\times ' + str(mn) + ' = $'
            answer = '$' + str(Fraction(whole * num, den)) + '$'
        else:
            question = '$' + str(mn) + ' \\times ' + str(whole) + ' = $'
            answer = '$' + str(Fraction(whole * den, den)) + '$'
    
    elif rand == 2:
        f = fraction.LessThan1Fraction(10, 10)
        temp = fraction.LessThan1Fraction(10, 10)
        mn = MixedNumber(random.randint(1, 6), temp.numerator, temp.denominator)
        if random.randint(0, 1):
            question = '$' + str(f) + ' \\times ' + str(mn) + ' = $'
            answer = '$' + str(fraction.Multiply(f, mn.ToFraction())) + '$'
        else:
            question = '$' + str(mn) + ' \\times ' + str(f) + ' = $'
            answer = '$' + str(fraction.Multiply(mn.ToFraction(), f)) + '$'
    
    elif rand == 3:
        den1 = random.randint(2, 8)
        den2 = random.randint(2, 8) if random.randint(0, 2) == 0 else (den1 * random.randint(1, 2))
        num1 = random.randint(den1+1, den1*4)
        num2 = random.randint(den2+1, den2*4)
        
        mn1 = MixedNumber(num1, den1)
        mn2 = MixedNumber(num2, den2)
        
        if mn1.f.numerator == mn2.f.numerator and mn1.f.denominator == mn2.f.denominator:
            return FractionMultiplication(probNum)
        question = '$' + str(mn1) + ' \\times ' + str(mn2) + ' = $'
        answer = '$' + str(fraction.Multiply(mn1.ToFraction(), mn2.ToFraction())) + '$'
    return [question, answer, end]

def FractionToPercent(probNum):
    question, answer, end = '', '', ''
    likelyDen = [7, 14, 8, 16, 40, 125]
    den = random.randint(3, 16) if random.randint(0, 2) == 0 else likelyDen[random.randint(0, len(likelyDen)-1)]
    if random.randint(0, 3) == 0:
        den *= random.randint(1, 3)
    num = random.randint(1, den - 1)
    while utility.GCD(den, num) != 1:
        num = random.randint(1, den - 1)
    if random.randint(0, 4) == 0: num += den * random.randint(1, 7)
    f = Fraction(num, den)
    question = '$' + str(f) + ' ='
    end = '\\%$'
    if num >= den and random.randint(0, 1):
        question = '$' + str(f.ToMixedNumber()) + ' ='
    end = '\\%$'
    answer = '$' + Fraction(num*100, den).ToStringAns() + '$'
    return [question, answer, end]

def HowManyXDigitNumbers(probNum):
    question, answer, end = '', '', ''
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if random.randint(0, 1):
        compNumber = (random.randint(100, 999) if random.randint(0, 1) else random.randint(1000, 9999)) \
                     if random.randint(0, 2) == 0 else \
                     (random.randint(1, 9) * (111 if random.randint(0, 1) else 1111))
        add = ''
        type = random.randint(0, 3)
        numDigs = len(str(compNumber))
        minNumber = 10**(numDigs - 1)
        if type == 0:
            add = 'less than $' + str(compNumber) + '$ are there?'
            answer = '$' + str(compNumber - minNumber) + '$'
        elif type == 1:
            add = 'greater than $' + str(compNumber) + '$ are there?'
            answer = '$' + str(minNumber * 10 - compNumber - 1) + '$'
        elif type == 2:
            add = 'less than or equal to $' + str(compNumber) + '$ are there?'
            answer = '$' + str(compNumber - minNumber + 1) + '$'
        elif type == 3:
            add = 'greater than or equal to $' + str(compNumber) + '$ are there?'
            answer = '$' + str(minNumber * 10 - compNumber) + '$'
        question = 'How many $' + str(numDigs) + '$-digit numbers ' + add
    else:
        numDigs = random.randint(3, 4)
        amount = 10**numDigs - 10**(numDigs-1)
        type = random.randint(0, 3)
        if type == 0:
            question = 'How many $' + str(numDigs) + '$-digit numbers are even?'
            answer = '$' + str(amount/2) + '$'
        elif type == 1:
            question = 'How many $' + str(numDigs) + '$-digit numbers are odd?'
            answer = '$' + str(amount/2) + '$'
        elif type == 2:
            question = 'How many $' + str(numDigs) + '$-digit numbers end in a $' + digits[random.randint(0, len(digits)-1)] + '$?'
            answer = '$' + str(amount / 10) + '$'
        elif type == 3:
            type1 = random.randint(0, len(digits)-1)
            type2 = random.randint(0, len(digits)-1)
            while type1 == type2:
                type2 = random.randint(0, len(digits)-1)
            question = 'How many $' + str(numDigs) + '$-digit numbers end in a $' + digits[type1] + '$ or a $' + digits[type2] + '$?'
            answer = '$' + str(amount / 5) + '$'
    return [question, answer, end]

def Inequalities(probNum):
    question, answer, end = '', '', ''
    l1 = Linear(random.randint(-5, 5), random.randint(-15, 15))
    l2 = Linear(random.randint(-5, 5), random.randint(-15, 15))
    if random.randint(0, 2) == 0:
        l1.B = 0
    if random.randint(0, 2) == 0:
        if random.randint(0, 1): l1.A = 1
        else: l1.A = 0
    types = ['<', '>']
    itype = random.randint(0, 1)
    constant = l2.B - l1.B
    coeff = l1.A - l2.A
    if coeff == 0:
        return Inequalities(probNum)
    ans = Fraction(constant, coeff)
    itype2 = itype
    if coeff < 0: itype2 = abs(itype2 - 1)
    rand = random.randint(0, 19)
    if len(str(l1)) == 0 or len(str(l2)) == 0:
        return Inequalities(probNum)
    if len(str(l1)) + len(str(l2)) <= 4:
        return Inequalities(probNum)
    if rand < 16:
        question = 'If $' + str(l1) + ' ' + types[itype] + ' ' + str(l2) + '$ then $x ' + types[itype2] + '$'
        answer = '$' + ans.ToStringAns() + '$'
    elif rand < 20:
        type = 'largest' if types[itype2] == '<' else 'smallest'
        question = 'The ' + str(type) + ' integer $x$ such that $' + str(l1) + ' ' + types[itype] + ' ' + str(l2) + '$ is'
        if types[itype2] == '<':
            i = 1000
            while True:
                if i < float(constant) / coeff:
                    answer = '$' + str(i) + '$'
                    break
                i-=1
        else:
            i = -1000
            while True:
                if i > float(constant) / coeff:
                    answer = '$' + str(i) + '$'
                    break
                i+=1
    return [question, answer, end]

def Parabolas(probNum):
    question, answer, end = '', '', ''
    type = random.randint(0, 5)
    if type < 2:
        if random.randint(0, 1):
            A = random.randint(-5, 5)
            B = random.randint(-10, 10)
            C = random.randint(-12, 12)
            q = Quadratic(A, B, C)
            if random.randint(0, 2) == 0:
                question = 'The y-intercept of $y = ' + str(q) + '$ is $(a, b)$ and $a + b =$'
            else:
                question = 'The y-intercept of $y = ' + str(q) + '$ is $(a, b)$ and $b = $'
            answer = '$' + str(C) + '$'
        else:
            AA = random.randint(1, 3)
            A = random.randint(-5, 5)
            B = random.randint(-10, 10)
            C = random.randint(-12, 12)
            q = Cubic(AA, A, B, C)
            if random.randint(0, 2) == 0:
                question = 'The y-intercept of $y = ' + str(q) + '$ is $(a, b)$ and $a + b =$'
            else:
                question = 'The y-intercept of $y = ' + str(q) + '$ is $(a, b)$ and $b =$'
            answer = '$' + str(C) + '$'
    
    elif type < 4:
        if random.randint(0, 3) < 3:
            A1 = random.randint(1, 4)
            B2 = random.randint(-3, 4)
            q = Quadratic(A1**2, A1*B2*2, B2**2)
            if random.randint(0, 2) == 0:
                question = 'The x-intercept of $y = ' + str(q) + '$ is $(a, b)$ and $a + b =$'
            else:
                question = 'The x-intercept of $y = ' + str(q) + '$ is $(a, b)$ and $a =$'
            answer = '$' + str(Fraction(-B2, A1)) + '$'
        else:
            if random.randint(0, 1):
                if random.randint(0, 1):
                    question = 'The x-intercept of $y = x^3 + 3x^2 + 3x + 1$ is $(a, b)$. Find $a + b$.'
                else:
                    question = 'The x-intercept of $y = x^3 + 3x^2 + 3x + 1$ is $(a, b)$ and $a = $'
                answer = '$-1$'
            else:
                if random.randint(0, 1):
                    question = 'The x-intercept of $y = x^3 - 3x^2 + 3x - 1$ is $(a, b)$. Find $a + b$.'
                else:
                    question = 'The x-intercept of $y = x^3 - 3x^2 + 3x - 1$ is $(a, b)$ and $a = $'
                answer = '$1$'
    
    elif type == 4:
        A = random.randint(-6, 6)
        while A == 0:
            A = random.randint(-6, 6)
        B = random.randint(-5, 5)
        C = random.randint(-10, 10)
        q = Quadratic(A, B, C)
        if random.randint(0, 1):
            question = '$f(x) = '
        else:
            question = '$g(x) = '
        question += str(q) + '$.  The axis of symmetry is $x = $'
        answer = '$' + str(Fraction(-B, 2*A)) + '$'
    
    elif type < 6:
        A = random.randint(-3, 3)
        B = random.randint(-3, 3)
        C = random.randint(-5, 6)
        q = Quadratic(A, B, C)
        if random.randint(0, 2) == 0:
            q.C = 0
            question = 'The discriminant of $' + str(q) + ' = ' + str(-C) + '$ is'
        else:
            question = 'The discriminant of $' + str(q) + '= 0$ is'
        answer = '$' + str(B**2 - 4*A*C) + '$'
    return [question, answer, end]

def PolynomialDivision(probNum):
    question, answer, end = '', '', ''
    p = Polynomial(random.randint(3, 5))
    for i in range(len(p.coeff)):
        p.coeff[i] = random.randint(-5, 5)
    l = Linear(1, random.randint(-5, 2))
    question = 'The remainder when $' + str(p) + '$ is divided by $' + str(l) + '$ is'
    ans = 0
    for i in range(len(p.coeff)):
        if i!=0: ans *= -l.B
        ans += p.coeff[i]
    answer = '$' + str(ans) + '$'
    return [question, answer, end]

def SolvingInvolvesFactoring(probNum):
    question, answer, end= '', '', ''
    type = random.randint(0, 2)
    if type == 0:
        A = random.randint(-2, 4)
        B = random.randint(-2, 4)
        while B == 0: B = random.randint(-2, 4)
        val = random.randint(3, 25)
        x = random.randint(0, val * 2 / 3 - 1)
        y = Fraction((val - A * x), B)
        q = Polynomial(3)
        q.coeff[0] = A**2
        q.coeff[1] = B*A*2
        q.coeff[2] = B**2
        sq = ''
        
        for i in range(3):
            if q.coeff[i] == 0: continue
            b = False
            for j in range(i):
                if q.coeff[j] != 0:
                    b = True
            if not b:
                if q.coeff[i] < 0:
                    sq += '-'
            else:
                sq += ' - ' if q.coeff[i] < 0 else ' + '
            if abs(q.coeff[i]) != 1:
                sq += str(abs(q.coeff[i]))
            if i == len(q.coeff) - 2:
                sq += 'xy'
            elif i < len(q.coeff) - 2:
                sq += 'x^' + str(len(q.coeff) - i - 1)
            elif i == len(q.coeff) - 1: sq += 'y^2'
        
        if A == 0:
            question = "If $" + str(sq) + " = " + str(val * val) + "$ then the largest value of $y$ is "
            answer = "$" + str(y) + "$"
        elif random.randint(0, 1):
            question = "If $" + str(sq) + " = " + str(val * val) + "$ and $x = " + str(x) + "$ then the largest value of $y$ is "
            answer = "$" + str(y) + "$"
        else:
            question = "If $" + str(sq) + " = " + str(val * val) + "$ and $x = " + str(x) + "$ then the smallest value of $y$ is "
            y = Fraction(-val - A * x, B)
            answer = "$" + str(y) + "$"
    
    elif type == 1:
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        if random.randint(0, 1):
            question = "If $x = " + str(x) + "$ and y = " + str(y) + " then $(x - y)(x^2 + xy + y^2) =$"
            answer = "$" + str(x**3 - y**3) + "$"
        else:
            question = 'If $x = ' + str(x) + '$ and y = ' + str(y) + ' then $(x + y)(x^2 - xy + y^2) =$'
            answer = '$' + str(x**3 + y**3) + '$'
    
    elif type == 2:
        rand = random.randint(0, 3)
        if rand == 0:
            val = random.randint(2, 15)
            x = random.randint(2, 15)
            if random.randint(0, 1):
                question = 'If $x = ' + str(x) + '$ then $x^2 + 2(' + str(val) + ')(x) + ' + str(val) + '^2$'
                answer = "$" + str((x + val) * (x + val)) + "$"
            else:
                question = "If $x = " + str(x) + "$ then $x^2 - 2(" + str(val) + ")(x) + " + str(val) + "^2$"
                answer = "$" + str((x - val) * (x - val)) + "$"
        elif rand == 1:
            val = random.randint(2, 15)
            x = random.randint(2, 15)
            if random.randint(0, 1):
                question = "$" + str(x) + "^2 - 2(" + str(x) + ")(" + str(val) + ") + " + str(val) + "^2 = $"
                answer = "$" + str((x - val) * (x - val)) + "$"
            else:
                question = "$" + str(x) + "^2 + 2(" + str(x) + ")(" + str(val) + ") + " + str(val) + "^2 = $"
                answer = "$" + str((x + val) * (x + val)) + "$"
        elif rand == 2:
            val = random.randint(2, 10)
            x = random.randint(2, 10)
            if random.randint(0, 1):
                question = "If $x = " + str(x) + "$ then $(x + " + str(val) + ")(x^2 - " + str(val) + "x + " + str(val * val) + ") =$"
                answer = "$" + str(x * x * x + val * val * val) + "$"
            else:
                question = "If $x = " + str(x) + "$ then $(x - " + str(val) + ")(x^2 + " + str(val) + "x + " + str(val * val) + ") =$"
                answer = "$" + str(x * x * x - val * val * val) + "$"
        elif rand == 3:
            val = random.randint(2, 10)
            x = random.randint(2, 10)
            if random.randint(0, 1):
                question = "$(" + str(x) + " + " + str(val) + ")(" + str(x * x) + " - (" + str(val) + ")(" + str(x) + ") + " + str(val * val) + ") =$"
                answer = "$" + str(x * x * x + val * val * val) + "$"
            else:
                question = "$(" + str(x) + " - " + str(val) + ")(" + str(x * x) + " + (" + str(val) + ")(" + str(x) + ") + " + str(val * val) + ") =$"
                answer = "$" + str(x * x * x - val * val * val) + "$"
    return [question, answer, end]

def Limits(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 4) < 4:
        val = random.randint(0, 3)
        rand = random.randint(0, 6)
        if rand < 3:
            c = Cubic()
            c.A = random.randint(1, 2)
            c.B = random.randint(-2, 3) if random.randint(0, 2) == 0 else 0
            c.C = random.randint(-2, 3) if random.randint(0, 4) == 0 else 0
            c.D = -c.Evaluate(val)
            
            if random.randint(0, 2) == 0:
                q = Quadratic()
                q.A = random.randint(1, 2)
                q.B = random.randint(-2, 2) if random.randint(0, 4) == 0 else 0
                q.C = -q.Evaluate(val)
                if q.Derivative().Evaluate(val) == 0:
                    return Limits(probNum)
                question = "$\\displaystyle\\lim_{x \\to " + str(val) + "}\\frac{" + str(c) + "}{" + str(q) + "} = $"
                ans = Fraction(c.Derivative().Evaluate(val), q.Derivative().Evaluate(val))
                answer = "$" + ans.ToStringAns() + "$"
            else:
                l = Linear()
                l.A = random.randint(1, 4)
                l.B = -l.Evaluate(val)  
                question = "$\\displaystyle\\lim_{x \\to " + str(val) + "}\\frac{" + str(c) + "}{" + str(l) + "} = $"
                ans = Fraction(c.Derivative().Evaluate(val), l.A)
                answer = "$" + ans.ToStringAns() + "$"
        elif rand < 6:
            c = Quadratic()
            c.A = random.randint(1, 2)
            c.B = random.randint(-2, 2) if random.randint(0, 2) == 0 else 0
            c.C = -c.Evaluate(val)
            
            if random.randint(0, 2) == 0:
                q = Quadratic()
                q.A = random.randint(1, 2)
                q.B = random.randint(-2, 2) if random.randint(0, 2) == 0 else 0
                q.C = -q.Evaluate(val)
                if q.Derivative().Evaluate(val) == 0:
                    return Limits(probNum)
                question = "$\\displaystyle\\lim_{x \\to " + str(val) + "}\\frac{" + str(c) + "}{" + str(q) + "} = $"
                ans = Fraction(c.Derivative().Evaluate(val), q.Derivative().Evaluate(val))
                answer = "$" + ans.ToStringAns() + "$"
            else:
                l = Linear()
                l.A = random.randint(1, 4)
                l.B = -l.Evaluate(val)
                question = "$\\displaystyle\\lim_{x \\to " + str(val) + "}\\frac{" + str(c) + "}{" + str(l) + "} = $"
                ans = Fraction(c.Derivative().Evaluate(val), l.A)
                answer = "$" + ans.ToStringAns() + "$"
        else:
            if random.randint(0, 1):
                top = Linear()
                top.A = random.randint(-5, 5)
                top.B = random.randint(-8, 8)
                bottom = Linear()
                bottom.A = random.randint(-5, 5)
                bottom.B = random.randint(-5, 5)
                while bottom.A == 0:
                    top.A = random.randint(-5, 5)
                    bottom.A = random.randint(-5, 5)
                question = "$\\displaystyle\\lim_{x \\to \\infty}\\frac{" + str(top) + "}{" + str(bottom) + "} = $"
                ans = Fraction(top.A, bottom.A)
                answer = "$" + ans.ToStringAns() + "$"
            else:
                val = random.randint(1, 8)
                if random.randint(0, 1):
                    q = Quadratic()
                    q.A = random.randint(1, 2)
                    q.B = random.randint(-2, 2) if random.randint(0, 2) == 0 else 0
                    q.C = random.randint(-10, 14)
                    
                    while True:
                        l = Linear()
                        l.A = random.randint(-3, 5)
                        if random.randint(0, 2) < 2 and q.Evaluate(val) != 0:
                            factors = utility.Factors(abs(q.Evaluate(val)))
                            value = factors[random.randint(0, len(factors)-1)]
                            l.B = value - l.A * val
                        else: l.B = random.randint(0, 8)
                        if l.Evaluate(val) != 0:
                            break
                    
                    question = "$\\displaystyle\\lim_{x \\to " + str(val) + "}\\frac{" + str(q) + "}{" + str(l) + "} = $"
                    ans = Fraction(q.Evaluate(val), l.Evaluate(val))
                    answer = "$" + ans.ToStringAns() + "$"
                else:
                    q = Linear()
                    q.A = random.randint(-3, 5)
                    q.B = random.randint(-10, 14)
                    
                    while True:
                        l = Linear()
                        l.A = random.randint(-3, 5)
                        if random.randint(0, 2) < 2 and q.Evaluate(val) != 0:
                            factors = utility.Factors(abs(q.Evaluate(val)))
                            value = factors[random.randint(0, len(factors)-1)]
                            l.B = value - l.A * val
                        else:
                            l.B = random.randint(0, 8)
                        if l.Evaluate(val) != 0:
                            break
                    
                    question = "$\\displaystyle\\lim_{x \\to " + str(val) + "}\\frac{" + str(q) + "}{" + str(l) + "} = $"
                    ans = Fraction(q.Evaluate(val), l.Evaluate(val))
                    answer = "$" + ans.ToStringAns() + "$"
    return [question, answer, end]

def Equations(probNum):
    question, answer, end = '', '', ''
    rand, type = random.randint(0, 29), 0
    if rand < 10: type = 0
    elif rand < 20: type = 1
    elif rand < 23: type = 2
    elif rand < 25: type = 3
    elif rand < 27: type = 4
    else: type = 5
    
    if type == 0:
        while True:
            l1, l2 = Linear(), Linear()
            l1.A = random.randint(-5, 5) if random.randint(0, 4) == 0 else random.randint(1, 5)
            l2.A = random.randint(-5, 5) if random.randint(0, 4) == 0 else random.randint(1, 5)
            if l1.A == 0 or l2.A == 0:
                l1.A = random.randint(-5, 5) if random.randint(0, 4) == 0 else random.randint(1, 5)
                l2.A = random.randint(-5, 5) if random.randint(0, 4) == 0 else random.randint(1, 5)
            l1.B = random.randint(-8, 8)
            l2.B = random.randint(-8, 8)
            
            x = Fraction(l2.B - l1.B, l1.A - l2.A)
            if x.denominator != 1 and random.randint(0, 2) < 2:
                continue
            break
        
        q = Linear(1, 0)
        if random.randint(0, 3) < 3:
            q.A = random.randint(-5, 5) if random.randint(0, 4) == 0 else random.randint(1, 6)
            q.B = random.randint(-5, 5)
        question = 'If $' + str(l1) + ' = ' + str(l2) + '$ then $' + str(q) + ' = $'
        ans = Fraction(x.numerator, x.denominator)
        ans = fraction.Multiply(ans, Fraction(q.A, 1))
        ans = fraction.Add(ans, Fraction(q.B, 1))
        if ans.denominator == 0:
            return Equations(probNum)
        answer = '$' + ans.ToStringAns() + '$'
    
    elif type == 1:
        choosex = random.randint(0, 1) == 0
        if choosex:
            x1 = -1 if random.randint(0, 1) else 1
            x2 = -1 if random.randint(0, 1) else 1
            if random.randint(0, 5) == 0:
                if random.randint(0, 1):
                    x1 = random.randint(-3, -2) if random.randint(0, 1) else random.randint(2, 3)
                else:
                    x2 = random.randint(-3, -2) if random.randint(0, 1) else random.randint(2, 3)
            while True:
                y1 = random.randint(-2, 3)
                y2 = random.randint(-2, 3)
                if not (y1 == 0 or y2 == 0):
                    break
        else:
            y1 = -1 if random.randint(0, 1) == 0 else 1
            y2 = -1 if random.randint(0, 1) == 0 else 1
            if random.randint(0, 5) == 0:
                if random.randint(0, 1):
                    y1 = random.randint(-3, -2) if random.randint(0, 1) else random.randint(2, 3)
                else:
                    y2 = random.randint(-3, -2) if random.randint(0, 1) else random.randint(2, 4)
            while True:
                x1 = random.randint(-2, 3)
                x2 = random.randint(-2, 3)
                if not (x1 == 0 or x2 == 0):
                    break
        c1 = random.randint(-10, -1) if random.randint(0, 2) == 0 else random.randint(2, 16)
        c2 = random.randint(-10, -1) if random.randint(0, 2) == 0 else random.randint(2, 16)
        if x1*y2 - x2*y1 == 0:
            return Equations(probNum)
        x = Fraction(c1*y2 - y1*c2, x1*y2 - x2*y1)
        y = Fraction(x1*c2 - c1*x2, x1*y2 - x2*y1)
        if not choosex:
            lin1 = (('' if x1 == 1 else '-') if abs(x1) == 1 else str(x1)) + 'x ' + ('- ' if y1 < 0 else '+ ') + \
                   ('' if abs(y1) == 1 else str(abs(y1))) + 'y = ' + str(c1)
            lin2 = (('' if x2 == 1 else '-') if abs(x2) == 1 else str(x2)) + 'x ' + ('- ' if y2 < 0 else '+ ') + \
                   ('' if abs(y2) == 1 else str(abs(y2))) + 'y = ' + str(c2)
        else:
            lin1 = (('' if y1 == 1 else '-') if abs(y1) == 1 else str(y1)) + 'y ' + ('- ' if x1 < 0 else '+ ') + \
                   ('' if abs(x1) == 1 else str(abs(x1))) + 'x = ' + str(c1)
            lin2 = (('' if y2 == 1 else '-') if abs(y2) == 1 else str(y2)) + 'y ' + ('- ' if x2 < 0 else '+ ') + \
                   ('' if abs(x2) == 1 else str(abs(x2))) + 'x = ' + str(c2)
        question = "If $" + str(lin1) + "$ and $" + str(lin2) + "$ then $" + ("y" if choosex else "x") + " =$"
        answer = "$" + (y.ToStringAns() if choosex else x.ToStringAns()) + "$"
    elif type == 2:
        while True:
            den = random.randint(4, 15)
            Factors = utility.Factors(den)
            if not (len(Factors) <= 2):
                break
        
        sub1 = Factors[random.randint(1, len(Factors) - 2)]
        sub2 = den / sub1
        
        while True:
            add1 = random.randint(-3, 4)
            add2 = random.randint(-3, 4)
            if not (add1 == 0 or add2 == 0):
                break
        
        add = random.randint(0, 1) == 0
        question = "If $\\displaystyle\\frac{x " + (" - " if add1 < 0 else " + ") + str(abs(add1)) + "}{" + str(sub1) + "}" + \
                   (" + " if add else " - ") + "\\displaystyle\\frac{x " + (" - " if add2 < 0 else " + ") + str(abs(add2)) + \
                   "}{" + str(sub2) + "} = \\displaystyle\\frac{x}{" + str(den) + "}$ then $x =$"
        ans = Fraction(-(add1 * sub2 + add2 * sub1 * (1 if add else -1)), sub2 + sub1 * (1 if add else -1) - 1)
        if ans.denominator == 0:
            return Equations(probNum)
        answer = "$" + ans.ToStringAns() + "$"
    
    elif type == 3:
        words = ['zero', 'one', 'two', 'three', 'four', 'five']
        num = random.randint(3, 5)
        x = random.randint(30, 59)
        val = x * num + num * (num - 1) / 2
        if random.randint(0, 1):
            if random.randint(0, 1):
                question = "The sum of " + words[num] + " consecutive integers is $" + str(val) + "$.  The largest integer is "
                answer = "$" + str(x + num - 1) + "$"
            else:
                question = "The sum of " + words[num] + " consecutive integers is $" + str(val) + "$.  The smallest integer is "
                answer = "$" + str(x) + "$"
        else:
            question = '$x'
            for i in range(1, num):
                question += ' + (x + ' + str(i) + ')'
            question += ' = ' + str(val) + '$. '
            l = Linear(random.randint(1, 3), random.randint(1, 3))
            question += 'Find $' + str(l) + '$'
            answer = '$' + str(l.Evaluate(x)) + '$'
    elif type == 4:
        while True:
            l = Linear(random.randint(1, 4), random.randint(-5, 6))
            cons = random.randint(5, 20)
            sol1 = Fraction(cons - l.B, l.A)
            sol2 = Fraction(-cons - l.B, l.A)
            if not (sol1.denominator != 1 and sol2.denominator != 1):
                break
        if random.randint(0, 1):
            question = "The largest value of $x$ such that $|" + str(l) + "| = " + str(cons) + ".$"
            answer = "$" + (sol1.ToStringAns() if sol1.numerator * sol2.denominator > sol2.numerator * sol1.denominator else sol2.ToStringAns()) + "$"
        else:
            question = "The smallest value of $x$ such that $|" + str(l) + "| = " + str(cons) + ".$"
            answer = "$" + (sol2.ToStringAns() if sol1.numerator * sol2.denominator > sol2.numerator * sol1.denominator else sol1.ToStringAns()) + "$"
    elif type == 5:
        while True:
            l = Linear(random.randint(1, 6), random.randint(-5, 5))
            while l.B == 0:
                l.B = random.randint(-5, 5)
            cons = random.randint(-15, 15)
            words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', \
                     'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', \
                     'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
            start = words[l.A]
            start = string.upper(start[0]) + start[1:]
            question = start + ' times a number ' + ('minus' if l.B < 0 else 'plus') + ' ' + \
                       words[abs(l.B)] + ' is ' + ('negative ' if cons < 0 else '') + words[abs(cons)] + \
                       '. Find the number.'
            ans = Fraction(cons - l.B, l.A)
            answer = '$' + ans.ToStringAns() + '$'
            if not (ans.denominator != 1 and random.randint(0, 2) < 3):
                break
    return [question, answer, end]

def Estimations(probNum):
    if probNum == 10: return estimations.Exp10()
    elif probNum == 20: return estimations.Exp20()
    elif probNum == 30: return estimations.Exp30()
    elif probNum == 40: return estimations.Exp40()
    elif probNum == 50: return estimations.Exp50()
    elif probNum == 60: return estimations.Exp60()
    elif probNum == 70: return estimations.Exp70()
    else: return estimations.Exp80()

def ExponentialEquations(probNum):
    question, answer, end = '', '', ''
    type = -1
    rrand = random.randint(0, 7)
    if rrand < 3: type = 0
    elif rrand < 4: type = 1
    elif rrand < 5: type = 2
    else: type = 3
    if type == 0:
        if random.randint(0, 9) == 0:
            firstExp = random.randint(2, 3)
            secondExp = random.randint(1, 3)
            while firstExp == secondExp:
                secondExp = random.randint(1, 3)
            bb = random.randint(2, 17)
            bbase = random.randint(2, 24)
            eq = bb**firstExp
            question = 'If $' + str(bbase) + '^{' + str(firstExp) + 'x} = ' + \
                       str(eq) + '$ then $' + str(bbase) + '^{' + \
                       ('' if secondExp == 1 else str(secondExp)) + 'x} = $'
            answer = '$' + str(bb**secondExp) + '$'
        else:
            l1 = Linear(1, random.randint(-2, 2))
            l2 = Linear(1, random.randint(-2, 2))
            bbase = random.randint(2, 9)
            while l1.B == l2.B:
                l2.B = random.randint(-2, 2)
            eq = random.randint(2, 19) if random.randint(0, 2) == 0 else random.randint(100, 799)
            while (l1.B > l2.B) and (eq % (bbase ** (l1.B - l2.B)) != 0):
                eq = (bbase ** (l1.B - l2.B)) * random.randint(1, 7000 / (bbase ** (l1.B - l2.B)))
            deq = 0.0
            if eq > 100 and random.randint(0, 3) < 3:
                deq = utility.Decimalize(eq)
            question = 'If $' + str(bbase) + '^{' + str(l1) + '} = ' + str(eq if deq == 0 else deq) + '$ then $' + str(bbase) + '^{' + str(l2) + '} = $'
            ans = (eq if deq == 0 else deq) / (bbase ** (l1.B - l2.B))
            answer = '$' + str(ans) + '$'
    elif type == 1:
        if random.randint(0, 1):
            bbase = random.randint(2, 4)
            exp = random.randint(2, 3)
            bbase2 = bbase ** exp
            l1 = Linear(random.randint(1, 3), random.randint(-1, 2))
            l2 = Linear(l1.A * exp, random.randint(-1, 2))
            eq = (bbase ** exp) * random.randint(1, 19)
            question = "If $" + str(bbase2) + "^{" + str(l1) + "} = " + str(eq) + "$ then $" + str(bbase) + "^{" + str(l2) + "} = $"
            num = eq
            den = 1
            if l1.B < 0: num *= bbase2 ** abs(l1.B)
            else: den *= bbase2 ** abs(l1.B)
            if l2.B > 0: num *= bbase ** abs(l2.B)
            else: den *= bbase ** abs(l2.B)
            ans = Fraction(num, den)
            answer = '$' + str(ans) + '$'
        else:
            bbase = random.randint(2, 14)
            exp = random.randint(2, 3)
            bbase2 = bbase ** exp
            eq = random.randint(3, 14)
            if random.randint(0, 1):
                question = "If $" + str(bbase) + "^{x} = " + str(eq) + "$ then $" + str(bbase2) + "^{x} = $"
                answer = "$" + str(eq**exp) + "$"
            else:
                question = "If $" + str(bbase2) + "^{x} = " + str(eq**exp) + "$ then $" + str(bbase) + "^{x} = $"
                answer = "$" + str(eq) + "$"
    elif type == 2:
        if random.randint(0, 1):
            bbase = random.randint(2, 5)
            ex1 = random.randint(1, 3)
            ex2 = random.randint(1, 3)
            bbase2 = bbase ** ex1
            bbase3 = bbase ** ex2
            l1 = Linear(random.randint(-2, 3), random.randint(-2, 3))
            l2 = Linear(random.randint(-2, 3), random.randint(-2, 3))
            question = 'If $' + str(bbase2) + '^{' + str(l1) + '} = ' + str(bbase3) + '^{' + str(l2) + '}$ then $x = $'
            l1.A *= ex1
            l1.B *= ex1
            l2.A *= ex2
            l2.B *= ex2
            ans = Fraction(l2.B - l1.B, l1.A - l2.A)
            if ans.denominator == 0: return ExponentialEquations(probNum)
            answer = '$' + str(ans) + '$'
        else:
            x = random.randint(-4, 4)
            bbase = random.randint(2, 4)
            l1 = Linear(1, random.randint(-2, 2))
            frac = Fraction()
            if x + l1.B < 0: frac = Fraction(1, bbase**abs(x+l1.B))
            else: frac = Fraction(bbase ** abs(x+l1.B), 1)
            question = "If $" + str(bbase) + "^{" + str(l1) + "} = " + str(frac) + "$ then $x = $"
            if l1.B < 0: frac.numerator *= bbase ** -l1.B
            else: frac.denominator *= bbase ** l1.B
            answer = '$' + str(x) + '$'
    elif type == 3:
        rand = random.randint(0, 1)
        if rand == 0:
            bbase = 2 if random.randint(0, 2) == 0 else (3 if random.randint(0, 1) else 5)
            bbase2 = bbase * (random.randint(2, 5) ** 2)
            ex = random.randint(3, 5)
            if bbase2 > 60 and ex >= 5:
                return ExponentialEquations(probNum)
            rad = Radical(1, 1, bbase2**ex)
            if rad.rad == 1:
                question = "$(\\sqrt{" + str(bbase2) + "})^{" + str(ex) + "} = $"
                answer = "$" + rad.co.ToStringAns() + "$"
            else:
                question = "$(\\sqrt{" + str(bbase2) + "})^{" + str(ex) + "} = a\\sqrt{" + str(rad.rad) + "}$ and $a = $"
                answer = "$" + rad.co.ToStringAns() + "$"
            rad.Reduce()
            answer = '$' + str(rad.co) + '$'
        elif rand == 1:
            firstRoot = random.randint(2, 5)
            secondRoot = random.randint(2, 5)
            thirdRoot = utility.LCM(firstRoot, secondRoot)
            ex1 = random.randint(2, 8)
            ex2 = random.randint(2, 8)
            question = '$\\sqrt[' + str(firstRoot) + ']{x^{' + str(ex1) + '}} \\times \\sqrt[' + str(secondRoot) + ']{x^{' + str(ex2) + '}} = \\sqrt[' + str(thirdRoot) + ']{x^{n}}$ and $n = $'
            ans = fraction.Add(Fraction(ex1, firstRoot), Fraction(ex2, secondRoot))
            ans.numerator *= thirdRoot
            answer = '$' + str(ans) + '$'
    return [question, answer, end]

def FofX(probNum):
    question ,answer, end = '', '', ''
    type = random.randint(0, 1)
    if type == 0:
        if random.randint(0, 1):
            l1 = Linear(random.randint(2, 3) if random.randint(0, 2) == 0 else 1, random.randint(-4, 4))
            q = Quadratic(l1.A**2, 2*l1.A*l1.B, l1.B**2)
            process = 0
            dprocess = 0.0
            type2 = random.randint(0, 2)
            if type2 == 0: process = (random.randint(1, 7) * 10 - l1.B) / l1.A
            elif type2 == 1: process = random.randint(4, 19)
            else: dprocess = float(random.randint(5, 59)) / 10
            if len(str(q)) == 0: return FofX(probNum)
            question = 'If $f(x) = ' + str(q) + '$ then $f(' + str(process if dprocess == 0 else dprocess) + ') = $'
            if dprocess == 0: dprocess = process
            answer = '$' + utility.DoubleToAns(float(dprocess * dprocess * q.A + dprocess * q.B + q.C)) + '$'
        else:
            p = Polynomial()
            if random.randint(0, 2):
                p = Polynomial(4)
                p.coeff[0] = random.randint(-1, 1)
                p.coeff[1] = random.randint(-1, 1)
                p.coeff[2] = random.randint(-1, 1)
                p.coeff[3] = random.randint(-1, 1)
            else:
                p = Polynomial(3)
                p.coeff[0] = random.randint(-3, 6)
                p.coeff[1] = random.randint(-3, 6)
                p.coeff[2] = random.randint(-10, 10)
            process = random.randint(-3, 3)
            if len(str(p)) == 0: return FofX(probNum)
            question = 'If $f(x) = ' + str(p) + '$ then $f(' + str(process) + ') = $'
            answer = '$' + str(p.Evaluate(process)) + '$'
    else:
        if random.randint(0, 1):
            if random.randint(0, 3) == 0:
                p = Polynomial(random.randint(3, 5))
                p.coeff[0] = random.randint(1, 6)
                p.coeff[-1] = random.randint(-10, 10)
            else:
                p = Polynomial(2)
                p.coeff[0] = random.randint(-7, 6)
                p.coeff[1] = random.randint(-10, 9)
            process = random.randint(-4, 4)
            if len(p.coeff) > 2: process = random.randint(-1, 1)
            if len(str(p)) == 0: return FofX(probNum)
            question = 'If $f(x) = ' + str(p) + '$ then $f[f(' + str(process) + ')] = $'
            ans = p.Evaluate(p.Evaluate(process))
            if ans > 5000: return FofX(probNum)
            answer = '$' + str(ans) + '$'
        else:
            if random.randint(0, 3) == 0:
                p = Polynomial(random.randint(3, 5))
                p.coeff[0] = random.randint(1, 6)
                p.coeff[-1] = random.randint(-10, 10)
            else:
                p = Polynomial(2)
                p.coeff[0] = random.randint(-7, 6)
                p.coeff[1] = random.randint(-10, 9)
            if random.randint(0, 3) == 0:
                p2 = Polynomial(random.randint(3, 5))
                p2.coeff[0] = random.randint(1, 6)
                p2.coeff[-1] = random.randint(-10, 10)
            else:
                p2 = Polynomial(2)
                p2.coeff[0] = random.randint(-7, 6)
                p2.coeff[1] = random.randint(-10, 9)
            process = random.randint(-4, 4)
            if len(p.coeff) > 2 and len(p2.coeff) > 2: process = random.randint(-1, 2)
            if len(p.coeff) > 2 and len(p2.coeff) > 2: process = random.randint(-1, 1)
            if len(str(p)) == 0 or len(str(p2)) == 0: return FofX(probNum)
            question = 'If $f(x) = ' + str(p) + '$ and $g(x) = ' + str(p2) + '$ then $g[f(' + str(process) + ')] = $'
            ans = p2.Evaluate(p.Evaluate(process))
            if ans > 5000: return FofX(probNum)
            answer = '$' + str(ans) + '$'
    return [question, answer, end]

def FofXInverse(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 1):
        l1 = Linear(random.randint(-4, 4) if random.randint(0, 3) == 0 else random.randint(1, 5), random.randint(-8, 8))
        process = random.randint(-5, 5)
        question = 'If $f(x) = ' + str(l1) + '$ then $f^{-1}(' + str(process) + ') = $'
        ans = Fraction(process - l1.B, l1.A)
        if ans.denominator == 0: return FofXInverse(probNum)
        answer = '$' + str(ans) + '$'
    else:
        l1 = Linear(random.randint(-4, 4) if random.randint(0, 3) == 0 else random.randint(1, 5), random.randint(-8, 8))
        l2 = Linear(random.randint(-4, 4) if random.randint(0, 3) == 0 else random.randint(1, 5), random.randint(-8, 8))
        process = random.randint(-5, 5)
        question = 'If $f(x) = \\displaystyle\\frac{' + str(l1) + '}{' + str(l2) + '}$ then $f^{-1}(' + str(process) + ') = $'
        l2.A *= process
        l2.B *= process
        ans = Fraction(l2.B - l1.B, l1.A - l2.A)
        if ans.denominator == 0: return FofXInverse(probNum)
        answer = '$' + str(ans) + '$'
    return [question, answer, end]

def ImaginaryNumbers(probNum):
    question, answer, end = '', '', ''
    type = random.randint(0, 26)
    if type < 2:
        small = random.randint(1, 6) * 2 + 1
        med = small*small / 2
        big = med + 1
        if random.randint(0, 1):
            temp = small
            small = med
            med = temp
        question = 'The modulus of $(' + str(small) + ' + ' + str(med) + 'i)^2$ is '
        answer = '$' + str(big**2) + '$'
    elif type < 16:
        ansA, ansB = 0, 0
        if random.randint(0, 4) < 2:
            a = random.randint(1, 9)
            b = random.randint(-8, 8)
            c = random.randint(1, 9)
            d = random.randint(-8, 8)
            while b == 0:
                b = random.randint(-8, 8)
            while d == 0:
                d = random.randint(-8, 8)
            ansA = a*c - b*d
            ansB = a*d + b*c
            insert = '(' + str(a) + (' - ' if b < 0 else ' + ') + ('' if abs(b) == 1 else str(abs(b))) + \
                     'i)(' + str(c) + (' - ' if d < 0 else ' + ') + ('' if abs(d) == 1 else str(abs(d))) + 'i)'
        else:
            a = random.randint(1, 9)
            b = random.randint(-8, 8)
            while b == 0:
                b = random.randint(-8, 8)
            ansA = a**2 - b**2
            ansB = 2*a*b
            insert = '(' + str(a) + (' - ' if b < 0 else ' + ') + ('' if abs(b) == 1 else str(abs(b))) + 'i)^2'
        rand = random.randint(0, 2)
        if rand == 0:
            question = "If $" + str(insert) + " = a + bi$ then $a = $"
            answer = "$" + str(ansA) + "$"
        elif rand == 1:
            question = "If $" + str(insert) + " = a + bi$ then $b = $"
            answer = "$" + str(ansB) + "$"
        else:
            question = "If $" + str(insert) + " = a + bi$ then $a + b = $"
            answer = "$" + str(ansA + ansB) + "$"
    elif type < 17:
        b = random.randint(-10, 10)
        while b == 0:
            b = random.randint(-10, 10)
        a = random.randint(-10, -1)
        insert = Linear(b, a).ToString('i')
        ansA = a
        ansB = -b
        rand = 0 if random.randint(0, 9) == 0 else (1 if random.randint(0, 1) else 2)
        if rand == 0:
            question = "The conjugate $" + str(insert) + "$ is $a + bi$ and $a = $"
            answer = "$" + str(ansA) + "$"
        elif rand == 1:
            question = "The conjugate $" + str(insert) + "$ is $a + bi$ and $b = $"
            answer = "$" + str(ansB) + "$"
        else:
            question = "The conjugate $" + str(insert) + "$ is $a + bi$ and $a + b = $"
            answer = "$" + str(ansA + ansB) + "$"
    elif type < 22:
        a = random.randint(1, 30)
        b = random.randint(-30, 30)
        question = '$(' + str(a) + (' - ' if b < 0 else ' + ') + ('' if abs(b) == 1 else str(abs(b))) + 'i)(' + \
                   str(a) + (' + ' if b < 0 else ' - ') + ('' if abs(b) == 1 else str(abs(b))) + 'i)$'
        answer = '$' + str(a*a + b*b) + '$'
    elif type < 24:
        co = random.randint(1, 3)
        pow = random.randint(2, 6)
        question = '$' + ('' if co == 1 else ('(' + str(co))) + 'i' + ('' if co == 1 else ')') + '^{' + str(pow) + '}$'
        ans = co**pow
        while pow >= 2:
            ans *= -1
            pow -=2
        answer = '$' + str(ans) + ('i' if pow > 0 else '') + '$'
    elif type < 27:
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        d = random.randint(-5, 5)
        if random.randint(0, 1): a = random.randint(1, 5)
        if random.randint(0, 1): c = random.randint(1, 5)
        ansA = Fraction(a*c + b*d, c*c + d*d)
        ansB = Fraction(a*-d + b*c, c*c + d*d)
        l1 = Linear(a, b)
        l2 = Linear(c, d)
        insert = '\\displaystyle\\frac{(' + l1.ToString('i') + ')}{(' + l2.ToString('i') + ')} = a + bi$ and '
        rand = random.randint(0, 1)
        if rand == 0:
            question = '$' + str(insert) + '$a = $'
            answer = '$' + str(ansA) + '$'
        elif rand == 1:
            question = '$' + str(insert) + '$b = $'
            answer = '$' + str(ansB) + '$'
    return [question, answer, end]

def LinesAndPoints(probNum):
    question, answer, end = '', '', ''
    rrand = random.randint(0, 6)
    type = 0
    if rrand < 4: type = 0
    elif rrand < 5: type = 1
    elif rrand < 6: type = 2
    elif rrand < 7: type = 3
    if type == 0:
        if random.randint(0, 1):
            slope = Fraction()
            yInter = Fraction()
            slope = Fraction(random.randint(1, 10), random.randint(1, 10))
            if random.randint(0, 2) == 0:
                slope = Fraction(random.randint(1, 10), 1)
            if random.randint(0, 1):
                slope.numerator *= -1
            yInter = Fraction(random.randint(1, 10), random.randint(1, 10))
            if random.randint(0, 2) == 0:
                yInter.numerator *= -1
            line = Line(slope, yInter)
            rand = random.randint(0, 1)
            if rand == 0:
                if random.randint(0, 2) == 0:
                    question = 'The slope of the line $' + str(line) + '$ is'
                    answer = '$' + str(slope) + '$'
                else:
                    question = 'The slope of the line parallel to $' + str(line) + '$ is'
                    answer = '$' + str(slope) + '$'
            elif rand == 1:
                question = 'The slope of the line perpendicular to $' + str(line) + '$ is'
                answer = '$' + str(Fraction(-slope.denominator, slope.numerator)) + '$'
        else:
            slopeDen = random.randint(2, 9)
            slopeNum = random.randint(2, 9)
            if random.randint(0, 1): 
                slopeNum = slopeDen * random.randint(2, 5)
            slope = Fraction(slopeNum, slopeDen)
            px1 = random.randint(-5, 5)
            py1 = random.randint(-5, 5)
            mult = random.randint(-5, 5)
            px2 = px1 + slope.denominator * mult
            py2 = py1 + slope.numerator * mult
            while px1 == px2 or py1 == py2:
                px1 = random.randint(-5, 5)
                py1 = random.randint(-5, 5)
                mult = random.randint(-5, 5)
                px2 = px1 + slope.denominator * mult
                py2 = py1 + slope.numerator * mult
            if random.randint(0, 1):
                temp = px1
                px1 = px2
                px2 = temp
                
                temp = py1
                py1 = py2
                py2 = temp
            if random.randint(0, 1):
                question = 'The slope of the line perpendicular to the line containing $(' + str(px1) + ',' + str(py1) + ')$ and $(' + str(px2) + ',' + str(py2) + ')$ is'
                answer = '$' + str(Fraction(-slope.denominator, slope.numerator)) + '$'
            else:
                question = 'Find the slope of the line containing the points $(' + str(px1) + ',' + str(py1) + ')$ and $(' + str(px2) + ',' + str(py2) + ')$'
                answer = '$' + str(slope) + '$'
    elif type == 1:
        if random.randint(0, 1):
            while True:
                px1 = random.randint(-10, 10)
                py1 = random.randint(-10, 10)
                px2 = px1 + random.randint(-5, 5)
                py2 = py1 + random.randint(-5, 5)
                if not ((px1 == px2 or py1 == py2) and random.randint(0, 3) < 3):
                    break
        else:
            small = random.randint(1, 3)
            big = small * small / 2
            px1 = random.randint(-10, 10)
            py1 = random.randint(-10, 10)
            if random.randint(0, 1):
                px2 = px1 + small * (-1 if random.randint(0, 1) else 1)
                py2 = py1 + big * (-1 if random.randint(0, 1) else 1)
            else:
                px2 = px1 + big * (-1 if random.randint(0, 1) else 1)
                py2 = py1 + small * (-1 if random.randint(0, 1) else 1)
        if random.randint(0, 1):
            temp = px1
            px1 = px2
            px2 = temp
            
            temp = py1
            py1 = py2
            py2 = temp
        
        question = 'Find the distance between $(' + str(px1) + ',' + str(py1) + ')$ and $(' + str(px2) + ',' + str(py2) + ')$'
        rad = Radical(1, 1, (px2 - px1) * (px2 - px1) + (py2 - py1) * (py2 - py1))
        answer = '$' + str(rad) + '$'
    elif type == 2:
        slope = Fraction(random.randint(2, 9), random.randint(2, 9))
        if random.randint(0, 2) < 2: slope = Fraction(random.randint(2, 5), 1)
        if random.randint(0, 2) == 0: slope = Fraction(random.randint(1, 4), random.randint(1, 4))
        if random.randint(0, 2) == 0: slope.numerator *= -1
        px1 = random.randint(-5, 5)
        py1 = random.randint(-5, 5)
        mult = random.randint(-5, 5)
        while mult == 0: mult = random.randint(-5, 5)
        px2 = px1 + slope.denominator * mult
        py2 = py1 + slope.denominator * mult
        leaveOut = random.randint(0, 3)
        if leaveOut == 0:
            question = 'A line with a slope of $' + str(slope) + '$ passes through points $(' + str(px1) + ',k)$ and $(' + str(px2) + ',' + str(py2) + ')$.  Find k.'
            answer = '$' + str(py1) + '$'
        if leaveOut == 1:
            question = "A line with a slope of $" + str(slope) + "$ passes through points $(k," + str(py1) + ")$ and $(" + str(px2) + "," + str(py2) + ")$.  Find k."
            answer = "$" + str(px1) + "$"
        if leaveOut == 2:
            question = "A line with a slope of $" + str(slope) + "$ passes through points $(" + str(px1) + "," + str(py1) + ")$ and $(k," + str(py2) + ")$.  Find k."
            answer = "$" + str(px2) + "$"
        if leaveOut == 3:
            question = "A line with a slope of $" + str(slope) + "$ passes through points $(" + str(px1) + "," + str(py1) + ")$ and $(" + str(px2) + ",k)$.  Find k."
            answer = "$" + str(py2) + "$"
    elif type == 3:
        if random.randint(0, 1):
            slope = Fraction(random.randint(1, 10), random.randint(1, 10))
            if random.randint(0, 2) == 0:
                slope = Fraction(random.randint(1, 10), 1)
            if random.randint(0, 1):
                slope.numerator *= -1
            yInter = Fraction(random.randint(1, 10), random.randint(1, 10))
            if random.randint(0, 2) == 0:
                yInter = Fraction(random.randint(1, 10), 1)
            if random.randint(0, 1):
                yInter.numerator *= -1
            line = Line(slope, yInter)
            question = 'The y-intercept of the line $' + str(line) + '$ is'
            answer = '$' + str(yInter) + '$'
        else:
            slope = Fraction(random.randint(-2, 2), 1)
            px1 = random.randint(-5, 5)
            py1 = random.randint(-5, 5)
            mult = random.randint(-5, 5)
            px2 = px1 + slope.denominator * mult
            py2 = py1 + slope.numerator * mult
            if random.randint(0, 1):
                temp = px1
                px1 = px2
                px2 = temp
                
                temp = py1
                py1 = py2
                py2 = py1
            yInter = py2 - px2*slope.numerator
            question = 'The y-intercept of the line containing $(' + str(px1) + ',' + str(py1) + ')$ and $(' + str(px2) + ',' + str(py2) + ')$ is $(x, y)$ and $y = $'
            answer = '$' + str(yInter) + '$'
    return [question, answer, end]

def Logs(probNum):
    question, answer, end = '', '', ''
    type = 0
    rrand = random.randint(0, 11)
    if rrand < 1: type = 0
    elif rrand < 5: type = 1
    elif rrand < 6: type = 2
    elif rrand < 8: type = 3
    elif rrand < 9: type = 4
    elif rrand < 12: type = 5
    if type == 0:
        if random.randint(0, 1):
            bbase = random.randint(2, 9)
            p = random.randint(2, 4)
            question = 'If log$_{x}' + str(bbase**p) + ' = ' + str(p) + '$ then $x = $'
            answer = '$' + str(bbase) + '$'
        else:
            bbase = Fraction(1, random.randint(2, 5))
            p = -random.randint(2, 4)
            question = 'If log$_{x}' + str(bbase.denominator**-p) + ' = ' + str(p) + '$ then $x = $'
            answer = '$' + str(bbase) + '$'
    elif type == 1:
        if random.randint(0, 4) == 0:
            l = Linear(random.randint(1, 4), random.randint(-5, 5))
            bbase = random.randint(2, 9)
            pow = random.randint(2, 4)
            while bbase**pow > 1000 or (random.randint(0, 4) < 4 and (bbase**pow - l.B) % l.A != 0):
                pow = random.randint(2, 4)
            question = 'If log$_{' + str(bbase) + '}' + str(l) + ' = ' + str(pow) + '$ then $x = $'
            ans = Fraction(bbase**pow - l.B, l.A)
            answer = '$' + str(ans) + '$'
        else:
            bbase = random.randint(2, 10)
            pow = Fraction(random.randint(2, 5), 1)
            if random.randint(0, 3):
                bbase2 = random.randint(2, 4)
                bbase = bbase ** bbase2
                pow = Fraction(random.randint(1, bbase2-1), bbase2)
            while bbase**pow.DecValue() > 1000:
                pow = Fraction(random.randint(2, 5), 1)
            question = 'If log$_{' + str(bbase) + '}k = ' + str(pow) + '$ then $k = $'
            answer = '$' + str(bbase**pow.DecValue()) + '$'
            if pow.denominator == 1 and pow.numerator % 2 == 0 and random.randint(0, 2) < 2:
                question = "If log$_{" + str(bbase) + "}k = " + str(pow) + "$ then $\\sqrt{k} = $"
                answer = "$" + str((bbase ** pow.DecValue()) / 2) + "$"
    elif type == 2:
        bbase1 = random.randint(2, 10)
        pow = random.randint(1, 2) * 2
        pow2 = random.randint(1, 4)
        bbase2 = 2**pow2
        question = 'log$_{' + str(bbase2) + '}$(log$_{' + str(bbase1) + '}' + str(bbase1**pow) + '$)$ = $'
        ex1 = int(math.log(pow, 2))
        ans = Fraction(ex1, pow2)
        answer = '$' + str(ans) + '$'
    elif type == 3:
        if random.randint(0, 4) < 2:
            bbase = random.randint(2, 5)
            ans = random.randint(1, 3)
            fin = bbase**ans
            while fin > 100:
                bbase = random.randint(2, 5)
                ans = random.randint(1, 3)
                fin = bbase**ans
            if random.randint(0, 1):
                div = random.randint(2, 9)
                f = Fraction(fin, div)
                question = "log$_{" + str(bbase) + "}" + f.ToStringPossDec(.9) + " + $log$_{" + str(bbase) + "}" + str(div) + " = $"
                answer = '$' + str(ans) + '$'
                if random.randint(0, 2) == 0:
                    question = "log$_{" + str(bbase) + "}" + str(div * fin) + " - $log$_{" + str(bbase) + "}" + str(div) + " = $"
                    answer = '$' + str(ans) + '$'
            else:
                big = fin * random.randint(2, 20)
                while utility.isPrime[big / fin]:
                    big = fin * random.randint(2, 20)
                f = fraction.LessThan1Fraction(6, 6)
                num1 = fraction.Multiply(Fraction(big, 1), f)
                num2 = Fraction(f.denominator, f.numerator)
                num3 = Fraction(big / fin, 1)
                question = "log$_{" + str(bbase) + "}" + num1.ToStringPossDec(.9) + " - $log$_{" + str(bbase) + "}" + \
                            num3.ToStringPossDec(.9) + " + $log$_{" + str(bbase) + "}" + num2.ToStringPossDec(.9) + " = $"
                answer = "$" + str(ans) + "$"
                if random.randint(0, 1):
                    question = "log$_{" + str(bbase) + "}" + num2.ToStringPossDec(.9) + " + $log$_{" + str(bbase) + "}" + \
                                num1.ToStringPossDec(.9) + " - $log$_{" + str(bbase) + "}" + num3.ToStringPossDec(.9) + " = $"
        else:
            bbase = random.randint(2, 5)
            nums = [0] * random.randint(2, 3)
            for i in range(len(nums)):
                nums[i] = random.randint(1, 5)
            question = 'log$_{' + str(bbase) + '}' + str(bbase**nums[0])
            ans = Fraction(nums[0], 1)
            for i in range(1, len(nums)):
                if random.randint(0, 1):
                    question += ' \\times $log$_{' + str(bbase) + '}' + str(bbase**nums[i])
                    ans = fraction.Multiply(ans, Fraction(nums[i], 1))
                else:
                    question += ' \\div $log$_{' + str(bbase) + '}' + str(bbase ** nums[i])
                    ans = fraction.Divide(ans, Fraction(nums[i], 1))
            question += ' =$'
            answer = '$' + str(ans) + '$'
    elif type == 4:
        bbase = random.randint(2, 5)
        exp = bbase**random.randint(1, 3)
        l = Linear(random.randint(1, 4), random.randint(-5, 5))
        question = 'Find $f(' + str(exp) + ')$ if $f(x) = ' + str(l) + ' + $log$_{' + str(bbase) + '}x$'
        ans = l.Evaluate(exp) + int(math.log(exp, bbase))
        answer = '$' + str(ans) + '$'
        if random.randint(0, 1):
            question = "Find $f(" + str(exp) + ")$ if $f(x) = $log$_{" + str(bbase) + "}x + " + str(l) + "$"
    elif type == 5:
        rand = random.randint(0, 1)
        if rand == 0:
            bbase1 = random.randint(2, 10)
            bbase2 = random.randint(2, 10)
            question = "(log$_{" + str(bbase1) + "}" + str(bbase2) + "$)(log$_{" + str(bbase2) + "}" + str(bbase1) + "$)$ = $"
            answer = "$1$"
        elif rand == 1:
            bbase1 = random.randint(2, 4)
            pow1 = random.randint(2, 5)
            pow2 = random.randint(2, 5)
            question = 'log$_{' + str(bbase1**pow1) + '}' + str(bbase1**pow2) + ' = $'
            answer = '$' + str(Fraction(pow2, pow1)) + '$'
    return [question, answer, end]

def LiquidMeasurements(probNum):
    question, answer, end = '', '', ''
    if random.randint(0, 1):
        den = 3 if random.randint(0, 2) == 0 else (7 if random.randint(0, 1) else 11)
        f = Fraction(random.randint(1, den*2 - 1), den)
        question = '$' + str(f) + ('$ gallons ' if f.numerator > f.denominator else '$ of a gallon ') + ' equals'
        end = 'cubic inches'
        answer = '$' + str(Fraction(f.numerator*231, f.denominator)) + '$'
    else:
        type = ['ounce', 'cup', 'pint', 'quart', 'gallon']
        amounts = [1, 8, 16, 32, 128]
        fr = random.randint(0, 4)
        to = random.randint(0, 4)
        while fr == to:
            to = random.randint(0, 4)
        tempDen = 2**random.randint(1, 7)
        if (fr < to and random.randint(0, 3) == 0) or (fr > to and random.randint(0, 3) < 3):
            fromAmount = Fraction(random.randint(1, 20), 1)
        else:
            fromAmount = Fraction(random.randint(1, tempDen-1), tempDen)
        toAmount = fraction.Multiply(fromAmount, Fraction(amounts[fr], amounts[to]))
        question = '$' + str(fromAmount) + '$ ' + ((' of a ' + type[fr]) if fromAmount.numerator < fromAmount.denominator else (type[fr] + 's ')) + '$ =$'
        end = type[to] + 's'
        answer = '$' + str(toAmount) + '$'
    return [question, answer, end]

def GeometricFigures(probNum):
    question, answer, end = '', '', ''
    type = 0
    rand2 = random.randint(0, 11)
    if rand2 < 2: type = 0
    elif rand2 < 5: type = 1
    elif rand2 < 8: type = 2
    elif rand2 < 9: type = 3
    elif rand2 < 12: type = 5
    if type == 0:
        types = ['edge length', 'surface area', 'volume']
        edgeLength = random.randint(2, 12)
        vals = [edgeLength, edgeLength * edgeLength * 6, edgeLength**3]
        fr, to = random.randint(0, 2), random.randint(0, 2)
        while fr == to: fr = random.randint(0, 2)
        question = "The " + str(types[fr]) + " of a cube is $" + str(vals[fr]) + "$.  The " + str(types[to]) + " of the cube is"
        answer = "$" + str(vals[to]) + "$"
    elif type == 1:
        rand = random.randint(0, 3)
        if rand == 0:
            types = ['side length', 'height', 'perimeter', 'area']
            sideLength = Radical(random.randint(2, 10), 1, 3 if random.randint(0, 3) == 0 else 1)
            vals = [sideLength,
                    Radical(sideLength.co.numerator, sideLength.co.denominator * 2, sideLength.rad*3),
                    Radical(sideLength.co.numerator*3, sideLength.co.denominator, sideLength.rad),
                    Radical(sideLength.co.numerator*sideLength.co.numerator, sideLength.co.denominator*sideLength.co.denominator*4, sideLength.rad * sideLength.rad * 3)]
            fr, to = random.randint(0, 3), random.randint(0, 3)
            while fr == to: fr = random.randint(0, 3)
            question = "The " + types[fr] + " of an equilateral triangle is $" + str(vals[fr]) + "$ and its " + types[to] + " is "
            answer = "$" + str(vals[to]) + "$"
        elif rand == 1:
            side1 = random.randint(3, 6)
            side2 = random.randint(5, 12)
            if random.randint(0, 1):
                question = 'An acute triangle has integer side lengths of $' + str(side1) + '$, $' + str(side2) + '$, and $x$.  The largest value of $x$ is'
                ans = 50
                while (ans**2 + side1**2 <= side2**2) or (ans**2 + side2**2 <= side1**2) or (side1**2 + side2**2 <= ans**2) or \
                      (side1 + side2 <= ans) or (side1 + ans <= side2) or (side2 + ans <= side1):
                    ans -= 1
                answer = '$' + str(ans) + '$'
            else:
                question = 'An acute triangle has integer side lengths of $' + str(side1) + '$, $' + str(side2) + '$, and $x$.  The smallest value of $x$ is'
                ans = 0
                while (ans**2 + side1**2 <= side2**2) or (ans**2 + side2**2 <= side1**2) or (side1**2 + side2**2 <= ans**2) or \
                      (side1 + side2 <= ans) or (side1 + ans <= side2) or (side2 + ans <= side1):
                    ans += 1
                answer = '$' + str(ans) + '$'
        elif rand == 2:
            side1 = random.randint(3, 6)
            side2 = random.randint(5, 12)
            if random.randint(0, 1):
                question = "An obtuse triangle has integer side lengths of $" + str(side1) + "$, $" + str(side2) + "$, and $x$.  The largest value of $x$ is"
                ans = 50
                while not ((ans * ans + side1 * side1 <= side2 * side2) or (ans * ans + side2 * side2 <= side1 * side1) or (side1 * side1 + side2 * side2 <= ans * ans)) or (side1 + side2 <= ans) or (side1 + ans <= side2) or (side2 + ans <= side1):
                    ans -= 1
                answer = "$" + str(ans) + "$"
            else:
                question = "An obtuse triangle has integer side lengths of $" + str(side1) + "$, $" + str(side2) + "$, and $x$.  The smallest value of $x$ is"
                ans = 1
                while not ((ans * ans + side1 * side1 <= side2 * side2) or (ans * ans + side2 * side2 <= side1 * side1) or (side1 * side1 + side2 * side2 <= ans * ans)) or (side1 + side2 <= ans) or (side1 + ans <= side2) or (side2 + ans <= side1):
                    ans+=1
                answer = '$' + str(ans) + '$'
        else:
            side1 = random.randint(1, 99)
            side2 = random.randint(1, 99)
            if random.randint(0, 1):
                question = "A triangle has integer side lengths of $" + str(side1) + "$, $" + str(side2) + "$, and $x$.  The largest value of $x$ is"
                ans = side1 + side2 - 1
                answer = "$" + str(ans) + "$"
            else:
                question = "A triangle has integer side lengths of $" + str(side1) + "$, $" + str(side2) + "$, and $x$.  The smallest value of $x$ is"
                ans = abs(side2 - side1) + 1
                answer = "$" + str(ans) + "$"
    elif type == 2:
        types = ['side length', 'diagonal', 'perimeter', 'area']
        sideLength = Radical(random.randint(2, 12), 1, 1)
        if random.randint(0, 3) == 0: sideLength.co.denominator = random.randint(2, 14)
        if random.randint(0, 2) == 0: sideLength.rad = random.randint(2, 3)
        vals = [sideLength,
                Radical(sideLength.co.numerator, sideLength.co.denominator, sideLength.rad*2),
                Radical(sideLength.co.numerator*4, sideLength.co.denominator, sideLength.rad),
                Radical(sideLength.co.numerator*sideLength.co.numerator, sideLength.co.denominator**2, sideLength.rad**2)]
        
        fr, to = random.randint(0, 3), random.randint(0, 3)
        while fr == to: to = random.randint(0, 3)
        question = "The " + types[fr] + " of a square is $" + str(vals[fr]) + "$ and the " + str(types[to]) + " is"
        answer = "$" + str(vals[to]) + "$"
    elif type == 3:
        ratio = Fraction(random.randint(1, 12), random.randint(1, 12))
        firstSide = ratio.numerator * random.randint(2, 5)
        secondSide = ratio.denominator * firstSide / ratio.numerator
        question = "A rectangle's sides are in the ratio $" + str(ratio.numerator) + "$:$" + str(ratio.denominator) + "$." 
        if random.randint(0, 1):
            question += "  If its shorter side is $" + str(firstSide if firstSide < secondSide else secondSide) + '$ then its longer side is'
            answer = '$' + str(firstSide if firstSide > secondSide else secondSide) + '$'
        else:
            question += '  If its longer side is $' + str(firstSide if firstSide > secondSide else secondSide) + '$ then its shorter side is'
            answer = '$' + str(firstSide if firstSide < secondSide else secondSide) + '$'
    elif type == 4:
        h = random.randint(-4, 4)
        k = random.randint(-4, 4)
        if random.randint(0, 1): h = 0
        if random.randint(0, 1): k = 0
        radius = random.randint(2, 6)
        question = 'x^2 ' + ('' if h == 0 else ((' - ' if h < 0 else ' + ') + str(abs(2*h)) + 'x ')) + \
                   ' + y^2 ' + ('' if k == 0 else ((' - ' if k < 0 else ' + ') + str(abs(2*k)) + 'y ')) + ' = ' + str(radius**2 - h**2 - k**2)
        rand = random.randint(0, 2)
        if rand == 0:
            question = "The circle $" + str(equation) + "$ has a center at $(h, k)$ and $h = $"
            answer = "$" + str(-h) + "$"  
        elif rand == 1:
            question = "The circle $" + str(equation) + "$ has a center at $(h, k)$ and $k = $"
            answer = "$" + str(-k) + "$"
        else:
            question = "The circle $" + str(equation) + "$ has a radius of"
            answer = "$" + str(radius) + "$"
    elif type == 5:
        dtypes = ['pentahedron', 'heptahedron', 'nonahedron', 'decahedron', 'dodecahedron', 'icosahedron']
        types = ['pentagon', 'heptagon', 'nonagon', 'decagon', 'dodecagon', 'icosagon']
        vals = [5, 7, 9, 10, 12, 20]
        ttype = random.randint(0, len(dtypes)-1)
        if random.randint(0, 1):
            question = 'A ' + dtypes[ttype] + ' has'
            end = 'faces'
        else:
            question = 'A ' + types[ttype] + ' has'
            end = 'sides'
        answer = '$' + str(vals[ttype]) + '$'
    return [question, answer, end]

def OddsProb(probNum):
    question, answer, end = '', '', ''
    type = 4
    rand3 = random.randint(0, 12)
    if rand3 < 4: type = 0
    elif rand3 < 5: type = 1
    elif rand3 < 10: type = 2
    elif rand3 < 12: type = 3
    elif rand3 < 13: type = 4
    if type == 0:
        numDice = random.randint(1, 3)
        if numDice == 1:
            question = 'A die is rolled. '
            num = random.randint(2, 16)
            tot = 0
            for i in range(1, 7):
                if num % i == 0:
                    tot += 1
            if random.randint(0, 1):
                question += 'What is the probability that a factor of $' + str(num) + '$ is showing?'
                answer = '$' + str(Fraction(tot, 6)) + '$'
            else:
                question += 'What are the odds that a factor of $' + str(num) + '$ is showing?'
                answer = '$' + str(Fraction(tot, 6 - tot)) + '$'
        elif numDice == 2:
            question = 'A pair of dice is tossed. '
            freq = [0] * 13
            for i in range(1, 7):
                for j in range(1, 7):
                    freq[i+j]+=1
            rand = random.randint(0, 1)
            if rand == 0:
                num = random.randint(2, 6)
                tot = 0
                for i in range(num, 13, num):
                    tot += freq[i]
                if random.randint(0, 1):
                    question += 'What is the probability that the sum is a multiple of $' + str(num) + '$?'
                    answer += '$' + str(Fraction(tot, 36)) + '$'
                else:
                    question += 'What are the odds that the sum is a multiple of $' + str(num) + '$?'
                    answer = '$' + str(Fraction(tot, 36 - tot)) + '$'
            elif rand == 1:
                num = random.randint(1, 12)
                tot = freq[num]
                if random.randint(0, 1):
                    question += 'What is the probability that the sum is $' + str(num) + '$?'
                    answer = '$' + str(Fraction(tot, 36)) + '$'
                else:
                    question += 'What are the odds that the sum is $' + str(num) + '$?'
                    answer = '$' + str(Fraction(tot, 36-tot)) + '$'
        elif numDice == 3:
            question = 'Three dice are tossed. '
            num = random.randint(1, 6)
            types = ['', 'ones', 'twos', 'threes', 'fours', 'fives', 'sixes']
            if random.randint(0, 1):
                question += 'What is the probability of getting three $' + types[num] + '$?'
                answer = '$' + str(Fraction(1, 216)) + '$'
            else:
                question += 'What are the odds of getting three $' + str(types[num]) + '$?'
                answer = '$' + str(Fraction(1, 215)) + '$'
    elif type == 1:
        numCoins = random.randint(2, 3)
        if numCoins == 2: question = 'Two coins are tossed. '
        else: question = 'Three coins are tossed. '
        if random.randint(0, 1):
            question += 'Find the probability of getting $' + str(numCoins) + '$ tails.'
            answer = '$' + str(Fraction(1, 2**numCoins)) + '$'
        else:
            question += 'Find the odds of getting $' + str(numCoins) + '$ tails.'
            answer = '$' + str(Fraction(1, 2**numCoins-1)) + '$'
    elif type == 2:
        typeA = ['winning', 'success', 'fun']
        typeB = ['losing', 'failure', 'no fun']
        prob = fraction.LessThan1Fraction(21, 21)
        probComp = Fraction(prob.denominator - prob.numerator, prob.denominator)
        odds = Fraction(prob.numerator, prob.denominator - prob.numerator)
        oddsComp = Fraction(probComp.numerator, probComp.denominator - probComp.numerator)
        ttype = random.randint(0, len(typeA)-1)
        rr = random.randint(0, 1)
        insert1, insert2 = '', ''
        if rr == 0:
            insert1 = typeA[ttype]
            insert2 = typeB[ttype]
        else:
            insert1 = typeB[ttype]
            insert2 = typeA[ttype]
        rrand = random.randint(0, 1)
        if rrand == 0:
            question = 'The odds of ' + insert1 + ' is $' + (odds.ToStringPossDec(1) if random.randint(0, 1) else (odds.ToPercent() if random.randint(0, 3) == 0 else str(odds))) + '$. The odds of ' + insert2 + ' is'       
            answer = '$' + str(oddsComp) + '$'
        elif rrand == 1:
            question = 'The probability of ' + insert1 + ' is $' + (prob.ToStringPossDec(1) if random.randint(0, 1) else (prob.ToPercent() if random.randint(0, 3) == 0 else str(prob))) + '$. The probability of ' + insert2 + ' is'
            answer = '$' + str(probComp) + '$'
        elif rrand == 2:
            question = 'The odds of ' + insert1 + ' is $' + (odds.ToStringPossDec(1) if random.randint(0, 1) else (odds.ToPercent() if random.randint(0, 3) == 0 else str(odds))) + '$. The probability of ' + insert2 + ' is'
            answer = '$' + str(probComp) + '$'
        else:
            question = 'The probability of ' + insert1 + ' is $' + (prob.ToStringPossDec(1) if random.randint(0, 1) else (prob.ToPercent() if random.randint(0, 3) == 0 else str(prob))) + '$. The odds of ' + insert2 + ' is'
            answer = '$' + str(oddsComp) + '$'
    elif type == 3:
        bagTypes = ['bag', 'bowl', 'hat', 'bucket']
        ballTypes = ['balls', 'marbles', 'cards', 'ribbons']
        numBlue = random.randint(1, 12)
        numRed = random.randint(1, 12)
        numWhite = random.randint(1, 12)
        question = 'A ' + bagTypes[random.randint(0, len(bagTypes) - 1)] + ' has $' + str(numBlue) + '$ blue, $' + str(numRed) + '$ red, and $' + str(numWhite) + '$ white ' + ballTypes[random.randint(0, len(ballTypes)-1)] + '. '
        rrand = random.randint(0, 2)
        if rrand == 0:
            if random.randint(0, 1):
                question += 'What is the probability of drawing a blue one?'
                answer = '$' + str(Fraction(numBlue, numBlue + numRed + numWhite)) + '$'
            else:
                question += 'What are the odds of drawing a blue one?'
                answer = '$' + str(Fraction(numBlue, numRed + numWhite)) + '$'
        elif rrand == 1:
            if random.randint(0, 1):
                question += 'What is the probability of drawing a red one?'
                answer = '$' + str(Fraction(numRed, numBlue + numRed + numWhite)) + '$'
            else:
                question += 'What is the probability of drawing a red one?'
                answer = '$' + str(Fraction(numRed, numBlue + numWhite)) + '$'
        else:
            if random.randint(0, 1):
                question += 'What is the probability of drawing a white one?'
                answer = '$' + str(Fraction(numWhite, numBlue + numRed + numWhite)) + '$'
            else:
                question += 'What are the odds of drawing a white one?'
                answer = '$' + str(Fraction(numWhite, numRed + numBlue)) + '$'
    elif type == 4:
        words = ['BANANA', 'MATHEMATICS', 'MENTAL MATH', 'BIGGER IN TEXAS', 'FOOTBALL', 'CROSS COUNTRY']
        word = words[random.randint(0, len(words)-1)]
        c = word[random.randint(0, len(word)-1)]
        while c == ' ':
            c = word[random.randint(0, len(word)-1)]
        numberSpaces, numberChar = 0, 0
        for i in range(len(word)):
            if word[i] == ' ': numberSpaces += 1
            if word[i] == c: numberChar += 1
        if random.randint(0, 1):
            question = 'If all the letters of "' + str(word) + '" are put in a bag.  What is the probability of drawing out a "' + str(c) + '"'
            answer = '$' + str(Fraction(numberChar, len(word) - numberSpaces)) + '$'
        else:
            question = 'If all the letters of "' + str(word) + '" are put into a bag.  What are the odds of drawing out a "' + str(c) + '"'
            answer = '$' + str(Fraction(numberChar, len(word) - numberSpaces - numberChar)) + '$'
    return [question, answer, end]

def RandomOperations(probNum):
    question, answer, end ='', '', ''
    type = -1
    rand2 = random.randint(0, 19)
    if rand2 < 6: type = 0
    elif rand2 < 7: type = 1
    elif rand2 < 8: type = 2
    elif rand2 < 12: type = 3
    elif rand2 < 20: type = 4
    if type == 0:
        num1, num2 = 0, 0
        if random.randint(0, 1):
            num1, num2 = random.randint(100, 999), random.randint(100, 999)
        else:
            num1, num2 = random.randint(1000, 9999), random.randint(1000, 9999)
        if random.randint(0, 2) == 0:
            num1 = random.randint(100, 999)
        if random.randint(0, 1):
            temp = num1
            num1 = num2
            num2 = temp
        dnum1, dnum2 = -1.0, -1.0
        if random.randint(0, 5) == 0:
            dnum1 = utility.Decimalize(num1)
            dnum2 = utility.Decimalize(num2)
        if random.randint(0, 4) < 2:
            if random.randint(0, 2) == 0:
                question = '$' + str((num1 if num1 > num2 else num2) if dnum1 == -1 else (dnum1 if dnum1 > dnum2 else dnum2)) + ' - ' + str((num1 if num1 < num2 else num2) if dnum1 == -1 else (dnum1 if dnum1 < dnum2 else dnum2)) + ' = $'
                answer = '$' + str(abs(num1-num2) if dnum1 == -1 else abs(dnum1-dnum2)) + '$'
            else:
                question = '$' + str(num1 if dnum1 == -1 else dnum1) + ' - '+ str(num2 if dnum1 == -1 else dnum2) + ' = $'
                answer = '$' + str((num1-num2) if dnum1 == -1 else (dnum1 - dnum2)) + '$'
        else:
            question = '$' + str(num1 if dnum1 == -1 else dnum1) + ' + ' + str(num2 if dnum2 == -1 else dnum2)  + ' = $'
            answer = '$' + str((num1 + num2) if dnum1 == -1 else (dnum1 + dnum2)) + '$'
    elif type == 1:
        year = datetime.datetime.now().year
        if random.randint(0, 1):
            times = random.randint(2, 20)
            if random.randint(0, 2) == 0:
                temp = year
                year = times
                times = temp
            question = '$' + str(year) + ' \\times ' + str(times) + ' = $'
            answer = '$' + str(year * times) + '$'
        else:
            big = random.randint(100, 999) if random.randint(0, 1) else random.randint(1000, 9999)
            small = random.randint(2, 9)
            if random.randint(0, 1):
                temp = big
                big = small
                small = temp
            question = '$' + str(big) + ' \\times ' + str(small) + ' = $'
            answer = '$' + str(big * small) + '$'
    elif type == 2:
        terms = [0] * random.randint(3,5)
        ans = 1
        for i in range(len(terms)):
            while terms[i] == 0:
                terms[i] = random.randint(-10, 9)
            ans *= terms[i]
        question = '$' + str(terms[0])
        for i in range(1, len(terms)):
            question += ' \\times ' + ('(' if terms[i] < 0 else '') + str(terms[i]) + (')' if terms[i] < 0 else '')
        question += ' = $'
        answer = '$' + str(ans) + '$'
    elif type == 3:
        terms = [0] * (4 if random.randint(0, 4) == 0 else 3)
        rand = random.randint(0, 3)
        if rand == 0:
            for i in range(len(terms)):
                terms[i] = random.randint(100, 999)
        elif rand == 1:
            for i in range(len(terms)):
                terms[i] = random.randint(1000, 9999)
        elif rand == 2:
            for i in range(len(terms)):
                terms[i] = random.randint(100, 999) if random.randint(0, 1) else random.randint(1000, 9999)
        else:
            for i in range(len(terms)):
                terms[i] = random.randint(10, 99)
        if random.randint(0, 4) == 0:
            terms[0] *= -1
        for i in range(1, len(terms)-1):
            if random.randint(0, 1):
                terms[i] *= -1
        question = '$' + str(terms[0])
        for i in range(1, len(terms)-1):
            question += (' - ' if terms[i] < 0 else ' + ') + str(abs(terms[i]))
        question += ' = $'
        ans = 0
        for t in terms:
            ans += t
        answer = '$' + str(ans) + '$'
    elif type == 4:
        numTerms = random.randint(2, 3)
        terms = [''] * numTerms
        termVals = [None] * numTerms
        
        for i in range(numTerms):
            pType = random.randint(0, 6)
            if pType == 0:
                val = random.randint(1, 10)
                if random.randint(0, 1): val = 5 * random.randint(1, 2)
                if random.randint(0, 2) < 2: val += random.randint(1, 4)
                terms[i] = str(val)
                termVals[i] = Fraction(val, 1)
            elif pType == 1:
                val = random.randint(10, 99)
                if random.randint(0, 1): val = 10 * random.randint(1, 10) 
                if random.randint(0, 2) < 2: val += random.randint(1, 4)
                terms[i] = str(val)
                termVals[i] = Fraction(val, 1)
            elif pType == 2:
                val = random.randint(100, 2999)
                if random.randint(0, 1): val = 100 * random.randint(1, 29)
                if random.randint(0, 2) < 2: val += random.randint(1, 4)
                terms[i] = str(val)
                termVals[i] = Fraction(val, 1)
            elif pType == 3:
                val1, val2 = random.randint(1, 9), random.randint(1, 9)
                terms[i] = str(val1) + ' \\times ' + str(val2)
                termVals[i] = Fraction(val1*val2, 1)
            elif pType == 4:
                val1, val2 = random.randint(1, 9), random.randint(1, 9)
                terms[i] = str(val1) + ' \\div ' + str(val2)
                termVals[i] = Fraction(val1, val2)
            elif pType == 5:
                val1, val2 = random.randint(1, 29), random.randint(1, 9)
                tot = val1 * val2
                while tot == 1:
                    val1, val2 = random.randint(1, 29), random.randint(1, 9)
                    tot = val1 * val2
                temp = utility.Factors(tot)
                den = temp[random.randint(0, len(temp)-1)]
                while den == 1:
                    den = temp[random.randint(0, len(temp)-1)]
                termVals[i] = Fraction(tot, den)
                if random.randint(0, 1): terms[i] = str(val1) + ' \\times ' + str(val2) + ' \\div ' + str(den)
                else: terms[i] = str(val2) + ' \\div ' + str(den) + ' \\times ' + str(val1)
            elif pType == 6:
                val1 = random.randint(1, 32)
                temp = utility.Factors(val1)
                while len(temp) <=2:
                    val1 = random.randint(1, 32)
                    temp = utility.Factors(val1)
                val2 = temp[random.randint(0, len(temp)-1)]
                terms[i] = str(val1) + ' \\div ' + str(val2)
                termVals[i] = Fraction(val1, val2)
        question = '$' + str(terms[0])
        ans = termVals[0]
        for i in range(1, len(terms)):
            if random.randint(0, 1):
                question += ' - '
                ans = fraction.Subtract(ans, termVals[i])
            else:
                question += ' + '
                ans = fraction.Add(ans, termVals[i])
            question += str(terms[i])
        question += ' = $'
        answer = '$' + ans.ToStringAns() + '$'
    return [question, answer, end]

def VariousWordProblems(probNum):
    question, answer, end = '', '', ''
    type = random.randint(0, 2)
    if type == 0:
        rand = random.randint(0, 2)
        type2 = -1
        if rand == 0: type2 = 0
        elif rand < 3: type2 = 1
        if type2 == 0:
            cost = 100 * random.randint(1, 30)
            perc = random.randint(2, 10)
            numMonths = random.randint(1, 18)
            question = 'The simple interest on $\\$' + str(cost) + '$ at $' + str(perc) + '\\%$ for $' + str(numMonths) + '$ months is $\\$$'
            ans = Fraction(cost / 100 * perc * numMonths, 12)
            answer = '$' + ans.ToStringAns() + '$'
        elif type2 == 1:
            noun = utility.singNouns[random.randint(0, len(utility.singNouns)-1)]
            frac = Fraction(1, 1)
            if random.randint(0, 1):
                frac = Fraction(random.randint(2, 15), 100)
            else:
                den = utility.rationalDen()
                frac = Fraction(random.randint(1, den-1), den)
                if random.randint(0, 2) < 2: frac.numerator = 1
            ins = str(Fraction(frac.numerator * 100, frac.denominator).ToMixedNumber())
            if frac.canBeDecimal() and random.randint(0, 1):
                ins = str(Fraction(frac.numerator * 100, frac.denominator).DecValue())
            price = random.randint(1, 9) * 10
            if random.randint(0, 1):
                price = random.randint(1, 10)
            x = str(fraction.Multiply(frac, Fraction(price, 1)).DecValue())
            if x.find('.') == -1:
                x += '.'
            while len(x[x.find('.'):]) > 3:
                price = random.randint(1, 9) * 10
                if random.randint(0, 1):
                    price = random.randint(1, 10)
                x = str(fraction.Multiply(frac, Fraction(price, 1)).DecValue())
                if x.find('.') == -1:
                    x += '.'
            sPrice = str(price) + '.00'
            if random.randint(0, 2) == 0:
                question = 'A ' + noun + ' sells for $\\$' + sPrice + '$ plus $' + ins + '\\%$ tax.  The total cost of the ' + noun + ' is $\\$$'
                ans = price + fraction.Multiply(frac, Fraction(price, 1)).DecValue()
                sAns = str(ans)
                if sAns.find('.') == -1: sAns += '.'
                while len(sAns[sAns.find('.'):]) < 3:
                    sAns += '0'
                answer = '$' + sAns + '$'
            else:
                ans = fraction.Multiply(frac, Fraction(price, 1)).DecValue()
                sAns = str(ans)
                if sAns.find('.') == -1: sAns += '.'
                while len(sAns[sAns.find('.'):]) < 3:
                    sAns += '0'
                question = 'The $' + ins + '\\%$ sales tax on an item is $\\$' + sAns + '$.  What is the price of the item before sales tax? $\\$$'
                answer = '$' + sPrice + '$'
    elif type == 1:
        while True:
            val = random.randint(2, 9)
            num = random.randint(100, 999)
            if random.randint(0, 2) == 0: num = random.randint(1000, 9999)
            if random.randint(0, 3) == 0: num = random.randint(10000, 99999)
            place = random.randint(0, len(str(num))-1)
            temp = str(num)
            sNum = temp[0:place] + 'k' + temp[place+1:]
            canCon = False
            for i in range(10):
                div = 10 ** (len(temp) - place - 1)
                newNum = num / (div * 10) * (div * 10) + i * div + num%div
                if (newNum % val == 0):
                    canCon = True
            if not canCon: continue
            if random.randint(0, 1):
                question = 'Find the smallest $k, 0<=k<=9$ such that $' + str(sNum) + '$ is divisible by $' + str(val) + '$.'
                for i in range(10):
                    div = 10 ** (len(temp) - place - 1)
                    newNum = num / (div * 10) * (div * 10) + i*div + num%div
                    if newNum % val == 0: break
                if place == 0 and i == 0:
                    return VariousWordProblems(probNum)
                answer = '$' + str(i) + '$'
                break
            else:
                question = 'Find the largest $k, 0<=k<=9$ such that $' + str(sNum) + '$ is divisible by $' + str(val) + '$.'
                for i in range(9, -1, -1):
                    div = 10 ** (len(temp) - place - 1)
                    newNum = num / (div * 10) * (div * 10) + i*div + num%div
                    if newNum %val == 0:
                        break
                if place == 0 and i == 0:
                    return VariousWordProblems(probNum)
                answer = '$' + str(i) + '$'
                break
    elif type == 2:
        type2 = random.randint(0, 2)
        if type2 == 0:
            while True:
                num1, num2 = random.randint(-10, 10), random.randint(-10, 10)
                tryAgain = False
                for i in range(-100, 100):
                    for j in range(-100, 100):
                        if i + j == num1 + num2 and i * j == num1 * num2 and not ((i == num1 and j == num2) or (i == num2 and j == num1)):
                            tryAgain = True
                if tryAgain:
                    continue
                if random.randint(0, 1):
                    question = 'The smaller of two numbers whose sum is $' + str(num1 + num2) + '$ and whose product is $' + str(num1 * num2) + '$ is'
                    answer = '$' + str(num1 if num1 < num2 else num2) + '$'
                else:
                    question = 'The larger of two numbers whose sum is $' + str(num1 + num2) + '$ and whose product is $' + str(num1 * num2) + '$ is'
                    answer = '$' + str(num1 if num1 > num2 else num2) + '$'
                break
        elif type2 == 1:
            x1 = random.randint(1, 12)
            y1 = random.randint(1, 12)
            x2 = random.randint(1, 12)
            y2 = random.randint(1, 12)
            while x1 == x2:
                x1 = random.randint(1, 12)
                x2 = random.randint(1, 12)
            while y1 == y2:
                y1 = random.randint(1, 12)
                y2 = random.randint(1, 12)
            if random.randint(0, 1):
                question = "If $x$ and $y$ vary directly and $x = " + str(x1) + "$ when $y = " + str(y1) + "$, find $x$ when $y = " + str(y2) + "$"
                ans = Fraction(x1 * y2, y1)
                answer = "$" + ans.ToStringAns() + "$"
            else:
                question = "If $x$ and $y$ vary inversely and $x = " + str(x1) + "$ when $y = " + str(y1) + "$, find $x$ when $y = " + str(y2) + "$"
                ans = Fraction(x1 * y1, y2)
                answer = "$" + ans.ToStringAns() + "$"
        elif type2 == 2:
            words = ['MATH', 'NUMBER', 'FOUR', 'FIVE', 'NEWTON', 'TRIANGLE', 'SQUARE', 'CUBE', 'SHAPE', 'THEORY']
            ins = words[random.randint(0, len(words)-1)]
            question = 'The number of elements in the power set of $\\{'
            question += ins[0]
            for i in range(1, len(ins)):
                question += ',' + ins[i]
            question += '\\}$ is'
            answer = '$' + str(2**len(ins)) + '$'
    return [question, answer ,end]

def SinCosTan(probNum):
    question, answer, end = '', '', ''
    type = 0
    rrandmy = random.randint(0, 9)
    if rrandmy < 4: type = 0
    elif rrandmy < 5: type = 1
    elif rrandmy < 6: type = 2
    elif rrandmy < 7: type = 3
    else: type = 4
    if type == 0:
        frac = utility.goodTrigFrac()
        ins = ''
        if random.randint(0, 4) < 3:
            ins = str(trig.radToDeg(frac)) + '^\\circ'
        else:
            ins = frac.ToStringAddNum('\\pi')
        while True:
            type2 = random.randint(0, 11)
            if type2 < 3:
                question = '$\\sin ' + ins
                ans = trig.sin(trig.radToDeg(frac))
                if ans.co.denominator == 0: continue
                answer = '$' + str(ans) + '$'
                break
            elif type2 < 6:
                question = '$\\cos ' + ins
                ans = trig.cos(trig.radToDeg(frac))
                if ans.co.denominator == 0: continue
                answer = '$' + str(ans) + '$'
                break
            elif type2 < 9:
                question = '$\\tan ' + ins
                ans = trig.tan(trig.radToDeg(frac))
                if ans.co.denominator == 0: continue
                answer = '$' + str(ans) + '$'
                break
            elif type2 < 11:
                question = '$\\sec ' + ins
                ans = trig.sec(trig.radToDeg(frac))
                if ans.co.denominator == 0: continue
                answer = '$' + str(ans) + '$'
                break
            elif type2 < 12:
                question = '$\\cot ' + ins
                ans = trig.cot(trig.radToDeg(frac))
                if ans.co.denominator == 0: continue
                answer = '$' + str(ans) + '$'
                break
        if random.randint(0, 8):
            question = '(' + question + '$)$^2 =$'
            ans = radical.Multiply(ans, ans)
            answer = '$' + str(ans) + '$'
        else:
            question = question + ' =$'
            answer = '$' + str(ans) + '$'
    elif type == 1:
        trigCo = random.randint(-3, 3)
        while trigCo == 0: trigCo = random.randint(-4, 4)
        xCo = random.randint(1, 4)
        cons = random.randint(-9, 11)
        sin = random.randint(0, 1) == 0
        tRig = ('' if abs(trigCo) == 1 else str(abs(trigCo))) + ('\\sin{' if sin else '\\cos{') + ('' if xCo == 1 else str(xCo)) + 'x}'
        if random.randint(0, 1):
            if cons != 0: question = str(cons) + ' ' + ('-' if trigCo < 0 else '+') + ' ' + tRig
            else: question = ('-' if trigCo < 0 else '') + tRig
        else:
            if cons != 0: question = ('-' if trigCo < 0 else '') + tRig + (' - ' if cons < 0 else ' + ') + str(abs(cons))
            else: question = ('-' if trigCo < 0 else '') + tRig
        minum = random.randint(0, 6) < 3
        if minum:
            question = 'The minimum value of $' + question + '$ is'
            answer = '$' + str(cons - abs(trigCo)) + '$'
        if not minum:
            question = 'The maximum value of $' + question + '$ is'
            answer = '$' + str(cons + abs(trigCo)) + '$'
    elif type == 2:
        cons = random.randint(-7, 7)
        trigCo = random.randint(-4, 4)
        while trigCo == 0: trigCo = random.randint(-4, 4)
        xCo = random.randint(1, 5)
        xCons = random.randint(-6, 6)
        sin = random.randint(0, 1) == 0
        tRig = ('' if cons == 0 else str(cons)) + (' - ' if trigCo < 0 else ' + ') + \
               ('' if abs(trigCo) == 1 else str(abs(trigCo))) + \
               ('\\sin{' if sin else '\\cos{') + '(' + ('' if xCo == 1 else str(xCo)) + 'x' + \
               ('' if xCons == 0 else (' - ' if xCons < 0 else ' + ')) + str(abs(xCons)) + ')}'
        question = 'The graph of $y = '+ tRig + '$ has '
        ttype = random.randint(0, 3)
        if ttype == 0:
            question += 'a vertical ' + ('displacement' if random.randint(0, 1) else 'shift') + ' of'
            answer = '$' + str(cons) + '$'
        elif ttype == 1:
            question += 'a horizontal ' + ('displacement' if random.randint(0, 1) else 'shift') + ' of'
            frac = Fraction(-xCons, xCo)
            answer = '$' + frac.ToStringAns() + '$'
        elif ttype == 2:
            question += 'an amplitude of'
            answer = '$' + str(abs(trigCo)) + '$'
        else:
            question += 'a ' + ('wavelength' if random.randint(0, 1) else 'period') + ' of'
            frac = Fraction(2, abs(xCo))
            answer = '$' + frac.ToStringAddNum('\\pi') + '$'
    elif type == 3:
        while True:
            frac1 = utility.goodTrigFrac()
            frac2 = utility.goodTrigFrac()
            rrand2 = random.randint(0, 4)
            sin1 = random.randint(0, 1) == 0
            sin2 = random.randint(0, 1) == 0
            deg1 = trig.radToDeg(frac1)
            deg2 = trig.radToDeg(frac2)
            if rrand2 < 2:
                question = '$' + ('\\sin{' if sin1 else '\\cos{') + frac1.ToStringAddNum('\\pi') + '} \\times ' + \
                           ('\\sin{' if sin1 else '\\cos{') + frac2.ToStringAddNum('\\pi') + '} =$'
            elif rrand2 < 4:
                question = '$' + ('\\sin{' if sin1 else '\\cos{') + str(deg1) + '^\\circ} \\times ' + \
                           ('\\sin{' if sin1 else '\\cos{') + str(deg2) + '^\\circ} =$'
            else:
                question = '$' + ('\\sin{' if sin1 else '\\cos{') + frac1.ToStringAddNum('\\pi') + '} \\times ' + \
                           ('\\sin{' if sin1 else '\\cos{') + str(deg2) + '^\\circ} =$'
            ans1 = radical.Multiply((trig.sin(deg1) if sin1 else trig.cos(deg1)), trig.sin(deg2) if sin2 else trig.cos(deg2))
            if not (str(ans1) == '0' and random.randint(0, 4) < 4):
                break
        answer = '$' + str(ans1) + '$'
    elif type == 4:
        if random.randint(0, 1):
            f = utility.goodTrigFrac()
            ins = ''
            if random.randint(0, 1):
                ins = '\\cos{' + f.ToStringAddNum('\\pi') + '}'
                if random.randint(0, 1):
                    ins = '\\cos{' + str(trig.radToDeg(f)) + '^\\circ}'
                val = trig.cos(trig.radToDeg(f))
            else:
                ins = '\\sin{' + f.ToStringAddNum('\\pi') + '}'
                if random.randint(0, 1):
                    ins = '\\sin{' + str(trig.radToDeg(f)) + '^\\circ}'
                val = trig.sin(trig.radToDeg(f))
            if random.randint(0, 1):
                question = 'Arccos($' + ins + '$)$ =$'
                answer = '$' + str(trig.arccos(val)) + '$'
                end = '$^\\circ$'
                if random.randint(0, 1):
                    answer = '$' + trig.degToRad(trig.arccos(val)).ToStringAddNum('\\pi') + '$'
                    end = 'radians'
            else:
                question = 'Arcsin($' + ins + '$)$ =$'
                answer = '$' + str(trig.arcsin(val)) + '$'
                end = '$^\\circ$'
                if random.randint(0, 1):
                    answer = '$' + trig.degToRad(trig.arcsin(val)).ToStringAddNum('\\pi') + '$'
                    end = 'radians'
        else:
            rads = [Radical(-1, 1, 1), Radical(-1, 2, 3), Radical(-1, 2, 2), Radical(-1, 2, 1), \
                    Radical(0, 1, 1), Radical(1, 2, 1), Radical(1, 2, 2), Radical(1, 2, 3), \
                    Radical(1, 1, 1)]
            useRad = rads[random.randint(0, len(rads)-1)]
            ins = ''
            val = -1
            if random.randint(0, 1):
                ins = 'sin^{-1} ' + useRad.ToStringNoDisp()
                val = trig.arcsin(useRad)
            else:
                ins = 'cos^{-1} ' + useRad.ToStringNoDisp()
                val = trig.arccos(useRad)
            if random.randint(0, 1):
                question = '$\\sin{(' + ins + ')}$'
                answer = '$' + str(trig.sin(val)) + '$'
            else:
                question = '$\\cos{(' + ins + ')}$'
                answer = '$' + str(trig.cos(val)) + '$'
    elif type == 5:
        rrand = random.randint(0, 3)
        if rrand == 0:
            ttype = random.randint(0, 2)
            ins = ''
            if ttype == 1:
                deg = random.randint(0, 720)
                if random.randint(0, 2) < 2:
                    deg = trig.radToDeg(utility.goodTrigFrac())
                ins = str(deg) + '^\\circ'
            elif ttype == 0:
                ins = utility.goodTrigFrac().ToStringAddNum('\\pi')
            elif ttype == 2:
                lin = Linear(random.randint(-5, 5), random.randint(-5, 5))
                if random.randint(0, 2) < 2:
                    lin.B = 0
                ins = str(lin)
            question = '$sin^2 ' + ins + ' + cos^2 ' + ins + '$'
            answer = '$1$'
        elif rrand == 1:
            ins1, ins2, = '', ''
            f = utility.goodTrigFrac()
            while f.numerator == 0:
                f = utility.goodTrigFrac()
            dig = trig.radToDeg(f)
            if random.randint(0, 2) < 2:
                if deg < 0: small = -random.randint(0, -deg - 1)
                else: small = random.randint(0, deg-1)
                big = deg - small
                ins1 = str(small)
                ins2 = str(big)
                frac1 = trig.degToRad(small)
                frac2 = trig.degToRad(big)
            else:
                multby = random.randint(2, 5)
                den3 = f.denominator * multby
                mult1 = random.randint(0, multby - 1)
                small = Fraction(f.numerator * mult1, den3)
                big = Fraction(f.numerator * (multby - mult1), den3)
                ins1 = small.ToStringAddNum('\\pi')
                ins2 = big.ToStringAddNum('\\pi')
                frac1 = small
                frac2 = big
            if random.randint(0, 1):
                question = '$\\sin{(' + ins1 + ')}\\cos{(' + ins2 + ')} - \\cos{(' + ins1 + ')}\\sin{(' + ins2 + ')} =$'
                answer = '$' + trig.sin(trig.radToDeg(fraction.Subtract(frac1, frac2))) + '$'
        elif rrand == 2:
            ins1, ins2 = '', ''
            f = utility.goodTrigFrac()
            while f.numerator == 0: f = utility.goodTrigFrac()
            deg = trig.radToDeg(f)
            if random.randint(0, 2) < 2:
                if deg < 0: small = -random.randint(0, -deg - 1)
                else: small = random.randint(0, deg-1)
                big = deg - small
                ins1 = str(small)
                ins2 = str(big)
                frac1 = trig.degToRad(small)
                frac2 = trig.degToRad(big)
            else:
                multby = random.randint(2, 5)
                den3 = f.denominator * multby
                mult1 = random.randint(0, multby-1)
                small = Fraction(f.numerator * mul1, den3)
                big = Fraction(f.numerator * (multby - mult1), den3)
                ins1 = small.ToStringAddNum('\\pi')
                ins2 = big.ToStringAddNum('\\pi')
                frac1, frac2 = small, big
            if random.randint(0, 1):
                question = '$\\cos{(' + ins1 + ')}\\cos{(' + ins2 + ')} + \\sin{(' + ins1 + ')}\\sin{(' + ins2 + ')} =$'
                answer = '$' + str(trig.cos(trig.radToDeg(fracion.Subtract(frac1, frac2)))) + '$'
            else:
                question = '$\\cos{(' + ins1 + ')}\\cos{(' + ins2 + ')} - \\sin{(' + ins1 + ')}\\sin{(' + ins2 + ')} =$'
                answer = '$' + str(trig.cos(deg)) + '$'
                
        elif rrand == 3:
            ins1, ins2 = '', ''
            f = utility.goodTrigFrac()
            deg = trig.radToDeg(f)
            if random.randint(0, 1):
                d1 = float(deg) / 2
                d2 = d1
                ins1 = str(d1) + '^\\circ'
                ins2 = str(d2) + '^\\circ'
            else:
                f1 = fraction.Divide(f, Fraction(2, 1))
                f2 = f1
                ins1 = f1.ToStringAddNum('\\pi')
                ins2 = f2.ToStringAddNum('\\pi')
            question = '$2\\sin{(' + ins1 + ')}\\cos{(' + ins2 + ')} =$'
            answer = '$' + str(trig.sin(deg)) + '$'
            if random.randint(0, 1):
                question = '$2\\cos{(' + ins1 + ')}\\sin{(' + ins2 + ')} =$'
    return [question, answer, end]
                
            
                    
                    
            
                
