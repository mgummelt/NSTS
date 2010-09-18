import random, math
import utility, mixedNumber
from mixedNumber import MixedNumber

def Exp10():
    chance = random.random()
    if chance < .15: return Exp20()
    rand = random.randint(0, 26)
    if rand < 15: return EqualAddUp(10)
    elif rand < 25: return UnEqualAddUp(10)
    else: return Multiplication(10)

def Exp20():
    chance = random.random()
    if chance < .15: return Exp10()
    elif chance < .3: return Exp30()
    rand = random.randint(0, 27)
    if rand < 6: return BigDivision(20)
    elif rand < 21: return SqrtCbrt(20)
    elif rand < 27: return Multiplication(20)
    else: return OtherMultiplication(20)

def Exp30():
    chance = random.random()
    if chance < .15: return Exp20()
    elif chance < .3: return Exp40()
    rand = random.randint(0, 26)
    if rand < 5: return BigDivision(30)
    elif rand < 7: return SqrtCbrt(30)
    elif rand < 23: return Multiplication(30)
    elif rand < 26: return Exponents(30)
    else: return OtherMultiplication(30)

def Exp40():
    chance = random.random()
    if chance < .15: return Exp30()
    elif chance < .3: return Exp50()
    rand = random.randint(0, 26)
    if rand < 7: return SqrtCbrt(40)
    elif rand < 20: return Multiplication(40)
    elif rand < 22: return Exponents(40)
    else: return OtherMultiplication(40)

def Exp50():
    chance = random.random()
    if chance < .15: return Exp40()
    elif chance < .3: return Exp60()
    rand = random.randint(0, 26)
    if rand < 5: return BigDivision(50)
    elif rand < 16: return SqrtCbrt(50)
    else: return Multiplication(50)

def Exp60():
    chance = random.random()
    if chance < .15: return Exp50()
    elif chance < .3: return Exp70()
    rand = random.randint(0, 25)
    if rand < 3: return BigDivision(60)
    elif rand < 19: return Multiplication(60)
    elif rand < 24: return Exponents(60)
    else: return OtherMultiplication(60)

def Exp70():
    chance = random.random()
    if chance < .15: return Exp60()
    elif chance < .3: return Exp80()
    rand = random.randint(0, 26)
    if rand < 2: return BigDivision(70)
    elif rand < 8: return Multiplication(70)
    elif rand < 13: return Series(70)
    elif rand < 15: return OtherMultiplication(70)
    else: return EandPI(70)

def Exp80():
    chance = random.random()
    if chance < .15: return Exp70()
    rand = random.randint(0, 26)
    if rand < 2: return EandPI(80)
    elif rand < 8: return OtherMultiplication(80)
    elif rand < 12: return Exponents(80)
    elif rand < 25: return Multiplication(80)
    else: return BigDivision(80)

def EqualAddUp(probNum):
    question, answer, end = '', '', ''
    numNums = random.randint(3, 6)
    nums = [0] * numNums
    center = random.randint(2000, 7999) if random.randint(0, 3) == 0 else random.randint(200, 799)
    canNeg = random.randint(0, 2) == 0
    
    for i in range(numNums):
        nums[i] = random.randint(1, center*2-1)
        if random.randint(0, 1) and canNeg: nums[i] *= -1
    
    question = str(nums[0])
    if random.randint(0, 19) == 0:
        if nums[0] > 0:
            Factors = utility.Factors(nums[0])
            x = Factors[random.randint(0, len(Factors)-1)]
            y = nums[0] / x
            if x!=1 and y!=1:
                question = str(x) + ' * ' + str(y)
        else:
            Factors = utility.Factors(-nums[0])
            x = Factors[random.randint(0, len(Factors)-1)]
            y = -nums[0] / x
            if x!=1 and y!=1:
                if random.randint(0, 1):
                    question = '-' + str(x) + ' * ' + str(y)
                else:
                    question = str(x) + ' * -' + str(y)
    
    ans = nums[0]
    
    for i in range(1, numNums):
        ans += nums[i]
        if nums[i] > 0: question += ' + '
        else: question += ' - '
        d = abs(nums[i])
        if random.randint(0, 19) == 0:
            Factors = utility.Factors(d)
            x = Factors[random.randint(0, len(Factors)-1)]
            y = d / x
            if x == 1 or y == 1: question += str(nums[i])
            else: question += str(x) + ' * ' + str(y)
        else: question += str(d)
    
    question = '$' + question + ' = $'
    low = float(ans) * .95
    high = float(ans) * 1.05
    t = low
    low = low if low < high else high
    high = t if t > high else high
    
    answer = '$' + str(int(round(low))) + ' - ' + str(int(round(high))) + '$'
    return [question, answer, end]

