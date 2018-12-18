

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class UnorderedList(object):
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head # New temp.next now holds the value self.head use to hold. That is the node immedaite to it.
        self.head = temp # we replace the value of the original self.next, with our new node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            print("Value: {}".format(current.value))
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True 
            current = current.next

        return False     

    def remove(self, item):
        current = self.head
        previous = None

        while True: # caution, if item does not exist, we have infinit loop
            if current.value == item:
                break
            previous, current = current, current.next # order is important here, previous must first be moved one node ahead to the location of current, after then can the current be moved

        if previous is None:
            self.head = current.next # if the node to be remove is the first node
        else:
            previous.next = current.next

    def append(self, item):
        if self.head is None:
            self.head = Node(item)
            return

        current = self.head
        while (current.next):
            current = current.next

        current.next = Node(item)

    def insert(self, i, item):
        new_node = Node(item)
        if i == 0: # if you want to add right at the begining, use add
            new_node.next = self.head.next
            self.head.next = new_node
            return

        current = self.head
        counter = 0
        previous = None

        while(current.next):
            previous, current = current, current.next
            if i == counter:
                new_node.next = current 
                previous.next = new_node
                break
            
            counter = counter + 1 
       

    def pop(self):
        if self.head is None:
            return None

        current = self.head
        previous = None
        while (current.next):
            previous, current = current, current.next

        previous.next = None

        return current.value

