#ex3.py 
'''An implementation of the programs made with the linear data structures: Stacks, Queues'''

import linearstructures as ls 
import random


def parChecker(s_string):
    s= ls.Stack()
    balanced = True
    index = 0

    while index < len(s_string) and balanced:
        symbol = s_string[index]
        if symbol in '[{(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                balanced = match(s.pop(), symbol)

        index +=1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def match(left, right):
    opens = '([{'
    closeds = ')]}'

    return opens.index(left) == closeds.index(right)


#print parChecker('{{([][])}()}')
#print parChecker('[{()]')
#print parChecker('({)}')

############################################

def keydictgen(rangeno):
    totalkeys = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,:;!'
    return{i:totalkeys[i] for i in range(rangeno) }

def baseconverter(num, base):
    keydict = keydictgen(base)
    s = ls.Stack()
    while num>0:
        s.push(keydict[num%base])
        num = num/base
    output = ''
    while not s.isEmpty():
        output+=str(s.pop())
    return output

#no = 256

#print no, ' = ', baseconverter(no, 16)

############################################

def to_postfix(string_equation):
    op_parentheses = '({{'
    cl_parentheses = ')}]'
    operators = '+-*/^'
    s = ls.Stack()

 
    in_list = list(string_equation)
    out_list = []
    for i in in_list:
        if i in op_parentheses:
            s.push(i)
        elif i in cl_parentheses:        
            while s.peek() not in op_parentheses:
                out_list.append(s.pop())
            s.pop()
        elif i in operators:
            s.push(i)
        else:
            out_list.append(i)

    return  ''.join(out_list)

#print to_postfix('(5*(3^(4-2)))')
#print to_postfix("(( A + B ) * C)")
#print to_postfix("(A + B * C)")


############################################

class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task(object):
    def __init__(self, time):
        self.timestamp  = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = ls.Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining")%(averageWait, printQueue.size())

for i in range(10):
    simulation(3600, 10)