def UnEqualAddUp(probNum):
    question, answer, end = '', '', ''
    numNums = random.randint(3, 5)
    big = random.randint(0, 10**numNums-1)
    desc = random.randint(0, 1) == 0
    nums = [0] * numNums
    if desc:
        nums[0] = big
        for i in range(1, numNums):
            nums[i] = 10 ** (numNums - 1)
    else:
        nums[numNums-1] = big
        for i in range(numNums-2, -1, -1):
            nums[i] = 10 ** (numNums - i)
    
    sameNums = random.randint(0, 1) == 0
    if sameNums:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        nextNum = num1
        for i in range(numNums):
            size = len(str(nums[i])) - 1
            x = 0
            while size >= 0:
                x *= 10
                x += nextNum
                size-=1
                if nextNum == num1:
                    nextNum = num2
                else:
                    nextNum = num1
            nums[i] = x
    elif random.randint(0, 2) < 2:
        start = random.randint(0, 9)
        for i in range(numNums):
            x = 0
            size = len(str(nums[i])) - 1
            while size >= 0:
                x*=10
                x += start
                size -= 1
                start += 1
                start %= 10
            nums[i] = x
    
    if random.randint(0, 1):
        for i in range(numNums):
            if random.randint(0, 1):
                nums[i] *= -1
    
    question = str(nums[0])
    ans = nums[0]
    
    for i in range(1, numNums):
        ans += nums[i]
        if nums[i] > 0:
            question += ' + '
        else:
            question += ' - '
        d = abs(nums[i])
        question += str(d)
    
    question = '$' + question + ' = $'
    low = float(ans) * .95
    high = float(ans) * 1.05
    t = low
    low = low if low < high else high
    high = t if t > high else high
    
    answer = '$' + str(int(round(low))) + ' - ' + str(int(round(high))) + '$'
    return [question, answer, end]

def BigDivision(probNum):
    question, answer, end = '', '', ''
    bigNum = random.randint(10000, 99999) if random.randint(0, 1) else random.randint(100000, 999999)
    smallNum = random.randint(100, 999)
    question = '$' + str(bigNum) + ' \\div ' + str(smallNum) + ' = $'
    high = float(bigNum) / smallNum * 1.05
    low = float(bigNum) / smallNum * .95
    answer = '$' + str(int(round(low))) + ' - ' + str(int(round(high))) + '$'
    if (probNum > 40 and random.randint(0, 4) == 0) or (probNum <= 40 and random.randint(0, 15) == 0):
        question = '$(' + str(bigNum) + ' \\div ' + str(smallNum) + ')^2 = $'
        high = ((float(bigNum) / smallNum) ** 2) * 1.05 
        low = high / 1.05 * .95
        answer = '$' + str(int(round(low))) + ' - ' + str(int(round(high))) + '$'
    return [question, answer, end]

def SqrtCbrt(probNum):
    question, answer, end = '', '', ''
    if probNum <= 40 and random.randint(0, 3) == 0:
        type = 1
    else:
        type = 0 if random.randint(0, 1) else 2
    ans = 0.0
    if type == 0:
        rand = random.randint(0, 2)
        if rand == 0:
            num = random.randint(1000000, 9999999)
        elif rand == 1:
            num = random.randint(100000, 999999)
        else:
            num = random.randint(10000, 99999)
        question = '$\\sqrt{' + str(num) + '} = $'
        ans = math.sqrt(num)
    elif type == 1:
        if random.randint(0, 1): num = random.randint(100, 999)
        else: num = random.randint(1000, 9999)
        mult = random.randint(10,99) if random.randint(0, 1) else random.randint(100, 999)
        question = '$\\sqrt{' + str(num) + '} \\times ' + str(mult) + ' = $'
        if random.randint(0, 1): question = '$' + str(mult) + ' \\times \\sqrt{' + str(num) + '} = $'
        ans = math.sqrt(num) * mult
        if random.randint(0, 4) == 0:
            num = random.randint(5, 16)**3 + random.randint(-100, 99)
            mult = random.randint(10, 99) if random.randint(0, 1) else random.randint(100, 399)
            question = '$\\sqrt[3]{' + str(num) + '} \\times ' + str(mult) + ' = $'
            if random.randint(0, 1): question = '$' + str(mult) + ' \\times \\sqrt[3]{' + str(num) + '} = $'
            ans = (num ** (1.0 / 3.0)) * mult
    elif type == 2:
        numTerms = random.randint(2, 3)
        ans = 1
        question = '$'
        for i in range(numTerms):
            rand = random.randint(0, 2)
            if rand == 0:
                b = random.randint(5, 39)
                num = (b**2 + random.randint(-b, b-1)) if random.randint(0, 1) else random.randint(100, 1499)
                if i!=0: question += ' \\times '
                question += '\\sqrt{' + str(num) + '}'
                ans *= math.sqrt(num)
            elif rand == 1:
                b = random.randint(5, 39)
                num = (b**3 + random.randint(-b*3, b*3-1)) if random.randint(0, 1) else random.randint(100, 1499)
                if i!=0: question += ' \\times '
                question += '\\sqrt[3]{' + str(num) + '}'
                ans *= num ** (1.0/3.0)
            elif rand == 2:
                num = random.randint(10, 99)
                if i!=0: question += ' \\times '
                question += str(num)
                ans *= num
        question += ' = $'
    answer = '$' + str(int(round(ans*0.95))) + ' - ' + str(int(round(ans*1.05))) + '$'
    return [question, answer, end]

