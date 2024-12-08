# Minimize the Heights II
# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

# Examples :

# Input: k = 2, arr[] = {1, 5, 8, 10}
# Output: 5
# Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
# Input: k = 3, arr[] = {3, 9, 12, 16, 20}
# Output: 11
# Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11. 
# Expected Time Complexity: O(n*logn)
# Expected Auxiliary Space: O(n)

# Constraints
# 1 ≤ k ≤ 107
# 1 ≤ n ≤ 105
# 1 ≤ arr[i] ≤ 107

SOLUTION:-

class Solution:
    def getMinDiff(self, arr,k):
        n = len(arr)
        arr.sort()
        res = arr[n - 1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - k < 0:
                continue

        # Minimum height after modification
            minH = min(arr[0] + k, arr[i] - k)

        # Maximum height after modification
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Store the minimum difference as result
            res = min(res, maxH - minH)
        return res
       
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
