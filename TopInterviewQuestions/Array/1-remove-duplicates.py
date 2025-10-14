# Remove Duplicates from Sorted Array
from typing import List

class Solution:    
    def removeDuplicates(self, nums: List[int]) -> int:
        base_index = 0
        comparison_index = 1
        
        while comparison_index < len(nums):
            if nums[base_index] != nums[comparison_index]:
                base_index += 1
                nums[base_index] = nums[comparison_index]
            
            comparison_index += 1

        print(nums)
        return base_index + 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))