class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = dict()
            node = node[c]

        node[None] = dict()

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            else:
                node = node[c]

        return True if None in node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            else:
                node = node[c]

        return True

# Your trie object will be instantiated and called as such:
# obj = trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)