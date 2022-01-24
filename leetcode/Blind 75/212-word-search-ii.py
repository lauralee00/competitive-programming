from typing import List

# Time Complexity: O (rows * cols * 3 ^ k + N * k)
# Trie -> O (N * k) -- k = length of words[i], N = number of words
# DFS  -> O (rows * cols * 3 ^ k)

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.end = False

    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        maxLen = max(len(word) for word in words)
        # break early if word is longer than max possible length of word

        # search board
        rows, cols = len(board), len(board[0])
        res = list()

        def dfs(r, c, curNode, word):
            if not (0 <= r < rows) or not (0 <= c < cols) or \
                    not board[r][c] or board[r][c] not in curNode.children:
                return

            ch = board[r][c]
            board[r][c] = None
            node = curNode.children[ch]
            word.append(ch)

            if len(word) > maxLen:
                return

            if node.end:
                res.append("".join(word))
                node.end = False

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # backtracking after end of each search
            word.pop()
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                if len(res) == len(words): break
                dfs(r, c, root, [])

        return res
