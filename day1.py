# Q1 Second Largest
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.
# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

OUTPUT:-

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # Check if the array length is valid
        if len(arr) < 2:
            return -1  # Not enough elements to find the second largest
        
        largest = second = -1  # Initialize largest and second largest

        for number in arr:
            if number > largest:
                second = largest  # Update second largest
                largest = number   # Update largest
            elif number > second and number != largest:
                second = number    # Update second largest if it's less than largest but greater than second

        return second if second != -1 else -1  # Return second largest or -1 if it doesn't exist


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
