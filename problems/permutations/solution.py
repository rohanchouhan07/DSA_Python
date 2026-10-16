class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path: List[int]) -> None:
            # if path has all numbers, it's a complete permutation
            if len(path) == len(nums):
                res.append(path[:])   # make a copy
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])

                backtrack(path)

                # undo (backtrack)
                path.pop()
                used[i] = False

        backtrack([])
        return res