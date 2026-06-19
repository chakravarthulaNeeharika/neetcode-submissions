class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            curr_num=nums[i]
            complement=target-curr_num
            if complement in seen:
                return[seen[complement],i]
            seen[curr_num]=i
        return[]