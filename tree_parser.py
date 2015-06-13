import operator
################################
#####  DATA STRUCTURES
################################

class Stack(object):

    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def push(self, a):
        self.items.append(a)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class BinaryTree(object):

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left_child(self, new_node):
        tree = BinaryTree(new_node)
        if self.left_child == None: #redundacy for clarity
            self.left_child = tree  
        else:
            tree.left_child = self.left_child
            self.left_child = tree  

    def insert_right_child(self, new_node):
        tree = BinaryTree(new_node)    #no redundancy
        tree.right_child = self.right_child
        self.right_child = tree

    def get_root_value(self):
        return self.key

    def set_root_value(self, val):
        self.key = val



class BinaryHeap():
    """implement using a list. since binary, for parent node p, children at 2p, 2p+1
    Can search along list, and eradicate blocks as multiples of 2."""
    
    def __init__(self, build=[]):
        self.hlist = [0]
        self.hsize = 0

        self.build_heap(build)

    def insert(self, k):
        self.hlist.append(k)
        self.hsize = self.get_size()
        self.perc_up(self.hsize)
        pass

    def find_min(self):
        return h.self[0]

    def del_min(self):
        rootval = self.hlist[1]
        self.hlist[1] = self.hlist.pop()
        self.get_size()
        self.perc_down(1)
        return rootval

    def is_empty(self):
        return get_size() == 0

    def get_size(self):
        self.hsize = len(self.hlist) - 1
        return self.hsize

    def build_heap(self, raw):
        self.hlist = [0] + raw[:]
        i = self.get_size()/2
        while i > 0:
            self.perc_down(i)
            i -=1

    def perc_up(self, i):
        """percolate a node up from bottom"""
        while i / 2  > 0:
            if self.hlist[i] < self.hlist[i/2]:
                self.hlist[i], self.hlist[i/2] = self.hlist[i/2], self.hlist[i]
            i = i/2

    def perc_down(self, i):
        """percolate a node down from root"""
        while i*2< self.hsize:
            mc = self.find_min_child(i)
            if self.hlist[i] > self.hlist[mc]:
                self.hlist[i], self.hlist[mc] = self.hlist[mc], self.hlist[i]
            i = mc

    def find_min_child(self, i):
        if i*2 + 1 >self.hsize:
            return i * 2
        else:
            if self.hlist[i*2] < self.hlist[i*2 +1]:
                return i*2
            else:
                return i*2 + 1

    # def __str__(self):
    #     string = ''
        
    #     def max_level(k):
    #         tally = 1
    #         while k>0:
    #             tally +=1
    #             k= k/2
    #         return tally

    #     rows = max_level(self.hsize)

    #     for level in range(rows):
    #         for i, x in enumerate(self.hlist):
    #             if i ==0:
    #                 pass
    #             else:
    #                 if (i//2**level) == 0 and (i//2**(level-1) != 0):
    #                     string += ' '*(rows-level) + str(x)

    #         string+= '\n' + ' '*(rows-level)
    #     return string
            

class TreeNode(object):
    
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right 
        self.parent = parent

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child==self

    def is_right_child(self):
        return self.parent and self.parent.right_child==self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.right_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left_child = lc
        self.right_child = rc
        if lc is not None:
            self.left_child.parent = self
        if rc is not None:
            self.right_child.parent = self

    def find_successor(self):
        succ = None
        if self.right_child:  #not only this if necc for deleting
            succ = self.right_child.find_min()
        else:   
            if self.parent:  
                if self.is_left_child(): #only left child, is a left child
                    succ = self.parent
                else:
                    self.parent.right_child = None  #only left child, is a right child
                    succ = self.parent.find_successor()   #(find succ by repeating on parent no node
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.left_child is not None:
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent

            else:
                if self.is_left_child:
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent








