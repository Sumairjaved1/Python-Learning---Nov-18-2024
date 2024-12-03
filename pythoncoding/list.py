# import csv

# with open('test.csv', 'w', newline='') as fp:
#       fieldnames = ["Name", "Age", "School"]
#       a = csv.DictWriter(fp,fieldnames=fieldnames, delimiter= "\t")
#       a.writeheader()
#       a.writerows([{"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"}])

# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})

# import csv

# with open('annual.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     counts = {}
#     for row in reader:
#         fav = row["Units"]
#         if fav in counts:
#             counts[fav] += 1
#         else:
#             counts[fav] = 1
# for fav in counts:
#     print(f"{fav}: {counts[fav]}")


#//////////////////////////////////////////////////////////////////////////

#LINKED LIST

# class Node:
#     def __init__(self, data):
#         self.data = data  # Node data
#         self.next = None  # Pointer to the next node (initially None)

# class LinkedList:
#     def __init__(self):
#         self.head = None  # The head of the list, initially set to None

#     # Method to append a new node at the end of the list
#     def append(self, data):
#         new_node = Node(data)
        
#         if not self.head:  # If the list is empty, the new node becomes the head
#             self.head = new_node
#         else:
#             last_node = self.head
#             while last_node.next:  # Traverse to the last node
#                 last_node = last_node.next
#             last_node.next = new_node  # Set the next of the last node to the new node
    
#     # Method to print the linked list
#     def print_list(self):
#         current_node = self.head
#         while current_node:  # Traverse through the list
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")  # Indicate the end of the list

# # Example usage:
# linked_list = LinkedList()

# # Adding nodes to the linked list
# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)
# linked_list.append(40)

# # Printing the linked list
# linked_list.print_list()

#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////



      

