class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False


class Trie:
    def __init__(self):
        self.__root = TrieNode()

    def char_to_int(self, char):
        return ord(char)-ord('a')

    def delete(self, word):
        node = self.__root
        l = len(word)
        for i in range(l):
            j = self.char_to_int(word[i])
            if node.children[j] is not None:
                node = node.children[j]
            else:
                raise ValueError("Keyword doesn't exist in trie")
        if node.is_end is not True:
            raise ValueError("Keyword doesn't exist in trie")
        node.is_end = False
        return

    def add(self, word):
        node = self.__root
        l = len(word)
        for i in range(l):
            j = self.char_to_int(word[i])
            if node.children[j] is not None:
                node = node.children[j]
            else:
                node.children[j] = TrieNode()
                node = node.children[j]
        node.is_end = True

    def search(self, word):
        node = self.__root
        l = len(word)
        for i in range(l):
            j = self.char_to_int(word[i])
            if node.children[j] is not None:
                node = node.children[j]
            else:
                return False
        if node.is_end is not True:
            return False
        return True

    def __getwords(self, node, pref, pref_list):
        if node is None:
            pref_list.append(pref)
            return
        if node.is_end == True:
            pref_list.append(pref)
        for i in range(26):
            if node.children[i] is not None:
                self.__getwords(node.children[i],
                                pref+chr(ord('a')+i), pref_list)

    def autocomplete(self, pref):
        node = self.__root
        pref_list = []
        l = len(pref)
        for i in range(l):
            j = self.char_to_int(pref[i])
            if node.children[j] is not None:
                node = node.children[j]
            else:
                return None
        self.__getwords(node, pref, pref_list)
        return pref_list

    def display(self):
        node = self.__root
        pref_list = []
        self.__getwords(node, "", pref_list)
        return pref_list
