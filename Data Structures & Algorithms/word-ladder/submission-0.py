class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])  # (current word, current transformation count)
        visited = set([beginWord])

        while queue:
            currentWord, steps = queue.popleft()

            if currentWord == endWord:
                return steps

            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = currentWord[:i] + c + currentWord[i+1:]
                    if nextWord in wordSet and nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, steps + 1))

        return 0        