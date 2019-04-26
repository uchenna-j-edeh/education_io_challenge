class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)


    def isEmpty(self):
        if self.head.next_element == None:
            return True
        else:
            return False

            