class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0) 
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):                    
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False 
                    heapq.heappop(minH)
        return True


### Intuition

# The problem requires us to determine if we can rearrange the cards in `hand` into groups of `groupSize` consecutive numbers. This can be approached by using a greedy algorithm combined with a min-heap to always try and form the next smallest possible group.

# ### Approach

# 1. **Initial Check**: If the total number of cards is not divisible by `groupSize`, then it is impossible to rearrange the cards into the required groups, and we should return `False` immediately.

# 2. **Count Frequencies**: Use a dictionary to count the frequency of each card in the hand.

# 3. **Min-Heap**: Convert the keys of the dictionary (the unique card values) into a min-heap. The min-heap helps in always processing the smallest available card first, which is crucial for forming consecutive sequences.

# 4. **Form Groups**:
#    - While the min-heap is not empty, attempt to form a group starting from the smallest card.
#    - For each card in the current sequence, check if it is available in the dictionary with a non-zero count.
#    - Decrement the count of each card in the group.
#    - If any card in the sequence has zero count after decrementing, ensure it is removed from the heap (only if it is the smallest element in the heap to maintain heap properties).

# ### Time and Space Complexities

# - **Time Complexity**: \(O(N \log N)\), where \(N\) is the number of cards. The heap operations dominate, and each insertion and removal operation in a heap is \(O(\log N)\).
# - **Space Complexity**: \(O(N)\), for storing the frequency count and the heap.

# ### Explanation

# - **Initial Check**: Ensures that the total number of cards can potentially be divided into groups of the specified size.
# - **Frequency Count**: Builds a frequency map of all cards.
# - **Min-Heap**: Helps in accessing the smallest card efficiently to attempt forming groups in a sorted manner.
# - **Group Formation**: Iteratively tries to form groups starting from the smallest card and adjusts counts accordingly. If it can't form a valid group at any step, it returns `False`. If all groups are formed successfully, it returns `True`. 

# This solution ensures that we always attempt to form the smallest possible group first, maintaining the required sequence order.