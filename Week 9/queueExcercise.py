class LinkedNode:

    def __init__(self, data=None, next= None, prev = None):
        self._data = data
        if (next is None or isinstance(next, LinkedNode)) and (prev is None or isinstance(prev, LinkedNode)):
            self._next = next
            self._prev = prev
        else:
            raise TypeError('Node type object expected!')
        

    def __str__(self):
        """
        Note, this is a recursive method (implicit via str()). As you can see
        recursion can be used for linked list.
        """
        if self._data is None:
            return ''
        elif self._next is None:
            return str(self._data)
        else:
            return str(self._data) + ', ' + str(self._next)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def tail(self):
        return self._next

    @tail.setter
    def tail(self, node):
        if node is None or isinstance(node, LinkedNode):
            self._next = node
        else:
            raise TypeError('Node type object expected!')

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        if node is None or isinstance(node, LinkedNode):
            self._prev = node
        else:
            raise TypeError('Node type object expected!')


class LinkedQueue:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value=None):
        if value==None:
            raise ValueError("Cannot push None to a queue")
        else:
            #newnode = LinkedNode(value, self._tail, self._head) #point down direction of q
            self._size += 1
            if self._size==0:
                newnode = LinkedNode(value, self._tail, self._head) #point down direction of q
                self._head = newnode
                self._tail = newnode
            else:
                newnode = LinkedNode(value, self._tail, None) #point down direction of q
                self._tail.prev = newnode
                self._tail = newnode

    def pop(self):
        if self._size==0:
            raise IndexError("QUEUE EMPTY: CANNOT POP FROM AN EMPTY QUEUE")
        else:
            self._size -= 1
            data = self._head.data
            self._head = self._head.prev
            return data
                
    def peek(self):
        if self._size==0:
            raise IndexError("QUEUE EMPTY: CANNOT PEEK ON AN EMPTY QUEUE")
        else:
            return self._head.data

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size==0