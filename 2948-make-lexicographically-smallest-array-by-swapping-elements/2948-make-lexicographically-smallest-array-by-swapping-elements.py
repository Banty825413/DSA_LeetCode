class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = [0] * n
        i = 0

        while i < n:
            j = i + 1

            
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            
            indices = sorted(index for _, index in arr[i:j])

            
            for index, (value, _) in zip(indices, arr[i:j]):
                ans[index] = value

            i = j

        return ans