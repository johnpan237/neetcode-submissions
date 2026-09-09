class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Create a Min-Heap (PriorityQueue in Java)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);

        // Process each number in the array
        for (int num : nums) {
            minHeap.offer(num); // Add number to the heap

            if (minHeap.size() > k) {
                minHeap.poll(); // Remove smallest element to maintain heap size of k
            }
        }

        // The root of the heap is now the k-th largest element
        return minHeap.peek();        
    }    
}
