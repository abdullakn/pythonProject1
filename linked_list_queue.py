import sys
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data, None)

        else:
            node=Node(data, None)
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        if self.get_length() == False:
            print("No elements in Queue")

        else:
            node = self.front
            self.front = node.next


    def print(self):
        # if self.head is None:
        #     print("empty linked list")
        #     return

        ptr = self.front
        link_list = ''
        while ptr:
            link_list += str(ptr.data) + "-->"
            ptr = ptr.next

        print(link_list)

    def get_length(self):
        ptr = self.front
        if ptr is None:
            return False
        else:
            return True


if __name__ == '__main__':

    li = Queue()

    ch = ''
    while ch != 3:
        print("1.Insert 2. Delete 3.Exit")
        print("enter your choice")
        ch = int(input())
        if ch == 1:
            print("enter the inserted element")
            data = int(input())
            li.enqueue(data)
            li.print()
        elif ch == 2:
            li.dequeue()
            li.print()
        else:
            sys.exit(0)



