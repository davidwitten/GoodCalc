print("Welcome to \"Good Calculator\"")
print("Remember, when doing a function, always have '/' in front!")
from math import *
import operator
ID = {'trig':0}#0 = radians, 1 = degrees
def TO(string):
    return string.replace('(','').replace(')','')
def string(x, ID, answer):
    while x.count('(') != 0:
        Oi = 0
        Ei = 0
        for i,n in enumerate(x):
            if n == '(':
                Oi = i
            elif n == ')':
                Ei = i
                break
        newt = x[Oi: Ei + 1]
        z = main(TO(newt),ID,answer)
        x = x.replace(newt,str(z))
    return main(x,ID,answer)
                    
def factors(number):
    factor = []
    for i in range(2,int(number/2) + 1):
        if number%i == 0:
            factor.append(i)
    return factor
def Help():
    thedict = {'/settings':'Change Settings','/prime x':'Returns 1 if prime, 0 otherwise','/primerange x y':'Returns a list of primes from x to y','/factor x':'Returns the factors of x','/sumlist x y z ...':'Returns sum of list',\
               '/choose x y ':'Returns the value of xCy','/comment abcde':'Returns the comment'}
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
    for i in range(2, int(sqrt(number))+1):
        if number%i == 0:
            return 0
    return 1
def primerange(low,high):
    el = []
    low = int(low)
    if low == 1:
        low = 2
    high = int(high)
    for i in range(low,high + 1):
        if prime(i):
            el.append(str(i))
    re = ' '.join(el)
    return re
def Settings(MR):
    MR += ' '
    print("Welcome to settings, here you can change and view settings.")
    print("To learn more, enter \"/help\"")
    mode = MR[0]
    if mode == 'ch' or mode == 'change':
        pass
def main(TI,ID,answer):#The Input, Initial Data
    ANSWER = ''
    origin = ''
    thein = TI[1:]
    thein = thein.split()
    ID = ID
    try:
        if '/' in TI:
            thein[1:] = [eval(i) for i in thein[1:]]
    except:
        ANSWER = "ERROR"
    try:
        origin = thein[0].lower()
    except IndexError:
        pass
    try:
        if origin == 'choose':
            ANSWER = (factorial(thein[1]))//(factorial(thein[1] - thein[2]) * factorial(thein[2]))
        elif origin == 'factor' or origin == 'factors':
            ANSWER = factors(thein[1])
        elif origin == 'comment':
            ANSWER = TI[9:]
        elif origin == 'sqrt':
             ANSWER =  sqrt(eval(''.join(thein[1:])))
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
        elif origin == 'prime':
            a = prime(int(thein[1]))
            ANSWER = a
        elif origin == 'primerange':
            ANSWER = primerange(thein[1],thein[2])
        elif origin == 'settings':
            changeit = Settings(thein[1:])
        elif origin == 'exit' or origin == 'quit':
            quit()
        elif origin in ['sumlist','sortedlist','meanlist']:
            try:
                newlist = [float(i) for i in thein[1:]]
            except: return "ERROR"
            if origin != 'meanlist':
                #
                ANSWER = eval(str(origin[:-4]) + '(' + str(newlist) + ')')
                #
            else:
                try:ANSWER = sum(newlist)/len(thein)-1
                except:return False
        elif origin == 'sto':
            ID[thein[1]] = thein[2]
            print(ID)
            ANSWER = 'DONE'
        else:
            TI = str(TI)
            try:
                ANSWER = eval(TI)
            except:
                return "xError"
    except FileNotFoundError:
        return "cERROR"
    return ANSWER
answer = 0        
while 1:
    x = input('>>> ')
    if '(' in x:
        answer = string(x, ID, answer)
        
    else:
        answer = main(x,ID,answer)
    print(answer)
