# list is dynamicallly sized array in python
# list is mutable and contains elements of different data types and duplicates are allowed
# In list append and pop are O(1) operations and insert and delete and search are O(n) operations

# Append()	Add an element to the end of the list
# Extend()	Add all elements of a list to another list
# Insert()	Insert an item at the defined index
# Remove()	Removes an item from the list
# Clear()	Removes all items from the list
# Index()	Returns the index of the first matched item
# Count()	Returns the count of the number of items passed as an argument
# Sort()	Sort items in a list in ascending order
# Reverse()	Reverse the order of items in the list
l = [1,2,3,4,5]
l.reverse()
print(l)

new_list = l[::-1]
print(new_list)


# copy()	Returns a copy of the list
# reduce()	apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value




# sum()	Sums up the numbers in the list  --> to find mean
def mean(arr):
    return sum(arr)/len(arr)






# ord()	Returns an integer representing the Unicode code point of the given Unicode character
# cmp()	This function returns 1 if the first list is “greater” than the second list
# max()	return maximum element of a given list
# min()	return minimum element of a given list
# all()	Returns true if all element is true or if the list is empty
# any()	return true if any element of the list is true. if the list is empty, return false
# len()	Returns length of the list or size of the list
# enumerate()	Returns enumerate object of the list
# accumulate()	apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
# filter()	tests if each element of a list is true or not
# map()	returns a list of the results after applying the given function to each item of a given iterable

# lambda()	This function can have any number of arguments but only one expression, which is evaluated and returned.
# def lambda(a,b): return a+b

# update()     Inserts the specified value at the specified position
def update(arr,idx,element):
    arr[idx] = element
    return arr


# pop()    Removes the element at the specified position
def pop(arr,idx):
    arr.pop(idx)
    arr.append(0)   # insert 0 at the end of the array
    return arr





# initialize the difference to infinity so that the first difference is always less than infinity
diff = float('inf')
def sol1(arr):
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
    return diff

# arr = [1, 5, 3, 19, 18, 25]
# 1st iteration : 5 - 1 = 4 < diff = inf --> diff = 4
# 2nd iteration : 3 - 5 = -2 < diff = 4 --> diff = -2
# 3rd iteration : 19 - 3 = 16 > diff = -2 --> diff = -2
# 4th iteration : 18 - 19 = -1 < diff = -2 --> diff = -1
# 5th iteration : 25 - 18 = 7 > diff = -1 --> diff = -1
# return diff = -1

# explaination :
# 1. Initialize the difference as infinite.
# 2. Compare all the pairs in the given sorted array and keep track of the minimum difference.
# 3. Return the minimum difference.


diff = float('-inf') # initialize the difference to -infinity so that the first difference is always greater than -infinity
def sol2(arr):
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > diff:
            diff = arr[i+1] - arr[i]
    return diff

# arr = [1, 5, 3, 19, 18, 25]
# 1st iteration : 5 - 1 = 4 > diff = -inf --> diff = 4
# 2nd iteration : 3 - 5 = -2 < diff = 4 --> diff = 4
# 3rd iteration : 19 - 3 = 16 > diff = 4 --> diff = 16
# 4th iteration : 18 - 19 = -1 < diff = 16 --> diff = 16
# 5th iteration : 25 - 18 = 7 > diff = 16 --> diff = 7
# return diff = 7




# slicing in python = [start:stop:step] => list, tuple, string and range objects are supported by slicing.




# list comprehension
def get_smaller(arr, num):
    return [i for i in arr if i < num]


l2 = [101, 102, 103]
l3 = ["Rohan", "Harry", "Sohan"]
d3 = {l2[i] : l3[i] for i in range(len(l2))}
print(d3)   # {101: 'Rohan', 102: 'Harry', 103: 'Sohan'}


l4 = ["rohan", "sohan", "mohan"]
l5 = [i.upper() for i in l4 if i.startswith('r')]
print(l5)   # ['ROHAN']


# set comprehension
l = [1, 3, 4, 2, 5]
d1 = {i : i**2 for i in l}
print(d1)   # {1: 1, 3: 9, 4: 16, 2: 4, 5: 25}


