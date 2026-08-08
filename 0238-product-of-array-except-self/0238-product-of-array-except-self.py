class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer= [1]*len(nums)
        product=1
        for i in range(len(nums)):
            answer[i]=product
           
            product=product *nums[i]
        product=1
        for i in range (len(nums)-1,-1,-1):
            answer[i]=answer[i]*product
            product=product* nums[i]
        return answer