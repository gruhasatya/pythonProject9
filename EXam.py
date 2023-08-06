# from functools import reduce
#
# def sol(A):
#     def sol1(n):
#         count = 0
#         while n:
#             count += n & 1
#             n >>= 1
#         return count
#
#     n = len(A)
#     valid_XORs = set()
#     for mask in range(1, 1 << n):
#         subseq = [A[i] for i in range(n) if mask & (1 << i)]
#         if not subseq or subseq != sorted(set(subseq)):
#             continue
#         valid = True
#         for i in range(1, len(subseq) - 1):
#             if sol1(subseq[i-1] ^ subseq[i]) != sol1(subseq[i+1]):
#                 valid = False
#                 break
#         if valid:
#             valid_XORs.add(reduce(lambda x, y: x ^ y, subseq))
#
#     return len(valid_XORs) + 1
#
# A = [1, 100]
# print(sol(A))


# Given two integers ‘a’ and ‘m’. The task is to find the smallest modular multiplicative inverse of ‘a’ under modulo ‘m’
# Example 1:
#
# Input:
# a = 3
# m = 11
# Output: 4
# Explanation: Since (4*3) mod 11 = 1, 4
# is modulo inverse of 3. One might think,
# 15 also as a valid output as "(15*3)
# mod 11"  is also 1, but 15 is not in
# ring {0, 1, 2, ... 10}, so not valid.

# Example 2:
#
# Input:
# a = 10
# m = 17
# Output: 12
# Explanation: Since (12*10) mod 17 = 1,
# 12 is the modulo inverse of 10.

# input : a = 2 , m = 1
# output : -1
# Explanation : Since (2*1) mod 1 = 0,
# 2 does not have any modular
# multiplicative inverse under 1.


#input : a = 6, m = 34
#output : -1
#Explanation : Since (6*6) mod 34 = 12,
#6 does not have any modular
#multiplicative inverse under 34.
#
# def sol(a, m):
#     for i in range(1, m):
#         if (a * i) % m == 1:
#             return i
#     return -1
#
# a = 3
# m = 11
# print(sol(a, m))
#
#
# def mod(a,m):







from typing import List

# class solution:
#     def minimumMagic(self,n:int,m:int,price: List[int],magical_price: List[int]) -> int:
#         dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
#
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 if price[i-1] <= j:
#                     dp[i][j] = max(dp[i-1][j], magical_price[i-1] + dp[i-1][j-price[i-1]])
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         return dp[n][m]

