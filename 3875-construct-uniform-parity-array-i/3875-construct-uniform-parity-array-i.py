class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        def check(parity):
            for x in nums1:
                if x % 2 == parity:
                    continue
                found = False
                for y in nums1:
                    if y != x and (x - y) % 2 == parity:
                        found = True
                        break
                if not found:
                    return False
            return True
        return check(0) or check(1)