class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=[]
        sec=[]
        third=[]
        nums=list(set(nums))
        # if len(nums)>=3:
        #     return nums[2]
        # else:
        #     return nums[0]
        if nums:
            max_value=max(nums)
            max_index=nums.index(max_value)
            first.append(max_value)
            nums.pop(max_index)
        if nums:
            max_value=max(nums)
            max_index=nums.index(max_value)
            sec.append(max_value)
            nums.pop(max_index)
        if nums:
            max_value=max(nums)
            max_index=nums.index(max_value)
            third.append(max_value)
            nums.pop(max_index)
        if third:
            return third[0]
        else:
            return first[0]
