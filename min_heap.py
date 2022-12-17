class Max_Heap:
    def __init__(self, arr):

        self.heap = []
        if arr is not None:
            for root in arr:
                self.push(root)


    def print(self):
        print(self.heap)


    def push(self, value):

        self.heap.append(value)


        bottom_up(self.heap, len(self.heap) - 1)


    def pop(self):
        if len(self.heap) != 0:
            _swap(self.heap, len(self) - 1, 0)
            root = self.heap.pop()
            _top_down(self.heap, 0)

        else:
            root = "Heap is empty"
        return root


    def __len__(self):
        return len(self.heap)


    def peek(self):
        if len(self.heap) != 0:
            return (self.heap[0])
        else:
            return ("heap is empty")



def _swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]



def bottom_up(heap, index):
    # Finding the root of the element
    root_index = (index - 1) // 2

    # If we are already at the root node return nothing
    if root_index < 0:
        return

    # If the current node is greater than the root node, swap them
    if heap[index] < heap[root_index]:
        _swap(heap, index, root_index)
        # Again call bottom_up to ensure the heap is in order
        bottom_up(heap, root_index)



def _top_down(heap, index):
    child_index = 2 * index + 1
    # If we are at the end of the heap, return nothing
    if child_index >= len(heap):
        return

    # For two children swap with the larger one
    if child_index + 1 < len(heap) and heap[child_index] > heap[child_index + 1]:
        child_index += 1

    # If the child node is smaller than the current node, swap them
    if heap[child_index] < heap[index]:
        _swap(heap, child_index, index)
        _top_down(heap, child_index)




m = Max_Heap([21,6,3,8,91,12])
# Checking the value at top
print("Value at top:", m.peek())
# pushing elements into heap
m.push(1)
m.push(11)
print("Value at top:", m.peek())
# Deleting the root node
print("Root popped:", m.pop())
m.push(7)
m.push(9)
m.push(15)
print("Value at top:", m.peek())
print("Root popped:", m.pop())
print("Root popped:", m.pop())
m.print()