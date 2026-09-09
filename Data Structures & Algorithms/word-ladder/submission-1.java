class Solution {

    // ladderLength: the main function that finds the minimum transformation sequence length
    // Parameters:
    //   - beginWord: the starting word of our transformation (String)
    //   - endWord: the target word we want to reach (String)
    //   - wordList: the list of valid intermediate/target words (List<String>)
    // Returns: int - the minimum number of words in the sequence, or 0 if impossible
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        // Convert wordList to a HashSet for O(1) average lookup time
        // Why HashSet? List.contains() is O(n) per call; HashSet.contains() is O(1)
        // This is critical because we'll check membership many times
        // Trade-off: uses O(n) extra space where n = wordList.size()
        // We name it 'wordSet' to clearly indicate it's a set representation of wordList
        Set<String> wordSet = new HashSet<>(wordList);

        // Early exit: if endWord is not in wordSet, transformation is impossible
        // This check is O(1) due to HashSet lookup
        // Without this check, BFS would run completely and return 0 anyway,
        // but this short-circuits for efficiency and clarity
        if (!wordSet.contains(endWord)) {
            // Return 0 as per problem specification: no valid sequence exists
            return 0;
        }

        // Create a Queue to support BFS traversal
        // We use LinkedList as it implements Queue interface and provides O(1) add/poll
        // Why Queue? BFS requires FIFO ordering to process nodes level by level
        // This guarantees we find the SHORTEST path first
        // We name it 'queue' to clearly indicate its role in BFS
        Queue<String> queue = new LinkedList<>();

        // Add beginWord to the queue as the starting point of BFS
        // This is level 1 of our BFS (beginWord itself counts as 1 word in the sequence)
        // O(1) operation for LinkedList
        queue.offer(beginWord);

        // Create a HashSet to track visited words
        // Why HashSet? O(1) average insert and lookup
        // We MUST track visited nodes to prevent infinite cycles
        // (e.g., cat -> bat -> cat -> bat... infinitely)
        // We name it 'visited' to clearly indicate its purpose
        Set<String> visited = new HashSet<>();

        // Mark beginWord as visited immediately to prevent it from being
        // re-added to the queue if some wordList word can transform to it
        // O(1) operation for HashSet
        visited.add(beginWord);

        // 'sequenceLength' tracks the current BFS level (= number of words in sequence so far)
        // We initialize to 1 because beginWord is the first word in any sequence
        // We use int because word sequence length fits well within int range
        // Named 'sequenceLength' to clearly represent what it counts
        int sequenceLength = 1;

        // BFS main loop: continue as long as there are words to explore
        // Each iteration of the outer while loop represents processing one BFS level
        // Time Complexity Note: In the worst case, we process all words = O(n) levels
        while (!queue.isEmpty()) {

            // 'levelSize' captures how many words are at the CURRENT BFS level
            // This is critical for level-by-level BFS processing
            // We need this snapshot because queue.size() changes as we add new words
            // O(1) operation for LinkedList
            int levelSize = queue.size();

            // Process all words at the current BFS level
            // This inner loop ensures we complete one full "level" before incrementing sequenceLength
            // This is key to BFS correctness: all words at distance k are processed before distance k+1
            for (int i = 0; i < levelSize; i++) {

                // Dequeue the next word to process (FIFO ordering)
                // poll() returns null if empty, but we know it's non-empty from outer while condition
                // O(1) for LinkedList
                String currentWord = queue.poll();

                // BRUTE FORCE: Iterate over EVERY word in the original wordList
                // to find neighbors (words differing by exactly 1 character)
                // This is O(n * L) per word where n = wordList.size(), L = word length
                // This is the INEFFICIENCY we'll optimize later
                for (String candidate : wordList) {

                    // Skip already-visited words to prevent cycles
                    // O(1) HashSet lookup
                    if (visited.contains(candidate)) {
                        continue; // Skip this candidate, already explored
                    }

                    // Check if 'candidate' differs from 'currentWord' by exactly 1 character
                    // We call our helper method 'isOneLetterDiff'
                    // This is O(L) where L = word length
                    if (isOneLetterDiff(currentWord, candidate)) {

                        // Found a valid transformation: currentWord -> candidate
                        // Check if 'candidate' is our target endWord
                        // String.equals() is O(L) in worst case
                        if (candidate.equals(endWord)) {
                            // We found endWord! Return sequenceLength + 1
                            // +1 because we add 'candidate' (which IS endWord) to the sequence
                            // sequenceLength represents words processed so far, candidate is the next
                            return sequenceLength + 1;
                        }

                        // Not yet endWord, but a valid step: add to queue for further exploration
                        // O(1) for LinkedList offer
                        queue.offer(candidate);

                        // Mark candidate as visited to prevent re-processing
                        // O(1) for HashSet add
                        visited.add(candidate);
                    }
                    // If not a one-letter diff, simply move to the next candidate
                    // No action needed
                }
                // End of inner for-loop: processed all candidates for currentWord
            }
            // End of level-processing for-loop

            // Increment sequenceLength after processing an entire BFS level
            // This moves us one step deeper in the transformation chain
            sequenceLength++;
        }
        // End of BFS while-loop: queue is empty and endWord was not reached

        // No transformation sequence found: return 0 as per problem specification
        return 0;
    }

    // Helper method: isOneLetterDiff
    // Determines if two words differ by EXACTLY one character
    // Parameters:
    //   - word1: first word to compare (String)
    //   - word2: second word to compare (String)
    // Returns: boolean - true if exactly 1 position differs, false otherwise
    // Time Complexity: O(L) where L = length of the words
    // We assume word1.length() == word2.length() (guaranteed by problem constraints)
    private boolean isOneLetterDiff(String word1, String word2) {

        // 'diffCount' tracks the number of positions where word1 and word2 differ
        // Initialized to 0: assume no differences until we find them
        // We use int because the count is at most L (word length, max 10 per constraints)
        int diffCount = 0;

        // Iterate over each character position from 0 to word length - 1
        // We use word1.length() since both words have equal length (problem guarantee)
        // charAt(i) is O(1) for Java strings
        for (int i = 0; i < word1.length(); i++) {

            // Compare characters at position i in both words
            // If they differ, increment diffCount
            if (word1.charAt(i) != word2.charAt(i)) {
                // Characters at position i are different
                diffCount++;

                // Early exit optimization: if diffCount exceeds 1, we can immediately
                // return false - we only want EXACTLY 1 difference
                // This avoids unnecessary character comparisons
                if (diffCount > 1) {
                    // More than 1 difference found, not a valid one-letter transformation
                    return false;
                }
            }
        }
        // After checking all positions, return true only if EXACTLY 1 difference was found
        // diffCount == 1 means exactly one position differed
        // diffCount == 0 would mean identical words (shouldn't happen per "all distinct" constraint)
        return diffCount == 1;
    }
}