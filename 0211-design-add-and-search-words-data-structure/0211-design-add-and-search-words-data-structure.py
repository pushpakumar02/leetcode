class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root 
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word 
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

### Intuition
# A WordDictionary is an extension of a Trie that supports adding words and searching words with wildcards ('.'). The wildcard '.' can represent any letter, making the search operation more complex and requiring depth-first search (DFS) to handle all possible character matches at each wildcard position.

# ### Approach
# 1. **AddWord**: Similar to a standard Trie, traverse through each character of the word. If a character doesn't exist in the current node's children, create a new TrieNode. Mark the end of the word with a special flag (`word`).
# 2. **Search**: Use DFS to handle the wildcard characters. For each character in the word:
#    - If it's a regular character, follow the Trie path.
#    - If it's a '.', recursively search all possible paths (all children nodes).
#    - Return true if a valid path is found and false otherwise.

# ### Time Complexity
# - **AddWord**: \(O(m)\), where \(m\) is the length of the word.
# - **Search**:
#   - **Best case**: \(O(m)\) for a word without any wildcards.
#   - **Worst case**: \(O(26^m)\) for a word with all wildcards, where \(m\) is the length of the word.

# ### Space Complexity
# - **Space**: \(O(n \cdot m)\), where \(n\) is the number of words and \(m\) is the average length of the words. Each node in the Trie can have up to 26 children (for the 26 letters of the alphabet in English).

# This approach ensures efficient handling of word addition and flexible word searches with wildcards.

