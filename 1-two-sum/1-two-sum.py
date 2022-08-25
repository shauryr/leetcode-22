class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_diff = {}
        for i, item in enumerate(nums):
            if item in dict_diff:
                return [dict_diff[item], i]
            else:
                dict_diff[target-item] = i