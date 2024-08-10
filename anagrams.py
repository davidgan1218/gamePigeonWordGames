from dict.trie import Trie, TrieNode

import copy

trie = Trie()
file_path = 'dict/CollinsDict.txt'

with open(file_path, 'r') as file:
    for line in file:
        word = line.strip()
        trie.insert(word)


letters = set()
not_seen = set()
for i in range(6):
    letter = input()
    letters.add(letter)
    not_seen.add(letter)


def dfs(cur_letter, cur_word, words, seen, not_seen):
    if len(not_seen) == 0:
        return
    if cur_letter in seen:
        return
    cur_word += cur_letter
    seen.add(cur_letter)
    not_seen.remove(cur_letter)
    if trie.search(cur_word):
        words.append(cur_word)
    for letter in list(not_seen):
        dfs(letter, cur_word, words, seen, not_seen)
    seen.remove(cur_letter)
    not_seen.add(cur_letter)
    

words = []
for letter in letters:
    seen = set()
    dfs(letter, "", words, seen, not_seen)

sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)
