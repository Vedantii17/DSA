# Doubly Linear Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def insert(self, new_node, pos):
        if pos == 1:  # Insert node at first position
            new_node.next = self.head

            if self.head != None:
                self.head.prev = new_node

            self.head = new_node

        else:  # Insert node from 2nd to last position
            p = 1
            temp = self.head

            while(p != pos-1):
                temp = temp.next
                p += 1

            new_node.next = temp.next
            new_node.prev = temp

            if temp.next != None:
                temp.next.prev = new_node

            temp.next = new_node

    def delete(self, value):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:  # First node to delete
            self.head = temp.next

            if self.head != None:
                self.head.prev = None

            temp = None

        else:
            while(temp != None and temp.data != value):
                temp = temp.next

            if temp == None:
                print("Value is not present in the list")
                return

            temp.prev.next = temp.next

            if temp.next != None:
                temp.next.prev = temp.prev

            temp = None

    def print(self):
        print("List elements: ")
        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Creating Linked List
list1 = LinkedList()

n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(55))
list1.append(Node(65))

list1.print()

list1.insert(Node(34), 7)
list1.print()

list1.delete(650)
list1.print()