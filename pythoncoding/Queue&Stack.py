# Queue Implementation using Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data  # Store the data
#         self.next = None  # Pointer to the next node (initially None)

# class Queue:
#     def __init__(self):
#         self.front = None  # Points to the front of the queue
#         self.rear = None   # Points to the rear of the queue
    
#     # Method to check if the queue is empty
#     def is_empty(self):
#         return self.front is None
    
#     # Method to add an element to the queue (enqueue)
#     def enqueue(self, data):
#         new_node = Node(data)
        
#         if self.rear is None:  # If the queue is empty, both front and rear are the new node
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node  # Attach the new node to the rear
#             self.rear = new_node       # Update the rear pointer
    
#     # Method to remove an element from the queue (dequeue)
#     def dequeue(self):
#         if self.is_empty():  # If the queue is empty, return None
#             return None
        
#         removed_node = self.front  # Node to be removed is the front of the queue
#         self.front = self.front.next  # Move the front pointer to the next node
        
#         # If the queue becomes empty, set rear to None
#         if self.front is None:
#             self.rear = None
        
#         return removed_node.data  # Return the data of the removed node
    
#     # Method to get the front element without removing it
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.front.data
    
#     # Method to print the queue
#     def print_queue(self):
#         current = self.front
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage:
# queue = Queue()

# # Enqueueing elements
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)

# # Print the current queue
# queue.print_queue()

# # Dequeue an element
# print("Dequeued:", queue.dequeue())

# # Print the updated queue
# queue.print_queue()

# # Peek the front element
# print("Front element:", queue.peek())

#//////////////////////////////////////////////////////
#//////////////////////////////////////////////////////

#Stack Implementation using Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data  # Store the data
#         self.next = None  # Pointer to the next node (initially None)

# class Stack:
#     def __init__(self):
#         self.top = None  # The top of the stack, initially set to None
    
#     # Method to check if the stack is empty
#     def is_empty(self):
#         return self.top is None
    
#     # Method to add an element to the stack (push)
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top  # Link the new node to the current top
#         self.top = new_node       # Update the top pointer to the new node
    
#     # Method to remove an element from the stack (pop)
#     def pop(self):
#         if self.is_empty():  # If the stack is empty, return None
#             return None
#         popped_node = self.top  # Node to be popped is the top of the stack
#         self.top = self.top.next  # Move the top pointer to the next node
#         return popped_node.data  # Return the data of the popped node
    
#     # Method to get the top element without removing it
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.top.data
    
#     # Method to print the stack elements
#     def print_stack(self):
#         current = self.top
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage:
# stack = Stack()

# # Pushing elements onto the stack
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)

# # Print the current stack
# stack.print_stack()

# # Popping an element from the stack
# print("Popped:", stack.pop())

# # Print the updated stack
# stack.print_stack()

# # Peek at the top element
# print("Top element:", stack.peek())