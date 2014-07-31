from math import *
from operator import *
import datetime
from itertools import *
from functools import *
from fractions import * 
print("Welcome to \"Good Calculator\"")
print("Remember, when doing a function, always have '/' in front!")
print("Enter '/dem' for a demonstration")
print("Enter '/help' for help\n\n")
ID = {}  #initial data


def TO(string):
    return string.replace('(', '').replace(')', '')

def demonstrate():
    z = '>>> '
    string = ''
    string += ("This is a demonstration of the implementation of the '/choose' function\n")
    string += (z + '(/choose 3 2) * 2\n')
    string += ('Answer:\n')
    string += ('9\n')
    string += ('\nIt is essential that you use parentheses to alleviate confusion over order of operations.\n')
    string += ("\nHere is a demonstration of a more complex function: The '/loop' function\n")
    string += (z + '/loop i 1 10 1 {/choose 10 i\n')
    string += ('Answer:\n')
    string += ("""\n10
45
120
210
252
210
120
45
10
""")
    string += ("This statement's pythonian equivalent is:\n")
    string += ('for i in range(1,10,1):\n')
    string += ('\tprint(choose(10,i))\n')
    string += ('In addition it saves the loop as a list.\n')
    string += ('For more information on the topics, visit /help')
    return string
    
def evaluate(TI, ID, answer):
    TI = str(TI)
    TI = TI.split()
    unwanted = '___z___z___'
    if 'loop' in TI[0]:
        unwanted = TI[1]    
    for i in TI:
        if i in ID and i != unwanted:
            TI[TI.index(i)] = TI[TI.index(i)].replace(i, "ID['" + i + "']")
    return ' '.join(TI)


def distl(array):
    tup = []
    for i in array:
        if i not in tup:
            tup.append(i)
    return tup


def string(x, ID, answer):
    origin = x 
    while x.count('(') + x.count(')') != 0:
        Oi = 0
        Ei = 0
        for i, n in enumerate(x):
            if n == '(':
                Oi = i
            elif n == ')':
                Ei = i
                break
        newt = x[Oi: Ei + 1]
        newt = evaluate(newt, ID, answer)
        z = main(TO(newt), ID, answer, 1)
        if z == 'ERROR':
            return main(origin, ID, answer, 1)
        x = x.replace(newt, str(z))
    b = main(x, ID, answer, 1)
    if b != 'ERROR':
        return x
    return origin


