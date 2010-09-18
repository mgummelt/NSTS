import random

class Day:
    leapDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    def __init__(self):
        self.day = self.month = self.year = 0
    def __str__(self):
        return Day.months[self.month] + ' ' + str(self.day) + ', ' + str(self.year)

def randomDay():
    d = Day()
    d.year = random.randint(2000, 2012)
    d.month = random.randint(0, 11)
    d.day = random.randint(1, Day.leapDays[d.month]) if d.year % 4 == 0 else random.randint(1, Day.days[d.month])
    return d

def nextDay(start, delta):
    end = Day()
    end.day = start.day
    end.year = start.year
    end.month = start.month
    for i in range(delta):
        end.day+=1
        leap = end.year%4==0
        if leap and Day.leapDays[end.month] < end.day:
            end.month +=1
            end.day = 1
        if not leap and Day.days[end.month] < end.day:
            end.month += 1
            end.day = 1
        if end.month > 11:
            end.month = 1
            end.year += 1
    return end