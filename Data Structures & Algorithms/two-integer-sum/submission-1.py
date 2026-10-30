class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}

        for i,n in enumerate(nums):
            comp = target - n
            if comp in HashMap:
                return [HashMap[comp],i]
            HashMap[n] = i
        