class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        res = 1
        q = deque([beginWord])
        visited = set([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0





# The problem at hand is to find the shortest transformation sequence from `beginWord` to `endWord` using a given word list, where each transformation can change only one letter at a time, and each intermediate word must be in the word list.

# To solve this problem, we can use Breadth-First Search (BFS). The idea is to explore all possible transformations level by level starting from `beginWord`. We use a queue to facilitate the BFS and a set to keep track of visited words to prevent cycles.

# Here is the implementation of the solution using BFS:

# ### Detailed Steps:

# 1. **Create a Pattern Dictionary**:
#    - For each word in the word list, create patterns by replacing each letter with `*`. For example, for the word "hot", the patterns are `*ot`, `h*t`, `ho*`.
#    - Store these patterns in a dictionary where the key is the pattern and the value is a list of words matching that pattern. This allows us to quickly find potential next words in the transformation sequence.

# 2. **Initialize BFS**:
#    - Use a queue to keep track of the current word and the number of transformations taken to reach it.
#    - Use a set to keep track of visited words to avoid processing the same word multiple times.

# 3. **BFS Execution**:
#    - For each word, generate its possible patterns.
#    - For each pattern, get the list of words from the dictionary and process each word that hasn't been visited yet.
#    - If we find the `endWord`, return the current transformation count.
#    - Otherwise, add the word to the queue and mark it as visited.

# 4. **Termination**:
#    - If the queue is exhausted and we haven't found the `endWord`, return 0 indicating that no transformation sequence exists.

# Here is the complete implementation:

# ```python
# from collections import defaultdict, deque
# from typing import List

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
        
#         # Create a dictionary of all combo patterns
#         nei = defaultdict(list)
#         wordList.append(beginWord)
#         for word in wordList:
#             for j in range(len(word)):
#                 pattern = word[:j] + "*" + word[j + 1:]
#                 nei[pattern].append(word)
        
#         # BFS initialization
#         res = 1
#         q = deque([beginWord])
#         visited = set([beginWord])

#         # BFS loop
#         while q:
#             for i in range(len(q)):
#                 word = q.popleft()
#                 if word == endWord:
#                     return res
#                 for j in range(len(word)):
#                     pattern = word[:j] + "*" + word[j + 1:]
#                     for neiWord in nei[pattern]:
#                         if neiWord not in visited:
#                             visited.add(neiWord)
#                             q.append(neiWord)
#             res += 1
#         return 0
# ```

# ### Explanation:

# 1. **Pattern Creation**: For each word in `wordList`, patterns are created by replacing each character with `*`. These patterns are stored in a dictionary for quick lookup.

# 2. **BFS Initialization**: The BFS starts with `beginWord` in the queue and a set `visited` containing `beginWord`.

# 3. **BFS Execution**: 
#    - For each word, patterns are generated.
#    - For each pattern, all corresponding words are checked.
#    - If a word is the `endWord`, the transformation count `res` is returned.
#    - If a word hasn't been visited, it's added to the queue and marked as visited.

# 4. **Return Result**: If the BFS completes without finding `endWord`, return 0.

# This approach ensures that we explore all possible transformations efficiently using BFS and avoid cycles using the visited set.
                