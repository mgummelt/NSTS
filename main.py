import datetime, random
import caller
import category
import utility
import os
import callCategories

fileBase = './tests/'
fileQName = ''
fileAName = ''
fileDebugName = './fileDebug.txt'
testDir = './tests/'
today = ''
counter = 0

fileQuestions = None
fileAnswers   = None
fileDebug     = None

def addHeaders(title):
    numAt = 1
    today = datetime.date.today()
        
    questionHeaders = "\\documentclass[twocolumn]{article}\n" \
    "\\usepackage{fancyhdr}\n" \
    "\\pagestyle{fancy}\n" \
    "\\renewcommand{\\headrulewidth}{0pt}\n" \
    "\\renewcommand{\\footrulewidth}{0pt}\n" \
    "\\setlength{\\textheight}{9.25in}\n" \
    "\\setlength{\\columnsep}{0.375in}\n" \
    "\\setlength{\\textwidth}{6.8in}\n" \
    "\\setlength{\\topmargin}{0.0625in}\n" \
    "\\setlength{\\headsep}{0.2in}\n" \
    "\\setlength{\\oddsidemargin}{-.30in}\n" \
    "\\setlength{\\parindent}{0pt}\n" \
    "\\setlength{\\parskip}{0.12in}\n" \
    "\\chead{%s}\n" \
    "\\begin{document}\n" % (title)

    answerHeaders = "\\documentclass[twocolumn]{article}\n" \
    "\\usepackage{fancyhdr}\n" \
    "\\pagestyle{fancy}\n" \
    "\\renewcommand{\\headrulewidth}{0pt}\n" \
    "\\renewcommand{\\footrulewidth}{0pt}\n" \
    "\\setlength{\\textheight}{9.25in}\n" \
    "\\setlength{\\columnsep}{0.375in}\n" \
    "\\setlength{\\textwidth}{6.8in}\n" \
    "\\setlength{\\topmargin}{0.0625in}\n" \
    "\\setlength{\\headsep}{0.2in}\n" \
    "\\setlength{\\oddsidemargin}{-.30in}\n" \
    "\\setlength{\\parindent}{0pt}\n" \
    "\\setlength{\\parskip}{0.12in}\n" \
    "\\chead{%s}\n" \
    "\\begin{document}\n" \
    "\n" % (title)

    fileQuestions.write(questionHeaders)
    fileAnswers.write(answerHeaders)
    

def addStandardQuesAns():
    numQuestions = 80
    for i in range(1, numQuestions+1):
        problem  = caller.callQuestion(i)        
        question = "(%d)  %s \\line(1,0){50} %s\\\\[.2in]\n" % (i, problem[0], problem[2])
        answer   = "(%d)  %s\\\\[.2in]\n" % (i, problem[1])
        if i % 10 == 0:
            question = '*' + question
            answer = '*' + answer
        fileDebug.write(str(i) + ' ' + problem[3] + '\n')        
        fileQuestions.write(question)
        fileAnswers.write(answer)

def addCustomQuesAns(cat):
    numQuestions = 40
    for i in range(1, numQuestions+1):
        problem  = cat.func(random.randint(1, 80))      
        question = "(%d)  %s \\line(1,0){50} %s\\\\[.2in]\n" % (i, problem[0], problem[2])
        answer   = "(%d)  %s\\\\[.2in]\n" % (i, problem[1])
        fileDebug.write(str(i) + ' ' + cat.name + '\n')        
        fileQuestions.write(question)
        fileAnswers.write(answer)

def createStandardTest(num):
    initStandardVars(num)
    addHeaders('Adelie Standard Test ' + today + ' ' + str(num))
    addStandardQuesAns()        
    addFooters()
    createStandardPDF()

def createCustomTest(cat, num):
    initCustomVars(cat, num)    
    addHeaders('Adelie Custom Test ' + today  + ' ' + cat.name + ' ' + str(num))
    addCustomQuesAns(cat)
    addFooters()
    createCustomPDF(cat)
    
            
def addFooters():
    fileQuestions.write('\\end{document}')
    fileAnswers.write('\\end{document}')
    fileQuestions.close()
    fileAnswers.close()
    fileDebug.close()
    
def createStandardPDF(): 
    print fileQName, fileAName
    os.system('pdflatex --output-directory=%s%s/standard %s' % (testDir, today, fileQName))
    os.system('pdflatex --output-directory=%s%s/standard %s' % (testDir, today, fileAName))

def createCustomPDF(cat): 
    print fileQName, fileAName
    os.system('pdflatex --output-directory=%s%s/custom/%s %s' % (testDir, today, cat.func.__name__, fileQName))
    os.system('pdflatex --output-directory=%s%s/custom/%s %s' % (testDir, today, cat.func.__name__, fileAName))

def initStandardVars(num):
    global fileQName, fileAName
    global fileQuestions, fileAnswers, fileDebug, today
    fileQName = fileBase + today + '_' + str(num) + '.txt'
    fileAName = fileBase + today + '_' + str(num) + 'a.txt'
    fileQuestions = open(fileQName, 'w')
    fileAnswers   = open(fileAName, 'w')
    fileDebug     = open(fileDebugName, 'w')
    category.initCategories()
    utility.initPrimes()

def initCustomVars(cat, num):
    global fileQName, fileAName
    global fileQuestions, fileAnswers, fileDebug, today
    fileQName = fileBase + today + '_' + cat.func.__name__ + str(num) + '.txt'
    fileAName = fileBase + today + '_' + cat.func.__name__ + str(num) + 'a.txt'
    fileQuestions = open(fileQName, 'w')
    fileAnswers   = open(fileAName, 'w')
    fileDebug     = open(fileDebugName, 'w')
    category.initCategories()
    utility.initPrimes()



if __name__ == '__main__':    
    t = datetime.datetime.now()
    today = t.strftime('%A-%B-%d')
    if os.path.exists(testDir + today):
        os.system('rm -rf ' + testDir + today)
    os.mkdir(testDir + today)
    os.mkdir(testDir + today + '/standard')
    os.mkdir(testDir + today + '/custom')
    for i in range(1, 2):
        createStandardTest(i)
        os.system('rm ' + testDir + today + '/standard/*.aux')
        os.system('rm ' + testDir + today + '/standard/*.log')
    # category.initCategories()
    # for cat in category.Category.categories:
    #     os.mkdir(testDir + today + '/custom/' + cat.func.__name__)
    #     for i in range(1, 6):
    #         createCustomTest(cat, i)         
    #     os.system('rm ' + testDir + today + '/custom/' + cat.func.__name__ + '/*.aux')
    #     os.system('rm ' + testDir + today + '/custom/' + cat.func.__name__ + '/*.log')
    
    
    
