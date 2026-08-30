class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        if len(nums) == 1 :
            return 1
        if min_num == max_num :
            return 0
        min_idx = nums.index(min_num)
        max_idx = nums.index(max_num)
        
        left = min(min_idx,max_idx)
        right = max(min_idx, max_idx)
        n = len(nums)
        #from left removal
        opt_1 = right +1 
        #from right end
        opt_2 = n - left
        #from both side
        opt_3 = left +1 + n - right 
        return min(opt_1, opt_2,opt_3)                
        