def Multiplication(probNum):
    question, answer, end = '', '', ''
    ans = 0.0
    type = 0
    rr = random.randint(0, 28)
    if rr < 2: type = 0
    elif rr < 12: type = 1
    elif rr < 22: type = 2
    elif rr < 23: type = 3
    elif rr < 29: type = 4
    if type == 0:
        rand = random.randint(0, 1)
        if rand == 0:
            first = random.randint(20, 99) if random.randint(0, 1) else random.randint(1000, 3999)
            second = first + random.randint(-first/2, first/2-1)
            mult = utility.fracNum(4) if random.randint(0, 1) else random.randint(10, 999)
            if random.randint(0, 1): second *= -1
            if random.randint(0, 1) == 0:
                sfirst = '(' + str(first) + (' - ' if second < 0 else ' + ') + str(abs(second)) + ' )'
                sSecond = str(mult)
                if random.randint(0, 1):
                    question = '$' + str(sfirst) + ' \\times ' + str(sSecond) + ' = $'
                else:
                    question = '$' + str(sSecond) + ' \\times ' + str(sfirst) + ' = $'
                ans = (first + second) * mult
            else:
                sfirst = str(first) + (' - ' if second < 0 else ' + ') + str(abs(second))
                sSecond = str(mult)
                if random.randint(0, 1):
                    question = '$' + str(sfirst) + ' \\times ' + str(sSecond) + ' = $'
                    ans = first + second * mult
                else:
                    question = '$' + str(sSecond) + ' \\times ' + str(sfirst) + ' = $'
                    ans = mult * first + second
        elif rand == 1:
            first = random.randint(100, 999)
            second = random.randint(100, 999)
            third = random.randint(100, 999)
            if random.randint(0, 1):
                question = '$' + str(first) + ' \\times ' + str(second) + ' \\div ' + str(third) + ' = $'
            else:
                question = '$' + str(first) + ' \\div ' + str(third) + ' \\times ' + str(second) + ' = $'
            ans = float(first) * second / third
    elif type == 1:
        if random.randint(0, 2) == 0:
            size = random.randint(2, 5)
            first = random.randint(10**(size-1), 10**size - 1)
            second = random.randint(10**(size-1), 10**size - 1)
            dfirst, dsecond = 0.0, 0.0
            if random.randint(0, 9) == 0: dfirst = utility.Decimalize(int(first))
            if random.randint(0, 9) == 0: dsecond = utility.Decimalize(int(second))
            question = '$' + str(first if dfirst == 0 else dfirst) + ' \\times ' + str(second if dsecond == 0 else dsecond) + ' = $'
            ans = (first if dfirst == 0 else dfirst) * (second if dsecond == 0 else dsecond)
        else:
            first, second = 0, 0
            dfirst, dsecond = 0.0, 0.0
            while True:
                first = utility.fracNum(5)
                second = utility.fracNum(5) if random.randint(0, 3) == 0 else random.randint(10, 99)
                if random.randint(0, 1):
                    temp = first
                    first = second
                    second = temp
                dfirst, dsecond = 0.0, 0.0
                if random.randint(0, 9) == 0:
                    dfirst = utility.Decimalize(int(first))
                if random.randint(0, 9) == 0:
                    dsecond = utility.Decimalize(int(second))
                if not (first < 100 or (second < 100 and random.randint(0, 9) < 9)):
                    break
            question = '$' + str(first if dfirst == 0 else dfirst) + ' \\times ' + str(second if dsecond == 0 else dsecond) + ' = $'
            ans = (first if dfirst == 0 else dfirst) * (second if dsecond == 0 else dsecond)
    elif type == 2:
        if random.randint(0, 5) == 0:
            first, second = random.randint(100, 999), random.randint(100, 999)
            third = random.randint(100, 999)
            dfirst, dsecond, dthird = 0.0, 0.0, 0.0
            if random.randint(0, 1): dfirst = utility.Decimalize(int(first))
            if random.randint(0, 1): dsecond = utility.Decimalize(int(second))
            if random.randint(0, 1): dthird = utility.Decimalize(int(third))
            question = '$' + str(first if dfirst == 0 else dfirst) + ' \\times ' + str(second if dsecond == 0 else dsecond) + ' \\times ' + str(third if dthird == 0 else dthird) + ' = $'
            ans = (first if dfirst == 0 else dfirst) * (second if dsecond == 0 else dsecond) * (third if dthird == 0 else dthird)
        else:
            center = random.randint(12, 120)
            diff = random.randint(1, 6)
            minus = diff + random.randint(-1, 1)
            plus = diff + random.randint(-1, 1)
            first = center - minus
            third = center + minus
            second = center
            question = '$' + str(first) + ' \\times ' + str(center) + ' \\times ' + str(third) + ' = $'
            ans = first * center * third
    elif type == 3:
        center = random.randint(15, 40)
        first = center + random.randint(-3, 3)
        second = center + random.randint(-3, 3)
        third = center + random.randint(-3, 3)
        fourth = center + random.randint(-3, 3)
        question = '$' + str(first) + ' \\times ' + str(second) + ' \\times ' + str(third) + ' \\times ' + str(fourth) + ' = $'
        ans = first * second * third * fourth
    elif type == 4:
        center = random.randint(15, 40)
        first = center + random.randint(-2, 2)
        third = center + random.randint(-2, 2)
        second = random.randint(10, 99) if random.randint(0, 1) else random.randint(100, 999)
        fourth = random.randint(10, 99) if random.randint(0, 1) else random.randint(100, 999)
        if random.randint(0, 1):
            temp = first
            first = second
            second = temp
        if random.randint(0, 1):
            temp = third
            third = fourth
            fourth = temp
        question = '$' + str(first) + ' \\times ' + str(second) + ' + ' + str(third) + ' \\times ' + str(fourth) + ' = $'
        ans = first * second + third * fourth
    if abs(ans) < 50: return Multiplication(probNum)
    high = ans * 1.05
    low = ans * .95
    answer = '$' + str(int(round(low if low < high else high))) + ' - ' + str(int(round(high if high > low else low))) + '$'
    return [question, answer, end]

