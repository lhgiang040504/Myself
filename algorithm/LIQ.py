'''n = int(input())
nums = list(map(int, input().split()))'''

n = 6
nums = [1, 2, 5, 4, 6, 2]

from collections import defaultdict 


def solve(nums, n):
    
    liq = defaultdict(int)
    
    def LIQ(idx):
        if idx < 0:
            return
        if idx == n - 1:
            liq[idx] = 1
        else:
            for i in range(n - 1, idx, -1):
                if nums[i] > nums[idx]:
                    liq[idx] = max(liq[idx], 1 + liq[i])        
        LIQ(idx - 1)

    LIQ(n-1)
    return max(liq.values())

print(solve(nums, n))


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        track = [nums[0]]
        for i in range(1, n):
            if nums[i] > track[-1]:
                track.append(nums[i])
            else:
                for j in range(len(track)):
                    if nums[i] <= track[j]:
                        track[j] = nums[i]
                        break
        
        return len(track)