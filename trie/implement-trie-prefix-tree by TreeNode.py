from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root
        for c in word:
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:

        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.word

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True

# Your trie object will be instantiated and called as such:
# obj = trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)