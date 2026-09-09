class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their starting point
        intervals.sort(key=lambda x: x[0])

        # Store the result for each query
        results = {}
        min_heap = []
        i = 0
        n = len(intervals)

        # Sort queries, but remember their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        for idx, query in sorted_queries:
            # Add all intervals starting before or at the query point
            while i < n and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1

            # Remove intervals from the heap that end before the query point
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # The smallest valid interval is at the top of the heap
            if min_heap:
                results[idx] = min_heap[0][0]
            else:
                results[idx] = -1

        # Map results back to the original order of queries
        return [results[i] for i in range(len(queries))]        