
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

# def quick_sort(arr):
#     # Base case: If the array has 1 or 0 elements, it's already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Choose a pivot element (here, we choose the last element)
#     pivot = arr[len(arr) - 1]
    
#     # Partition the array into two sub-arrays: less than pivot and greater than pivot
#     left = [x for x in arr[:-1] if x <= pivot]
#     right = [x for x in arr[:-1] if x > pivot]
    
#     # Recursively sort the left and right sub-arrays and combine them with the pivot
#     return quick_sort(left) + [pivot] + quick_sort(right)

# # Example usage:
# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("Sorted Array:", sorted_arr)


#////////////////////////////////////////
#////////////////////////////////////////

# MERGE SORTING

# def merge_sort(arr):
#     # Base case: if the array has 1 or 0 elements, it's already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Find the middle of the array
#     mid = len(arr) // 2
    
#     # Split the array into two halves
#     left_half = arr[:mid]
#     right_half = arr[mid:]
    
#     # Recursively sort the two halves
#     left_sorted = merge_sort(left_half)
#     right_sorted = merge_sort(right_half)
    
#     # Merge the two sorted halves and return the result
#     return merge(left_sorted, right_sorted)

# def merge(left, right):
#     sorted_arr = []
#     i = j = 0
    
#     # Merge the two sorted arrays into one sorted array
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_arr.append(left[i])
#             i += 1
#         else:
#             sorted_arr.append(right[j])
#             j += 1
    
#     # If there are remaining elements in either left or right, append them
#     sorted_arr.extend(left[i:])
#     sorted_arr.extend(right[j:])
    
#     return sorted_arr

# # Example usage:
# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = merge_sort(arr)
# print("Sorted Array:", sorted_arr)