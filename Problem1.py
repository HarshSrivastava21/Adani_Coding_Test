"""
Problem: Word Ladder with Minimum Transformation Path

You are given:
	•	A start word beginWord
	•	An end word endWord
	•	A list of valid words wordList

Return the shortest transformation sequence from beginWord to endWord such that:
	1.	Only one letter can be changed at a time.
	2.	Each intermediate word must exist in the given word list.
	3.	If no such sequence exists, return an empty list [].
⸻
Constraints
	•	All words are of the same length.
	•	All words are lowercase English letters.
⸻
Function Signature
def word_ladder(beginWord: str, endWord: str, wordList: list[str]) -> list[str]:
⸻
Example

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
["hit", "hot", "dot", "dog", "cog"]

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]  # Missing "cog"

Output:
[]
⸻
Optional Starter Code for Testing

def test():
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))
"""
from collections import deque


def word_ladder(beginWord: str, endWord: str, wordList: list[str]) -> list[str]:
    word_set = set(wordList)

    if endWord not in word_set:
        return []
    
    q = deque([(beginWord, [beginWord])])

    while q:
        current_word, path = q.popleft()
        
        if current_word == endWord:
            return path
        
        for index in range(len(current_word)):
            for character in "abcdefghijklmnopqrstuvwxyz":
                # Here we are replacing every character from a-z for an index
                next_word = current_word[:index] + character + current_word[index + 1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    q.append((next_word, path + [next_word]))
        
    return []


def test():
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))


if __name__ == "__main__":
    test()