def factors(number):
    factor = []
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            factor.append(str(i))
            factor.append(str(number//i))
    factor = sorted([int(i) for i in factor])
    return ' '.join([str(i) for i in factor])


def gcf(a,b):
    alist = [int(i) for i in distl(factors(a).split())]
    large = 1
    for i in alist:
        if b%i == 0:
            large = max(i,large)
    return large

def lcm(a,b):
    for n in range(1, b + 1):
        if (a * n)%b == 0:
            return (a * n)

def Help():
    go = ''
    thedict = {'/settings': 'Change Settings', '/prime x': 'Returns 1 if prime, 0 otherwise',\
               '/primerange x y': 'Returns a list of primes from x to y', '/factor x': 'Returns the factors of x',\
               '/sum x y z ...': 'Returns sum of list', \
               '/choose x y ': 'Returns the value of xCy', '/comment abcde': 'Returns the comment',
               '/grade a b c': 'Evaluates as if a is worth 60%, b- 30%, c- 10%',
               '/sqrt x': 'Returns the square root of x', '/sin x': 'Returns sin(x)', \
               '/cos x': 'Returns cos(x)', '/tan x': 'Returns tan(x)', '/mean list': 'Returns the mean of the list',
               '/sorted [list]': 'Returns the the sorted list that was entered.', \
               '/perfect x': 'Returns the boolean value of whether the number is a perfect number',
               '/log [x] y': 'x specifies the base, and y is the value, when x is not there, it is reverted to the common logarithm', \
               '/ln x': 'Returns the natural logarithm of x', '/pascr n': "Returns the n'th row of Pascal's Triangle",\
               '/lcm a b':'Returns the least common multiple of a and b', '/gcf a b':'Returns greatest common factor of a and b',\
               '/loop i begin end step {function ':'Creates a loop for functions to keep iterating','/sto x value':'Store a value for x to continue using',\
               '/dow month day year':'Returns day of the week','/ngon n a':'Lists an "a" amount of n-gons.','/int # base': 'Returns the number in base 10',\
               '/permute a': 'a can be a # or string, it returns the all of the permutations of a','/prod [list]':'Returns the product of the items in the list',\
               '/distl [list]':'Returns all of the distinct items in a list','/exit':'Exits the program',\
               '/filter function a b c d e ...':'Returns a filtered list, make sure your function (e.g. %5==0) has no spaces',\
               '/map function a b c d e ...':'Returns an affected list with each item being affected by the function (e.g. *5, /6)',\
               '/count x a b c d e f ...':'With x being a subset of (a b c d e...), it counts the number of items in the list',\
               '/conc a b c d ...':'It concatenates the terms a b c d',\
               '/simpf x y':'Returns the simplified fraction of x/y',\
               '/trunc x':'Returns the truncated form of x',\
               '/equal a b':'Returns True if a == b, False if not.','/conv n b':'Converts n from base b to base 10',\
               '/pfactor x': 'Returns the prime factorization of x','/not x':'Returns not(x)',\
               '/if statement action':'Returns the action, if the statement is true',\
               }
    items = sorted(thedict.keys())
    go += ('%-20s%-30s' % ('Function', 'Use\n'))
    for i in items:
        go += '\n' + ('%-20s%-30s' % (i, thedict.get(i)))
    return go


def ngon(x, y):
    for i in range(1, int(y) + 1):
        yield ((i ** 2) * (x - 2) - (i * (x - 4))) // 2

def prime(number):    
    if number < 2: return 0
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return 0
    return 1


def primerange(low, high):
    el = [str(i) for i in range(int(low), int(high) + 1)]
    re = ' '.join(list(filter(lambda x: prime(int(x)) == 1, el)))
    return re

def perfrange(low, high):
    a,z = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128,191561942608236107294793378084303638130997321548169216,13164036458569648337239753460458722910223472318386943117783728128],[]
    for i in a:
        if i in range(low,high):
            z.append(str(i))
    return ' '.join(z)
def Settings(MR):
    MR += ' '
    print("Welcome to settings, here you can change and view settings.")
    print("To learn more, enter \"/help\"")
    mode = MR[0]
    if mode == 'ch' or mode == 'change':
        pass
def NintoX(n,x):
    z = 1
    while x % (n**z) == 0:
        z += 1
    return z - 1
def pfactor(n):
    m = n
    n = [int(i) for i in factors(n).split()[1:]]
    n = list(filter(lambda x: prime(x) == 1, n))
    good = []
    for i in n:
        for j in range(NintoX(i,m)):
            good.append(i)
        m /= i**NintoX(i,m)
    return good
def pfactor2(n):
    up = {}
    m = [int(i) for i in factors(n).split()][1:]
    for k in m:
        if not prime(k):
            z = list(filter(lambda x: prime(x) == 1, [int(j) for j in factors(k).split()][1:]))
            for i in z:
                try:
                    if z.count(i) > up[i]:
                        up[i] = z.count(i)
                except:
                    up[i] = z.count(i)
            
    print(up)
def SplitS(string):
    if len(string) == 1:
        string = string[0]
    try:
        string = string.split()
    except:
        pass
    try:
        string = [eval(i) for i in string]
    except:
        pass
    return string
def main(TI, ID, answer, j):  #The Input, Initial Data, answer, eval or not
    equal = partial(lambda x,y: x == y)
    notbad = 0
    LIST = False
    justSTRING = TI.split()
    g = evaluate(TI, ID, answer)
    if '[' in g and ']' in g:
        if g.index('[') != 0:
            if g[g.index('[') -1]== '(' or g[g.index('[')-1] == ' ':
                notbad = 1
        if notbad == 1:
            g = g.replace('[','')
            g = g.replace(']','')
            LIST = True
    if j == 0:
        if 'loop' not in TI:            
            g = string(g, ID, answer)
        else:
            if (TI + '(').index('(') < TI.index('loop'):
                g = string(g, ID, answer)
    if LIST == True:
        return g
    origin = ''
    thein = str(g)
    thein = thein.split()
    ghein = thein
    for n,i in enumerate(ghein):
        try:
            thein[n] = eval(i)
        except:
            pass
        
    try:
        test = list(filter(lambda x: int(x) != x, thein))
    except:
        test = ['nope']

    if test == [] and len(thein) > 1:
        return TI

    try:
        origin = thein[0][1:].lower()
    except:
        pass
    try:
        if origin == 'choose':
            return (factorial(thein[1])) // (factorial(thein[1] - thein[2]) * factorial(thein[2]))
        elif origin == 'factor' or origin == 'factors':
            return factors(thein[1])
        elif origin == 'factorial':
            return factorial(thein[1])
        elif origin == 'comment':
            return TI[9:]
        elif origin == 'conc':
            return ''.join(list(filter(str, justSTRING[1:])))
        elif origin == 'conv':
            return int(str(thein[1]),thein[2])
        elif origin == 'count':
            a = ''.join([str(i) for i in thein[2:]])
            if justSTRING[2] == 'answer':
                a = SplitS(''.join(thein[2:]))
            return a.count(str(thein[1]))
        elif origin == 'dem':
            c = demonstrate()
            return c
        elif origin == 'dow':
            date = datetime.date(int(thein[3]), int(thein[1]), int(thein[2]))
            daychart = ['Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur', 'Sun']
            return daychart[date.weekday()] + 'day'
        elif origin == 'equal':
            return equal(thein[1],thein[2])
        elif origin == 'distl':
            return ' '.join([str(i) for i in distl(thein[1:])])
        elif origin == 'frac':
            return ' '.join(str(Fraction(str(thein[1]))).split('/'))
        elif origin == 'sqrt':
            return sqrt(thein[1])
        elif origin in ['sin', 'cos', 'tan']:
            if thein[2] == 'r':
                return eval(origin + '(int(thein[1]))')
            else:
                return eval(origin + '(radians(int(thein[1])))')
        elif origin == 'help':
            a = Help()
            return a
        elif origin == 'if':
            if thein[1]:
                return thein[2]
        elif origin == 'int':
            return int(str(thein[1]), thein[2])
        elif origin == 'filter':
            go = partial(lambda x: eval('x' + str(justSTRING[1])))
            return ' '.join([str(i) for i in list(filter(go, thein[2:]))])
        elif origin == 'grade':
            return ((thein[1] * 60) + (thein[2] * 30) + (thein[3] * 10)) / 100
            #grade: formative, summative, hw
        elif origin == 'gcf':
            return gcf(thein[1],thein[2])
        elif origin == 'map':
            go = partial(lambda x: eval('x '+ str(justSTRING[1])))
            return ' '.join([str(i) for i in list(map(go, thein[2:]))])
        elif origin == 'lcm':
            return lcm(thein[1],thein[2])
        elif origin == 'len':
            a = len(thein[1:])
            if a == 1:
                if thein[1] == str(thein[1]):
                    a = len(thein[1])
            return a
        elif origin == 'ln':
            return log1p(thein[1] - 1)
            #For log1p it computes ln(x + 1)
        elif origin == 'log':
            if len(thein[1:]) == 2:
                if thein[1] == 2:
                    return log2(thein[2])
                
                else:
                    return log(thein[2]) / log(thein[1])
            else:
                return log10(thein[1])
        elif origin == 'loop':
            DList = []
            if ' in ' not in thein:
                for i in range(int(thein[2]), int(thein[3]), int(thein[4])):
                    z = TI[TI.index('{') + 1:]
                    if thein[1] in z:
                        a = z.index(thein[1])
                        b = z.index(thein[1][-1])
                        z = z.replace(thein[1],str(i))
                        #print(z)
                    DList.append(str(main(z, ID, answer, 0)))
                    #print(DList[-1])
            return '\n'.join(DList)
        elif origin == 'not':
            return not(thein[1])
        elif origin == 'ngon':
            z = [str(j) for j in ngon(thein[1], thein[2])]
            return ' '.join(z)
        elif origin == 'pascr':
            return ' '.join([str(main('/choose ' + str(thein[1]) + ' ' + str(i), ID, answer,0)) for i in range(thein[1] + 1)])
        elif origin == 'perfect':
            return int(thein[1] == sum([int(i) for i in factors(thein[1]).split()[:-1]]))
        elif origin == 'perfrange':
            return perfrange(thein[1], thein[2])
        elif origin == 'perm':
            return (factorial(thein[1]) / (factorial(thein[1] - thein[2])))
        elif origin == 'permute':
            return '\n'.join(distl(list([''.join(i) for i in itertools.permutations(str(thein[1]))])))
        elif origin == 'pfactor':
            return ' '.join([str(i) for i in pfactor(thein[1])])
        elif origin == 'pow':
            return pow(thein[1], thein[2])
        elif origin == 'prime':
            a = prime(int(thein[1]))
            return a
        elif origin == 'primerange':
            return primerange(thein[1], thein[2])
        elif origin == 'prod':
            return reduce(mul, SplitS(thein[1:]), 1)
        elif origin == 'range':
            if len(thein) == 3:
                thein.append(1)
            return ' '.join(str(i) for i in range(thein[1],thein[2],thein[3]))
        elif origin == 'right':
            sides = sorted([thein[1], thein[2], thein[3]])
            if pow(sides[0], 2) + pow(sides[1], 2) == pow(sides[2], 2):
                return 1
            else:
                return 0
        elif origin == 'settings':
            changeit = Settings(thein[1:])
        elif origin == 'simpf':
            great = gcf(thein[1],thein[2])
            return str(thein[1]//great) + ' ' + str(thein[2]//great)
        elif origin == 'str':
            return str(thein[1])
        elif origin == 'trunc':
            return trunc(thein[1])
        elif origin == 'vars':
            print(tuple(ID.keys()))
            return 'done'
        elif origin == 'exit' or origin == 'quit':
            return 'Truth'
        elif origin in ['sum', 'sorted', 'mean']:
            if origin == 'sum':
                origin = 'fsum'
            try:
                newlist = SplitS(thein[1:])
            except FileExistsError:
                return "ERROR"
            if origin != 'mean':
                return eval(str(origin) + '(' + str(SplitS(newlist)) + ')')
            else:
                try:
                    return sum(newlist) / (len(thein) - 1)
                except FileExistsError:
                    return 'ERROR'
        elif origin == 'sto':
            #print(thein)
            ID[thein[1]] = SplitS(thein[2:])
            #print(ID)
            return 'done'
        else:
            try:
                return eval(str(g))
            except KeyboardInterrupt:
                return answer
    except KeyboardInterrupt:
        return answer


answer = 0
done = False
while done == False:
    TheBeginning = input(">>> ")
    answer = main(TheBeginning, ID, answer, 0)
    if answer == 'Truth':
        answer = 'Finished'
        done = True
    print(answer)


