import sys
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None


    def push(self,data):
        if self.head is None:
            self.head = Node(data, None)

        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def pop(self):
        if self.get_length() == False:
            print("No elements in stack")

        else:
            node=self.head
            self.head=self.head.next
            node.next=None



    def print(self):
        # if self.head is None:
        #     print("empty linked list")
        #     return

        ptr=self.head
        link_list=''
        while ptr:
            link_list+=str(ptr.data)+"-->"
            ptr=ptr.next

        print(link_list)


    def get_length(self):
        ptr=self.head
        if ptr is None:
            return False
        else:
            return True

if __name__ == '__main__':

    li = LinkedList()

    ch = ''
    while ch != 3:
        print("1.Push 2. Pop 3.Exit")
        print("enter your choice")
        ch = int(input())
        if ch == 1:
            print("enter the pushed element")
            data = int(input())
            li.push(data)
            li.print()
        elif ch == 2:
            li.pop()
            li.print()
        elif ch == 3:
            li.print()
        else:
            sys.exit(0)



