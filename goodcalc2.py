print("Welcome to \"Good Calculator\"")
print("Remember, when doing a function, always have '/' in front!")
print("Enter '/help' for help\n")
from math import *
import operator
ID = {'trig':0}#0 = radians, 1 = degrees
def TO(string):
    return string.replace('(','').replace(')','')
def evaluate(TI,ID,answer):
    TI = str(TI)
    TI = TI.split()
    for i in TI:
        if i in ID:
            TI[TI.index(i)] = TI[TI.index(i)].replace(i,"ID['" + i + "']")
    return ' '.join(TI)
def string(x, ID, answer):
    while x.count('(') + x.count(')') != 0:
        Oi = 0
        Ei = 0
        for i,n in enumerate(x):
            if n == '(':
                Oi = i
            elif n == ')':
                Ei = i
                break
        newt = x[Oi: Ei + 1]
        newt = evaluate(newt, ID, answer)
        z = main(TO(newt),ID,answer)
        x = x.replace(newt,str(z))
    return main(x,ID,answer)
def factors(number):
    factor = []
    for i in range(1,int(number/2) + 1):
        if number%i == 0:
            factor.append(str(i))
    factor.append(str(number))
    return ' '.join(factor)
def Help():
    thedict = {'/settings':'Change Settings','/prime x':'Returns 1 if prime, 0 otherwise','/primerange x y':'Returns a list of primes from x to y','/factor x':'Returns the factors of x','/sumlist x y z ...':'Returns sum of list',\
               '/choose x y ':'Returns the value of xCy','/comment abcde':'Returns the comment','/grade a b c':'Evaluates as if a is worth 60%, b- 30%, c- 10%','/sqrt x':'Returns the square root of x','/sin x':'Returns sin(x)',\
               '/cos x':'Returns cos(x)','/tan x':'Returns tan(x)','/meanlist list':'Returns the mean of the list','/sortedlist list':'Returns the the sorted list that was entered.',\
               '/perfect x':'Returns the boolean value of whether the number is a perfect number','/log [x] y':'X specifies the base, and y is the value, when x is not there, it is reverted to the common logarithm',\
               '/ln x':'Returns the natural logarithm of x','/pascr n':"Returns the n'th row of Pascal's Triangle"}
    items = sorted(thedict.keys())
    print('%-20s%-30s'%('Function', 'Use\n'))
    for i in items:    
        print('%-20s%-30s'%(i,thedict.get(i)))
    
def list_to_string(other):
    string = ''
    for i in other:
        string += str(i)
    return string
def prime(number):
    if number == 1: return 0
    for i in range(2, int(sqrt(number))+1):
        if number%i == 0:
            return 0
    return 1
def primerange(low,high):
    el = [str(i) for i in range(int(low), int(high) + 1)]
    re = ' '.join(list(filter(lambda x: prime(int(x)) == 1, el)))
    return re
def perfrange(low,high):
    el = [str(i) for i in range(int(low),int(high) + 1)]
    re = ' '.join(list(filter(lambda x: sum([int(i) for i in factors(int(x)).split()[:-1]]) == int(x),el)))
    return re
def Settings(MR):
    MR += ' '
    print("Welcome to settings, here you can change and view settings.")
    print("To learn more, enter \"/help\"")
    mode = MR[0]
    if mode == 'ch' or mode == 'change':
        pass
def main(TI,ID,answer):#The Input, Initial Data
    g = evaluate(TI, ID, answer)
    ANSWER = ''
    origin = ''
    thein = g[1:]
    thein = thein.split()
    try:
        thein[1:] = [eval(i) for i in thein[1:]]
    except:
        ANSWER = 'error'
    try:
        origin = thein[0].lower()
    except:
        pass
    try:
        if origin == 'choose':
            ANSWER = (factorial(thein[1]))//(factorial(thein[1] - thein[2]) * factorial(thein[2]))
        elif origin == 'factor' or origin == 'factors':
            ANSWER = factors(thein[1])
        elif origin == 'factorial':
            ANSWER = factorial(thein[1])
        elif origin == 'comment':
            ANSWER = TI[9:]
        elif origin == 'sqrt':
             ANSWER =  sqrt(thein[1])
        elif origin in ['sin','cos','tan']:
            if ID['trig'] == 0:
                ANSWER = eval(origin + '(int(thein[1]))')
            else:
                ANSWER = eval(origin + '(radians(int(thein[1]))')
        elif origin == 'help':
            Help()
        elif origin == 'grade':
            ANSWER = ((thein[1] * 60) + (thein[2] * 30) + (thein[3] * 10))/100
            #grade: formative, summative, hw
        elif origin == 'ln':
            ANSWER = log1p(thein[1]-1)
            #For log1p it computes ln(x + 1)
        elif origin == 'log': 
            if len(thein[1:]) == 2:
                ANSWER = log(thein[2])/log(thein[1])
            else:
                ANSWER = log10(thein[1])
        elif origin == 'loop':
            if ' in ' not in thein:
                for i in range(int(thein[2]),int(thein[3]),int(thein[4])):
                    z = TI[TI.index('{') + 1:]
                    if thein[1] in z:
                        a = z.index(thein[1])
                        b = z.index(thein[1][-1])
                        z = z[:a] + str(i) + z[b+1:]
                    print(main(z,ID,answer))
            ANSWER = ''
        elif origin == 'pascr':
            ANSWER = ' '.join([str(main('/choose ' + str(thein[1]) + ' ' + str(i),ID,answer)) for i in range(thein[1] + 1)])
        elif origin == 'perfect':
            ANSWER = (thein[1] == sum([int(i) for i in factors(thein[1])[:-1]]))
        elif origin == 'perfrange':
            ANSWER = perfrange(thein[1],thein[2])
        elif origin == 'perm':
            ANSWER = (factorial(thein[1])/(factorial(thein[1]-thein[2])))
        elif origin == 'pow':
            ANSWER = pow(thein[1],thein[2])
        elif origin == 'prime':
            a = prime(int(thein[1]))
            ANSWER = a
        elif origin == 'primerange':
            ANSWER = primerange(thein[1],thein[2])
        elif origin == 'right':
            sides = sorted([thein[1],thein[2],thein[3]])
            if pow(sides[0],2) + pow(sides[1],2) == pow(sides[2],2):
                ANSWER = 1
            else:
                ANSWER = 0
        elif origin == 'settings':
            changeit = Settings(thein[1:])
        elif origin == 'exit' or origin == 'quit':
            ANSWER = 'LoopDone'
        elif origin in ['sumlist','sortedlist','meanlist','lenlist']:
            try:
                newlist = [float(i) for i in thein[1:]]
            except: return "ERROR"
            if origin != 'meanlist':
                #
                ANSWER = eval(str(origin[:-4]) + '(' + str(newlist) + ')')
                #
            else:
                try:
                    ANSWER = sum(newlist)/(len(thein)-1)
                
                except:return 'ERROR'
        elif origin == 'sto':
            ID[thein[1]] = int(thein[2])
            print(ID)
            ANSWER = 'DONE'
        else:
            try:
                ANSWER = eval(g)
            except Exception as e:
                return e
    except Exception as e:
        return e
    return ANSWER
answer = 0
done = False
while done == False: 
    x = input(">>> ")
    if '(' in x:
        answer = string(x, ID, answer)
        
    else:
        answer = main(x,ID,answer)
    if answer == 'LoopDone':
        done = True
    print(answer)
