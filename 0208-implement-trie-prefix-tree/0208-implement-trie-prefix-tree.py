class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfNode = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfNode

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



### Intuition
# A Trie (prefix tree) is a specialized tree used to efficiently store and search strings, particularly for applications involving autocomplete, spell-checking, and dictionary implementations. Each node in the Trie represents a character of a word. The root node is empty, and paths down the tree represent words or prefixes. By traversing the tree, you can determine if a word or prefix exists in the Trie.

### Approach
# 1. **Insert**: Traverse through each character of the word. For each character, if it does not exist in the current node's children, create a new node. Mark the end of the word with a special flag (`endOfNode`).
# 2. **Search**: Traverse through each character of the word. If a character is not found in the current node's children, the word does not exist. If the traversal completes, check the `endOfNode` flag to confirm it's a complete word.
# 3. **StartsWith**: Similar to search, but only checks if the prefix exists without needing to reach the end of the word.

# ### Time Complexity
# - **Insert**: \(O(m)\) per word, where \(m\) is the length of the word.
# - **Search**: \(O(m)\) per word, where \(m\) is the length of the word.
# - **StartsWith**: \(O(m)\) per prefix, where \(m\) is the length of the prefix.

# ### Space Complexity
# - **Space**: \(O(n \cdot m)\), where \(n\) is the number of words and \(m\) is the average length of the words. Each node in the Trie can have up to 26 children (for the 26 letters of the alphabet in English).