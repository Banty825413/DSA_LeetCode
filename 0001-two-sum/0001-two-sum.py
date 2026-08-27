class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range (len(nums)):
            temp = target - nums[i]
            if temp in map :
                return [map[temp] , i] 
            map[nums[i]] = i