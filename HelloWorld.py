def sol(n):
  return abs(n)


def sol1(n):
  if n < 0:
    return -n
  else:
    return n



def celsiustofarenheat(n):
  sol = n * 9/5 + 32
  return sol



def count_digits(n):
  count = 0
  while n != 0:
    n //= 10                 # to looose the last number
    count += 1              # increment count while lossing the number
  return count




# question palindrome number

# palindrome first create a copy of n and have a reverse variable then while loop till and  get the last element of n using %
# and store at as last digit  and now reverse variable multiply with 10 to keep up places and then add last digit
# now remove the last digit from copy and return to check whethere n == reverse or not


def Palindrome_number(n):
  reverse = 0
  copy = n
  while copy > 0:                            # goes on till copy is greater then 0 if its less stops
    last_digit = copy%10                     # takes last digit of n ex : 1221 -- 1 
    reverse = reverse * 10 + last_digit     # 0*10+1 = 1, 1*10 + 2 = 12, 12*10+2= 122, 122*10+1= 1221
    copy = copy//10                          # removes the last digit of copy
  
  if n == reverse:
    return True
  else:
    return False




# question digit to factorial

def digit_to_factorial(n) :            # n = 5
  if n == 0 or n == 1:
    return 1
  elif n < 0:
    return 0
  else:
    fact = 1
    for i in range(1, n+1):
      fact = fact * i            # fact = 1*1 = 1, 1*2 = 2, 2*3 = 6, 6*4 = 24, 24*5 = 120
    digits = 0                   # to count the digits = 0
    while digits:                # goes on till digits is not 0
      digits += 1                #  digits = digits + 1 , 1, 2, 3
      fact = fact // 10          #  fact = 120//10 = 12, 12//10 = 1, 1//10 = 0
    return  digits               #  return digits = 3



# question factorial of a number

def factorial(n):
  if n == 0 or n == 1:
    return 1
  elif n < 0:
    return 0
  else:
      fact = 1
      for i in range(1, n+1):
        fact = fact * i
      return fact
      




                                                                                         # question count zeroes in factorial of a number

def zeroes(n):
  if n == 0 or n == 1:
    return 1
  elif n < 0:
    return 0
  else:
    fact = 1
    for i in range(1, n+1):
      fact = fact *1
    digits = 0
    while digits % 10 == 0:                  # if the last digit is 0 then it will go on till the last digit is not 0
        digits += 1
        fact = fact // 10                   # removes the last digit
    return digits





                                                                                        # question count five in factorial of a number d



def factorial(n):
    if n == 0 or n == 1:
      return 1
    elif n < 0:
      return 0
    else:
      fact = 1
      for i in range(1, n+1):
        fact = fact * i
      count = 0
      while n >= 5:               # if the number is greater then 5 then it will go on till the number is less then 5
        n = n // 5                # removes the last digit  ex : 25 // 5 = 5 => 5 // 5 = 1
        count += n                # increment count by n which is 5 + 1 = 6
      return count                # return the count which is 6

if __name__ == "__main__":
  n = int(input())
  print(factorial(n))



                                                                                          # question count trailing zeroes in factorial of a number





def findTrailingeros(n):
  # Initialize result
  count = 0

  # Keep dividing n by
  # powers of 5 and

  # update Count
  i = 5
  while (n / i >= 1):       # if 100 / 5 >= 1 = True, 100 / 25 >= 1 = True, 100 / 125 >= 1 = False
    count += int(n / i)     # count = count + int(100 / 5) = 20, count = 20 + int(100 / 25) = 24
    i *= 5                  # i = 5 * 5 = 25, i = 25 * 5 = 125 , it will go on till the condition is false

  return int(count)


# Driver program
n = 100
print("Count of trailing 0s " +
      "in 100 ! is", findTrailingZeros(n))










                                                   # ------------------------------------------------------- greatest common Devisor  ------------------------------------------------------- #

def gcd(a, b):
  gcd = 1
  for i in range(1, min(a, b) + 1):          # goes on till the min of a and b ex : 12 and 15 => 12 + 1 = 13
    if a % i == 0 and b % i == 0:            # if a and b are divisible by i then it will go on till the min of a and b, 12 % 1 ==0 and 15 % 1 == 0
      gcd = i                                # gcd = 1
    return gcd                               # return gcd which is 1


def gcd(a,b):
  gcd = 1
  for i in range(min(a,b), 0, -1):           # goes till 13 to 1 in reverse order
    if a % i == 0 and b % i == 0:            # if a and b are divisible by i then it will go on till the min of a and b, 12 % 1 ==0 and 15 % 1 == 0
        gcd = i
        break
  return gcd



def gcd(a,b):
  if b == 0:      # # or  while b!=0 both same
    return a
  else:
    return gcd(b, a%b)
# ------------------------------------ or ------------------------------------
def gcd(a, b):
  while  b != 0:
    a, b = b, a % b
  return a






def gcd(a, b):           # 12, 15
  while a != b:
    if a > b:            # 12 > 3 = True, 9 > 3 = True, 6 > 3 = True
      a = a - b          # 12 - 3 = 9, 9 - 3 = 6, 6 - 3 = 3
    else:
      b = b - a          # 12, 3
  return a






                                                                                                 # Recursive function to return gcd of a and b
def gcd(a, b):

	# Everything divides 0
	if (a == 0):
		return b
	if (b == 0):
		return a

	# base case
	if (a == b):
		return a

	# a is greater
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)

# Driver program to test above function
a = 98
b = 56
if(gcd(a, b)):
	print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
	print('not found')






# LCM
# if a = 4 and b = 6 then LCM = 12         # if a%b == 0 and b%a == 0 then LCM = a*b => 4*6 = 24 => 24/12 = 2 => LCM = 12
# if a = 12 and b = 15 then LCM = 60
# if a = 2 and b = 8 then LCM = 8
# if a = 3 and b = 7 then LCM = 21

def lcm(a, b):
  res = max(a, b)                         # res = 15
    while True:
        if res % a == 0 and res % b == 0: # 15 % 12 == 3 and 15 % 15 == 0 => 16 % 12 == 4 and 16 % 15 == 1 =>... => 60 % 12 == 0 and 60 % 15 == 0
          return res
        res += 1

    return res



def lcm(a, b):
  res = max(a,b)
  while True:
    if res % a == 0 and res % b == 0:
      return res
    res += 1
  return res



                                                                                                               # check for prime:

def prime(n):
  if n == 1:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
    return True

def prime(n):                      # 37
  if n == 1:
    return False
  i = 2                           # it uses power concept to check prime number because all the prime numbers cannot be divided by 2
  while(i * i <= n):              # 2 * 2 <= 37 => 4 <= 37 => 9 <= 37 => 16 <= 37 => 25 <= 37 => 36 <= 37 => 49 > 37
    if n % i == 0:                # 37 % 2 == 1 => 37 % 3 == 1 => 37 % 4 == 1 => 37 % 5 == 2 => 37 % 6 == 1 => 37 % 7 == 2  till last 37 % 36 == 1
      return False
    i += 1
    return True                 # 37 is a prime number


# explanantion of the above code: to check prime number

# [2,3,5,7,11,13,17,19,23,29,31,37]

def prime(n):
  if n == 1:
    return False
  if n == 2 or n == 3:               # 2 and 3 are prime numbers
    return True
  if n%2 == 0 or n%3 == 0:           # if n is divisible by 2 or 3 then it is not a prime number
    return False
  i = 5                              # 5 is the first prime number
  while (i*i<=n):                    # 5 * 5 <= 37 => 25 <= 37 => 36 <= 37 => 49 > 37
    if n%i == 0 or n%(i+2) == 0:     # if n is divisible by 5 or 7 then it is not a prime number
      return False
    i = i+6                          # 5 + 6 = 11
  return True





