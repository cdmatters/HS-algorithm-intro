#linearstructures.py 
'''An implementation of the various theoretical data structures 
referred to in the interactive python course: stacks, queues, 
deques and lists'''



class Stack(object):
    '''A stack is an ordered collection of items where items are added
to and removed from the 'top'. ie: Last-In-First-Out (LIFO). They 
require the following operations: 
    push(item)add to top of stack; pop()remove&return from top of stack;
    peek()return top item from stack; isEmpty()boolean check if empty;'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

class Queue(object):
    '''A queue is an ordered collection of items where items are added to the
'rear' or 'bottom' and removed from the 'front' or 'top'. ie: First-In-
Last-Out (FILO). They require the following operations:
    enqueue(item)add to rear of queue; dequeue()remove&return from front queue
    size()return no of items in queue; isEmpty()boolean check if empty;'''
    
    
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Deque(object):
    '''A deque is a double-ended queue, where an ordered collection of items
can be added or removed from either end. Therefore they can operate both LIFO and FIFO.
Correspondingly, there are more methods, below:'''

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

#### LISTS: UNORDERED AND ORDERED

    '''A list is a collection of items where each item holds a relative 
position with respect to all the others. Eg there is a 1st,2nd,3rd item
(unlike a Stack, where you can only peek() the top)...  For simplicity
we will assume you can't have duplicate items.'''
    

    '''UNORDERED LISTS: A collection of items where each item holds a relative position
WRT THE OTHER ITEMS. In other words, the relations between other items
are whats important (like a single linear movement/path through nodes)
    also called a LINKED LIST and requires a NODE '''

class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None    #this is called grounding the node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    #since these nodes only refer one way along string (not back)
    #our class of undordered lists will have to explicitly refer to the 'head' 
    #which you follow until you get to ground

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1 
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        new = Node(item)
        current = self.head

        while current != None:
            if current.next == None:
                current.setNext(new)
                break
            current = current.getNext()

    def index(self, ind):
        current = self.head
        count = 0
        while count<ind :
            current = current.getNext()
            count+=1
        return current

    def insert(self, ind, item):
        infront = self.index(ind)
        print infront.data
        new = Node(item)
        new.setNext(infront)
        if self.head != infront:
            behind = self.index(ind-1)
            behind.setNext(new)
            print behind.data


'''ORDERED LISTS: A collection of items where each item holds a relative
position, based upon an underlying characteristic (ordering either acscending
or descending.  Therefore, they are still linked by nodes, and have VERY similar
methods for most things, for searching searches can STOP when the characteristic
has been passed (ie search for 34 in 1,2,18,54,73,... can stop after 54)
Add, similarly will need to traverse the list, so that the list remains in order.

This means, add is now O(n), in orderd, as opposed to O(1) in unorderd, though,
as it may onlhy be half the distance this can be fine (and is an improvement to 
    unordered search, where every node must be checked).





    


