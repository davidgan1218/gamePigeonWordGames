from trie import Trie, TrieNode

import copy

trie = Trie()
file_path = 'CollinsDict.txt'

with open(file_path, 'r') as file:
    for line in file:
        word = line.strip()
        trie.insert(word)

board = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def dfs(i, j, seen, cur_word, path, words):
    if len(cur_word) > 10:
        return
    if (i, j) in seen:
        return
    if i < 0 or i > 3 or j < 0 or j > 3:
        return
    cur_word += board[i][j]
    path.append((i, j))

    #if cur_word in trie, then add cur_word to words
    if trie.search(cur_word):
        copied_path = copy.deepcopy(path)
        words.append([cur_word, copied_path])
    seen.add((i, j))
    for dir in dirs:
        dfs(i + dir[0], j + dir[1], seen, cur_word, path, words)
    
    seen.remove((i, j))
    path.pop()


def get_unique_words(unique_words, sorted_words, seen_words):
    for sublist in sorted_words:
        if sublist[0] not in seen_words:
            unique_words.append(sublist)
            seen_words.add(sublist[0])

def print_word_on_board(sublist):
    print(sublist[0])
    pos_dict = dict()
    count = 1
    for pos in sublist[1]:
        pos_dict[pos] = count
        count += 1

    for i in range(4):
        for j in range(4):
            print('| ', end="")
            if (i, j) in sublist[1]:
                print(pos_dict[(i, j)], end="")
            else:
                print('*', end="")
        print('|', end="")
        print()

for i in range(4):
    for j in range(4):
        board[i][j] = input()


words = []
for i in range(len(board)):
    for j in range(len(board[0])):
        seen = set()
        path = []
        dfs(i, j, seen, "", path, words)


sorted_words = sorted(words, key=lambda x : len(x[0]), reverse=True)
unique_words = []
seen_words = set()
get_unique_words(unique_words, sorted_words, seen_words)
print()

for i in range(15):
    print_word_on_board(unique_words[15-i])