def Prime(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

def primeFactors(n):
  for i in range(2, n+1):
    if Prime(i):
      x = i                               # x = 2 , 4 , 8
      while n % x == 0:                   # 100 % 2 == 0 -> print 2 -> x = 2 * 2 = 4 -----> 100 % 4 == 0 -> print 2 -> x = 4 * 2 = 8  ---> 100 % 8 == 4  breaks loop and goes to next iteration
        print(i)
        x = x * i
primeFactors(100)


# for loop - 3 iteration
# if 3 is prime False
# for loop - 4 iteration
# if 4 is prime False
# for loop - 5 iteration
# if 5 is prime True and x = 5
# while 100 % 5 == 0 -> print 5 -> x = 5 * 5 = 25  ----> 100 % 25 == 0 -> print 5 -> x = 25 * 5 = 125  ---> 100 % 125 == 100 Breaks the loop and goes to next iteration
# for loop - 6 iteration
# if 6 is prime False
# ....................
# for loop- 100 iteration
# if 100 is prime False


# prime factorization
# 100 = 2 * 2 * 5 * 5

def prime(n):
  if n == 1:
    return False
  for i in range(2, n):
    if n%i == 0:
      return False
  return True

def primefactor(x):
  for i in range(2, n+1):
    if prime(i):
      while x%i == 0:
        print(i)
        x = x*i
primefactor(100)





def all_divisors(n)
  for i in range(1, n+1):
    if n%i == 0:
      print(i)

all_divisors(100)
# output: 1, 2, 4, 5, 10, 20, 25, 50, 100

# efficient solution
# 1 - divisorss always come in pairs
#          30 - (1, 30), (2, 15), (3, 10), (5, 6)
# 2 - one of the pair is always less than or equal to sqrt(n)
#          30 - (1, 30), (2, 15), (3, 10), (5, 6), (6, 5), (10, 3), (15, 2), (30, 1)
# 3 - if n is a perfect square then the pair will be equal
#          36 - (1, 36), (2, 18), (3, 12), (4, 9), (6, 6), (9, 4), (12, 3), (18, 2), (36, 1)

def all_divisors(n):              # 36
  i = 1
  while i*i <= n:                  # 1 * 1 = 1 < 36 => 2 * 2 = 4 < 36 => 3 * 3 = 9 < 36 => 4 * 4 = 16 < 36 => 5 * 5 = 25 < 36 => 6 * 6 = 36 = 36
    if n%i == 0:
      print(i)                    # 1, 2, 3, 4, 6, 9, 12, 18, 36
        if i != n/i:              # it is used to check n/i value is alredy printed or not if not it will print the pair if already printed it will not print
          print(n/i)              # 36/1 =  36, 36/2 = 18, 36/3 = 12, 36/4, 36/6 = 6
  i += 1

all_divsors(36)


# in sorted way

def all_divsors(n):
  i = 1
  while i*i < n:
    if n%i == 0:
      print(i)
    i += 1
  while i >= 1:
    if n % i == 0:
      print(n/i)
    i -= 1












# A Better (than Naive) Solution to find all divisors
import math


# method to print the divisors
def printDivisors(n):
  # Note that this loop runs till square root
  i = 1
  while i <= math.sqrt(n):

    if (n % i == 0):

      # If divisors are equal, print only one
      if (n / i == i):
        print(i, end=" ")
      else:
        # Otherwise print both
        print(i, int(n / i), end=" ")
    i = i + 1


# Driver method
print("The divisors of 100 are: ")
printDivisors(100)





# given a positive integer value N. the task is tofind how many numbers less than or equal to N have number of divsors exactly to 3
# input  : 6
# output : 1
# the only number less than or equal to 6 that has exactly 3 divisors is 4

# input  : 10
# output : 2
# the only number less than or equal to 10 that has exactly 3 divisors is 4 and 9

# how to solve this problem
# 1 - find all the divisors of all the numbers less than or equal to N
# 2 - count the number of divisors of each number
# 3 - if the number of divisors is exactly 3 then increment the count




  class Solution:
    def exactly3Divisors(self, N):
      def prime(n):
        if n < 2:
          return False
        for i in range(2, int(math.sqrt(n)) + 1):
          if n % i == 0:
            return False
        return True

      count = 0
      for i in range(2, int(math.sqrt(N)) + 1):
        if i * i <= N and prime(i):
          count += 1
      return count




# efficient solution

  # for i in range(1, int(math.sqrt(N)) + 1): it is used to check the number is less than or equal to sqrt(N)
  # For example, let's say n is 100. The square root of 100 is 10. If we check all possible factors of 100 up to 10, we will find that 2, 4, 5, and 10 are factors of 100,
  # and we don't need to check any factors greater than 10, because any factors greater than 10 must correspond to factors less than 10 that we have already checked.
  # So, for example, if we were to check if 20 is a factor of 100, we would find that 100/20 is 5, which is a factor of 100 that we have already checked. Therefore, we don't need to check 20 as a factor of 100.


  def prime(n):
    if n < 2:
      return False
    for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
    return True


# i*i <= n is used to check the number is less than or equal to n
# For example, let's say we have the number 16. It has three divisors: 1, 2, and 4. We know that 1 and 16 are divisors,
# so we just need to find one more divisor that is a square root of 16. That divisor is 4, which is the square of 2, a prime number.
def exactly3Divisors(n):
  count = 0
  for i in range(1, n + 1):
    if i * i <= n and prime(i):
      count += 1
  return count


n = 6
result = exactly3Divisors(n)
print(result)




def sol(n):
  if n <= 1:
    return False
  prime = [True]*(n+1)
  i = 2
  while i*i <= n:
    if prime[i] == True:
      for j in range(2*i, n+1, i):
        prime[j] = False
    i += 1
    for i in range(2, n+1):
      if prime[i]:
        print(i, end=" ")







def sol(n):
  if n <= 1:
    return False
  prime = [True]*(n+1)
  i = 2
  while i*i <= n:
    if prime[i] == True:
      for j in range(i*i, n+1, i):
        prime[j] = False
    i += 1
  for i in range(2, n+1):
    if prime[i]:
      print(i, end=" ")







# give a x = 2 and n = 3 print 8 (2^3) = 8

def power(x, n):
  if n == 0:
    return 1
  if n%2 == 0:
    return power(x, n//2) * power(x, n//2)
  else:
    return power(x, n-1) * x

print(power(2, 3))









def quadraticrots(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return [-1]
    elif d == 0:
      x = (-b)/(2*a)
      return [int(math.floor(x)),int(math.floor(x))]
    else:
      x1 = (-b + d**0.5) / (2*a)
      x2 = (-b - d**0.5) / (2*a)
      return [int(math.floor(max(x1,x2))), int(math.floor(min(x1, x2)))]   # its + or - so its in two forms. ----> (-b±√(b²-4ac))/(2a)  ==> **0.5(square root)
    #The quadratic formula helps us solve any quadratic equation. First, we bring the equation to the form ax²+bx+c=0, where a, b, and c are coefficients. Then, we plug these coefficients in the formula: (-b±√(b²-4ac))/(2a)



def GpTErm(a, b, n):
  r = b/a
  result = a * (r ** (n-1))
  return result

#Question 3: If 2, 4, 8,…., is the GP, then find its 10th term.
# Here, a = 2 and r = 4/2 = 2
# an = arn-1
# a10 = 2 x 2^10 – 1 => 2 x 2^9 => 1024






def power(x,n):                      # x = 4 , n = 5(101)
  res = 1                            # res = 1
  while n > 0:                       # 1 iteration
    if n%2 != 0:                     #  5%2 = 1 => true,   res = 1*4 = 4,   x = 4*4 = 16,    n = 5//2 = 2
      res = res * x                  # 2 iteration
    x = x*x                          #  2%2 = 0 => false,  x = 16*16 = 256,   n = 2//2 = 1
    n = n//2                         # 3 iteration
  return res                         #   1%2 = 1 => true,  res = 4*256 = 1024,   x = 256*256 = 65536,    n = 1//2 = 0 break and return res

def power(x, n, m):                        # x = 2, n = 5, m = 13
    res = 1                                # res = 1
    while n > 0:                           # 1 iteration
        if n%2 != 0:                       # 5%2 = 1 => true,   res = (1*2) % 13 = 2,   x = (2*2) % 13 = 4,   n = 5//2 = 2
        res = (res * x) % m                # 2 iteration
        x = (x*x) % m                      # 2%2 = 0 => false,  x = (4*4) % 13 = 3,   n = 2//2 = 1
        n = n//2                           # 3 iteration
    return res                             # 1%2 = 1 => true,   res = (2*3) % 13 = 6,   x = (3*3) % 13 = 9,   n = 1//2 = 0 break and return res

# explaination of the above code power function takes 3 arguments x, n, m and
# The reason we take the modulus m in the fast modular exponentiation algorithm is to prevent integer overflow and reduce the amount of computation needed to compute large powers of a number.
# example: 2^5 % 13 = 2^101 % 13 = 2^100 % 13 * 2^ 1 %  13  = 2^100 % 13 * 2^ 1 %  13 =  2 % 13 * 2 % 13 = 4 * 2 = 8 % 13 = 6   (2^5 % 13 = 6)   (2^101 % 13 = 6)  (2^100 % 13 * 2^ 1 %  13 = 6)



def sumUnderModulo(self,a:int,b:int) -> int:
  M = 1000000007
  a %= M
  b %= M
  return (a+b)%M





def add(a,b):                                                          # a =  9223372036854775807, b =  9223372036854775807
  M = 1000000007                                                       # M = 1000000007
  ans = 0
  carry = 0
    while a > 0 or b > 0:                                             # 1 iteration
      d1 = a % 10                                                     #  d1 = 7,  d2 = 7, d = 14, carry = 1, d = 14%10 = 4, ans = 0*10 + 4 = 4, a = 922337203685477580, b = 922337203685477580
      d = d1 + d2 + carry                                             # 2 iteration
      carry = d // 10                                                 # d1 = 7,  d2 = 7, d = 14, carry = 1, d = 14//10 = 1, ans = 4*10 + 1 = 41, a = 92233720368547758, b = 92233720368547758
      d1 = d % 10
      ans = ans * 10 + d
      a = a // 10
      b = b // 10
    if carry > 0:
        ans = ans * 10 + carry
    return ans % M






# def extended(a,b):                              # a = 10, b = 17
#   if b == 0:                                    # b = 0 => false
#     return a, 1, 0
#   else:
#     g, x, y = extended(b, a%b)                  # g, x, y = extended(17, 10%17 = 10) so g = 1, x = 1, y = 0
#     return g, y, x - (a//b) * y                 # g = 1, x = y_prev = 3, y = x_prev - (a//b) * y_prev = 0 - (10//17) * 3 = -5
#                                                 # tuple - (1, 3, -5)
#
# def mod(a,m):                                   # a = 10, m = 17
#     g, x, y = extended(a,m)
#     if g != 1:
#       return -1
#     else:
#       return x%m

# if __name__ == '__main__':
#     print(mod(10,17))                             # 12





def modInverse(a,m):
  g = gcd(a,m)
    if g != 1:
        return -1
    else:
        return power(a,m-2,m)

def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

def power(x,y,m):
    res = 1
    while y > 0:
        if y%2 != 0:
        res = (res*x)%m
        x = (x*x)%m
        y = y//2
    return res

if __name__ == '__main__':
    print(modInverse(2,1))                             # -1
    print(modInverse(6,34))                            # -1
    print(modInverse(3,11))                            # 4

                                                              # ----------------------------------------------------- list ----------------------------------------------------- #





def findElement(arr,n,index):
  n = len(arr)                            # n = 5
  if index < n:                           # 4 < 5 => true
    return arr[index]                     # return arr[4] = 5
  else:
    return -1

if __name__ == '__main__':
  arr = [1,2,3,4,5]
  n = len(arr)
  index = 4
  print(findElement(arr,n,index))                     # 5
  print(findElement(arr,n,6))                         # -1



# append method is used element at last of the list
def insertAtEnd(arr, sizeOfArray, element):
  arr.insert(sizeOfArray,element)         # arr = [1, 2, 3, 4, 5, 6]
  return arr

def insertAtBegin(arr, sizeOfArray, element):
  arr.append(element)                     # arr = [1, 2, 3, 4, 5, 6]
  return arr

def insertAtPosition(arr, sizeOfArray, element):
  n = len(arr)
  new_arr = [0]*(n+1)
  for i in range(n):
    new_arr[i] = arr[i]
    new_arr[n] = element
    arr = new_arr
    print(arr)



def deleteElement(arr, n, index):
  arr.delete(index)                         # arr = [1, 2, 3, 4, 5, 6]
  print(arr)
  arr.append(0)
  return arr

if __name__ == '__main__':
  arr = [1,2,3,4,5]
  n = len(arr)
  index = 4
  print(deleteElement(arr,n,index))                     # 5








def sum(arr, n):
  sum = 0
  n = len(arr)
  for i in range(len(arr)):
    sum += arr[i]
  return sum // n


if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  print(sum(arr, n))  # 5


def mean(listt):
  return sum(listt) / len(listt)









def median(arr, n):
  arr.sort()
  n = len(arr)
  if n % 2 != 0:                                    # if odd
    result = arr[n // 2]                            # 5//2 = 2
  else:                                             # if even
    reult = (arr[n//2 - 1] + arr[n//2])// 2         # 4 + 5 = 9//2 = 4
  return result
def mean(arr ,n):
  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
  return sum//n

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print(median(arr, n))  # 5







def seprate(arr, n):
  even = []
  odd = []
  for i in range(len(arr)):
    if arr[i]%2 == 0:
      even.append(arr[i])
    else:
        odd.append(arr[i])
  return even, odd

def smal(arr, n):
  res = []
  for i in range(len(arr)):
    if arr[i] < n:
      res.append(arr[i])
  return res

if __name__ == '__main__':
  arr = [8, 100, 20, 40, 3, 7]
  n = 10
  print(smal(arr, n))  # 5





                                              # ------------------------------------------------------------- intermediate element ------------------------------------------------------------- #



def intermediate(arr, n, x):
  arr.sort()
  result = []
  for i in range(len(arr)):
    if arr[i] < x:
        result.append(arr[i])
        break
  if result:
    return result[-1]
  else:
    return -1

# -------------------------------- another method -------------------------------- #


def intermediate(arr, n, x):
  arr.sort()
  result = -1
  for i in range(len(arr)):
    if arr[i] < x:
        result = arr[i]
    else:
      break
  return result






# -------------------------------- another method and Efficient and less time -------------------------------- #




def intermediate(arr, n, x):
  result = -1
  diff = float('inf')             # it is used to find the minimum difference between the two numbers
  for i in range(len(arr)):
    if arr[i] < x:
      if x - arr[i] < diff:       # it checks the difference between the two numbers and
        diff = x - arr[i]         # if the difference is less than the diff then it will update the diff and result
        result = arr[i]
  return result

# diff = float('inf') -- diff to positive infinity usinf float('inf') so that the initial value arr[i] - x is always less than diff
# it is used to get the closest number to x

# arr = [5, 3, 20, 16, 14] n = 5 x = 15
# result = -1
# diff = 15 - 5 = 10
# result = 5
# diff = 15 - 3 = 12
# result = 3
# diff = 15 - 20 = 5
# result = 3
# diff = 15 - 16 = 1
# result = 3
# diff = 15 - 14 = 1
# result = 14
# return 14









def greater(arr, n, x):
  sum = 0
  for i in arr:
    if i > x:
      sum += 1
  return sum


def immediateGreater(arr, n, x):
    arr.sort()
    result = -1
    for i in range(len(arr)):
        if arr[i] > x:
        result = arr[i]
        break
    return result



                                                                              # -------------------------------- majority wins -------------------------------- #


def majorityWins(arr, n, x, y):
  x1 = 0
  y1 = 0
  for i in range(len(arr)):
    if arr[i] == x:
      x1 += 1
    elif arr[i] == y:
      y1 += 1
  if x1 < y1:
    return y
  elif x1 > y1:
    return x
  else:
    return min(x, y)


if __name__ == '__main__':
  arr = [1,1,2,2,3,3,4,4,4,4,5]
  n = len(arr)
  x = 4
  y = 5
  print(maj(arr, n, x, y))  # 4 are 4 times and 5 are 1 times so 4 is greater than 5



                                                                                  # -------------------------------- max element -------------------------------- #


def largest_element(arr):
  result = 0
  for i in range(len(arr)):
    if arr[i] > result:
      result = arr[i]
  return result

if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  print(lar(arr))  # 5

  # time complexity is O(n) and space complexity is O(1)

    # -------------------------------- another method -------------------------------- #

def largest_element(arr):
  if not arr:
    return None
  else:
    result = arr[0]
    for i in range(1, len(arr)):
      if arr[i] > result:
        result = arr[i]
    return result

# Time complexity theta(n) and space complexity is O(1)


                                                                               # -------------------------------- second Largest -------------------------------- #

def get_max(arr):
  result = arr[0]
  for i in range(len(arr)):
    if arr[i] > result:
      result = arr[i]
  return result

def second_largest(arr):
  max = get_max(arr)
  result = 0
  for i in range(len(arr)):
    if arr[i] > result and arr[i] != max:
      result = arr[i]
  return result

if __name__ == '__main__':
  arr = [1, 2, 3, 5, 4, 5]
  print(second_largest(arr))  # 4

  # time complexity is O(n) and space complexity is O(1)

    # -------------------------------- another method -------------------------------- #


def second_largest(arr):
  if not arr:
    return None
  else:
    largest = arr[0]
    second_largest = 0
    for i in range(1, len(arr)):
      if arr[i] > largest:
        second_largest = largest                             # it is used to store the previous largest number
        largest = arr[i]                                     # it is used to store the current largest number
      elif arr[i] > second_largest and arr[i] != largest:
# if arr[i] is greater than second_largest and if there are two same largest numbers then it will not update the second_largest
        second_largest = arr[i]
    return second_largest

if __name__ == '__main__':
  arr = [5, 20, 12, 10, 20, 10, 12]
  print(second_largest(arr))  # 12

  # time complexity is O(n) and space complexity is O(1)

                                                                                  # -------------------------------- Sorted -------------------------------- #

def sorted(arr):
  n = len(arr)
  if n == 1 or n == 0:
    return True
  for i in range(n-1):      # n-1 is used because if we use n then it will give index out of range error
    if arr[i] > arr[i + 1]: # because at n element there is no element after it which is n+1 so we use n-1
      return False
  return True

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(sorted(arr))  # True

    # time complexity is O(n) and space complexity is O(1)

                                                                        # -------------------------------- sorted in ascending or descending -------------------------------- #


def sorted(arr):
  n = len(arr)
  if n == 1 or n == 0:
    return 1
  for i in range(n-1):
    if arr[i] > arr[i+1]:
      break
  else:                                   # else is at the same level of for loop not at the same level of if loop because if we use else at the same level of if loop then it will give error because if loop will not execute and it will go to else
    return 1
  for i in range(n-1):
    if arr[i] < arr[i+1]:
      break
  else:
    return 1
  return 0

if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  print(sorted(arr))  # 1


# this is used to check whether the array is sorted in ascending or descending order or not

# --------------------------------- another method --------------------------------- #

def sorted(arr):
  n = len(arr)
  if n == 1 or n == 0:
    return 1
  inc = True
  dec = True
  for i in range(n-1):
    if arr[i] > arr[i+1]:
      inc = False
    elif arr[i] < arr[i+1]:
      dec = False
  return 1 if inc or dec else 0

# this worked for every case in ascending and descending order


                                                                             # --------------------------------- Reverse order --------------------------------- #

def reverse(arr):
   reverse = []
   for i in range(len(arr)-1, -1, -1):          # it is used to reverse the array
     reverse.append(arr[i])
   return reverse

def reverse(arr):                             # it divides the array into two parts and swap the elements
  n = len(arr)
  for i in range(n//2):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]  # n-i-1 is used because if we use n-i then it will give index out of range error
  return arr


def reverse(arr):
  start = 0
  end = len(arr)-1
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1


if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  print(reverse(arr))  # [5, 4, 3, 2, 1]

  # time complexity is O(n) and space complexity is O(n)

                                                                             # -------------------------------- Remove Duplicates -------------------------------- #

def remove_duplicates(arr):
  temp = [0] * n
  temp[0] = arr[0]
  res = 1
  for i in range(len(arr)):
    if temp[res - 1] != arr[i]:
      temp[res] = arr[i]
      res += 1
  for i in range(res):
    arr[i] = temp[i]
  return res

 # -------------------------------- another method -------------------------------- #

def remove_duplicates(arr):
  temp = []
  for i in range(len(arr)):
    if arr[i] not in temp:
      temp.append(arr[i])
  return temp

# -------------------------------- another method -------------------------------- #
def remove_duplicates(arr):
  result = 0
  for i in range(0, n-1):
    if arr[i] != arr[i+1]:
      arr[result] = arr[i]
      result += 1
  arr[result] = arr[n-1] # this is because we have excluded the last element in the for loop so add it here.
  result += 1
  return result




# -------------------------------- another method -------------------------------- #

def remove_dupliactes(arr,n):
  res = 1
  for i in range(1, n):
    if arr[res - 1] != arr[i]:
      arr[res] = arr[i]
      res += 1
  return res

if __name__ == '__main__':
  arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
  n = len(arr)
  print(remove_dupliactes(arr, n))  # 5

  # time complexity is O(n) and space complexity is O(1)






                                                                                     # -------------------------------- left rotate -------------------------------- #

arr = [1, 2, 3, 4, 5], n = 5, d = 3
output = [4, 5, 1, 2, 3]

def left_rotate(arr,n):
  ele = arr[0]
  for i in range(1,n):
    arr[i-1] = arr[i]  # it is used to shift the elements to the left
  arr[n-1] = ele


# -------------------------------- another method -------------------------------- #

l = [1, 2, 3, 4, 5]
l = l[1:] + l[:1]  # it is used to shift the elements to the left
print(l)  # [2, 3, 4, 5, 1]

# -------------------------------- another method -------------------------------- #

l = [1, 2, 3, 4, 5]
l.append(l.pop(0))  # it is used to shift the elements to the left


# -------------------------------- another method -------------------------------- #
def left_rotate(arr,d):                                        # arr = [1, 2, 3, 4, 5], d = 3
  result = []
  for i in range(d, len(arr)):                                 # result = [4, 5]
    result.append(arr[i])
  for i in range(d):                                         # result = [4, 5, 1, 2, 3]
    result.append(arr[i])
  return result

arr = [1, 2, 3, 4, 5]
d = 3
print(left_rotate(arr,d))  # [4, 5, 1, 2, 3]

# -------------------------------- another method -------------------------------- #

def left_rotate(arr,d):
  result = arr[d:] + arr[:d]
  return result


# -------------------------------- another method -------------------------------- #
def left_rotate(arr,d):
  for j in range(d):
    temp = arr[0]
    for i in range(1, len(arr)):
      arr[i-1] = arr[i]
    arr[len(arr)-1] = temp

# -------------------------------- Efficiet method - worked -------------------------------- #

  class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, A, D, N):
      D %= N
      # First reversing d elements from starting index.
      A[0:D] = reversed(A[0:D])

      # Then reversing the last n-d elements.
      A[D:N] = reversed(A[D:N])

      # Finally, reversing the whole array.
      A[0:N] = reversed(A[0:N])

# -------------------------------- another method - worked-------------------------------- #

def left_rotate(arr,d):
  d = d % len(arr) # it is used to find the index of the element from where we have to rotate the array
  reverse(arr, 0, d-1) # it is used to reverse the array from 0 to d-1
  reverse(arr, d, len(arr)-1) # it is used to reverse the array from d to n-1
  reverse(arr, 0, len(arr)-1) # it is used to reverse the whole array

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

                                                                               # -------------------------------- odd occuring -------------------------------- #

arr = [1, 2, 3, 2, 3, 1, 3]
output = 3

def odd(arr):
    res = 0
    for i in range(len(arr)):
      res = res ^ arr[i]
    return res

  # time complexity is O(n) and space complexity is O(n)

# -------------------------------- another method -------------------------------- #

def odd(arr):
  for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
      if arr[i] == arr[j]:
        count += 1
    if count % 2 != 0:
      return arr[i]
  return -1








# -------------------------------- wrong method -------------------------------- #
# # this will only provide 3 because after 1 it checks for 3 but 3 also starts and 2nd - 3 comes so it will not check for 1
# def odd(arr):
#   result = []
#   for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#       if arr[i] in result:
#         return [arr[i]]
#       else:
#         result.append(arr[i])
#   return []
#
# if __name__ == '__main__':
#   arr = [1, 2, 3, 2, 3, 1, 3, 5, 5, 5, 5]
#   print(odd(arr))  # [3]
#   # time complexity is O(n) and space complexity is O(n)

# -------------------------------- wrong method -------------------------------- #
# this will only print if number occur odd number of times
def odd(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] not in temp: # if the element is not in the temp then append it
        temp.append(arr[i])
        else:
        temp.remove(arr[i])    # if the element is in the temp then remove it
    return temp[0]

if __name__ == '__main__':
  arr = [1, 2, 3, 2, 3, 1, 3]
  print(odd(arr))  # 3

  # time complexity is O(n) and space complexity is O(n)




# ------------------------------------------------- Recursion ------------------------------------------------- #

# recursion is a function which calls itself again and again until the base condition is not satisfied
# base condition is the condition which stops the recursion its important to have base condition otherwise it will go to infinite loop
# example -  factorial of a number - 5! = 5 * 4 * 3 * 2 * 1 = 120 you need to stop the recursion when the number is 1 else it will go to infinite loop
# example -  fibonacci series - 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 you need to stop the recursion when the number is 0 or 1 else it will go to infinite loop
# example -  sum of n natural numbers - 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55 you need to stop the recursion when the number is 0 else it will go to infinite loop
# example -  sum of digits of a number - 1234 = 1 + 2 + 3 + 4 = 10 you need to stop the recursion when the number is 0 else it will go to infinite loop


# tail Recursion - when the recursive call is the last statement in the function then it is called tail recursion
# example - fibonacci series is a tail recursion because the recursive call is the last statement in the function
# example - factorial of a number is not a tail recursion because the recursive call is not the last statement in the function
# factorial can be written as tail recursion by using helper function
# int fact(int n, int k):
#   if n == 0 or n == 1:
#     return k
#   return fact(n-1, k*n)







def fun(n):                    # ===>                fun(3)
  if n == 0:                                         # print(3)
    return                                                # fun(2)
  print(n)                                                # print(2)
  fun(n-1)                                                      # fun(1)
  print(n)                                                      # print(1)                                                    # fun(0)     now if is true so it will return
fun(3)                                                          # if is True
                                                                # print(1)   now it will print 1
                                                          # print(2)   now it will print 2
                                                    # print(3)   now it will print 3
# it will print 3 2 1 1 2 1 3 it print like this because it need to close the function call so it will print 1 2 1 3 2 1 3




# s(n) = n + n*(s(n-1)) and s(0) = 1
# s(3) = 3 + 3*(s(2)) = 3 + 3*(2 + 2*(s(1))) = 3 + 3*(2 + 2*(1 + 1*(s(0)))) = 3 + 3*(2 + 2*(1 + 1*(1))) = 3 + 3*(2 + 2*(1 + 1)) = 3 + 3*(2 + 2*2) = 3 + 3*(2 + 4) = 3 + 3*6 = 3 + 18 = 21

def s(n):
  if n == 0:
    return 1
  return n + n*(s(n-1))

print(s(3)) # 21






# -------------------------------- another example -------------------------------- #

def fun(n):                                          # fun(16)
  if n <= 1:                                         # else: return 1 + fun(8)
    return 0                                         # else: return 1 + fun(4)
  else:
    return 1 + fun(n/2)                              # else: return 1 + fun(2)
print(fun(16)) # 4                                   # else: return 1 + fun(0)
# now if is true so it will return 0 and it will go to else and return 1 + 0 = 1
# now if is true so it will return 0 and it will go to else and return 1 + 1 = 2
# now if is true so it will return 0 and it will go to else and return 1 + 2 = 3
# now if is true so it will return 0 and it will go to else and return 1 + 3 = 4



                                                                          #  -------------------------------- decimal to binar conversion -------------------------------- #


def fun(n):                       #    fun(13)
  if n == 0:                          #  fun(6)
    return 0                               # fun(3)
  fun(n/2)                                      #fun(1)
  print(n%2)                                      # fun(0)
                                               # print(1%2)
fun(13) # 1 1 0 1                           print(3%2)
                                      #  print(6%2))
                                     # print(13%2)



# -------------------------------------- Example -------------------------------------- #

def print1toN(n):
  if n == 0:
    return
  print1toN(n-1)
  print(n)

# n = 10 if you want 1,2,3..10 first write recursive then print or else you will get 10,9,8....3,2,1.


def printArrayRecursively(arr, n):
  if n == 0:
    return
  printArrayRecursively(arr, n-1)
  print(arr[n-1]) # print(arr[n]) will give error because array index out of range because array index start from 0 and n start from 1
  # printArrayRecursively(arr, n-1) this line means it will read the array from last to first and print the array from first to last


def printRecursiveOrder(n):
  if n <= 0:
    return 0
  print(n)
  printRecursiveOrder(n-1)

# printRecursiveOrder(5) # 5 4 3 2 1

def sum_digits(n):
  if n < 10:
    return n
  return sum_digits(n//10) + n%10

# step 1 - sum_digits(1234) = 4 + sum_digits(123)
# step 2 - sum_digits(123) = 3 + sum_digits(12)
# step 3 - sum_digits(12) = 2 + sum_digits(1)
# step 4 - sum_digits(1) = 1
# step 5 - sum_digits(12) = 2 + 1 = 3
# step 6 - sum_digits(123) = 3 + 3 = 6
# step 7 - sum_digits(1234) = 4 + 6 = 10


def count_digit(n):
  if n <= 0:
    return n
  else:
    return 1 + count_digit(n//10)    # this line counts the number of digits in a number by dividing the number by 10 and adding 1 to the count



def fibonacci(n):
  if n == 0 or n == 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n-1)


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)





# def Palindrome_number(n):
#   reverse = 0
#   copy = n
#   while copy > 0:                                       # goes on till copy is greater then 0 if its less stops
#     last_digit = copy % 10                              # takes last digit of n ex : 1221 -- 1
#     reverse = reverse * 10 + last_digit                 # 0*10+1 = 1, 1*10 + 2 = 12, 12*10+2= 122, 122*10+1= 1221
#     copy = copy // 10                                   # removes the last digit of copy
#
#   if n == reverse:
#     return True
#   else:
#     return False








def Palindrome(n, start, end):
  if start >= end:                               # if start is greater then end then it will return True because it means it is palindrome
    return True                                  # ex: 1,2,3,2,1 start = 0 end = 4 so it will return True
  return Palindromen(n[start] == n[end] and palindrome(n, start+1, end-1))



def Palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return Palindrome(n[1:-1])
    else:
        return False


def PalindroemDigit(n):
    if n < 10:
        return True
    if n%10 == n//10:
        return PalindroemDigit(n//10)
    else:
        return False


def palindrome(n):
  result = 0
  copy = n
  while copy > 0:
    last_digit = copy % 10
    result = result * 10 + last_digit
    copy = copy // 10

  if n == result:
    return True
  else:
    return False

# write it in recursive way

def palindrome(n):
    result = 0
    copy = n
    if copy == 0:
        return result
    last_digit = copy % 10
    result = result * 10 + last_digit
    copy = copy // 10
    return palindrome(n, result, copy)






# -------------------------------------- Example -------------------------------------- #

def palindrome(n):
  st = str(n)
  if len(st) <= 1:
    return True
  if st[0] == st[-1]:
    return palindrome(st[1:-1])
  return False



# -------------------------------------- Example -------------------------------------- #

  class Solution:
    def isPalin(self, N):

      return self.check(N, N, 0)

    def check(self, n, cn, pn):
      if cn == 0:
        if pn == n:
          return 1
        else:
          return 0

      pn = pn * 10 + (cn % 10)
      cn = cn // 10

      return self.check(n, cn, pn)


# -------------------------------------  sum of natural numbers using    ------------------------------------- #

def sum(n):
  if n <= 1:
    return n
  return n + sum(n-1)
















# ///////////////////////////////////////////////////////   Binary search   /////////////////////////////////////////////////////// #

def linear(n):
  for i in range(len(n)):
    if n[i] == x:
      return i
  return -1



def binary(arr, start, end):
  if start > end:
    return -1
  mid = (start + end) // 2                # mid = start + (end - start) // 2  --> to avoid overflow
  if arr[mid] == x:
    return mid
  elif arr[mid] > x:                      # if the middle element is greater then x then it will search in the left side of the array
    return binary(arr, start, mid-1)
  else:
    return binary(arr, mid+1, end)



def binary(arr, start, end):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      start = mid + 1
    else:
      end = mid - 1
  return -1





# ------------------------------------------------    first occurance      ---------------------------------------------------------- #

def find(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return arr[i]
  return -1



def find_using_binary_search(arr, x, start, end):
  if start > end:
    return -1
  mid = start + end // 2
  if x > arr[mid]:
    return find_using_binary_search(arr, x, mid+1, end)
  elif x < arr[mid]:
    return find_using_binary_search(arr, x, start, mid-1)
  else:
    if mid == 0 or arr[mid-1] != arr[mid]:     #
      return mid
    else:
      find_using_binary_search(arr, x, low, mid-1)







def find_using_recursion(arr, x, start, end):
  start = 0
  end = len(arr)-1
  while(start <= end):
    mid = (start+end)//2
    if x > arr[mid]:
      start = mid + 1
    elif x < arr[mid]:
      end = mid - 1
    else:
      if mid == 0 or arr[mid-1] != arr[mid]:            # if the element which is mid is first ooccured or check wheather
        return mid                                      # the previous element is not the same element if same then
      else:                                                     # change start = mid +1 and start now binary seaerch
        start = mid -1
  return -1





def find_last_occured(arr, x):
  for i in reversed(range(len(arr))):
    if arr[i] == x:
      return i
  return -1





def find_last_occur1(arr, x):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end)//2
    if arr[mid] < x:
      start = mid + 1
    elif arr[mid] > x:
      end = mid - 1
    else:
      if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
        return mid
      else:
        start = mid + 1
  return -1





#        ----------------------------------------   basic approach ----------------------------------------------        #

def find_first_and_last(arr, x):
  first = -1
  last = -1
  for i in range(len(arr)):
    if arr[i] == x:
      if first == -1:
        first = i
      last = i
  return first, last

# it loops through the array and check wheather the element is equal to x if it is ot checks wheather the first is -1
# it its -1 then it means it is the first occurance of the element and it stores the index of the element in first
# it first = -1 is false the already the first occurance is stored in first and it stores the last occurance in last
# and runs loop till last and update last if found ellse return first and last

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 8
print(find_first_and_last(arr, x))


####################################################### optimized code for searching occurance ##################################################

def occurance(arr, x):
  start = 0
  end = len(arr) - 1
  first = -1
  while start <= end:
    mid = (start + end)//2
    if arr[mid] < x:
      start = mid + 1
    elif arr[mid] > x:
      end = mid -1
    else:
      first = mid
      end = mid - 1      # we kept end = mid - 1 because we want left most element occurance of x which would be the first occurance
  return first


######################################################## count the occurance of the element  #####################################################

arr = [1, 2, 3, 3, 3, 4, 5, 5]
x = 3


def binary_search(arr, x, start, end):
  if start > end:
    return -1
  mid = (start + end)//2                             # mid = 0 + 7 // 2 = 3 ==> arr[3] = 3 return 3
  if arr[mid] == x:
    return mid
  elif arr[mid] > x:
    return binary_search(arr, x, start, mid-1)
  else:
    return binary_search(arr, x, mid+1, end)

def count_occurance(arr, x):
  first = binary_search(arr, x, 0, len(arr)-1)     # first occurance = 3
  if first == -1:                                  # if binary search return -1 then no element is found so return 0 count will be 0 because no element
    return 0
  count = 1                                       # if element is found then count = 1

  left = first - 1                                # left = 3 - 1 = 2
  while left >= 0 and arr[left] == x:             # while left is greater then 0 and arr[2] == 3 then increment count and decrement left
    count += 1                                    # to check wheather the previous element is same or not
    left -= 1

  right = first + 1                               # now check right because binary gives mid element so check right and left
  while right < len(arr) and arr[right] == x:     # while right is less then len(arr) and arr[4] == 3 then increment count and increment right
    count += 1                                    # to check wheather the next element is same or not from the mid till last loops goes on right side
    right += 1








# -------------------------------------------------   Peak element  ------------------------------------------------------ #


arr = [1, 3, 4, 6, 7, 9, 10]
# peak element is 10
# peak element is the element which is greater then its neighbours


def peak_element(arr):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end)//2
    #         if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid] ):
    #             return mid
    if (mid == 0 or arr[mid] >= arr[mid-1]) and (mid == len(arr)-1 or arr[mid] >= arr[mid+1]):  # False or True = True
      return mid                                                                                # True or False = True
    elif mid > 0 and arr[mid] < arr[mid-1]:                                                     # True and True = True
      end = mid - 1
    else:
      start = mid + 1
  return -1

# mid = 3 ==> arr[3] = 6
# if mid is first or last element in the array it means it is the peak element because it has only one neighbour and it is greater then its neighbour
# if mid is not first and last element and mid is greater then its previous and next element then return mid
# in this 6 is not at first or last position and it is greater then its previous element but not greater then its next element so we go to elif

# elif 6 is gretaer then zero and arr[3] < arr[2] ==> 6 < 4 is false so we go to else

# else put start = mid + 1 ==> start = 3 + 1 = 4

# mid = 4 ==> arr[4] = 7
# In this 7 is not at first or last position and it is greater then its previous element but not greater then its next element so we go to elif

# elif 7 is gretaer then zero and arr[4] < arr[3] ==> 7 < 6 is false so we go to else

# else put start = mid + 1 ==> start = 4 + 1 = 5

# mid = 5 ==> arr[5] = 9
# In this 9 is not at first or last position and it is greater then its previous element but not greater then its next element so we go to elif

# elif 9 is gretaer then zero and arr[5] < arr[4] ==> 9 < 7 is false so we go to else

# else put start = mid + 1 ==> start = 5 + 1 = 6

# mid = 6 ==> arr[6] = 10
# In this 10 is not first element but its last element and its greater then previous element so we return mid

################################################## Basic code for peak element ########################################################
def peakElement(arr, n):
  if n == 1:
    return 0
  if arr[0] >= arr[1]:
    return 0
  if arr[n - 1] >= arr[n - 2]:
    return n - 1
  for i in range(1, n - 1):
    if (arr[i] >= arr[i - 1]) and (arr[i] >= arr[i + 1]):
      return i










# -------------------------------------------------   count 1's in a sorted Binary List  ------------------------------------------------------ #

def count(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] == 1:
      count += 1
  return count

######################################### only works if array is sorted ##################################
# if arr = [1,1,0,0,0,0] =======> then this code will not work
arr = [0, 0, 0, 0, 1, 1, 1, 1]

def count_ones(arr):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end)//2          # mid = 0 + 7 // 2 = 3 ==> arr[3] = 0
    if arr[mid] < 1:                # if arr[3] < 1 ==> 0 < 1 is true
      start = mid + 1               # start = 3 + 1 = 4
    elif arr[mid] >= 1:             # if arr[4] >= 1 ==> 1 >= 1 is true
      end = mid - 1                 # end = 4 - 1 = 3
  return len(arr) - start            # return 8 - 4 = 4


arr = [0, 0, 0, 0, 1, 1, 1, 1]
print(count_ones(arr))



#   ------------------------------------------------------------- Proper code --------------------------------------------------------------------   #

# The code traverse left side because array is in non incresing order so we traverse left side and count 1's and then traverse right side and count 0
# this code doesnt work if array is in incresing order ==> arr = [0,0,0,0,1,1,1,1] it will return 0 because it will traverse left side and count 0's

arr = [1,0,0,0]

def count_ones(arr):
  start = 0
  end = len(arr) - 1
  while start <= end:                 # end >= start
    mid = (start+end)//2                                # mid = 0 + 3// 2 = 2 ==> arr[2] = 0
    if arr[mid] < 1:                                    # if arr[2] < 1 ==> 0 < 1 is true  end = 2 - 1 = 1   => mid = 0 + 1 // 2 = 0 ==> arr[0] = 1
      end = mid - 1                                     # if arr[0] < 1 ==> 1 < 1 is false so we go to elif if arr[0] > 1 ==> 1 > 1 is false so we go to else
    elif arr[mid] > 1:                                  # if 1 == 3 or arr[1 + 1] != arr[1] ==> 1 == 3 or arr[2] != arr[1] ==> 1 == 3 or 0 != 1 is true
      start = mid + 1                                   # so we return mid + 1 ==> return 0 + 1 = 1
    else:
      if mid == len(arr) - 1 or arr[mid + 1] != arr[mid]:
        return mid + 1
      else:
        start = mid + 1
  return 0

# if arr = [0,0,1,1]
# start = 0 and end = 3 mid = 0 + 3 // 2 = 1 ==> arr[1] = 0
# if arr[1] < 1 ==> 0 < 1 is true end = 1 - 1 = 0
# start = 0 and end = 0 mid = 0 + 0 // 2 = 0 ==> arr[0] = 0
# if arr[0] < 1 ==> 0 < 1 is true end = 0 - 1 = -1












#########################################################################    sqaure root of a number   ################################################################################



def power(x, n):                                          # 2, 3
  if n == 0:                                              # 3 == 0 is false
    return 1
  if n%2 == 0:                                            # 3 % 2 == 0 is false
    return power(x, n//2) * power(x, n//2)
  else:
    return power(x, n-1) * x                              # return power(2, 2) * power(2, 2) = 4 * 4 = 16

print(power(2, 3))



def power(x, n):                                     # 4, 5
  result = 1                                         # result = 1
  while n > 0:
    if n % 2 == 1:                                   # 5 % 2 == 1 is true
      result *= x                                    # result = 1 * 4 = 4
    x *= x                                           # x = 4 * 4 = 16
    n = n//2                                         # n = 5 // 2 = 2
  return result                                      # 2 % 2 == 1 is false so we go to else x = 16 * 16 = 256 n = 2 // 2 = 1
                                                     #  1 % 2 == 1 is true result = 4 * 256 = 1024 x = 256 * 256 = 65536 n = 1 // 2 = 0 loop breaks return 1024



def power(x, n):                                  # it's multiplying x by itself n times  => 3, 4
  result = 1
  while n != 0:
    result = result * x                           # result = 1 * 3 * 3 * 3 * 3 = 81
    n -= 1
  return result


def square_root(x):                     # 9
  i = 1
  while i * i <= x:                     # 1 * 1 = 9 ==> 2 * 2 = 4 => 3 * 3 = 9  ==>  4 * 4 = 16   loop breaks return 4-1 = 3
    i += 1
  return i - 1


def square_root(x):                                                # x = 10, low = 1 and high = 10
  if x == 0 or x == 1:                                             # 1st iteration
    return x                                                                        # mid = 1 + 10 // 2 = 5 ==> 5 * 5 = 25 ==>   25 > 10 is true so end = 5 - 1 = 4
  start = 1                                                        # 2nd iteration
  end = x                                                                           # mid = 1 + 4 // 2 = 2 ==> 2 * 2 = 4 ==> 4 < 10 is true so start = 2 + 1 = 3 and ans = 2
  while start <= end:                                              # 3rd iteration
    mid = (start + end)//2                                                          # mid = 3 + 4 // 2 = 3 ==> 3 * 3 = 9 ==> 9 < 10 is true so start = 3 + 1 = 4 and ans = 3
      if mid * mid == x:                                           # 4th iteration
        return mid                                                                  # mid = 4 + 4 // 2 = 4 ==> 4 * 4 = 16 ==> 16 > 10 is true so end = 4 - 1 = 3  loop breaks return 3
      elif mid* mid > x:
        end = mid - 1
      else:
        start = mid + 1
        ans = mid
    return ans


##################################################################    sqaure root of a number   ################################################################################

#################################################################    Floor in a sorted array   ################################################################################






arr = [1, 2, 8, 10, 11, 12, 19]
x = 13

def find_floor(arr, x):
  start = 0
  end = len(arr) - 1                                       # start = 0 and end = 6
  ans = -1                                                 # 1st iteration
  while start <= end:                                                       # mid = 0 + 6 // 2 = 3 ==> arr[3] = 10 ==> 10 > 13 is false so start = 3 + 1 = 4 and ans = 3
    mid = (start + end)//2                                 # 2nd iteration
    if arr[mid] == x:                                                       # mid = 4 + 6 // 2 = 5 ==> arr[5] = 12 ==> 12 > 13 is false so start = 5 + 1 = 6 and ans = 5
      return mid                                           # 3rd iteration
    elif arr[mid] > x:                                                      # mid = 6 + 6 // 2 = 6 ==> arr[6] = 19 ==> 19 > 13 is true so end = 6 - 1 = 5  loop breaks return 5
      end = mid - 1
    else:
      start = mid + 1
      ans = mid
  return ans





#################################################################    Floor in a sorted array   ################################################################################






#################################################################  improve linear search   ################################################################################

def Linear_serach(arr, x):
  left = 0
  right = len(arr) - 1
  positionn = -1
  for left in range(start, end, 1):      # this loop will run from 0 to 5 with increment of 1
    if arr[left] == x:
      positionn = left
      print("element found at index: ", positionn)
      break
    if arr[right] == x:
      positionn = right
      print("element found at index: ", positionn)
      break
    left += 1
    right -= 1

    if positionn == -1:
      print("element not found")

arr = [1, 2, 3, 4, 5, 6]
x = 5

Linear_serach(arr, x)

#################################################################  improve linear search   ################################################################################

























#################################################################################   Sorting   ###################################################################################

# 1. .sort() method  -  it makes changes in the original list and returns None
# 2. sorted() function - it doesn't make changes in the original list and returns a new list

# syntax Sorted :-  sorted(iterable, key, reverse)

# syntax sort :-  list.sort(key, reverse)

# Stable sorting algorithm -  it maintains the relative position  of the elements with equal keys --> Bubble sort, Insertion sort, Merge sort, Tim sort, Count sort, Bucket sort, Radix sort.
# ex : l = [("Anil",50),("Piyush",50),("Ram",80)]
#      l.sort()

#      output :  [("Anil",50),("Piyush",50),("Ram",80)]

# Unstable sorting algorithm - it doesn't maintain the relative popsition of the elements with equal keys --> Selection sort, Heap sort, Quick sort.

#       output : [("Piyush",50),("Anil",50),("Ram",80)]


# question :- You are given an unsorted array and you are onlu allowed to sort the adjacent data. How will you sort the entire array?
# answer :- 1. Bubble sort is the only algorithm that can sort the adjacent data without using any extra space. It is also called as ripple sort.



def bubble_sort(arr):                                                                                # arr = [10, 8, 20, 5]
  n = len(arr)                                                                                       # j = o    [10 | 8 | 20 | 5]
  for i in range(n-1):                                                                               # j = 1    [8 | 10 | 20 | 5]                               --> 1st iteration
    for j in range(n-i-1):                                                                           # j = 2    [8 | 10 | 20 | 5]                                      i = 0
      if arr[i] > arr[i+1]:                                                                          # j = 3    [8 | 10 | 5 | 20] ---- last element is sorted
        arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr                                                                                         # j = 0    [8 | 10 | 5 | 20]
                                                                                                     # j = 1    [8 | 5 | 10 | 20]                               --> 2nd iteration
                                                                                                     # j = 2    [8 | 5 | 10 | 20] ---> last 2 element is sorted        i = 1

                                                                                                    # j = 0    [5 | 8 | 10 | 20]
                                                                                                    # j = 1    [5 | 8 | 10 | 20] ---> last 3 element is sorted        i = 2


# second loop sorts the last element of the array in each iteration after sorting for next iteration of outerloop it reduces the size of the array by 1
# so the outer loop will run from 0 to n-1 which is 3 times in this case if we have four elemnets in the array then it will run 4-1 = 3 times


# time complexity of bubble sort is O(n^2) and space complexity is O(1)


####################################################################### improved bubble sort #####################################################################################


def bubble_sort(arr):
  n = len(arr)

  for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True

    if swapped == False:
      return arr


# in this case if the array is already sorted then the outer loop will run only once and the inner loop will not run at all
# loop runs with swapped as false and checks if the array is sorted or not if it is sorted then it will return the array as it is.
# time complexity of this improved bubble sort is O(n) and space complexity is O(1)









######################################################################## Selection sort ##########################################################################################

# it is an unstable sorting algorithm and it is not adaptive in nature because it doesn't take advantage of the sorted array in any case. It always runs in O(n^2) time complexity.
# it does less memory writes as compared to bubble sort, quick sort, insertion sort, etc.But cycle sort is optimal in terms of memory writes.
# Basic idea for heapsort
# its in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end.

# 1. Find the minimum element in the unsorted array and swap it with the element at the beginning.




def selection_sort(arr):                                                                         # arr = [64 | 25 | 12 | 22 | 11]
  n = len(arr)                                                                                   # 1st iteration
  for i in range(n-1):                                                                           # i = 0  , min_index = 0
    min_index = i                                                                                # j = 1  , arr[1] < arr[0] is true ==> 25 < 64 ==> min_index = 1
    for j in range(i+1,n):                                                                       # j = 2  , arr[2] < arr[1] is true ==> 12 < 25 ==> min_index = 2
      if arr[j] < arr[min_index]:                                                                # j = 3  , arr[3] < arr[2] is false ==> 22 < 12 ==> min_index = 2
        min_index = j                                                                            # j = 4  , arr[4] < arr[2] is true ==> 11 < 12 ==> min_index = 4
    arr[i], arr[min_index] = arr[min_index], arr[i]                                              # swap(arr[0], arr[4])                                                   ==> [11 | 25 | 12 | 22 | 64]
  return arr                                                                                     # 2nd iteration
                                                                                                 # i = 1  , min_index = 1
                                                                                                 # j = 2  , arr[2] < arr[1] is true ==> 12 < 25 ==> min_index = 2
                                                                                                 # j = 3  , arr[3] < arr[2] is false ==> 22 < 12 ==> min_index = 2
                                                                                                 # j = 4  , arr[4] < arr[2] is false ==> 64 < 12 ==> min_index = 2
                                                                                                 # swap(arr[1], arr[2])                                                   ==> [11 | 12 | 25 | 22 | 64]
                                                                                                 # 3rd iteration
                                                                                                 # i = 2  , min_index = 2
                                                                                                 # j = 3  , arr[3] < arr[2] is true ==> 22 < 25 ==> min_index = 3
                                                                                                 # j = 4  , arr[4] < arr[3] is false ==> 64 < 22 ==> min_index = 3
                                                                                                 # swap(arr[2], arr[3])                                                   ==> [11 | 12 | 22 | 25 | 64]
                                                                                                 # 4th iteration
                                                                                                 # i = 3  , min_index = 3
                                                                                                 # j = 4  , arr[4] < arr[3] is false ==> 64 < 25 ==> min_index = 3
                                                                                                 # swap(arr[3], arr[3])                                                   ==> [11 | 12 | 22 | 25 | 64]
                                                                                                 # 5th iteration
                                                                                                 # i = 4  , min_index = 4
                                                                                                    # j = 5  , j is out of range so loop will not run and the array is sorted now so it will return the array as it is.



######################################################################################### Insertion sort ########################################################################################

# its time complexity is O(n^2) in worst case and O(n) in best case when the array is already sorted.
# its stable and in-place sorting algorithm.
# it is adaptive in nature because it takes advantage of the sorted array in some cases.
# used in online sorting when the array is sorted in real time.
# it is used in hybrid sorting algorithms like timsort, introsort, etc.
# it is used in insertion sort tree to construct a binary search tree from a sequence of inputs.
# it is used in many online games for sorting the scores of players.
# it works well with small data sets but not with large data sets.





def insertion_sort(arr):                                                     # arr = [12 | 11 | 13 | 5 | 6]
  for i in range(1, n):                                                      # 1st iteration
    element = arr[i]                                                         # i = 1 , element = 11, j = 0 => 12
    j = i - 1                                                                # j = 0 , arr[0] > element ==> 12 > 11 true , arr[1] = arr[0] ==> arr[1] = 12
    while j >= 0 and arr[j] > element:                                       # j = -1 , loop will not run
      arr[j+1] = arr[j]                                                      # arr[0] = 11                                                                             ==> [11 | 12 | 13 | 5 | 6]
      j -= 1                                                                 # 2nd iteration
    arr[j+1] = element                                                       # i = 2 , element = 13 , j = 1 => 11
  return arr                                                                 # j = 1 , arr[1] > element ==> 12 > 13 false , arr[2] = 13                                ==> [11 | 12 | 13 | 5 | 6]
                                                                             # 3rd iteration
                                                                             # i = 3 , element = 5 , j = 2 => 13
                                                                             # j = 2 , arr[2] > element ==> 13 > 5 true , arr[3] = arr[2] ==> arr[3] = 13
                                                                             # j = 1 , arr[1] > element ==> 12 > 5 true , arr[2] = arr[1] ==> arr[2] = 12
                                                                             # j = 0 , arr[0] > element ==> 11 > 5 true , arr[1] = arr[0] ==> arr[1] = 11
                                                                             # j = -1 , loop will not run
                                                                             # arr[0] = 5                                                                              ==> [5 | 11 | 12 | 13 | 6]
                                                                             # 4th iteration
                                                                             # i = 4 , element = 6 , j = 3 => 13
                                                                             # j = 3 , arr[3] > element ==> 13 > 6 true , arr[4] = arr[3] ==> arr[4] = 13
                                                                             # j = 2 , arr[2] > element ==> 12 > 6 true , arr[3] = arr[2] ==> arr[3] = 12
                                                                             # j = 1 , arr[1] > element ==> 11 > 6 true , arr[2] = arr[1] ==> arr[2] = 11
                                                                             # j = 0 , arr[0] > element ==> 5 > 6 false , arr[1] = element ==> arr[1] = 6
                                                                             # arr[1] = 6                                                                              ==> [5 | 6 | 11 | 12 | 13]
                                                                             # 5th iteration
                                                                                # i = 5 , i is out of range so loop will not run and the array is sorted now so it will return the array as it is.

# starting from the second element because the first element or single element is alwayse sorted so we will start from the second element.
# we will store the second element in a variable called element and also store the previous element to compare it with the element.
# we will compare the element with the previous element and if the previous element is greater than the element then we will shift the previous element to the next index.
# we will do this until the previous element is less than the element or the previous element is the first element.
# then we will store the element in the index of the previous element.
# we will do this for all the elements in the array.







######################################################################################### Merge sort ########################################################################################

# its time complexity is O(nlogn) in all cases.
# its stable and out-place sorting algorithm.
# it is used in external sorting.
# it is used in sorting linked lists.
# it is used in counting inversions in an array.
# it is used in external merge sort.
# it is used in merge sort tree to construct a binary search tree from a sequence of inputs.
# it is used in merge sort tree to find the number of elements less than a given number in a given range.
# but more memory is required for this algorithm because it uses temporary arrays for merging.
# it is used in hybrid sorting algorithms like timsort, introsort, etc.



def meerge_sort(arr1, arr2):
  result = []
  m = len(arr1)
  n = len(arr2)
  i = j = 0
  while i < m and j < n:
    if arr1[i] < arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1

  while i < m:
    result.append(arr1[i])
    i += 1

  while j < n:
    result.append(arr2[j])
    j += 1

  return result




#############################################################################################################      Problem
# reverse im groups of size k
# Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 3
# output = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]
# it sorts the array in groups of 3 elements in reverse order.


def reverese_group(arr, k):                                                          # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3    to get k loop in every i add it and do -1 to get exact
  n = len(arr)
  for i in range(0, n, k):                                                           # 1 iteration
    left = i                                                                         # left = 0, right = 2  => if 2 > 8 false , now we will swap the elements
    right = i + k - 1                                                                # arr = [3, 2, 1, 4, 5, 6, 7, 8, 9]
    if right > n - 1:                                                                # 2 iteration
      right = n - 1                                                                  # left = 3, right = 5  => if 5 > 8 false , now we will swap the elements
    while left < right:                                                              # arr = [3, 2, 1, 6, 5, 4, 7, 8, 9]
      arr[left], arr[right] = arr[right], arr[left]                                  # 3 iteration
      left += 1                                                                      # left = 6, right = 8  => if 8 > 8 false , now we will swap the elements
      right -= 1                                                                     # arr = [3, 2, 1, 6, 5, 4, 9, 8, 7]
                                                                                     # loop will not run because left = right
  return arr

# if we have to reverse the array in groups of 4 lements then left += 1 and right -= 1 will be used properly
# example :- arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , k = 4
# left = 0 and right = 3 ==> [1, 2, 3, 4] ==> first swap 1 and 4 ==> [4, 2, 3, 1] ==> then swap 2 and 3 ==> [4, 3, 2, 1]
# left = 4 and right = 7 ==> [5, 6, 7, 8] ==> first swap 5 and 8 ==> [8, 6, 7, 5] ==> then swap 6 and 7 ==> [8, 7, 6, 5]
# left = 8 and right = 9 ==> [9, 10] ==> first swap 9 and 10 ==> [10, 9] ==> then swap 9 and 10 ==> [10, 9]
# now the loop will not run because left = right.




#########################################################################  Merge - merge two subarray ######################################################################

arr = [10, 15, 20, 40, 8, 11, 55]
# output :-  [8, 10, 11, 15, 20, 40, 55]


def merge(arr, low, mid, high):                                                           # a = [10, 15, 20, 40, 8, 11, 55], low = 0, mid = 3, high = 6
  left = arr[low : mid + 1]                                                               # left = [10, 15, 20, 40] , right = [8, 11, 55]
  right = arr[mid + 1 : high + 1]
  i = j = 0                                                                               # i = 0 , j = 0, k = 0
  k = low
  while i < len(left) and j < len(right):                                                 # a = [8,.......................] , i = 0 , j = 1, k = 1
    if left[i] <= right[j]:                                                               # a = [8, 10, ..................] , i = 1 , j = 1, k = 2
      arr[k] = left[i]                                                                    # a = [8, 10, 11, ..............] , i = 1 , j = 2, k = 3
                                                                                          # a = [8, 10, 11, 15, ..........] , i = 2 , j = 2, k = 4
      K += 1                                                                              # a = [8, 10, 11, 15, 20, ......] , i = 3 , j = 2, k = 5
      i += 1                                                                              # a = [8, 10, 11, 15, 20, 40,...] , i = 4 , j = 2, k = 6
                                                                                          # a = [8, 10, 11, 15, 20, 40, 55] , i = 4 , j = 3, k = 7
    else:
      arr[k] = right[j]:                                                                  # k is at starting at low at arr[k] is a array of 0 to 6 sorting the elements and adding it to the arr and incrementing k to keep track of the index.
      k += 1
      j += 1

  while i < len(left):
    arr[k] = left[i]
    k += 1
    i += 1

  while j < len(right):
    arr[k] = right[j]
    k += 1
    j += 1
# arr = [10, 15, 20, 40, 8, 11, 55]
# merge_sort(arr, 0, 3, 6)
# print(*arr)

# till now we have sorted the array in two parts now we have to merge it

def merge_sort(arr, left, right):                                    # format                                                                      arr = [10, 15, 20, 40, 8, 11, 55], left = 0, right = 6, mid = 3
  if left < right: # or if right > left:                             #     /                                                                               /                       \
    mid = (left + right) // 2                                        #   /                                               l = 0, r = 3 , m = 1  [10, 15, 20, 40]                     [8, 11, 55] l = 4, r = 6, m = 5
    merge_sort(arr, left, mid)                                       #  /                                                                      /                \                     /             \
    merge_sort(arr, mid + 1, right)                                  #      \                                                         [10, 15]             [20, 40]             [8, 11]             [55]
    merge(arr, left, mid, right)                                                                                        #           /       \             /       \           /       \           /       \
  return arr                                                                                                            #       [10]        [15]        [20]        [40]        [8]        [11]        [55]


arr = [10, 15, 20, 40, 8, 11, 55]                                                                                       # now we will merge the array
merge_sort(arr, 0, len(arr) - 1)
print(*arr)                                                                                                             #              [10, 15]             [20, 40]             [8, 11]             [55]
# output :-  [8, 10, 11, 15, 20, 40, 55]                                                                                #                     [10, 15, 20, 40]                     [8, 11, 55]
                                                                                                                        #                                   [8, 10, 11, 15, 20, 40, 55]


# Time complexity of merge sort is O(nlogn) in all cases and space complexity is O(n) in worst case and O(logn) in best case.
# it can improve time complexity by using insertion sort for small arrays.






def naive_union(arr1, arr2):
  result = arr1 + arr2
  result.sort()
  for i in range(len(result) - 1):
    if i == 0 or result[i] != result[i - 1]:
      print(result[i], end = " ")




def union_Sortedarra(arr1, arr2):
  i = j = 0
  while i < len(arr1) and j < len(arr2):
    if i > 0 and arr1[i] == arr1[i - 1]: # if the element is same as the previous element then we will skip it because we have to print unique elements
      i += 1
    elif j > 0 and arr2[j] == arr2[j - 1]:
      j += 1
    elif arr1[i] < arr2[j]:
      print(arr1[i], end = " ")
      i += 1
    elif arr1[i] > arr2[j]:
      print(arr2[j], end = " ")
      j += 1
    else:
      print(arr1[i], end = " ")
      i += 1
      j += 1

  while i < len(arr1):
    if i > 0 and arr1[i] != arr1[i - 1]:
      print(arr1[i], end = " ")
    i += 1

  while j < len(arr2):
    if j > 0 and arr2[j] != arr2[j - 1]:
      print(arr2[j], end = " ")
    j += 1

arr1 = [1, 2, 2, 3, 4, 5, 6, 7, 8]
arr2 = [2, 3, 4, 5, 6, 7, 8, 9]
union_Sortedarra(arr1, arr2)
print()
# output :- 1 2 3 4 5 6 7 8 9



########################################################    given code  -----------------------------------------------/
# Function to print union of two unsorted arrays
  def doUnion(a, n, b, m):
    i = j = count = 0
    n = len(a)
    m = len(b)
    union_set = set()

    while i < n and j < m:
      if a[i] < b[j]:
        union_set.add(a[i])
        i += 1
      elif a[i] > b[j]:
        union_set.add(b[j])
        j += 1
      else:
        union_set.add(a[i])
        i += 1
        j += 1

    while i < n:
      union_set.add(a[i])
      i += 1

    while j < m:
      union_set.add(b[j])
      j += 1

    return len(union_set)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
print(doUnion(a, len(a), b, len(b)))
# output :- 5


# ------------------------------------------------------------- intersection of two sorted arrays -------------------------------------------- #

def concatination(a1, a2, m, n):
  m = len(a1)
  n = len(a2)
  for i in range(m):
    if i > 0 and a[i] != a[i - 1]:  # if i greater then zero means it contins previous value to check previous value exist you can use the this condition.
      continue
    for j in range(n):              # after iterating both loops and checking the previous value exist condition now iterate
      if a1[i] == a2[j]:               #the second array and check if the value of first array is equal to second array then print it.
        print(a[i],end = '')
        break



#                                                                  Efficient approach

def intersection(a1, a2, m, n):
  i = j = 0
  while i < m and j < n:
    if i > 0 and a[i] != a[i - 1]:
      i += 1
      continue
    if a1[i] < a2[j]:
      i += 1
    elif a1[i] > a2[j]:
      j += 1
    else:
      print(a[i], end = '')
      i += 1
      j += 1



############################################################################################################ count inversion in an array

def inv_count(arr):
  n = len(arr)
  res = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if arr[i] > arr[j]:
        res += 1
  return res


def countInv(arr, l, r):
  result = 0
  if l < r:
    mid = (l + r) // 2
    result += countInv(arr, l, mid)
    result += countInv(arr, mid + 1, r)
    result += merge(arr, l, mid, r)
  return result

def merge(arr, l, m, r):                                                                  #[2| 5| 8| 11| 3| 6| 9| 13|]
  left = arr[l:m+1]                                                                       # [2| 5| 8| 11]
  right = arr[m+1:r+1]                                                                    # [3| 6| 9| 13]
  res, i, j, k = 0, 0, 0, l                                                               # res = 0, i = 0, j = 0, k = 0
  while i < len(left) and j < len(right):                                                 # i < 4 and j < 4 true
    if left[i] <= right[j]:                                     # 1 iteration             # 2 <= 3 true
      arr[k] = left[i]                                                                    # arr[0] = 2    => [2|.....................] => k = 0 so put 2 at 0th index
      i += 1                                                                              # i = 1         => now i = 1 which is 5
      k += 1                                                                              # k = 1
    else:                                                       # 2 iteration             # 5 <= 3 false so else
      arr[k] = right[j]                                                                   # arr[1] = 3    => [2| 3|..................] => k = 1 so put 3 at 1st index
      j += 1                                                                              # j = 1         => now j = 1 which is 6
      k += 1                                                                              # k = 2
      res += (len(left) - i)                                                              # res = 0 +  (4 - 1) = 3 that mens in left array 3 elements are greater than 3 which are 5, 8, 11 so 3 inversions
  while i < len(left):                                          # 3 iteration             # 5 <= 6 true
      arr[k] = left[i]                                                                    # arr[2] = 5    => [2| 3| 5|................] => k = 2 so put 5 at 2nd index
      i += 1                                                                              # i = 2         => now i = 2 which is 8
      k += 1                                                                              # k = 3
  while j < len(right):                                         # 4 iteration             # 8 <= 6 false so else
      arr[k] = right[j]                                                                   # arr[3] = 6    => [2| 3| 5| 6|.............] => k = 3 so put 6 at 3rd index
      j += 1                                                                              # j = 2         => now j = 2 which is 9
      k += 1                                                                              # k = 4
  return res                                                                              # res = 3 + (4 - 2) = 5 that mens in left array 2 elements are greater than 6 which are 8, 11 so 2 inversions
                                                                # 5 iteration             # 8 <= 9 true
                                                                                          # arr[4] = 8    => [2| 3| 5| 6| 8|..........] => k = 4 so put 8 at 4th index
                                                                                          # i = 3         => now i = 3 which is 11
                                                                                          # k = 5
                                                                # 6 iteration             # 11 <= 9 false so else
                                                                                          # arr[5] = 9    => [2| 3| 5| 6| 8| 9|.......] => k = 5 so put 9 at 5th index
                                                                                          # j = 3         => now j = 3 which is 13
                                                                                          # k = 6
                                                                                          # res = 5 + (4 - 3) = 6 that mens in left array 1 elements are greater than 9 which is 11 so 1 inversions
                                                                # 7 iteration             # 11 <= 13 true
                                                                                          # arr[6] = 11   => [2| 3| 5| 6| 8| 9| 11|....] => k = 6 so put 11 at 6th index
                                                                                          # i = 4         => now i = 4 which is 13
                                                                                          # k = 7
                                                                # while loop 3            # 13 <= 13 true
                                                                                          # arr[7] = 13   => [2| 3| 5| 6| 8| 9| 11| 13|] => k = 7 so put 13 at 7th index
                                                                # loop ends and return res = 6 + (4 - 4) = 6 that mens in left array 0 elements are greater than 13 so 0 inversions

  # time complexity = O(nlogn)







########################################################################################### partion of given array ----#

def partion(arr, k):
  n = len(arr)
  arr[k], arr[n-1] = arr[n-1], arr[k]
  temp = []
  for i in range(len(arr)):
    if arr[i] <= arr[n-1]:                   # kth element is swapped with last element so compare it with last because it is not updated in original array
      temp.append(arr[i])
  for i in range(len(arr)):
    if arr[i] > arr[n-1]:
      temp.append(arr[i])
  for i in range(len(arr)):                  # its copy temp array to original array
    arr[i] = temp[i]
  return arr

arr = [5, 13, 6, 9, 12, 8, 11]
k = 5
print(partion(arr, k))
# output = [5, 6, 8, 9, 12, 13, 11]

# time complexity = O(n)



####################################################################################################  lomuto partion --

def lomuto_partion(arr, l, h):                                             # arr = [10, 80, 30, 90, 50, 70] l = 0, h = 5
  pivot = arr[h]                                                           # pivot = 70
  i = l - 1                                                                # i = -1
  for j in range(l, h):                                                    # j = 0 to 4
    if arr[j] < pivot:                                                     # 10 < 70 true
      i += 1                                                               # i = 0
      arr[i], arr[j] = arr[j], arr[i]                                      # arr[0], arr[0] = arr[0], arr[0] => [10, 80, 30, 90, 50, 70]
    arr[i+1], arr[h] = arr[h], arr[i+1]                                    # j = 1
    return i + 1                                                           # 80 < 70 false => loop continues and j = 2
                                                                           # 30 < 70 true
arr = [10, 80, 30, 90, 50, 70]                                             # i = 1
lomuto_partion(arr, 0, len(arr)-1)                                         # arr[1], arr[2] = arr[2], arr[1] => [10, 30, 80, 90, 50, 70]
print(*arr)                                                                # j = 3
                                                                           # 90 < 70 false => loop continues and j = 4
                                                                           # 50 < 70 true
                                                                           # i = 2
                                                                           # arr[2], arr[4] = arr[4], arr[2] => [10, 30, 50, 90, 80, 70]
                                                                           # loop ends  => arr[i+1], arr[h] = arr[h], arr[i+1] => arr[3], arr[5] = arr[5], arr[3] => [10, 30, 50, 70, 80, 90]
                                                                           # return i + 1 => 3 + 1 = 4
# In the code pivot element is always last element of array
# i is the index of smaller element and its initial value is -1 because we have to compare it with pivot element
# for loops runs from l to h-1 because h is pivot element and it is not included in loop
# if arr[j] is less then pivot element then increment i and swap arr[i] and arr[j] so that smaller element comes before pivot element loop continues
# if not small then loop continues and checks for next element
# in this i keeps the track of small element and only increment when arr[j] is less then pivot element and swap arr[i] and arr[j] so that smaller element comes before pivot element.








####################################################################################################  hoare partion --

def Hoare_partion(arr, l, h):
  pivot = arr[l]  # Selecting the pivot element
  i = l - 1  # Initialize pointer i to the left of the pivot
  j = h + 1  # Initialize pointer j to the right of the pivot

  while True:
    i += 1  # Move i to the right
    while arr[i] < pivot:  # Find the first element greater than or equal to the pivot
      i += 1

    j -= 1  # Move j to the left
    while arr[j] > pivot:  # Find the first element less than or equal to the pivot
      j -= 1

    if i >= j:
      return j  # Return the partitioning index

    # Swap the elements at indices i and j
    arr[i], arr[j] = arr[j], arr[i]








####################################################################################################  quick sort -------

# quick sort is a divide and conquer algorithm
# worst case time complexity = O(n^2)
# best case time complexity and average case time complexity = O(nlogn)
# its consider faster than merge sort because its in place sorting algorithm and cache friendly and tail recursive
# its not inplace algorithm because it uses extra space for recursion call stack or auxilary space for partitioning.


# when you dont need stable sorting algorithm then use quick sort if you need stable sorting algorithm then use merge sort.




##############################################################lumoto partition quick sort
  class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):

      if low < high:
        # pi is partitioning index, arr[pi] is now at right place.
        pi = self.lumoto_partition(arr, low, high)

        # Separately sorting elements before and after partitioning index.
        self.quickSort(arr, low, pi - 1)
        self.quickSort(arr, pi + 1, high)

    # Function that takes last element as pivot, places the pivot element at
    # its correct position in sorted list, and places all smaller elements
    # to left of pivot and all greater elements to right of pivot.
    def lumoto_partition(self, arr, low, high):

      # Index of smaller element and indicates the right position of
      # pivot found so far.
      i = (low - 1)
      # Picking the pivot.
      pivot = arr[high]

      for j in range(low, high):
        # If current element is smaller than or equal to pivot we increment
        # the value of i and swap the values at ith and jth index.
        if arr[j] <= pivot:
          i = i + 1
          # Swapping of values at ith and jth index.
          arr[i], arr[j] = arr[j], arr[i]

      # At last, swapping of value at ith and the last index which was
      # selected as pivot.
      arr[i + 1], arr[high] = arr[high], arr[i + 1]

      # returning the partitioning index.
      return (i + 1)




def hoarse_partion(arr, l, h):
  pivot = arr[l]
  i = l - 1
  j = h + 1

  while True:
    i += 1
    while arr[i] < pivot:
      i += 1
    j -= 1

    while arr[i] > pivot:
      j -= 1

    if i >= j:
      return j

    arr[i], arr[j] = arr[j], arr[i]

def quick_Sort(arr, l, h):
  if l < h:
    p = hoarse_partion()
    quick_sort(arr, l, p)
    quick_sort(arr, p+1, h)

arr = [8, 4, 7, 9, 3, 10, 5]
quick_sort(arr, 0, 6)
print(*arr)




# Analysis of QuickSort
# if the input array is already sorted or reverse sorted and if we select last element or first element as pivot element then time complexity will be O(n^2)
# Because in this case we will not be able to divide the array into two parts and one part will be empty and other part will have n-1 elements so we will have to do n-1 comparisions

##################################### so best to use when array is not sorted or reverse sorted and pivot element is selected randomly ###############################################








################################################################################################### heap sort ----------

# heap sort is a comparison based sorting algorithm
# its is used to sort the elements in ascending or descending order
# it can be used to select maximum or minimum element from array in 0(logn) time complexity
# its can be used over selection sort because in selection sort we have to do n-1 comparisions but in heap sort we have to do only logn comparisions
# its slower than quick sort and merge sort but its more efficient and faster than selection sort and bubble sort

# two steps:
# 1. build max heap
# 2. reptedly swap the root element with last element and reduce the size of heap by 1 and heapify the root element

# ----> (n-1) element -1 = ((n-1)-1)//2 by 2 for parent = ((n-2))//2 is the last non leaf node in heap



# if a node is at index i then its left child is at 2*i and right child is at 2*i+1 and parent is at i//2



def heapify(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and arr[i] < arr[l]:
    largest = l

  if r < n and arr[largest] < arr[r]
    largest = r

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

def heap_sort(arr):
  n = len(arr)
  for i in range(n//2-1, -1, -1):
    heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)


arr = [8, 4, 7, 9, 3, 10, 5]
heap_sort(arr)
print(*arr)
# output = 3 4 5 7 8 9 10






# find largest among root
def heapify(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and arr[i] < arr[l]:
    largest = l

  if r < n and arr[largest] < arr[r]:
    largest = r

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)
# If largest is not equal to i, it means that the value at index i is not the largest among the node and its children.
# In this case, a swap is performed between the values at indices i and largest to maintain the max heap property.
# Then, the heapify function is called recursively on the subtree rooted at index largest.

def heapsort(arr):
  n = len(arr)
  for i in range(n//2-1, -1, -1):
    heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)








#################################################################################################  hashing -------------

# hashing is a technique that is used to uniquely identify a specific object from a group of similar objects
# some examples of hashing are:
# 1. hashing is used in password
# 2. hashing is used in cryptography
# 3. hashing is used in indexing
# 4. hashing is used in compiler design
# 5. hashing is used in data security
# 6. hashing is used in graphics
# 7. hashing is used in robin - karp algorithm

# in hashing insertion and deletion and searching can be done in O(1) time complexity
# Basic operations of hashing:
# 1. Hashtable - this operation is used to create a hashtable
# 2. Delete - this operation is used to delete an element from hashtable
# 3. Get - this operation is used to get an element from hashtable
# 4. Put - this operation is used to insert an element in hashtable
# 5. DeleteHashTabel - this operation is used to delete the hashtable






# direct addressing table
# we can use direct addressing table when we know the range of keys in advance
# in direct addressing table we create an array of size equal to the range of keys and then we store the values at the index equal to the key

# if we dont know the range of keys in advance then we can use hash table
# direct addressing table is not suitable when the range of keys is very large like 10^6 or 10^9
# direct addressing table is not suitable when the keys are not integers like strings are used as keys






# How hash function works?
# A hash function is any function that can be used to map data of arbitrary size to fixed-size values.
# The values returned by a hash function are called hash values, hash codes, digests, or simply hashes.
# should generate the same values from 0 to n-1
# should generate values uniformly distributed across the table

# hash function is used to convert a large number into a small number by performing arithmetic operations on it.------->  h(k) = k mod m
# Hash function for strings:
# 1. simple hash function
# 2. polynomial rolling hash function
# 3. cyclic hash function
# 4. universal hash function

# simple hash function:
# h(k) = (sum of ascii values of characters in string) mod m
# m = size of hash table

# polynomial rolling hash function:
# h(k) = (sum of ascii values of characters in string * p^i) mod m
# p = prime number
# m = size of hash table
# i = index of character in string

# cyclic hash function:
# h(k) = (h(k) << 1) | (h(k) >> (m-1))
# m = size of hash table

# universal hash function:
# h(k) = ((a*k + b) mod p) mod m
# p = prime number
# m = size of hash table
# a = random number between 1 to p-1
# b = random number between 0 to p-1









# collision handling:  it means that two or more keys are mapped to the same index in hash table by hash function.
# 1. chaining
# 2. open addressing
 # 1. linear probing , 2. quadratic probing , 3. double hashing

# chaining:
# in chaining we create a linked list at each index of hash table and then we insert the elements in the linked list at the index equal to the hash value of the key
# chaining is used when we dont know the number of keys in advance
# chaining is used when the keys are not integers like strings are used as keys
# chaining is used when the range of keys is very large like 10^6 or 10^9
# chaining is used when the hash function is not uniform
# Example:
# hash table = [None, None, None, None, None, None, None, None, None, None]
# keys = [50, 700, 76, 85, 92, 73, 101] => keys mod 7 => [1, 0, 6, 1, 1, 3, 3]
# hash table = 0 [ 700]
#              1 [ 50 | 85 | 92]
#              2 [ ]
#              3 [ 73 | 101]
#              4 [ ]
#              5 [ ]
#              6 [ 76 ]

# performance of chaining:
# m = size of hash table
# n = number of keys
# load factor = n/m
# expected length of linked list = load factor = n/m
# expected time complexity of search , insert , delete = O(1 + load factor) = O(1 + n/m)

# data structure used in chaining:
# 1. linked list
# search and delete and insert in linked list takes O(n) time complexity because we have to traverse the linked list to find the element

# 2. self balancing binary search tree
# search and delete and insert in self balancing binary search tree takes O(logn) time complexity because we have to traverse the tree to find the element
# avl tree and red black tree are self balancing binary search tree

# 3. dynamic sized array
# search and delete and insert in dynamic sized array takes O(1) time complexity because we can directly access the element using index
# dynamic sized array is used when the keys are integers
# dynamic sized array is used when the range of keys is small
# dynamic sized array is used when the hash function is uniform



class myhash:
  def __init__(self, b):
    self.bucket = b
    self.table = [[] for x in range(b)]

  def insert(self, x):
    i = x % self.bucket
    self.table[i].append(x)

  def remove(self, x):
    i = x % self.bucket
    if x in self.table[i]:
      self.table[i].remove(x)

  def search(self, x):
    i = x % self.bucket
    return x in self.table[i]



# open addressing:
# in open addressing we insert the elements in the hash table at the index equal to the hash value of the key
# if the index is already occupied then we find the next empty index and insert the element there
# open addressing is used when we know the number of keys in advance
# open addressing is used when the keys are integers
# open addressing is used when the range of keys is small
# open addressing is used when the hash function is uniform


# linear probing:
# in linear probing we find the next empty index by incrementing the index by 1
# function used to find the next empty index = (index + 1) % m
# m = size of hash table

# search in linear probing:
# we search for the element by starting from the index equal to the hash value of the key
# if the element is not found at the index then we search for the element by incrementing the index by 1
# the search stops when we find the element [or] we find an empty index [or] we reach the index equal to the hash value of the key

# delete in linear probing:

# the deletion puts a tombstone at the index where the element was present so that the search does not stop at that index.

# we delete the element by starting from the index equal to the hash value of the key
# if the element is not found at the index then we delete the element by incrementing the index by 1


#    cluster = a group of consecutive elements in the hash table which are not at their hash value index and are not empty.






# quadratic probing:
# in quadratic probing we find the next empty index by incrementing the index by 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ....
# function used to find the next empty index = (index + i^2) % m
# m = size of hash table
# i = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ....




# double hashing:
# in double hashing we find the next empty index by incrementing the index by hash2(key)
# function used to find the next empty index = (index + hash2(key)) % m
# m = size of hash table
# hash2(key) = prime - (key % prime)
# prime = prime number less than m

# hash(key, i) = (hash1(key) + i * hash2(key)) % m
# example: 49, 63, 56, 52, 54, 48   m = 7
# hash1(key) = key % m = 49 % 7 = 0 no collision
# hash1(key) = key % m = 63 % 7 = 0 collision
# hash2(key) = prime - (key % prime) = 6 - (63 % 6) = 3 =>[ (0 + 1 * 3) % 7 = 3] no collision
# hash1(key) = key % m = 56 % 7 = 0 collision
# hash2(key) = prime - (key % prime) = 6 - (56 % 6) = 4 =>[ (0 + 1 * 4) % 7 = 4] no collision
# hash1(key) = key % m = 52 % 7 = 3 collision
# hash2(key) = prime - (key % prime) = 6 - (52 % 6) = 2 =>[ (3 + 1 * 2) % 7 = 5] no collision
# hash1(key) = key % m = 54 % 7 = 5 collision
# hash2(key) = prime - (key % prime) = 6 - (54 % 6) = 6 =>[ (5 + 1 * 6) % 7 = 4] collision  -> increment i
# hash2(key) = prime - (key % prime) = 6 - (54 % 6) = 6 =>[ (5 + 2 * 6) % 7 = 3] collision  -> increment i
# hash2(key) = prime - (key % prime) = 6 - (54 % 6) = 6 =>[ (5 + 3 * 6) % 7 = 2] no collision
# hash1(key) = key % m = 48 % 7 = 6 no collision


# performance of open addressing:
# m = size of hash table
# n = number of keys
# load factor = n/m
# expected length of cluster = O(logn)
# expected time complexity of search , insert , delete = O(1 / (1 - load factor)) = O(1 / (1 - n/m))





def sumExist(arr, n, sum):                           # first iteration
  s = set()
  for i in arr:
    diff = sum - i
    if diff in s:
      return 1
    s.add(i)
  return 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 14
n = len(arr)
print(sumExist(arr, n, sum))
# output: 1
# pair exist -> 4 + 10 = 14, 5 + 9 = 14, 6 + 8 = 14
# this code intialize empty set and traverse the array and  sum - i would give the other element of the pair ex: 14 - 4 = 10 and
# if 10 is present in the set then we return 1 else we add the element to the set and continue the loop.
# if the other element of the pair is present in the set then we return 1 else we add the element to the set and continue the loop.


# Function to check if there is a pair with the given sum in the array.
def sumExists(arr, N, sum):
  # using set to store the elements.
  mySet = set()

  # inserting all elements in the set.
  for i in arr:
    mySet.add(i)

    # iterating over the array.
  for i in arr:
    # taking care of cases like 4-2=2 as two 2's cannot exist in distinct
    # array so we continue iteration over next element.
    if (sum - i == i):
      continue
    else:
      # if (sum-arr[i]) exists in set, we return 1.
      if sum - i in mySet:
        return 1

  # if no such pair is present, we return 0.
  return 0







def linear_probing(hashsize, arr, sizeOfArray):
  hash = [-1] * hashsize
  for i in range(sizeOfArray):
    index = arr[i] % hashsize
    # linear probing
    while hash[index] != -1 and hash[index] != arr[i]:              # while loop iterates till the empty slot and checks the element is present or not
      index = (index + 1) % hashsize                                # hashtable[index] != arr[i]: checks if the element at the current slot is not equal to the element we are trying to insert (arr[i])

      if index == arr[i] % hashsize:                                #  check if probing process is complete one full cycle
        break
    if hash[index] == -1:
      hash[index] = arr[i]
  return hash



# In linear probing, when a collision occurs and the current slot is occupied,
# we increment the index and continue probing linearly until an empty slotor the same element is found.
# Therefore, we need to check if the current slot is occupied by the same element being inserted ///(hash[index] != arr[i])/// to avoid inserting duplicates.


arr = [4, 14, 24, 44]
hashsize = 10
sizeOfArray = len(arr)
linear_probing(hashsize, arr, sizeOfArray)



################################################################################################################### example code of linear probing
def linear_probing(hash_size, arr):
  hash_table = [-1] * hash_size  # Initialize the hash table with -1 (indicating an empty slot)

  for num in arr:
    index = num % hash_size  # Calculate the index for the current element

    while hash_table[index] != -1:  # hash_table[index] != arr[i]: means that the element at the current slot is not equal to the element we are trying to insert (arr[i])
      index = (index + 1) % hash_size  # Increment the index until an empty slot is found

    hash_table[index] = num  # Store the element in the next available slot

  return hash_table
################################################################################################################### example code of linear probing





def quadratic_probing(hash, hashSize, arr, N):
  for i in range(N):                                                              # => arr[i] not in hash: to avoid duplicate elements in hash table
    hash_value = arr[i] % hashSize
    if hash[hash_value] == -1:
      hash[hash_value] = arr[i]
    else:                                                                        # using while loop -> j = 1
      for j in range(1, hashSize):                                               # while j < hashSize:
        hash_value = (arr[i] + j * j) % hashSize                                 #   hash_value = (arr[i] + j * j) % hashSize
        if hash[hash_value] == -1 and arr[i] not in hash:                        #   if hash[hash_value] == -1 and arr[i] not in hash:
          hash[hash_value] = arr[i]                                              #     hash[hash_value] = arr[i]
          break                                                                  #     break
    return hash                                                                  #   j += 1



#In quadratic probing, when a collision occurs, we use a quadratic function to calculate the next probe position.
# We increment the iteration variable j and calculate a new hash value (arr[i] + j * j) % hashSize.
# Since the new position is calculated based on the element and the iteration variable,
# we need to check if the element is already present in the hash table (arr[i] not in hash) to avoid inserting duplicates.


##########################################  quadraric probing  -- but only 87 % test cases passed ##########################################

def quadraticProbing(hash, hashSize, arr, N):
  for i in range(N):
    index = arr[i] % hashSize
    if hash[index] == -1:
      hash[index] = arr[i]
    else:
      k = 1
      while True:
        next_index = (index + k * k) % hashSize
        if hash[next_index] == -1 and arr[i] not in hash:
          hash[next_index] = arr[i]
          break
        k += 1
  return hash










###################################################################################################   separate chaining

# In separate chaining, each slot of the hash table is a linked list.
# When a collision occurs, the element is inserted at the end of the linked list at the current slot.
# Therefore, we need to check if the element is already present in the linked list to avoid inserting duplicates.

# Function to insert elements of into hashTable

def sperateChaining(hashSize, arr, sizeOfArray):
  hashtable =[[] for i in range(hashSize)]             # the loop is used to create a empty list for each index of the hash table till the hash size.
  for i in range(sizeOfArray):
    index = arr[i] % hashSize
    hashtable[index].append(arr[i])
  return hashtable


def sperateChaining(hashSize, arr, sizeOfArray):
  hastbale = [0] * hashSize
  for i in range(hashSize):                            # the loop is used to create a empty list for each index of the hash table till the hash size.
    hastbale[i] = []
    for i in range(sizeOfArray):
      hashtable[arr[i] % hashSize].append(arr[i])
  return hashtable








def countFrequency(arr):
  frequency = {}
  for num in arr:
    if num in frequency:
      frequency[num] += 1
    else:
      frequency[num] = 1
  return frequency


arr = [1, 2, 4, 3, 4, 5, 6, 7, 8, 9, 1]
print(countFrequency(arr))
# output: {1: 2, 2: 1, 4: 2, 3: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}







def countFrequency(arr):
  visited = [False for i in  range(len(arr))]   # it makes a list of false values with the length of the array
  for i in range(len(arr)):          # it iterates through the array
    if visited[i] == True:           # if the element is already visited then we continue the loop and go to the next iteration
      continue
    count = 1                        # else we make the count as 1 and make the visited element as true
    for j in range(i + 1, len(arr)): # then we iterate through the array from the next element of the current element
      if arr[i] == arr[j]:           # if we find same element then we increment the count and make the visited element as true
        visited[j] = True
        count += 1
    print(arr[i], count)






############################################################################################### open addressing implementation of linear probing


class MyHash:
  def __init__(self, c):
    self.capacity = c
    self.table = [-1] * c
    self.size = 0

  def hashFunction(self, key):
    return key % self.capacity

  def search(self, element):
    h = self.hashFunction(element)
    index = h
    while self.table[index] != -1:
      if self.table[index] == element:
        return True
      index = (index + 1) % self.capacity
      if index == h:
        return False
    return False

  def insert(self, element):
    if self.size == self.capacity:
      return False
    if self.search(element) == True:
      return False
    h = self.hashFunction(element)
    index = h
    while self.table[index] not in (-1, -2):
      index = (index + 1) % self.capacity
    self.table[index] = element
    self.size += 1
    return True

  def delete(self, element):
    h = self.hashFunction(element)
    index = h
    while self.table[index] != -1:
      if self.table[index] == element:
        self.table[index] = -2
        return True
      index = (index + 1) % self.capacity
      if index == h:
        return False
    return False

#############################################################################################################################################################################################################################

  class Book:
    def __init__(self, title, author):
      self.title = title
      self.author = author


class LibraryCatalog:
  def __init__(self):
    self.table_size = 10
    self.table = [[] for _ in range(self.table_size)]

  def hash_function(self, title):
    # A simple hash function that calculates the sum of ASCII values of the characters in the title
    # and returns the modulo with the table size
    hash_value = sum(ord(char) for char in title)
    return hash_value % self.table_size

  def add_book(self, book):
    index = self.hash_function(book.title)
    self.table[index].append(book)

  def find_books_by_title(self, title):
    index = self.hash_function(title)
    books = self.table[index]
    found_books = [book for book in books if book.title == title]
    return found_books

  def find_books_by_author(self, author):
    found_books = []
    for bucket in self.table:
      for book in bucket:
        if book.author == author:
          found_books.append(book)
    return found_books


# Example usage
library = LibraryCatalog()

# Adding books to the library catalog
book1 = Book("Python Programming", "John Smith")
library.add_book(book1)

book2 = Book("Data Structures", "Alice Johnson")
library.add_book(book2)

book3 = Book("Python Programming", "Michael Brown")
library.add_book(book3)

# Finding books by title
title = "Python Programming"
found_books = library.find_books_by_title(title)
print("Books with title '" + title + "':")
for book in found_books:
  print(book.title + " by " + book.author)

# Finding books by author
author = "John Smith"
found_books = library.find_books_by_author(author)
print("Books by author " + author + ":")
for book in found_books:
  print(book.title + " by " + book.author)


#############################################################################################################################################################################################################################

#  chaining and open addressing are the two ways to implement the hash table

#  chaining is the best way to implement the hash table
#  open addressing is the worst way to implement the hash table


# chaining is better than open addressing when the load factor is greater than 0.7
#  open addressing is better than chaining when the load factor is less than 0.7

# chaining is better than open addressing when the size of the hash table is large or hash table is dynamic size
# chaining is better than open addressing when the hash table is not fixed size
#  open addressing is better than chaining when the size of the hash table is small or hash table is fixed size






##################################################################################################        set in python

# distinct elements in an array
# unordered
# no indexing
# union, intersection, difference, symmetric difference, subset, superset, disjoint are the operations that can be performed on the set


# methods in set                                                                                                                             s1 = {1, 2, 3, 4, 5}          if s = {} then it is a dictionary
# add() - adds an element to the set                                                                                                         => s1.add(6) => {1, 2, 3, 4, 5, 6}
# clear() - removes all the elements from the set                                                                                            => s1.clear() => {}
# copy() - returns a copy of the set                                                                                                         => s2 = s1.copy()
# difference() - returns a set containing the difference between two or more sets                                                            => s1.difference(s2) => {1, 2, 3, 4, 5}
# difference_update() - removes the items in this set that are also included in another, specified set                                       => s1.difference_update(s2) => {1, 2, 3, 4, 5}
# discard() - remove the specified item IF NOT PRESENT, do nothing                                                                           => s1.discard(6) => {1, 2, 3, 4, 5}
# remove() - remove the specified item IF NOT PRESENT, raise an error                                                                        => s1.remove(6) => error
# intersection() - returns a set, that is the intersection of two other sets  => A.intersection(B)                                           => s3 = {1, 2, 3} s4 = {2, 3, 4} s3.intersection(s4) => {2, 3}
# intersection_update() - removes the items in this set that are not present in other, specified set(s) => A.intersection_update(B)          => s3.intersection_update(s4) => {2, 3}
# isdisjoint() - returns whether two sets have a intersection or not => A.isdisjoint(B)                                                      => s3.isdisjoint(s4) => False
# issubset() - returns whether another set contains this set or not => A.issubset(B)                                                         => s3.issubset(s4) => False
# issuperset() - returns whether this set contains another set or not => A.issuperset(B)                                                     => s3.issuperset(s4) => False
# pop() - removes an element from the set                                                                                                    => s1.pop() => {2, 3, 4, 5}
# symmetric_difference() - returns a set with the symmetric differences of two sets => A.symmetric_difference(B)                             => s3.symmetric_difference(s4) => {1, 4}
# symmetric_difference_update() - inserts the symmetric differences from this set and another => A.symmetric_difference_update(B)            => s3.symmetric_difference_update(s4) => {1, 4}
# union() - return a set containing the union of sets => A.union(B)                                                                          => s3.union(s4) => {1, 2, 3, 4}
# update() - update the set with the union of this set and others => A.update(B)                                                             => s3.update(s4) => {1, 2, 3, 4}






##################################################################################################        dictionary in python

# key value pairs
# unordered
# no indexing
# keys are unique
# values can be duplicate
# keys can be any immutable data type
# values can be any data type

# methods in dictionary
# clear() - removes all the elements from the dictionary
# copy() - returns a copy of the dictionary
# fromkeys() - returns a dictionary with the specified keys and values
# get() - returns the value of the specified key
# items() - returns a list containing a tuple for each key value pair




##################################################################################################       count distinct elements in an array

def countDistinct(arr, n):
  res = 1
  for i in range(1, n):
    if arr[i] not in arr[0:i]:
      res += 1
  return res

arr = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(countDistinct(arr, n))
# output => 8



##################################################################################################       count distinct elements in an array
def countNonRepeated(arr, n):
  d = {}
  for i in range(n):
    if arr[i] in d:
      d[arr[i]] += 1
    else:
      d[arr[i]] = 1
  count = 0
  for i in d:                     # in this for loop we check for the keys which are frequency of the elements
    if d[i] == 1:
      count += 1
  return count

def printNonRepeated(arr, n):
  d = {}
  for i in range(n):
    if arr[i] in d:
      d[arr[i]] += 1
    else:
      d[arr[i]] = 1
  list = []
  for i in range(n):                       # to get output in the same order as the input
    if d[arr[i]] == 1:
      list.append(arr[i])                  # i gives index and arr[i] gives the element at that index
  return list
  # for i in d:                            # this is to get output in any order
  #   if d[i] == 1:
  #     list.append(d[arr[i]])
  # return list
##################################################################################################### `count distinct char in a string
def nonrepeatingchar(s):
  seen = {}
  for char in s:
    if char in seen:
      seen[char] += 1
    else:
      seen[char] = 1
  list = []
  for char in s:
    if seen[char] == 1:
      list.append(char)
  return list

#############################################################################################################################################################################################################################

##################################################################################################       count distinct names in a list

def countDistinct(votes, n):
  vote_count = {}
  for candiate in votes:
    if candiate in vote_count:
      vote_count[candiate] += 1
    else:
      vote_count[candiate] = 1                                                                                                                  # best code to expalin how to use dictionary
  max_votes = 0
  winner = ""
  for candiate in vote_count:
    if vote_count[candiate] > max_votes:
      max_votes = vote_count[candiate]
      winner = candiate
  return winner


##################################################################################################       count distinct names in a list

# lexographically smallest string
# if two strings are same then the one with the smaller length is the smallest
# if two strings are same then the one with the smaller index is the smallest

def lexographicallySmallestString(votes, n):
  vote_count = {}
  for candiate in votes:
    if candiate in vote_count:
      vote_count[candiate] += 1
    else:
      vote_count[candiate] = 1
  max_votes = 0
  winner = ""
  for candiate, count in vote_count.items():
    if count > max_votes or (count == max_votes and candiate < winner):   # when count is max votes and candiate is smaller than previous candiate who have same votes then we update the winner
      max_votes = count
      winner = candiate
  return winner

############################################################################################################################################################################################################################






def first_repat(arr, n):
  seen = {}
  for num in arr:
    if num in seen:
      seen[num] += 1
    else:
      seen[num] = 1
  for num in arr:          # this loop runs through the array and checks if the element is present in the dictionary or not
    if seen[num] > 1:      # and if it is present then it checks if the value of that key is greater than 1 or not
      return num + 1
  return -1


#  sring -> have reverse function ->
# or for loop -> for char in string

def rotate(s, s1):
  if len(s) != len(s1)
    return False
  for i in range(len(s1)):
    if s[i:] + s[:i] == s1: # it would work like this -> s1 = "abcde" -> s1[1:] = "bcde" -> s1[:1] = "a" -> s1[1:] + s1[:1] = "bcdea"
      return True
  return False

def rotate(s, s1):
    if len(s) != len(s1)
        return False
    result = s + s
    if s1 in result:
        return True
    return False

def rotate(s, s1):
    if len(s) != len(s1)
        return False
    return s1 in s + s






def palindrome(s):   # abba
  low = 0
  high = len(s) - 1
  while low < high:
    if s[low] != s[high]:  # a != a => false -> low = 1, high = 2 => b != b => false
      return False         # -> low = 2, high = 1 => low > high => false
    low += 1
    high -= 1
  return True

def palindrome(s):
  return s == s[::-1]




def subSequence(s1, s2):
  j = 0
  for char in s1:
    if char == s2[j]:
      j += 1
      if j == len(s2):
        return True
  return False
s1 = "abcde"
s2 = "ace"
print(subSequence(s1, s2))
# output => True




def subSequence(s1, s2, m, n):                   # iterating from the end of the string m = len(s1) and n = len(s2)
  if n == 0:                                     # if n == 0 then it means that we have reached the end of the string s2 and we have found all the characters of s2 in s1
    return True
  if m == 0:                                     # if n is not 0 and m is 0 then m is not the subsequenece of n return false else travel to the next if statement
    return False
  if s1[m - 1] == s2[n - 1]:
    return subSequence(s1, s2, m - 1, n - 1)
  return subSequence(s1, s2, m - 1, n)










def anagram(s1, s2):
  if len(s1) != len(s2):
    return False
  seen = {}
  for char in s1:
    if char in seen:
      seen[char] += 1
    else:
      seen[char] = 1
  for char in s2:
    if char in seen:
      seen[char] -= 1
      if seen[char] == 0:
        del seen[char]         # if you return True here then it will return True for "abc" and "ab" also so you have to check if the length of the dictionary is 0 or not
    else:                      # else should be here because if the char is not in seen then it is not an anagram
      return False        #note----- if you put else under 2 if statment it will check for the char == 1 then it will go to else and return False which is wrong because it is not an anagram
  return len(seen) == 0





def anagram(s1, s2):
  if len(s1) != len(s2):
    return False
  s1 = sorted(s1)
  s2 = sorted(s2)
  return s1 == s2

def anagram(s1, s2):
  if len(s1) != len(s2):
    return False
  count = [0] * 256
  for i in range(len(s1)):
    count[ord(s1[i])] += 1
    count[ord(s2[i])] -= 1
  for x in count:
    if x != 0:
      return False
  return True

s1 = "abcde"
s2 = "edcba"
print(anagram(s1, s2))








def leftmost(str):
  for i in range(len(str)):
    for j in range(i + 1, len(str)):
      if str[i] == str[j]:
        return str[i]
  return -1


str = "geeksforgeeks"
print(leftmost(str))
# output => g









def leftmost(str):
  count = [0] * 256
  for i in range(len(str)):
    count[ord(str[i])] += 1
  for i in range(len(str)):
    if count[ord(str[i])] > 1:
      return i
  return -1










65 - 90 and 97 - 122
def isPanagram(s):
  for i in range(65, 91):
    if chr(i) not in s and chr(i + 32) not in s:
      return False
  return True

s = thequickbrownfoxjumpsoverthelazydog
print(isPanagram(s))
# output => True because all the alphabets are present in the string s


# def missing_panagram(s):
#   ch = [False] * 26
#   for i in range(len(s)):
#     if s[i] >= 'a' and s[i] <= 'z':             # if operation on m
#       ch[ord(s[i]) - ord('a')] = True           # ord('m') - ord('a') => 109 - 97 => 12 => ch[12] = True
#     elif s[i] >= 'A' and s[i] <= 'Z':
#       ch[ord(s[i]) - ord('A')] = True
#   res = ""
#   for i in range(26):
#     if ch[i] == False:
#         res += chr(i + ord('a'))
#   return res


def missing_panagram(s):
  ch = [False] * 26
  for i in range(len(s)):
    if s[i].isalpha():
      if s[i].islower():
        ch[ord(s[i]) - ord('a')] = True
      else:
        ch[ord(s[i]) - ord('A')] = True
  res = ""
  for i in range(26):
    if ch[i] == False:
      res += chr(i + ord('a'))
  return res







# left most non repeating character

def left_most_nrepat(s):
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      if s[i] == s[j]:
        break
      return i
  return -1

# this is better but do not work for all the cases

def left_most_norep(s):
  count = [0] * 256
  for i in range(len(s)):
    count[ord(s[i])] += 1
  for i in range(len(s)):
    if count[ord(s[i])] == 1:
      return i
  return -1


# this is the best solution for this problem

def left_most_norep(s):
  count = [-1] * 256
  for i in range(len(s)):
    if count[ord(s[i])] == -1:
      count[ord(s[i])] = i
    else:
      count[ord(s[i])] = -2  # it means that the character is repeating
  res = float('inf')
  for i in range(256):
    if count[i] >= 0:
      res = min(res, count[i])
  return res if res != float('inf') else -1










def reverse_words(s):
  while start < end:
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1

def reverse(s):
  n = len(s)
  s = list(s)
  start = 0
  for end in range(n):
    if s[end] == ' ':                       # it will run till it find the space
      reverse_words(s, start, end - 1)      # it will reverse the word                 like "welcome" => "emoclew"
      start = end + 1                       # to count the space and start from the next word
  reverse_words(s, start, n - 1)            # it will reverse the last word because there is no space after the last word so it will not reverse the last word
  return "".join(s)                         # it will join the list and return the string










def validate(s):
  if len(s) < 10:
    return False
  digit = False
  lower = False
  upper = False
  special = False
  for i in range(len(s)):
    if s[i].isdigit():
      digit = True
    elif s[i].islower():
      lower = True
    elif s[i].isupper():
      upper = True
    else:
      special = True
  return digit and lower and upper and special

















############################################################################################################## linked list

# Difference between array and linked list
# 1. Array is a collection of elements of similar data type whereas the Linked list is a collection of elements of different data types.
# 2. Array size is fixed whereas the linked list size is dynamic.
# 3. Array elements are stored in contiguous memory locations whereas the linked list elements are stored in random memory locations.
# 4. Array access time is fast whereas the linked list access time is slow.
# 5. Array deletion or insertion is time consuming whereas the linked list deletion or insertion is fast.
# 6. Array memory is allocated during compile time whereas the linked list memory is allocated during execution or runtime.
# 7. Array elements can be accessed randomly whereas the linked list elements cannot be accessed randomly.
# 8. Array elements are stored in stack memory whereas the linked list elements are stored in heap memory.




# applications of linked list
# 1. worst case insertion and deletion is O(1)
# 2. insertion and deletion is fast in linked list
# 3. Round robin scheduling algorithm
# 4. Merging of two sorted linked list is easy
# 5. implementation of stack and queue is easy

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def displayList(head):
    curr = head
    while curr != None:
      print(curr.data, end=" ")
      curr = curr.next

def sumofElements(head):
    curr = head
    sum = 0
    while curr != None:
      sum += curr.data
      curr = curr.next
    return sum

def search(head, x):
  curr = head
  position = 1
  while curr != None:
    if curr.data == x:
      return position
    else:
      position += 1
      curr = curr.next
  return -1

def insert(head, key):
  temp = Node(key)
  temp.next = head
  return temp

def insertAtEnd(head, key):
    temp = Node(key)
    if head == None:          # if the linked list is null then it will return the temp
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    return head

def insertatPos(head, position, data):
  newnode = Node(data)
  if position == 1:
    newnode.next = head
    return newnode
  curr = head
  for i in range(position - 2):
    curr = curr.next
    if curr == None:
      return head
    newnode.next = curr.next
    curr.next = newnode
    return head


# 45 at position 4  => temp = 45 and next is none
# [10, 20, 30, 40, 50]
# for loop iterates till 20 and curr = curr.next => 30
# temp.next = curr.next => 45.next will be 40
# curr.next = temp => 30.next will be 45


def deleteFirst(head):
  if head == None:
      return None
  newHead = head.next
  head.next = None
  return newHead


################################################################################################# delete last node



def deleteLast(head):
  if head == None:                # if the linked list is empty
    return None
  if head.next == None            # it means that there is only one node in the linked list
    return None
  curr = head
  while curr.next.next != None:   # it will iterate till the second last node
    curr = curr.next
  curr.next = None                # it will unlink the last node
  return head

############################################################################################# delete at position

# to delete the node at the given position in the linked list we have to iterate till the previous node of the given position
# and then we have to unlink the node at the given position and link the previous node to the next node of the given position

def deleteAtPos(head, position):
  if position == 1:                   # if the position is 1 then we have to delete the first node
    newHead = head.next               # newHead will be the next node of the head and head.next will be None
    head.next = None
    return newHead
  curr = head
  for i in range(position - 2):      # it will iterate till the previous node of the given position and if the position is 3 then it will iterate till the 1.
    curr = curr.next
    if curr == None:                 # if the position is greater than the length of the linked list then it will return the head
      return head
  curr.next = curr.next.next         # it will unlink the node at the given position and link the previous node to the next node of the given position
  return head



# trick question

# delete the node where pointer is pointing to the node to be deleted
# swap the data of the node to be deleted with the next node
def deleteNode(ptr):                         #    -> 10 -> 20 -> 30 -> 40 -> 50 ptr = 30 you need to delete 30 cant go back
  temp = ptr.next                            #    temp = 40
  ptr.data = temp.data                       #    ptr.data = 40        -> 10 -> 20 -> 40 -> 40 -> 50
  ptr.next = temp.next                       #    ptr.next = temp.next => ptr.next = 50   drop the 40 node
  temp.next = None                           #    temp.next = None
  del temp                                   #    delete the temp node
  return head







##################################################################################################### sort the linked list

def sort(head, x):
  if head == None:
    return None
  temp = Node(x)
  curr = head
  # if the value of the node is less than the value of the head then the temp will be the new head like 10 -> 20 -> 30 -> 40 -> 50 and x = 5 then temp will be the new head
  if x < curr.data:
    temp.next = curr
    return temp
  # we use curr.next.data because we have to compare the value of the node with the value of the next node
  # because we have to insert the node after the node whose value is less than the value of the node like 10 -> 20 -> 30 -> 40 -> 50 and x = 35 then temp will be inserted after 30
  # note : curr.data < x will take curr as 40 do it iteration so we use curr.next.data------------------------------------------
  while curr.next != None and curr.next.data < x: # Pattern : curr.next != None and curr.next.data < x -------------------------
    curr = curr.next
  temp.next = curr.next
  curr.next = temp
  return head                                      # while loop first check curr.next != None and then it will check curr.next.data < x because if the curr.next is None then it will give error











############################################################################################ middle of the linked list

def middle(head):
  if head == None:
    return None
  curr = head
  count = 0
  while curr != None:
    curr = curr.next
    count += 1
  curr = head
  for i in range(count // 2):
    curr = curr.next
  return curr.data

----------------------------------  OR  ----------------------------------

def middle(head, data):
  if head == None:
    return None
  temp = Node(data)
  slow = head
  fast = head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
  temp.next = slow.next
  slow.next = temp
  return head









##########################################################################################  sorted - in ascending order or descending order

def insorted(head):
  if head == None:
    return None
  curr = head
  increasing = True
  decreasing = True
  while curr.next != None:
    if curr.data < curr.next.data:
      decreasing = False
    elif curr.data > curr.next.data:
      increasing = False
    curr = curr.next
  return increasing or decreasing






#############################################  nth node from end of linked list  #############################################
def n_node(head, n):
  length = 0
  curr = head
  while curr != None:
    curr = curr.next
    length += 1
  if n > length:  # it should be outside the while loop because if the n is greater than the length of the linked list then it will return -1
    return -1
  curr = head
  for i in range(length - n):
    curr = curr.next
  return curr.data



----------------------------------  OR  ----------------------------------


def n_node(head, n):
  if head == None:
    return None
  slow  = head
  fast = head
  for i in range(n):
    if fast == None:    # after the for loop if the fast is None then it means that the n is greater than the length of the linked list
      return -1         # so check if the fast is None then return -1 if the fast is not None then continue the loop and increment the fast
    fast = fast.next
  while fast != None:
    slow = slow.next
    fast = fast.next
  return slow.data








def join(head1, head2):
  if head1 == None:
    return head2
  if head2 == None:
    return head1
  curr = head1
  while curr.next != None:
    curr = curr.next
  curr.next = head2
  return head1










def removedupli(head):
  curr = head
  while curr != None and curr.next != None: # curr.next != None because we have to compare the value of the node with the value of the next node
    if curr.data == curr.next.data:
      curr.next = curr.next.next     # unlink 10 -> 20 -> 20 -> 30 -> 30 => curr = 20 => curr.next = 20 => curr.next.next = 30 => curr.next = 30
    else:
      curr = curr.next
  return head










#############################################  reverse the linked list  #############################################

def reverse(head):
  stack = []
  curr = head
  while curr != None:
    stack.append(curr.data)
    curr = curr.next

  curr = head
  while curr != None:
    curr.data = stack.pop()
    curr = curr.next

  return head





----------------------------------  OR  ----------------------------------

def reverse(head):
  curr = head
  prev = None    # prev = None because the last node will point to None and after 1 iteration the head will point to None
  while curr != None:
    next = curr.next   # its storing the next node of the current node in pointer next so that we dont loose link to the next node
    curr.next = prev   # it will point the current node to the previous node
    # now we have to move the prev and curr pointer to the next node
    prev = curr        # prev will point to the current node
    curr = next        # curr will point to the next node
  return prev          # prev will point to the last node so return prev






----------------------------------  OR  ----------------------------------

def recursive_reverse(head):
  if head == None or head.next == None:       # head is second last node
    return head
  rest_head = recursive_reverse(head.next)   # it will recursively call the function until the head.next == None and make recursive call stack for each node and rest head is last node
  rest_tail = head.next                      #it will be the last node of the linked list named rest_tail
  rest_tail.next = head                      # it will point the last node to the second last node
  head.next = None                           # it will point the second last node to None -> none would be moving backwards from last at every stack frame
  return rest_head




----------------------------------  OR  ----------------------------------
# it will reverse linked list reursively by using 2 pointers
def recursive_reverse(head, prev = None):   # prev = None because the last node will point to None and after 1 iteration the head will point to None
  if head == None:                          # this base case will return the last node because the last node will point to None and after 1 iteration the head will point to None
    return prev
  next = head.next
  head.next = prev
  return recursive_reverse(next, head)      # moving the prev and curr pointer to the next node



def maximum(head):
  if head == None:
    return None
  curr = head
  max = head.data
  while curr != None:
    if curr.data > max:
      max = curr.data
    curr = curr.next
  return max

def minimum(head):
  if head == None:
    return None
  curr = head
  min = head.data         # min = float('inf')  # min = sys.maxsize
  while curr != None:
    if curr.data < min:
      min = curr.data
    curr = curr.next
  return min






def areidentical(head1, head2):
  if head1 == None and head2 == None:
    return False
  curr1 = head1
  curr2 = head2
  while curr1 != None and curr2 != None:
    if curr1.data == curr2.data:
      curr1 = curr1.next
      curr2 = curr2.next
    else:
      return False
  if curr1 == None and curr2 == None:
    return True

  ----------------------------------  OR  ----------------------------------

def areidentical(head1, head2):
  while head1 != None and head2 != None:
    if head1.data != head2.data:
      return False
    head1 = head1.next
    head2 = head2.next
  if head1 == None and head2 == None:
    return True












#################################################                                       circular linked list

# advantages of circular linked list    -----------  There is no need to maintain the tail pointer in circular linked list

# 1. we can traverse the whole linked list by using any node
# 2. we can insert and delete the node at the beginning and end of the linked list in O(1) time complexity
# 3. implementation of queue and stack is easy and round robin scheduling is done by using circular linked list

# disadvantages of circular linked list

# 1. Direct access of any node is not possible
# 2. we can not traverse the linked list in backward direction
# 3. we can not insert and delete the node at the middle of the linked list in O(1) time complexity



# insert at the beginning of the circular linked list
def insert_at_beginning(head, data):
  temp = Node(data)
  if head == None:
    temp.next = temp
    return temp
  curr = head
  while curr.next != head:
    curr = curr.next
  curr.next = temp
  temp.next = head
  return temp


----------------------------------  OR  ----------------------------------

def insert_at_beginning(head, data):
  temp = Node(data)
  if head is None:
    temp.next = temp
    return temp
  temp.next = head.next
  head.next = temp
  head.data, temp.data = temp.data, head.data
  return head





# insert at the end of the circular linked list



























# is circular linked list

def iscircular(head):
  if head == None:
    return True
  curr = head
  while curr != None and curr.next != head:
    curr = curr.next
  if curr == None:                                # if curr == None then it means that the linked list is not circular
    return False
  return True



# split circular linked list into 2 halves
def split(head):
    if head == None:
        return None
    slow = head
    fast = head
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    if fast.next.next == head:
        fast = fast.next
    head1 = head
    head2 = slow.next
    slow.next = head1
    fast.next = head2
    return head1, head2






# delete a head node from the circular linked list
def delete_head(head):
  if head == None:
    return None
  if head.next == head:
    return head.next
  curr = head
  while curr.next != head:
    curr = curr.next
  curr.next = head.next
  head.next = None     # it is not necessary to write this line
  return curr.next


----------------------------------  OR  ----------------------------------

def delete_head(head):
  if head == None:
    return None
  if head.next == head:
    return head.next
  head.data = head.next.data
  head.next = head.next.next
  return head






# delete a node from the circular linked list

def deleteAtPosition(head, pos):
  if head == None:
    return None
  elif head.next == head:
    return None

  if pos == 1:
    head.data = head.next.data
    head.next = head.next.next
    return head

  curr = head
  for _ in range(pos - 2):
    curr = curr.next
  curr.next = curr.next.next
  return head








def insert_at_position(head, data, pos):
  if head == None:
    return None
  temp = Node(data)
  curr = head
  if pos == 1:
    while curr.next != head:
      curr = curr.next
    curr.next = temp
    temp.next = head
    return temp                                              ################         --- important
  for _ in range(pos - 1):   # to insert we go to previos node of the position and to delete we go to the previous node of the position means we have to run the loop pos - 2 times
    curr = curr.next
    if curr == head:
      return head
  temp.next = curr.next
  curr.next = temp
  return head












#########################################                        doubly linked list

# advantages of doubly linked list

# 1. we can traverse the linked list in both directions
# 2. we can insert and delete the node at the beginning and end of the linked list in O(1) time complexity
# 3. we can insert and delete the node at the middle of the linked list in O(1) time complexity if we have the pointer to the node

# disadvantages of doubly linked list

# 1. we have to maintain the previous pointer also so it will take extra space
# 2. we can not traverse the linked list in backward direction if we don't have the previous pointer
# 3. implementation of queue and stack is difficult as compared to singly linked list





# display the doubly circular linked list

def iscircular(head):
    if head == None:
        return True
    curr = head
    while curr.next != head:
      if curr.next == None:
        return False
      curr = curr.next
    return True



----------------------------------  OR  ----------------------------------

def iscircular(head):
    if head == None:
      return True
    curr = head
    while curr != None and curr.next != head:   # only when curr != None then only we will check for curr.next != head it means that if curr == None then there is no need to check for curr.next != head
      curr = curr.next
    if curr == None:
      return False
    return True







# Doubly Linked list at given position

def addNode(head, pos, data):
  temp = Node(data)
  curr = head
  while p != 0:
    curr = curr.next
    p -= 1

  if curr.next is None:
    curr.next = temp
    temp.prev = curr
    return head
  else:
    temp.next = curr.next     # it means that we are inserting the node at the middle of the linked list
    curr.next = temp
    temp.prev = curr
    return head


----------------------------------  OR  ----------------------------------

def addNode(head, pos, data):
  temp = Node(data)
  curr = head
  for _ in range(pos):
    curr = curr.next
  temp.next = curr.next
  curr.next = temp
  temp.prev = curr
  return head


----------------------------------  OR  ----------------------------------


def addNode(head, p, data):
  temp = Node(data)
  curr = head
  for i in range(p):
    curr = curr.next
  if curr.next is not None:
    temp.next = curr.next  # if you dont write this you will lose rest nodes
    curr.next = temp
    temp.prev = curr
  else:
    curr.next = temp
    temp.prev = curr
  return head





# delete head of a doubly linked list

def delete_head(head):
  if head == None:
    return None
  if head.next == None:
    return None
  head = head.next
  head.prev = None
  return head








# find middle of a circular doubly linked list

def find_mid(head):
  if head == None:
    return None
  if head.next == None:
    return head
  slow = head
  fast = head
  while fast.next != head and fast.next.next != head:
    slow = slow.next
    fast = fast.next.next
  if fast.next.next == head:
    fast = fast.next
  return slow

 ----------------------------------  OR  ----------------------------------

 def find_mid(head):
   if head is None and head.next is None:
     return head
   curr = head
   length = 0
   for _ in range(length//2):
     curr = curr.next       # or if curr != None and curr.next != None: curr = curr.next.nexta
    return curr.data




 # delete a last node from a doubly linked list

def delete_last(head):
  if head is None and head.next is None:
    return None
  curr = head
  while curr.next.next is not None:
    curr = curr.next
  curr.next = None
  return head








# delete a node from a doubly linked list

def delete_node(head, pos):
  curr = head
  if pos == 1:
    head = head.next
    head.prev = None
    return head
  else:
    while pos > 1:
      curr = curr.next
      pos -= 1
    curr.prev.next = curr.next
    if curr.next is not None:
      curr.next.prev = curr.prev
    return head








def sortedInsert(head, data):
  temp = Node(data)
  if head == None:
    return temp
  if head.data > data:
    temp.next = head
    head.prev = temp
    return temp
  curr = head
  while curr.next != None and curr.next.data < data:
    curr = curr.next
  temp.next = curr.next   # it means that if curr.next == None then temp.next = None
  curr.next = temp
  temp.prev = curr
  if temp.next != None:   # it means that if temp.next == None then temp.next.prev = None so we have to check for temp.next != None
    temp.next.prev = temp
  return head









def compareCll(head1, head2):
  if head1 == None and head2 == None:
    return 1
  if head1 == None or head2 == None:
    return 0
  curr1 = head1
  curr2 = head2
  while curr1.next != head1 and curr2.next != head2:
    if curr1.data != curr2.data:
      return 0
    curr1 = curr1.next
    curr2 = curr2.next
  if curr1.next == head1 and curr2.next == head2:
    if curr1.data == curr2.data:
      return 1
    else:
      return 0
  return 0












#########################################                        stack

# stack is a linear data structure in which insertion and deletion of the element takes place at one end only
# the end at which the insertion and deletion takes place is called top of the stack
# the order in which the element is inserted into the stack is called LIFO (last in first out) or FILO (first in last out)


# stack can be implemented using array and linked list
# stack implemented using array is called static stack
# stack implemented using linked list is called dynamic stack



def push(data):
  global top, stack, stackMax
  if top == stackMax - 1:
    print("Stack Full")
  else:
    top += 1
    stack[top] = data

def pop():
  global top, stack
  if top == -1:
    print("Stack Empty")
  else:
    top -= 1

def display():
  global top, stack
  if top == -1:
    print("-1")
  else:
    for i in range(top, -1, -1):
      print(stack[i], end = " ")
    print()














# Implement stack using Linked List

  class MyStack:
    class StackNode:
      # Constructor to initialize a node
      def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
      self.head = None

    def push(self, x):
      new_node = self.StackNode(x)
      new_node.next = self.head
      self.head = new_node         # head is now the new node

    def pop(self):
      if self.head is None:
        return -1
      pop = self.head.data
      self.head = self.head.next  # head next is now the new head
      return popped_value


# stack Applications

# 1. Reversing a word
# 2. Balancing of symbols
# 3. Infix to Postfix / Prefix conversion
# 4. Redo-Undo features at many places like editors, photoshop.
# 5. Forward and backward feature in web browsers
# 6. Used in many algorithms like Tower of Hanoi, tree traversals, stock span problem, histogram problem.
# 7. Other applications can be Backtracking, Knight tour problem, rat in a maze, N queen problem and sudoku solver






# Infix to Postfix

def precedence(i):                # we are giving operator value according to their precedence so that we can compare them later
  if i == "+" or i == "-":
    return 1
  if i == "*" or i == "/":
    return 2
  if i == "^":
    return 3
  else:
    return 0

def InfixtoPostfix(exp):
  stack = []
  result = ""
  for i in exp:
    if i.isalpha() or i.isdigit():
      result += i
    elif i == "(":
      stack.append(i)
    elif i == ")":
      while stack is not None and stack[-1] != "(":
        result += stack.pop()
      stack.pop()
    else:
      if precedence(i) > precedence(stack[-1]):
        stack.append(i)
      else:
        while stack is not None and precedence(i) <= precedence(stack[-1]):    # the scanned operator has less precedence than the operator in the stack then pop the stack and add it to the result
          result += stack.pop()                                                # until the scanned operator has higher precedence
        stack.append(i)
    while stack is not None:
      result += stack.pop()
    return result








