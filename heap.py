class Max_Heap:
    # initializing the constructor with arr (array that we have to convert into heap). The default value is None([])
    def __init__(self, arr):
        # Initializing the heap with no elements in it
        self.heap = []

        # If the array by the user is not empty, push all the elements
        if arr is not None:
            for root in arr:
                self.push(root)


    def print(self):
        print(self.heap)

    # push is used to insert new value to the heap
    def push(self, value):
        # Appending the value given by user at the last
        self.heap.append(value)
        # Calling the bottom_up() to ensure heap is in order.
        # here we are passing our heap
        bottom_up(self.heap, len(self.heap) - 1)

    # push is used to insert new value to the heap
    def pop(self):
        if len(self.heap) != 0:
            # swapping the root value with the last value.

            _swap(self.heap, len(self) - 1, 0)
            # storing the popped value in the root variable

            root = self.heap.pop()

            # Calling the top_down function to ensure that the heap is still in order
            _top_down(self.heap, 0)

        else:
            root = "Heap is empty"
        return root

    # It tells the length of the heap
    def __len__(self):
        return len(self.heap)

    # print the first element (The root)
    def peek(self):
        if len(self.heap) != 0:
            return (self.heap[0])
        else:
            return ("heap is empty")


# Swaps value in heap between i and j index
def _swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


# This is a private function used for traversing up the tree and ensuring that heap is in order
def bottom_up(heap, index):
    # Finding the root of the element
    root_index = (index - 1) // 2

    # If we are already at the root node return nothing
    if root_index < 0:
        return

    # If the current node is greater than the root node, swap them
    if heap[index] > heap[root_index]:
        _swap(heap, index, root_index)
        # Again call bottom_up to ensure the heap is in order
        bottom_up(heap, root_index)


# This is a private function which ensures heap is in order after root is popped
def _top_down(heap, index):
    child_index = 2 * index + 1
    # If we are at the end of the heap, return nothing
    if child_index >= len(heap):
        return

    # For two children swap with the larger one
    if child_index + 1 < len(heap) and heap[child_index] < heap[child_index + 1]:
        child_index += 1

    # If the child node is smaller than the current node, swap them
    if heap[child_index] > heap[index]:
        _swap(heap, child_index, index)
        _top_down(heap, child_index)

    # Making the object of the Heap class and passing the array to convert into heap


m = Max_Heap([1, 2, 3, 4, 5, 6])
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
# print("Root popped:", m.pop())
m.print()