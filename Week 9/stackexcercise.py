class LinkedNode:

    def __init__(self, data=None, next= None):
        self._data = data
        if next is None or isinstance(next, LinkedNode):
            self._next = next
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


class LinkedStack():
    
    def __init__(self):
        self._top = None
        self._size = 0

    def __str__(self):
        if self._size==0:
            return "LinkedStack([])"
        else:
            return "LinkedStack([" + str(self._top) + "])"

    def push(self, value=None):
        if value==None:
            raise ValueError("You cannot push an empty item to the stack")
        else:
            newnode = LinkedNode(value, self._top)
            self._top = newnode
            self._size += 1

    def pop(self):
        if self._size==0:
            raise IndexError("STACK EMPTY: CANNOT POP FROM STACK")
        data = self._top.data
        self._top = self._top.tail
        self._size -= 1
        return data

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size==0