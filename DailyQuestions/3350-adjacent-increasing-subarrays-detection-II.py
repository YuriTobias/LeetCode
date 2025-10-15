# Adjacent Increasing Subarrays Detection II
from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        second_sequence_size, first_sequence_size, final_size = 1, 0, 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                second_sequence_size += 1
            else:
                first_sequence_size, second_sequence_size = second_sequence_size, 1
            final_size = max(final_size, min(first_sequence_size, second_sequence_size))
            final_size = max(final_size, second_sequence_size // 2)
            
        return final_size

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))
    print(solution.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))
    print(solution.maxIncreasingSubarrays([1,1]))