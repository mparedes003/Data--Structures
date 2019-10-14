from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # we need to increment/increase size by 1
        self.size += 1
        # use add_to_tail() to add the value in a new node
        # to the back/tail of the DLL
        self.storage.add_to_tail(value)

    def pop(self):
        # if there is no node in storage
        if self.storage.tail == None:
            # return None
            return None

        else:
            # use remove_from_tail() to delete the last node/the tail
            self.storage.remove_from_tail()

    def len(self):
        return self.size
