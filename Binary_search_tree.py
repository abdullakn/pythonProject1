class BinarySearch:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



    def insert(self,data):
        if data==self.data:
            return

        if data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=BinarySearch(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=BinarySearch(data)



def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def build_tree(numbers):
    root=BinarySearch(numbers[0])
    for i in range(1,len(numbers)):
        root.insert(numbers[i])
        return root


if __name__ == '__main__':
    numbers=[17,4,1,20,9,23,18,24]
    number_tree=build_tree(numbers)
    print(number_tree.right.data)
    inorder(number_tree)

