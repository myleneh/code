class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        """
        Adds a new item to the list. It needs the item and returns nothing. 
        Assume the item is not already in the list.
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        """
        Removes the item from the list. It needs the item and modifies the 
        list. Assume the item is present in the list.
        """
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
        """
        Adds a new item to the end of the list making it the last item in the 
        collection. It needs the item and returns nothing. Assume the item is 
        not already in the list.
        """
        current = self.head
        new_item = Node(item)

        # Empty list 
        if current == None:
            self.head = new_item
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(new_item)

    def insert(self, pos, item):
        """
        Adds a new item to the list at position pos. It needs the item and 
        returns nothing. Assume the item is not already in the list and there 
        are enough existing items to have position pos.
        """
        pass

    def index(self, item):
        """
        Returns the position of item in the list. It needs the item and 
        returns the index. Assume the item is in the list.
        """
        current = self.head
        pos = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                pos = pos + 1

        return pos

    def pop(self):
        """
        Removes and returns the last item in the list. It needs nothing and 
        returns an item. Assume the list has at least one item.
        """
        pass

    def pop(self, pos):
        """
        Removes and returns the item at position pos. It needs the position 
        and returns the item. Assume the item is in the list.
        """
        pass