class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k,v)

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, key):
        if self._get(self, key, self.root):
            return True 
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)


    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size +=1

    def _put(self, key, value, this_node):    
        """helper for putting"""
        if key> this_node.key:
            if this_node.right_child:
                self._put(key, value, this_node.right_child)
            else:
                this_node.right_child = TreeNode(key, value, parent=this_node) 
        elif key < this_node.key:
            if this_node.left_child:
                self._put(key, value, this_node.left_child)
            else:
                this_node.left_child = TreeNode(key, value, parent=this_node)
        else:
            this_node.payload = value

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
        else:
            return None

    def _get(self, key, this_node):
        if not this_node:
            return None        
        elif key == this_node.key:
            return this_node       
        elif key<this_node.key:
            return self._get(key, this_node.left_child)
        elif key>this_node.key:
            return self._get(key, this_node.right_child)

    def delete(self, key):
        if self.size>1:
            node_out = self._get(key, self.root)
            if node_out:
                self._remove(node_out)
                self.size -=1
            else:
                raise KeyError('Error, key not in Tree')
        elif self.size ==1 and self.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in Tree')


    
    def _remove(self, this_node):
        if this_node.is_leaf():  #leaf
            if this_node.is_left_child():
                this_node.parent.left_child = None
            elif this_node.is_right_child():
                this_node.parent.right_child = None
            this_node.parent = None

        elif this_node.has_both_children(): #both children
            succ = this_node.find_successor()
            succ.splice_out()
            this_node.key = succ.key
            this_node.payload = succ.payload

        else: #one child
            if this_node.left_child:
                if this_node.is_left_child():
                    this_node.parent.left_child=this_node.left_child
                    this_node.left_child.parent=this_node.parent
                elif this_node.is_right_child():
                    this_node.parent.right_child=this_node.left_child
                    this_node.left_child.parent=this_node.parent
                else:
                    this_node.replace_node_data(this_node.left_child.key,
                                                this_node.left_child.payload,
                                                this_node.left_child.left_child,
                                                this_node.left_child.right_child)
            else: 
                if this_node.is_left_child():
                    this_node.parent.left_child=this_node.right_child
                    this_node.right_child.parent=this_node.parent
                elif this_node.is_right_child():
                    this_node.parent.right_child=this_node.right_child
                    this_node.right_child.parent=this_node.parent
                else:
                    this_node.replace_node_data(this_node.right_child.key,
                                                this_node.right_child.payload,
                                                this_node.right_child.left_child,
                                                this_node.right_child.right_child)










###############################
########## PARSER  ############              
###############################

def build_parse_tree(math_string):

    math_list = list(math_string)
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)

    current_tree = tree

    for i in math_list:
        if i in '([{':
            current_tree.insert_left_child('')
            stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i in '1234567890':
            current_tree.set_root_value(current_tree.get_root_value() + i)
        elif i in '*/+-%':
            current_tree = stack.peek()
            current_tree.set_root_value(i)
            current_tree.insert_right_child('')
            current_tree = current_tree.right_child
        elif i in ')}]':
            current_tree = stack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return tree

def evaluate(tree):
    ops = {'*': operator.mul, "/": operator.truediv,
            '+': operator.add, '-': operator.sub, '%': operator.mod}

    if tree.right_child == None and tree.left_child==None:
        return int(tree.get_root_value())
    else:
        fn = ops[tree.get_root_value()]
        return fn(evaluate(tree.left_child) , evaluate(tree.right_child))

def binary_tree_traversal(tree):
    if tree:
        print tree.get_root_value()
        tree_traversal(tree.get_left_child())
        tree_traversal(tree.get_right_child())

def bst_tree_traversal(tree):
    
    def _bst_trav(this_node):
        if this_node:
            
            _bst_trav(this_node.get_left_child())
            print this_node.key
            _bst_trav(this_node.get_right_child())
    
    _bst_trav(tree.root)


################################
#### BINARY HEAP IMPLEMENTATION
################################




        

if __name__ == "__main__":
    # ex_tree = build_parse_tree('((1+(3*7))*(4%5))')
    # print evaluate(ex_tree)
    # binary_tree_traversal(ex_tree)
    
    # bheap = BinaryHeap([15,61,33,47,12,45,7,9,38,72,56,18,9])
    # [bheap.insert(x) for x in [4,5,6,7,3,9,1,10]]
    # bheap.del_min()
    # print bheap

    bst = BinarySearchTree()
    bst.put(5, 'ya')
    bst.put(7, 'yo')
    bst.put(3, 'you')
    bst.put(6, 'zup')
    bst.put(10, 'hey')
    bst.put(4, 'soo')

    print bst.get(6)
    bst_tree_traversal(bst)
    bst.delete(3)
    bst_tree_traversal(bst)

     






