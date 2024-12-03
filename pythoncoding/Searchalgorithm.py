#linear Search Algorithm

# list = [25, 45, 78, 23, 15]

# def linear(list, target):
#     for i in range(len(list)):
#         if list[i] == target:
#             print("Number Found")
#             return i  # Return the index of the found number
#     print("Number not found")  # This will print once if the number is not found
#     return -1  # Return -1 if the number is not in the list

# linearsearch = linear(list, 23)
# print(linearsearch)


#///////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#Binary Search Algorithm

# list = [25, 45, 125, 90, 78, 23, 100, 600, 35]
# list.sort()  # Sort the list before applying binary search

# def binary(list, target):
#     begin_index = 0
#     end_index = len(list) - 1

#     while begin_index <= end_index:
#         mid = (begin_index + end_index) // 2  # Corrected calculation of mid
#         midpoint_value = list[mid] 

#         if midpoint_value == target:
#             return mid
#         elif target < midpoint_value:
#             end_index = mid - 1
#         else:
#             begin_index = mid + 1

#     return None

# binarysearch = binary(list, 35)
# print(binarysearch)
