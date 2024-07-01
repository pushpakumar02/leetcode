class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if  w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)
        
        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)





'''
### Intuition and Approach

The problem of determining the order of letters in a foreign language dictionary can be visualized as finding a topological sort of characters based on the given words. Here's the step-by-step approach to solve this problem:

1. **Create Adjacency List**:
   - Initialize an adjacency list to represent the graph where each node is a character, and directed edges show the order between characters.

2. **Build the Graph**:
   - Compare adjacent words to infer the order of characters. For the first differing character between two words, create a directed edge from the character in the first word to the character in the second word.

3. **Detect Cycles**:
   - Use Depth-First Search (DFS) to detect cycles in the graph. If a cycle is detected, it implies that the given words cannot form a valid order, and we should return an empty string.

4. **Topological Sorting**:
   - Perform a DFS to compute the topological ordering of the characters. If no cycles are detected, append characters to the result list in reverse postorder.

### Detailed Steps:

1. **Adjacency List Initialization**:
   - Create an adjacency list where each character points to a set of characters that come after it.

2. **Building the Graph**:
   - Iterate through the pairs of adjacent words. For each pair, find the first character that differs and create a directed edge from the first character to the second character in the graph.

3. **Cycle Detection and Topological Sorting**:
   - Use DFS with three states: unvisited, visiting, and visited. During DFS, mark nodes as visiting when they are first visited, and mark them as visited when all their descendants have been fully processed. If a node is encountered again while in the visiting state, a cycle exists.

4. **Return the Result**:
   - If no cycles are detected, reverse the result list to get the correct order of characters.

Here's the complete implementation:

```python
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
```

### Explanation:
- **Initialization**: `adj` is the adjacency list, initialized to an empty set for each unique character in the words.
- **Graph Building**: Compare each pair of adjacent words to determine the order of characters and update the adjacency list.
- **Cycle Detection and Topological Sorting**: Perform DFS with cycle detection. If a cycle is detected, return an empty string. Otherwise, collect characters in a list in reverse postorder.
- **Result**: Reverse the result list and convert it to a string.

This approach ensures that we correctly determine the character order or detect if no valid order exists due to a cycle.
