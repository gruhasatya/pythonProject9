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














# XOR subsequences
#
# Problem Description
#
# You are given an array A, you have to create an array which subsequence of A
#
# An array B is called valid if it satisfies both the conditions
#
# 1. B[i] <B[i+1] where 1 <i<|B).
#
# 2. bit count(B[1] ^ .......... AB[i-1] B[i])bit_count(B[i+1]) where 1 <i<|B).
#
# Let X be the Bitwise XOR of all the elements in valid array B.
#
# You need to find the number of different values of X that can be formed.
#
# Note: bit_count(t) is the number of set bits present in the binary representation of t

# input 1:
# A = [1,3,2]
# output 1:
# 4

def sol(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        result = result ^ arr[i]
    return result


arr = [1, 3,2]
print(sol(arr)









