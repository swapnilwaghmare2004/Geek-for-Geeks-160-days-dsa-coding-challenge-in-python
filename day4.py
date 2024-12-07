# Rotate Array
# Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
# Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
# Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
# Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
# Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
# Input: arr[] = [7, 3, 9, 1], d = 9
# Output: [3, 9, 1, 7]
# Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
# Constraints:
# 1 <= arr.size(), d <= 105
# 0 <= arr[i] <= 105

SOLUTION:-

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                 # Step 1: Reverse the first d elements
        reverse(0, d - 1)
        
        # Step 2: Reverse the remaining n - d elements
        reverse(d, n - 1)
        
        # Step 3: Reverse the entire array
        reverse(0, n - 1)

# Example usage
sol = Solution()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
