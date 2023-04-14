import itertools
from typing import List

class Solution:
    # def check_beauty(self, tupe, diff):
    #     for f_i in range(len(tupe) - 1):
    #         for c_i in range(f_i + 1, len(tupe)):
    #             if abs(tupe[f_i] - tupe[c_i]) == diff:
    #                 return False
    #     return True

    # def beautifulSubsets(self, nums: List[int], k: int) -> int:
    #     count = 0
    #     for iterator in range(1, len(nums) + 1):
    #         pwr_set = list(itertools.combinations(nums, iterator))
    #         for subset in pwr_set:
    #             if self.check_beauty(subset, k):
    #                 count += 1
    #     return count
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        res = 0

        for i in range(n):
            for j in range(i):
                if abs(nums[i] - nums[j]) < k:
                    dp[i] = max(dp[i], dp[j] + 1)
            res += dp[i]

        total_subsets = 2 ** n - 1
        non_beautiful_subsets = total_subsets - res
        return non_beautiful_subsets
