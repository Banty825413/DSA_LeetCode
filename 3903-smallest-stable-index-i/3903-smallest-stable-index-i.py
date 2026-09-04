class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n ==0:
            return -1
        max_left = [0]*n
        cur = float('-inf')
        for i in range(n):
            cur = max(cur,nums[i])
            max_left[i] = cur
        
        # calculating the minimum from left  
        min_right = [0]*n

        cur_min = float('inf')
        for i in range (n-1,-1,-1):
            cur_min = min(cur_min,nums[i])
            min_right[i] = cur_min

        stable = k
        idx = -1
        # Last to loop to check stablizer
        for i in range (n):
            temp = max_left[i] - min_right[i]
            if temp <= k:
                return i
                
                
        return -1

