# condition arr[n - 1] < arr[0] is for clockwise rotation
# Array is sorted and rotated in counter- clockwise direction
# if sorted then its False
# From the minimum element to the end of the array, the array is sorted in ascending order.
# From the start of the array to the maximum element, the array is sorted in descending order.
# like 1 is minimum element and 4 is maximum element in the array so 1, 2 will be sorted in ascending order and 3, 4, 5 will be sorted in descending order -> 3 , 4 , 5 , 1 , 2
# 3, 4, 5, 1, 2  if the array is sorted and arr[n-1] < arr[0] -> 2 < 3 -> it will be True if is rotated in counter-clockwise direction
# 1, 2, 3, 4, 5   ->   5, 1, 2, 3, 4  -> 4, 5, 1, 2, 3  -> 3, 4, 5, 1, 2  -> 2, 3, 4, 5, 1 this is the clockwise rotation it will be true main follow condition in code


# steps
# 1. find the minimum element in the array
# 2. find the index of the minimum element
# 3. check if the array is sorted from the minimum element to the end of the array in ascending order
# 4. check if the array is sorted from the start of the array to the maximum element in descending order
# 5. if both the conditions are true and also check if the array is sorted and arr[n-1] < arr[0] then return True else return False


def checkRotatedAndSorted(arr, n):
        minEle = arr[0]
        minIndex = -1

        for i in range(n):
            if arr[i] < minEle:
                minEle = arr[i]
                minIndex = i

        condition1 = True
        for i in range(1, minIndex):
            if arr[i] < arr[i - 1]:
                condition1 = False
                break

        condition2 = True
        for i in range(minIndex + 1, n):
            if arr[i] < arr[i - 1]:
                condition2 = False
                break

        if (condition1 and condition2 and arr[n - 1] < arr[0]):
            return True
        else:
            return False

arr = [3, 4, 5, 1, 2]
n = len(arr)
print(checkRotatedAndSorted(arr, n))


# This code

def checkRotatedAndSorted(arr, n):
    count = 0
    for i in range(n):
        if (arr[i - 1] > arr[i]):
            count += 1
    if (arr[n - 1] > arr[0]):
        count += 1
    return count <= 1






# first find the maximum element in the array
# then check if the left side of the maximum element is sorted in ascending order
# then check if the right side of the maximum element is sorted in descending order
# here the maximum element is 5 right side and left side of the maximum element is smaller than the maximum element


# arr =     [2, 3, 4, 5, 1]
# the pivot element is 5 then right side of that would be smaller element
def findPivot(arr, start, end):
    if start > end:
        return -1
    if start == end:
        return start
    mid = start + (end - start) // 2
    if mid < end and arr[mid] > arr[mid + 1]:    # left side of the pivot element should be smaller than the pivot element
        return mid
    if mid > start and arr[mid] < arr[mid - 1]:     # The condition is true when you take 1 as mid and 5 as mid-1.
        return mid -1
    if arr[start] >= arr[mid]:
        return findPivot(arr, start, mid - 1)
    return findPivot(arr, mid + 1, end)

def checkRotatedAndSorted(arr, n):
    pivot = findPivot(arr, 0, n-1)
    if pivot == -1:
        return False
    if pivot == 0:
        return True
    if arr[0] < arr[n-1]:
        return False
    for i in range(1, pivot+1):
        if arr[i] < arr[i-1]:
            return False
    for i in range(pivot+1, n):
        if arr[i] > arr[i-1]:
            return False
    return True







# Stock Buy and Sell
# The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
# For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
# the maximum profit can earned by buying on day 0, selling on day 3.
# Again buy on day 4 and sell on day 6.
# If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

# 1. Find the local minima and store it as starting index. If not exists, return.
# 2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
# 3. Update the solution (Increment count of buy sell pairs)
# 4. Repeat the above steps if end is not reached.

def stockBuySell(price, n):
    if n == 1:
        return
    i = 0
    while i < n-1:
        while i < n-1 and price[i+1] <= price[i]:  # if you put price[i] <= price[i+1] then it will give you the maximum profit not the minimum profit
            i += 1
        if i == n-1:
            break
        buy = i
        i += 1
        while i < n and price[i] >= price[i-1]:
            i += 1
        sell = i-1
        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)

# arr = [100, 180, 260, 310, 40, 535, 695] n = 7
# i = 0 180 <= 100 --> False
# buy = 0 and i = 1
# i = 180 >= 100 --> True -> i = 2
# i = 260 >= 180 --> True -> i = 3
# i = 310 >= 260 --> True -> i = 4
# i = 40 >= 310 --> False
# sell = 4-1 = 3
# print("Buy on day: ", buy, "\t", "Sell on day: ", sell) --> Buy on day:  0 	 Sell on day:  3
# i = 4
# i = 535 <= 40 --> False
# buy = 4 and i = 5
# i = 535 >= 40 --> True -> i = 6
# i = 695 >= 535 --> True -> i = 7
# i = 7 > 7 --> False
# sell = 7-1 = 6
# print("Buy on day: ", buy, "\t", "Sell on day: ", sell) --> Buy on day:  4 	 Sell on day:  6





# Kadens Algorithm
# maximum subarray sum

def maxSum(arr, n):
    maxEnd = arr[0]
    res = arr[0]
    for i in range(1, n):
        maxEnd = max(maxEnd + arr[i], arr[i])
        res = max(res, maxEnd)
    return res

# arr = [2, 3, -8, 7, -1, 2, 3] n = 7
# maxEnd = 2
# res = 2
# i = 1
# maxEnd = max(2+3, 3) = 5
# res = max(2, 5) = 5
# i = 2
# maxEnd = max(5-8, -8) = -3
# res = max(5, -3) = 5
# i = 3
# maxEnd = max(-3+7, 7) = 7
# res = max(5, 7) = 7
# i = 4
# maxEnd = max(7-1, -1) = 6
# res = max(7, 6) = 7
# i = 5
# maxEnd = max(6+2, 2) = 8
# res = max(7, 8) = 8
# i = 6
# maxEnd = max(8+3, 3) = 11
# res = max(8, 11) = 11
# return 11


---------------- or ----------------

# if there is window of size k then the maximum sum of the subarray of size k is the maximum sum of the window

def maxSum(arr, n, k):
    maxSum = 0
    windowSum = 0
    for i in range(k):
        windowSum += arr[i]
    for i in range(k, n):
        windowSum += arr[i] - arr[i-k]
        maxSum = max(maxSum, windowSum)
    return maxSum

# arr = [2, 3, -8, 7, -1, 2, 3] n = 7 k = 3
# windowSum = 2+3-8 = -3
# i = 3
# windowSum = -3+7 = 4
# maxSum = max(0, 4) = 4
# i = 4
# windowSum = 4-1 = 3
# maxSum = max(4, 3) = 4
# i = 5
# windowSum = 3+2 = 5
# maxSum = max(4, 5) = 5
# i = 6
# windowSum = 5+3 = 8
# maxSum = max(5, 8) = 8
# return 8

