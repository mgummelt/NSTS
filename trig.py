import radical, utility
from radical import Radical
from fraction import Fraction

def sin(theta):
    while theta < 0: theta += 360
    theta = theta % 360
    refa = utility.RefAngle(theta)
    bNeg = theta > 180
    if refa == 0: return Radical(0, 0, 0)
    elif refa == 30: return Radical(-1 if bNeg else 1, 2, 1)
    elif refa == 45: return Radical(-1 if bNeg else 1, 2, 2)
    elif refa == 60: return Radical(-1 if bNeg else 1, 2, 3)
    else: return Radical(-1 if bNeg else 1, 1, 1)

def cos(theta):
    while theta < 0: theta += 360
    theta = theta % 360
    refa = utility.RefAngle(theta)
    bNeg = theta > 90 and theta < 270
    if refa == 0: return Radical(-1 if bNeg else 1, 1, 1)
    elif refa == 30: return Radical(-1 if bNeg else 1, 2, 3)
    elif refa == 45: return Radical(-1 if bNeg else 1, 2, 2)
    elif refa == 60: return Radical(-1 if bNeg else 1, 2, 1)
    else: return Radical(0, 0, 0)
    
def tan(theta):
    ssin, scos = sin(theta), cos(theta)
    return radical.Divide(ssin, scos)

def sec(theta):
    scos = cos(theta)
    return Radical(scos.co.denominator, scos.co.numerator * scos.rad, scos.rad)

def csc(theta):
    ssin = sin(theta)
    return Radical(ssin.co.denominator, ssin.co.numerator * ssin.rad, ssin.rad)

def cot(theta):
    stan = tan(theta)
    return Radical(stan.co.denominator, stan.co.numerator * stan.rad, stan.rad)

def arccos(rad):
    if rad == Radical(-1, 1, 1): return 180
    if rad == Radical(-1, 2, 3): return 150
    if rad == Radical(-1, 2, 2): return 135
    if rad == Radical(-1, 2, 1): return 120
    if rad == Radical(0, 1, 1): return 90
    if rad == Radical(1, 2, 1): return 60
    if rad == Radical(1, 2, 2): return 45
    if rad == Radical(1, 2, 3): return 30
    if rad == Radical(1, 1, 1): return 0
    return -1

def arcsin(rad):
    if rad == Radical(-1, 1, 1): return -90
    if rad == Radical(-1, 2, 3): return -60
    if rad == Radical(-1, 2, 2): return -45
    if rad == Radical(-1, 2, 1): return -30
    if rad == Radical(0, 1, 1): return 0
    if rad == Radical(1, 2, 1): return 30
    if rad == Radical(1, 2, 2): return 45
    if rad == Radical(1, 2, 3): return 60
    if rad == Radical(1, 1, 1): return 90
    return -1

def radToDeg(rad):
    return 180 / rad.denominator * rad.numerator

def degToRad(deg):
    return Fraction(deg, 180)

