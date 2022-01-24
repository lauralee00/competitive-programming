# Time Complexity:
# insert -> O(N)
# search -> O(N)
# startsWith -> O(N)

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.end = False


class Trie:

    def __init__(self, char=""):
        self.root = TrieNode()
        # this is the head, no char stored, only children that serve as the first letters of all the words

    def insert(self, word: str) -> None:
        node = self.root  # create a reference
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
