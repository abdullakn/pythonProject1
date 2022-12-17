import sys
from collections import deque

def push(stack, item):
    stack.append(item)


def pop(stack):
    if len(stack) == 0:
        return "stack is empty"
    else:
        return stack.pop()


stack = deque()

ch=''
while ch!=3:
    print("1.Push 2. Pop 3.Exit")
    print("enter your choice")
    ch=int(input())
    if ch==1:
        print("enter the pushed element")
        data=int(input())
        push(stack, data)
        print("stack after popping an element: " + str(stack))
    elif ch==2:
        pop_ele=pop(stack)
        if len(stack) == 0:

            print("stack is empty")
        else:
           print("poped elements",pop_ele)
    else:
        sys.exit(0)

