class TrieNode:

    def __init__(self, p=None):
        self.children = [None for _ in range(256)]
        self.parent, self.cno = p, 0

    def transition(self, c):
        return self.children[ord(c)]

    def insert(self, c):
        cn = self.transition(c)
        if cn is None:
            ncn = TrieNode(self)
            self.children[ord(c)] = ncn
            self.cno += 1
            return ncn
        else:
            return cn

    def remove(self, c):
        cn = self.transition(c)
        if cn is not None:
            self.children[ord(c)] = None
            self.cno -= 1
            return True
        return False

    def __str__(self):
        s = 'Children(' + str(self.cno) + '):'
        for i in range(256):
            if self.children[i] is not None:
                s += ' ' + chr(i)
        return s


class Trie:

    def __init__(self, terminal='$'):
        self.root = TrieNode()
        self.terminal = terminal
        
    def search(self, q):
        currTN = self.root
        for c in q + "$":
            currNTN = currTN.transition(c)
            if currNTN is None:
                return False, currTN
            currTN = currNTN
        return currTN.isLeaf(), currTN

    def insert(self, word):
        """Inserts a word into the trie.

        Args:
            word (str): word to insert
        """
        if self.terminal in word:
            raise Exception(f'Explicit terminal ({self.terminal}) use is not allowed within words!')

        node = self.root
        for char in word:
            node = node.insert(char)
        node.insert("$")

        pointer_dict = {

        }  # TODO: fill in with the right object

        # proper terminating the word
        if self.terminal not in pointer_dict:
            pointer_dict[self.terminal] = None

    def search_prefix(self, prefix: str):
        if self.terminal in prefix:
            raise Exception(
                f'Explicit terminal ({self.terminal}) use is not allowed within words!')
        node = self.root
        for char in prefix:
            pass
            # TODO: fill in the missing code

        return True, node

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie.

        Args:
            word (str): searching term

        Returns:
            bool: True, if the word is in trie
                  False, otherwise
        """
        # TODO: implement the function