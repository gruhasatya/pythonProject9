# def sol(arr):
#     temp = arr[0]
#     # Shift all the elements of the array one position to the left
#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]
#
#         arr[-1] = temp
#     return arr
#
# def sol1(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True
#
# def sol3(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#
# def sol3i(arr, D):
#     n = len(arr)
#     if D == 0:
#         return arr
#     sol3(arr, 0, D-1)   # reverse the first D elements
#     sol3(arr, D, n-1)   # reverse the rest of the elements
#     sol3(arr, 0, n-1)   # reverse the whole array
#     return arr
#
#
# def find_leaders(arr):
#     result = []
#     max = arr[-1]
#     result.append(max)
#     for i in range(len(arr)-2, -1, -1): # start from the second last element and go till the first element in the array
#         if arr[i] > max:
#             max = arr[i]
#             result.append(max)
#     return result[::-1]
#
# arr = [16, 17, 4, 3, 5, 2]
# print(find_leaders(arr))

# def sol5(arr):
#     min = arr[0]
#     max = 0
#     for i in range(1, len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#         else:
#             if arr[i] - min > max:   # if the difference between the current element and the minimum element is greater than the max difference
#                 max = arr[i] - min   # then update the max difference
#     return max
#
# arr = [7, 1, 5, 3, 6, 4]
# print(sol5(arr))























