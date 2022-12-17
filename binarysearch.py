class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root



def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)



def preorder(root):

    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def find_closest(root,find):
    current_node=root
    closest_data=current_node.val
    while current_node != None:
        if abs(find-closest_data) > abs(find-current_node.val):
            closest_data=current_node.val

        if find < current_node.val:
            current_node=current_node.left
        elif find > current_node.val:
            current_node=current_node.right
        else:
            break
    return closest_data



r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("inorder")
inorder(r)
print("preorder\n")
preorder(r)
print("postorder\n")
postorder(r)
print("\n")

print("closest vales is",find_closest(r,77))