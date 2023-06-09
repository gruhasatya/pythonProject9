def sol(n, start, inter, end):
    if n == 1:
        print(start, end)
    else:
        sol(n-1,start, end, inter)
        print(start, end)
        sol(n-1, inter, start, end)
n = int(input())
print(2**n-1)
sol(n, 1, 2, 3)





def sol1(a, b):
    if b == 0:
        return a
    else:
        return sol1(b, a%b)
a, b = map(int, input().split())
print(sol1(a, b))



def sol3(a, b):
    if b == 0:
        return a
    else:
        return sol3(b, a%b)

    lcm = a*b//sol3(a,b)
    return lcm
a, b = map(int, input().split())
print(sol3(a, b))


def sol4(arr, curr_index, curr_sum):
    if curr_index == len(arr):
        return curr_sum
    else:
        return sol4(arr, curr_index+1, curr_sum+arr[curr_index])


def sol5(arr, curren_element):
    if curren_element == len(arr) -1:
        return arr[curren_element]
    else:
        m = max(arr[curren_element], sol5(arr, curren_element+1))
        return m
arr = [1, 2, 3, 4, 5]
print(sol5(arr, 0))


def sol6(arr, curren_element):
    if curren_element == len(arr) -1:
        return arr[curren_element]
    else:
        m = min(arr[curren_element], sol6(arr, curren_element+1))
        return m

def sol7(s,first, last):
    if last >= first:
        return first
    else:
        s[first], s[last] = s[last], s[first]
        return sol7(s, first+1, last-1)


def sol8(s,start, last):
    if last >= start:
        return start
    else:
        if s[start] == s[last]:
            return sol8(s, start+1, last-1)


def sol9(s, current_index):
    if current_index == len(s):
        return 0
    else:
        return sol9(s, current_index+1) + 1


def sol10(s, char, current_index):
    if current_index == len(s):
        return 0
    else:
        if s[current_index] == char:
            return sol10(s, char, current_index+1)
        else:
            return s[current_index] + sol10(s, char, current_index+1)





def check(int):
    if int%2 == 0:
        return True
    else:
        return False




def index(arr, n):
    if not arr:                                          # base case: empty array
        return -1

    mid = len(arr)//2
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return index(arr[:mid], n)
    else:
        result = index(arr[mid + 1:], n)
        return result + mid + 1 if result != -1 else -1



# gpt ---


def binary_search(arr, target):
    # base case: empty array
    if not arr:
        return -1

    mid = len(arr) // 2
    # base case: target found
    if arr[mid] == target:
        return mid
    # recursive case: search left half
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    # recursive case: search right half
    else:
        result = binary_search(arr[mid+1:], target)
        # if target not found, result will be -1
        if result == -1:
            return -1
        # otherwise, offset the result by the left half's length
        else:
            return result + mid + 1

# gpt ---









