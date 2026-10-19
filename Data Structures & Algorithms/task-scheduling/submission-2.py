
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        tasks_count = [-x for x in Counter(tasks).values()]
        heapq.heapify(tasks_count)

        wait_queue = deque()

        while tasks_count or wait_queue:
            # Release tasks whose cooldown has expired
            while wait_queue and wait_queue[0][1] <= time:
                task_cnt, _ = wait_queue.popleft()
                heapq.heappush(tasks_count, task_cnt)

            if tasks_count:
                task = heapq.heappop(tasks_count)

                # One execution reduces the remaining count
                task += 1

                if task < 0:
                    wait_queue.append([task, time + n + 1])

            time += 1

        return time
