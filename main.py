"""
Given an array arr[] of N integers and an integer S. The task is to find an element K in the array such that if all the elements from the array > K are made equal to K then the sum of all the elements of the resultant array becomes equal to S. If it is not possible to find such an element then print -1 .

Examples: 

Input: M = 15, arr[] = {12, 3, 6, 7, 8} 
Output: 3 
Resultant array = {3, 3, 3, 3, 3} 
Sum of the array elements = 15 = S

Input: M = 5, arr[] = {1, 3, 2, 5, 8} 
Output: 1 


"""

def getElement(a, n, s):
  a.sort()
  sum = 0 
  for i in range(s):
    if (sum + a[i] * (n-1) == s):
      
      return a[i]

    sum += a[i]

    
  return -1

a = [ 1, 3, 2, 5, 8 ]
n = len(a)
s = 5

print(getElement(a, n, s ))