class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}                      # value -> index, of numbers already visited
        for i, n in enumerate(nums):
            diff = target - n          # number needed to complete the pair
            if diff in seen:
                return [seen[diff], i] # seen[diff] was stored first, so it's the smaller index
            seen[n] = i                # store for later lookups

        # O(n^2) using nested loops
#        for i in range(len(nums)):           # first number
#            for j in range(i + 1, len(nums)):  # second number, always after i
#                if nums[i] + nums[j] == target:
#                    return [i, j]