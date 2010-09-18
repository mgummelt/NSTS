import callCategories
import utility
import random
from category import Category

def callQuestion(probNum):
    if probNum % 10 == 0:
        return callCategories.Estimations(probNum) + ['Estimations']
    catWeights = [0] * len(Category.categories)
    
    for i in range(len(catWeights)): #for every category
        if Category.categories[i].name == 'Estimations':
            continue
        for pn in Category.categories[i].data:
            catWeights[i] += .86**(pn - probNum)
        catWeights[i] *= mults[i]
        
    tot = 0
    for weight in catWeights: 
        tot+=weight
    choose = random.random() * tot
        
    for i in range(len(catWeights)):
        category = Category.categories[i]
        if choose < catWeights[i]:
            if category.func == callCategories.Estimations:
                return callQuestion(probNum)
            cons = .1
            mults[i] *= cons
            if mults[i] < .1**2 + 1e-7: #already used this category twice
                return callQuestion(probNum)
            return category.func(probNum) + [category.func.__name__]
        choose -= catWeights[i]
        