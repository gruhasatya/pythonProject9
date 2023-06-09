# 1. Find the minimum element in the unsorted array and swap it with the element at the beginning.
# explnation : repeat this process n - 1 times to get the sorted array.
# 24. The algorithm can be implemented as follows (with 0-based indexing):
# 25. for i = 0 to n - 2
# 26.     min = i
# 27.     for j = i + 1 to n - 1
# 28.         if A[j] < A[min]
# 29.             min = j
# 30.     swap A[i] and A[min]
# 31. end for
# 32. The algorithm can be implemented with a single loop by keeping track of both the minimum and maximum elements seen so far:
# 33. for i = 0 to ⌊n / 2⌋
# 34.     min = i
# 35.     max = i
# 36.     for j = i + 1 to n - i - 1
# 37.         if A[j] < A[min]
# 38.             min = j
# 39.         else if A[j] > A[max]
# 40.             max = j
# 41.     swap A[i] and A[min]
# 42.     swap A[n - i - 1] and A[max]
# 43. end for
# 44. The algorithm can also be implemented recursively:
# 45. selection_sort(A, n, i)
# 46.     if i == n - 1
# 47.         return
# 48.     min = i
# 49.     for j = i + 1 to n - 1
# 50.         if A[j] < A[min]
# 51.             min = j
# 52.     swap A[i] and A[min]
# 53.     selection_sort(A, n, i + 1)
# 54. end selection_sort
# 55. The algorithm can also be implemented using recursion with a single loop:
# 56. selection_sort(A, n, i)
# 57.     if i == ⌊n / 2⌋
# 58.         return
# 59.     min = i
# 60.     max = i
# 61.     for j = i + 1 to n - i - 1
# 62.         if A[j] < A[min]
# 63.             min = j
# 64.         else if A[j] > A[max]
# 65.             max = j
# 66.     swap A[i] and A[min]
# 67.     swap A[n - i - 1] and A[max]
# 68.     selection_sort(A, n, i + 1)
# 69. end selection_sort
# 70. The algorithm can also be implemented using recursion with a single loop and without swapping:
# 71. selection_sort(A, n, i)
# 72.     if i == ⌊n / 2⌋
# 73.         return
# 74.     min = i
# 75.     max = i
# 76.     for j = i + 1 to n - i - 1
# 77.         if A[j] < A[min]
# 78.             min = j
# 79.         else if A[j] > A[max]
# 80.             max = j
# 81.     swap A[i] and A[min]
# 82.     swap A[n - i - 1] and A[max]
# 83.     selection_sort(A, n, i + 1)
# 84. end selection_sort
# 85. The algorithm can also be implemented using recursion with a single loop and without swapping and without using the min and max variables:
# 86. selection_sort(A, n, i)
# 87.     if i == ⌊n / 2⌋
# 88.         return
# 89.     for j = i to n - i - 1
# 90.         if A[j] < A[i]
# 91.             swap A[i] and A[j]
# 92.         else if A[j] > A[n - i - 1]
# 93.             swap A[n - i - 1] and A[j]
# 94.     selection_sort(A, n, i + 1)
# 95. end selection_sort
# 96. The algorithm can also be implemented using recursion with a single loop and without swapping and without using the min and max variables and without using the i variable:
# 97. selection_sort(A, n, i)
# 98.     if i == ⌊n / 2⌋
# 99.         return
# 100.     for j = 0 to n - 1
# 101.         if A[j] < A[0]
# 102.             swap A[0] and A[j]
# 103.         else if A[j] > A[n - 1]
# 104.             swap A[n - 1] and A[j]
# 105.     selection_sort(A, n, i + 1)
# 106. end selection_sort