def Series(probNum):
    question, answer, end = '' ,'', ''
    if random.randint(0, 2):
        start = random.randint(1, 3)
        end = start * random.randint(10, 30)
        while end > 40:
            end = start * random.randint(10, 30)
        question = '$(' + str(start) + ' + ' + str(start * 2) + ' + ' + str(start * 3) + ' + ... + ' + str(end) + ')^2 = $'
        ans = ((start + end) * (end / start) / 2) ** 2
        low = int(round(ans * .95))
        high = int(round(ans * 1.05))
        answer = '$' + str(low) + ' - ' + str(high) + '$'
    else:
        max = random.randint(8, 15)
        question = '$1^3 + 2^3 + 3^3 + 4^3 + ... + ' + str(max) + '^3 = $'
        ans = (max * (max + 1) / 2) ** 2
        low = int(round(ans * .95))
        high = int(round(ans * 1.05))
        answer = '$' + str(low) + ' - ' + str(high) + '$'
    return [question, answer, end]

def Exponents(probNum):
    question, answer, end = '', '', ''
    type = 0
    rand = random.randint(0, 8)
    if rand < 4: type = 0
    elif rand < 6: type = 1
    elif rand < 8: type = 2
    else: type = 3
    
    ans = 0.0
    if type == 0:
        num = random.randint(10, 19)
        pow = random.randint(3, 6)
        question = '$' + str(num) + '^' + str(pow) + ' = $'
        ans = num**pow
    elif type == 1:
        num = random.randint(20, 119)
        question = '$' + str(num) + '^3 = $'
        ans = num**3
    elif type == 2:
        num = random.randint(20, 39)
        pow = random.randint(3, 4)
        question = '$' + str(num) + '^' + str(pow) + ' = $'
        ans = num**pow
    elif type == 3:
        ten = random.randint(2, 9) * 10
        less1 = ten - random.randint(1, 4)
        less2 = ten - random.randint(1, 4)
        if random.randint(0, 3) == 0: less1 = ten + random.randint(1, 4)
        if random.randint(0, 3) == 0: less2 = ten + random.randint(1, 4)
        question = '$' + str(less1) + '^2 + ' + str(less2) + '^2 = $'
        ans = less1**2 + less2**2
    
    low = int(round(ans * .95))
    high = int(round(ans*1.05))
    
    answer = '$' + str(low) + ' - ' + str(high) + '$'
    return [question, answer, end]

