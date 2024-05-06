class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # optimal: O(m + n)
        nums1Idx = {n : i for i,n in enumerate(nums1)}  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
        res = [-1] * len(nums1)
        stack  = [] 
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if nums2[i] in nums1Idx:
                    stack.append(cur)
        return res                         


# Intuition and Approach:

# - We're given two lists of integers `nums1` and `nums2`.
# - For each element in `nums1`, we want to find the next greater element in `nums2` (to its right).
# - We can achieve this efficiently by using a stack and a hashmap.
# - We create a hashmap `nums1Idx` to store the indices of elements in `nums1`.
# - We initialize a result list `res` with -1, indicating that there's no greater element found yet.
# - We iterate through `nums2`.
#   - For each element `cur` in `nums2`, we compare it with the elements at the top of the stack.
#   - If `cur` is greater than the top element of the stack, it's the next greater element for the elements on the stack.
#     - We pop elements from the stack and update the corresponding indices in `res` with `cur`.
#   - If `cur` is in `nums1`, we add it to the stack.
# - Finally, we return `res`.

# Time Complexity: O(m + n), where m is the length of `nums1` and n is the length of `nums2`. We iterate through `nums2` once, and each element is pushed and popped from the stack at most once.

# Space Complexity: O(m), where m is the length of `nums1`. The space used by the hashmap and the result list `res` is proportional to the size of `nums1`.

        

        # Brute_force: O(m * n)
        nums1Idx = {n : i for i,n in enumerate(nums1)} 
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res                        




# Intuition and Approach:

# - We're given two lists of integers `nums1` and `nums2`.
# - For each element in `nums1`, we want to find the next greater element in `nums2` (to its right).
# - We can achieve this by iterating through `nums2` and searching for the next greater element for each element in `nums1`.
# - We initialize a hashmap `nums1Idx` to store the indices of elements in `nums1`.
# - We initialize a result list `res` with -1, indicating that there's no greater element found yet.
# - We iterate through `nums2`.
#   - For each element `nums2[i]`, if it's not present in `nums1`, we continue to the next element.
#   - If `nums2[i]` is in `nums1`, we search for the next greater element for it.
#     - We iterate through the elements to the right of `nums2[i]` in `nums2`.
#     - If we find an element greater than `nums2[i]`, we update the corresponding index in `res` with the greater element and break out of the loop.
# - Finally, we return `res`.

# Time Complexity: O(m * n), where m is the length of `nums1` and n is the length of `nums2`. For each element in `nums1`, we potentially iterate through the entire `nums2`.

# Space Complexity: O(m), where m is the length of `nums1`. The space used by the hashmap and the result list `res` is proportional to the size of `nums1`.