d2 = {i : f"Id{i}"for i in range(1, 11)}
print(d2)   # {1: 'Id1', 2: 'Id2', 3: 'Id3', 4: 'Id4', 5: 'Id5', 6: 'Id6', 7: 'Id7', 8: 'Id8', 9: 'Id9', 10: 'Id10'}









def missingNumber(arr, n):
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == mid+1:
            start = mid+1
        else:
            end = mid-1
    return start+1

if __name__ == '__main__':
    arr = [10, 9, 7, 6, 3 ,1, 2, 4, 5
    n = len(arr)
    print(missingNumber(arr, n))







# find kth smallest element

class solution:
    def kthSmallest(self, arr, l, r, k):      # l = 0, r = len(arr)-1  arr = [7, 10, 4, 3, 20, 15]  k = 3
        def partition(arr, l, r):
            pivot = arr[r]                                  # pivot = 15
            i = l-1                                         # i = -1
            for j in range(l, r):                           # j = 0, 1, 2, 3, 4
                if arr[j] < pivot:                          # arr[0] = 7 < 15 --> True i = 0, arr[1] = 10 < 15 --> True i = 1, arr[2] = 4 < 15 --> True i = 2, arr[3] = 3 < 15 --> True i = 3, arr[4] = 20 < 15 --> False
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]         # arr[0], arr[0] = arr[0], arr[0] --> arr[0] = 7 ... arr[3], arr[3] = arr[3], arr[3] --> arr[3] = 3 now arr = [7, 10, 4, 3, 20, 15] loop ends
            arr[i+1], arr[r] = arr[r], arr[i+1]             # arr[3+1], arr[5] = arr[5], arr[3+1] --> arr[4], arr[5] = arr[5], arr[4] --> arr[4] = 15, arr[5] = 20 now arr = [7, 10, 4, 3, 15, 20]
            return i+1                                      # return 4  now it means that the pivot is at the 4th index of the array and all the elements to the left of the pivot are smaller than the pivot
                                                            # and all the elements to the right of the pivot are greater than the pivot

        if l == r:                                          # 0 == 5 --> False
            return arr[l]                                   # return arr[0] --> return 7
        pos = partition(arr, l, r)                          # pos = 4
        if pos == k-1:                                      # 4 == 3-1 --> False
            return arr[pos]                                 # return arr[4] --> return 15
        elif pos > k-1:                                     # 4 > 3-1 --> True
            return self.kthSmallest(arr, l, pos-1, k)       # return self.kthSmallest(arr, 0, 4-1, 3) --> return self.kthSmallest(arr, 0, 3, 3)
        else:                                               # 4 < 3-1 --> False
            return self.kthSmallest(arr, pos+1, r, k)       # return self.kthSmallest(arr, 4+1, 5, 3) --> return self.kthSmallest(arr, 5, 5, 3)



def print2largest(arr, n):
    if n < 2:
        return -1
    arr.sort()
    for i in range(n-2, -1, -1):   # it means that the loop will start from the second last element of the array and will end at the 0th index of the array and will decrement by 1
        if arr[i] != arr[n-1]:
            return arr[i]
    return -1

def print2largest(arr, n):
    if n < 2:
        return -1
    arr.sort()
    largest = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] != largest:
            return arr[i]
    return -1


def print2largest(arr, n):
    if n < 2:
        return -1
    arr.sort()
    largest = float('-inf')
    for i in range(n-1, -1, -1):
        if arr[i] > largest and arr[i] != arr[n-1]:
            largest = arr[i]
            return arr[i]
    return -1





def custom_arrange(arr):
    arr.sort()
    n = len(arr)
    res = []
    start , end = 0, n-1
    while start <= end:
        if start == end:  # if the start and end are equal then it means that there is only one element left in the array and we have to append it to the result array
            res.append(arr[start])
            break
        res.append(arr[end])
        res.append(arr[start])
        start += 1
        end -= 1
    return res




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def reverse(self, head, k):
        if head is None or head.next is None:
            return head
        prev = None
        next = None
        curr = head
        count = 0
        while curr is not None and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        if next_node is not None:
            head.next = self.reverse(next_node, k)   # it means that the head.next will point to the next_node which is the head of the next k nodes
        return prev

