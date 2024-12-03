
#Selection Sorting

# list = [2, 5, 1, 3, 6, 9, 8, 7]

# def selectionsort(list):
#     for i in range(0, len(list)-1):  # Loop through the list
#         cur_min = i
#         for j in range(i + 1, len(list)):  # Compare remaining unsorted part of the list
#             if list[j] < list[cur_min]:  # If found a smaller element, update cur_min
#                 cur_min = j
        
#         # Swap the found minimum element with the first element of the unsorted part
#         list[i], list[cur_min] = list[cur_min], list[i]

# selectionsort(list)
# print(list)

#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////

#Bubble Sorting

# list = [2, 5, 1, 3, 6, 9, 8, 7]


# def bubblesort(list):
#     for i in range(len(list)-1, 0, -1):
#         for j in range(i):
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp

# bubblesort(list)
# print(list)


#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////

#Insertion Sorting

# def insertionsort(List):
#     for i in range(1, len(List)):  # Start from the second element
#         j = i
#         while j > 0 and List[j - 1] > List[j]:  # Compare and shift elements
#             List[j - 1], List[j] = List[j], List[j - 1]  # Swap elements
#             j -= 1

# List = [5, 6, 2, 8, 4, 9]
# insertionsort(List)
# print(List)

#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////

#Quick Sorting