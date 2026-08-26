class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie from the words list
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True # Mark end of a valid word

        rows, cols = len(board), len(board[0])
        res = []

        # 2. Backtracking function (DFS)
        def dfs(r, c, node, word):
            # Check boundaries and visited status
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "#":
                return
            
            char = board[r][c]
            # Prune path if the character doesn't match any valid prefix
            if char not in node.children:
                return

            # Move to the child node and append the character
            node = node.children[char]
            word += char

            # Base Case: Found a complete word!
            if node.is_word:
                res.append(word)
                node.is_word = False # Prevent matching the same word again

            # Mark cell as visited
            board[r][c] = "#"

            # Explore 4 directional paths
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack: Restore the cell
            board[r][c] = char

        # 3. Kick off DFS from every single cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return res
