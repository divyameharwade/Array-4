# Time complexity - O(nlogn)
# space complexity - O(1)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]
        return res
