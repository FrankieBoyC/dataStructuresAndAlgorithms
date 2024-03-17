# Finds shortest path of weighted graphs
# https://www.youtube.com/watch?v=_B5cx-WD5EA
import itertools
import heapq


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def __len__(self):
        return len(self.pq)

    def add_task(self, priority, task):
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return self
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def update_priority(self, priority, task):
        entry = self.entry_finder[task]
        count = next(self.counter)
        entry[0], entry[1] = priority, count

    def pop_task(self):
        while self.pq:
            priority, count, task = - heapq.heappop(self.pq)
            del self.entry_finder[task]
            return priority, task
        raise KeyError('pop from empty priority queue')


def dijkstra(graph, start):
    previous = {v: None for v in graph.adjacency_list.keys()}
    visited = {v: False for v in graph.adjacency_list.keys()}
    distances = {v: float("inf") for v in graph.adjacency_list.keys()}
    distances[start] = 0
    queue = PriorityQueue()
    queue.add_task(0, start)
    while queue:
        removed_distance, removed = queue.pop_task()
        visited[removed] = True
        for edge in graph.adjacency_list[removed]:
            if visited[edge.vertex]:
                continue
            new_distance = removed_distance + edge.distance
            if new_distance < distances[edge.vertex]:
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)
    return
