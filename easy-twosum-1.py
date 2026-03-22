class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        tempDict = defaultdict(int)

        for index, value in enumerate(nums):

            if (target - value) in tempDict:
                return [index,tempDict[target-value]]

            tempDict[value] = index
     #Time complexity is O(n) since we traverse the array once, and space complexity is O(n) due to the hash map storing up to n elements.”



























        
        # dict = {}

        # if len(nums) == 2:
        #     return [0,1]
        
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in dict:
        #         return [i, dict[diff]]

        #     dict[nums[i]] = i




        # if len(nums) == 2:
        #     return [0,1]

        # dict = {}

        # for i in range(len(nums)):
            
        #     diff = target - nums[i]
        #     if diff in dict:
        #         return [i,dict[diff] ]
        #     dict[nums[i]] = i

        # for i in reversed(range(len(nums))):
        #     hold = target - nums[i]
        #     if hold in nums and nums.index(hold)!=i:
        #         return [i,nums.index(hold)]            
        
