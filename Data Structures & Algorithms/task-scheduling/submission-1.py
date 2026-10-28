class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq_map = {}
        for char in tasks:
            task_freq_map[char] = task_freq_map.get(char, 0) + 1
        
        task_freq = list(task_freq_map.values())
        heapq.heapify_max(task_freq)

        q = deque([])
        time = 0
        while task_freq or q:
            time += 1

            if task_freq:
                freq = heapq.heappop_max(task_freq)
                if freq > 1:
                    q.append([freq-1, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(task_freq, q.popleft()[0])

        
        return time

        
        
        