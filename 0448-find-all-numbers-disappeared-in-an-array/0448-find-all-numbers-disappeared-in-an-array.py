class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set(nums)
        for i in range(len(nums)):

            if i+1 not in s:
                ans.append(i+1)
        return ans


