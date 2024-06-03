class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k > p: return quickSelect(p + 1, r)
            elif k < p: return quickSelect(l, p - 1)
            else : return nums[p]

        return quickSelect(0, len(nums) - 1)

### Intuition and Approach for `findKthLargest`

#### Intuition
# To find the k-th largest element in an array, we can use the Quickselect algorithm, which is a selection algorithm to find the k-th smallest element in an unordered list. By modifying it slightly, we can find the k-th largest element.

#### Approach
# 1. **Adjust k**:
#    - Convert the k-th largest problem to finding the (len(nums) - k)-th smallest element.

# 2. **Quickselect Algorithm**:
#    - **Partitioning**: 
#      - Choose a pivot element and partition the array such that elements less than or equal to the pivot are on the left, and elements greater than the pivot are on the right.
#      - Place the pivot in its correct position.
#    - **Recursion**:
#      - If the pivot position is the target index k, return the pivot value.
#      - If the pivot position is less than k, recursively apply Quickselect on the right part of the array.
#      - If the pivot position is greater than k, recursively apply Quickselect on the left part of the array.

#### Time Complexity
# - **Average Case**: \(O(n)\), where \(n\) is the number of elements. This happens because each partition step reduces the problem size by approximately half.
# - **Worst Case**: \(O(n^2)\), which occurs if the pivot selections are poor (e.g., always picking the smallest or largest element).

#### Space Complexity
# - **Space Complexity**: \(O(1)\), apart from the recursion stack space, as Quickselect is an in-place algorithm. The recursion depth is \(O(\log n)\) on average.