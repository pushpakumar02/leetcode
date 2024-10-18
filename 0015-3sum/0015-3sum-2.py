class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            
            if nums[i] > 0: break

            elif i > 0 and nums[i - 1] == nums[i]: continue

            l, r = i + 1, n - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1


                elif threeSum < 0 :
                    l += 1
                else:
                    r -= 1
        return res