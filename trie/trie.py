class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEndOfWord

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True


trie = Trie()

trie.insert('sajid')
print(trie.search('sajid'))
print(trie.startsWith('saji'))
