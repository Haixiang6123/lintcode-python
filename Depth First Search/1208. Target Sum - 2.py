class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """

    def findTargetSumWays(self, nums, s):
        return self.dfs(0, 0, nums, s, {})

    def dfs(self, index, curt, nums, target, memo):
        if (index, curt) in memo:
            return memo[(index, curt)]

        if index == len(nums):
            if curt == target:
                return 1
            return 0

        result = 0
        result += self.dfs(index + 1, curt + nums[index], nums, target, memo)
        result += self.dfs(index + 1, curt - nums[index], nums, target, memo)

        memo[(index, curt)] = result

        return result
