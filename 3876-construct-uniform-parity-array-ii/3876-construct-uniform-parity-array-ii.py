class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = min(nums1)
        if min_num %2 ==1 :
            return True
        return all(i % 2 == 0 for i in nums1)
        