def OtherMultiplication(probNum):
    question, answer, end = '', '', ''
    type = random.randint(0, 1)
    ans = 0.0
    if type == 0:
        mult = random.randint(1000, 9999)
        div = random.randint(mult / 20, mult / 10 - 1)
        m = MixedNumber()
        m.co = random.randint(2, 18)
        m.f.denominator = random.randint(2, 5)
        m.f.numerator = random.randint(1, m.f.denominator-1)
        question = '$' + str(m) + ' \\times ' + str(mult) + ' \\div ' + str(div) + ' = $'
        ans = float(m.co * m.f.denominator + m.f.numerator) / m.f.denominator * mult / div
    elif type == 1:
        numTerms = random.randint(3, 4)
        ans = 1
        for i in range(numTerms):
            rand = random.randint(0, 2)
            if rand == 0:
                num = random.randint(10, 99) if random.randint(0, 1) else (random.randint(100, 999) if random.randint(0, 1) else random.randint(1000, 9999))
                if random.randint(0, 1) and i != 0:
                    question += ('' if i == 0 else ' \\div ') + str(num)
                    ans /= num
                else:
                    question += ('' if i == 0 else ' \\times ') + str(num)
                    ans *= num
            elif rand == 1:
                num = utility.fracNum(random.randint(2, 5))
                if random.randint(0, 1) and i != 0:
                    question += ('' if i == 0 else ' \\div ') + str(num)
                    ans /= num
                else:
                    question += ('' if i == 0 else ' \\times ') + str(num)
                    ans *= num
            elif rand == 2:
                b = random.randint(2, 10)
                exp = random.randint(-3, 3)
                if random.randint(0, 1) and i != 0:
                    question += ('' if i == 0 else ' \\div ') + str(b) + '^{' + str(exp) + '}'
                    ans /= b**exp
                else:
                    question += ('' if i == 0 else ' \\times ') + str(b) + '^{' + str(exp) + '}'
                    ans *= b**exp
        question = '$' + str(question) + ' = $'
    if abs(ans) < 60: return OtherMultiplication(probNum)
    low = ans * .95
    high = ans * 1.05
    answer = '$' + str(int(round(low if low < high else high))) + ' - ' + str(int(round(low if low > high else high))) + '$'
    return [question, answer, end]

def EandPI(probNum):
    question, answer, end = '', '', ''
    type = random.randint(0, 2)
    ans = 0.0
    if type == 0:
        co = random.randint(-2, 4)
        while co == -1 or co == 0 or co == 1:
            co = random.randint(-2, 4)
        exp = random.randint(2, 4)
        if random.randint(0, 1):
            question = '$(' + str(co) + '\\pi)^{' + str(exp) + '} = $'
            ans = (co*math.pi)**exp
        else:
            question = '$(' + str(co) + 'e)^{' + str(exp) + '} = $'
            ans = (co*math.e)**exp
    elif type == 1:
        if random.randint(0, 3) == 0:
            co1 = random.randint(1, 4)
            co2 = random.randint(1, 4)
            exp = random.randint(2, 4)
            question = '$(' + ('' if co1 == 1 else str(co1)) + '\\pi + ' + ('' if co2 == 1 else str(co2)) + 'e)^{' + str(exp) + '} = $'
            ans = (co1*math.pi + co2*math.e)**exp
        else:
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 4)
            question = '$\\pi^{' + str(exp1) + '}e^{' + str(exp2) + '} = $'
            ans = (math.pi ** exp1) * (math.e**exp2)
    elif type == 2:
        exp = random.randint(3, 6)
        if random.randint(0, 1):
            question = '$\\pi^{' + str(exp) + '} = $'
            ans = math.pi ** exp
        else:
            question = '$e^{' + str(exp) + '} = $'
            ans = math.e ** exp
    high = int(round(ans * 1.05))
    low = int(round(ans * .95))
    answer = '$' + str(low if low < high else high) + ' - ' + str(low if low > high else high) + '$'
    return [question, answer, end]
                
                
                
                
                
                