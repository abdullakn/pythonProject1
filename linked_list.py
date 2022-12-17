class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None



    def insert_begining(self,data):
        node=Node(data,self.head)
        self.head=node



    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        ptr=self.head
        while ptr.next:
            ptr=ptr.next

        ptr.next=Node(data,None)



    def delete_specific_value(self,value):

        #delete at begining
        if self.head.data == value:
            self.head=self.head.next
        else:
            ptr=self.head
            while ptr:


                if ptr.next.data == value:
                    ptr.next=ptr.next.next
                    break
                ptr=ptr.next


    def print(self):
        if self.head is None:
            print("empty linked list")
            return

        ptr=self.head
        link_list=''
        while ptr:
            link_list+=str(ptr.data)+"-->"
            ptr=ptr.next

        print(link_list)





    def print_reverse(self):
        ptr = self.head
        link_list = ''
        while ptr:
            if ptr.next == None:

                link_list += str(ptr.data) + "-->"
            ptr = ptr.next

        print(link_list)




    def get_length(self):
        count=0
        ptr=self.head
        while ptr:
            count=count+1
            ptr=ptr.next

        print(count)




    def add_before_node(self,data,index):
        if index<0 and index>=self.get_length():
            print("invalid index")
        else:
            ptr = self.head
            count=0
            while ptr:

                if count == index-1:
                    tmp=ptr.next
                    node = Node(data,ptr.next)
                    ptr.next=node
                    print(node.next.data)
                    # ptr.next.next=tmp
                    # ptr.next.next.data=tmp.data

                    break
                count=count+1
                ptr = ptr.next






    def add_after_node(self, data, index):
        if index < 0 and index >= self.get_length():
            print("invalid index")

        else:
            ptr = self.head
            count = 0
            while ptr:
                if count == index:
                    print(ptr.next.data)
                    tmp=ptr.next
                    node = Node(data, None)
                    ptr.next = node
                    node.next=tmp
                    print(node.next.next.data)
                count = count + 1
                ptr = ptr.next





    def sort(self):

        ptr = self.head
        link_list = ''

        #sorting

        while ptr:
            ptr1=ptr
            while ptr1:
                if ptr1.data < ptr.data :
                    temp=ptr1.data
                    ptr1.data=ptr.data
                    ptr.data=temp
                ptr1=ptr1.next
            ptr=ptr.next

        #Remove Duplicate

        current_node=self.head
        while current_node != None:
            next_node=current_node.next
            while next_node != None and current_node.data == next_node.data:
                next_node=next_node.next

            current_node.next=next_node

            current_node=next_node

        #
        # current_node = self.head
        # next_node = current_node.next
        # while next_node != None :
        #     if current_node.data == next_node.data :
        #         current_node.next = next_node.next
        #     else :
        #         current_node = next_node
        #
        # next_node = next_node.next;











if __name__ == '__main__':
    n=Node()
    li=LinkedList()
    print("Insert some element")
    li.insert_begining(5)
    li.insert_begining(11)

    li.insert_begining(7)
    li.insert_end(10)
    li.insert_end(11)
    li.print()
    print("delete 7 from the list")
    li.delete_specific_value(7)
    li.print()
    print("length of the list")
    li.get_length()

    print("add before node")
    li.add_before_node(30, 2)
    li.print()
    print("add after node")
    li.add_after_node(40, 2)
    li.print()
    print("after sort and  remove duplicate")
    li.sort()
    li.print()
    li.print_reverse()

