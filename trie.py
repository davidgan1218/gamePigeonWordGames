class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.is_end_of_word = True
    
    def search(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_end_of_word


# trie = Trie()
# file_path = '/usr/share/dict/words'


# with open(file_path, 'r') as file:
#     for line in file:
#         word = line.strip()
#         trie.insert(word)



# test_words = ["apple", "banana", "orange", "khdakhkadjs", "a", "b"]

# for word in test_words:
#     if trie.search(word):
#         print(f"Found '{word}' in Dictionary.")
#     else:
#         print(f"'{word}' is not an English word.")


