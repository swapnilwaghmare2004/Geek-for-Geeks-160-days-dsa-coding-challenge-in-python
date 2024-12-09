# Majority Element II
# You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

# Note: The answer should be returned in an increasing format.

# Examples:

# Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# Output: [5, 6]
# Explanation: 5 and 6 occur more n/3 times.
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: []
# Explanation: no candidate occur more than n/3 times.
# Constraint:
# 1 <= arr.size() <= 106
# -109 <= arr[i] <= 109

SOLUTION:-

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        from collections import defaultdict
        
        # Step 1: Count the votes
        vote_count = defaultdict(int)
        for vote in arr:
            vote_count[vote] += 1
        
        # Step 2: Determine the threshold
        n = len(arr)
        threshold = n // 3
        
        # Step 3: Collect valid candidates
        valid_candidates = []
        for candidate, count in vote_count.items():
            if count > threshold:
                valid_candidates.append(candidate)
        
        # Step 4: Sort the result
        valid_candidates.sort()
        
        return valid_candidates


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
