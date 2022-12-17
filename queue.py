import sys
from collections import deque



queue = deque()
ch = ''
while ch != 3:
    print("1.Insert 2. Delete 3.Exit")
    print("enter your choice")
    ch = int(input())
    if ch == 1:
        print("enter the inserted element")
        data = int(input())
        queue.append(data)
        # push(queue, data)
        print("queue after inserting an element: " + str(queue))
    elif ch == 2:
        if len(queue) == 0:
            print("queue is empty")
        else:
            pop_ele = queue.popleft()
            print("deleted element is ",pop_ele)
    else:
        sys.exit(0)
