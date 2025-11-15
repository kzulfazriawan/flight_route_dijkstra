import heapq
from typing import List


class DijkstraAlgorithm:
    def __init__(self, n: int, flights: List[List[int]]):
        # new adjacently lists
        self.graph = [[] for _ in range(n)]
        for a, b, cost in flights:
            self.graph[a].append([b, cost])

    def priority_queue(self, source, destination, limit):
        # set the priority queue (total cost, city, and transits/stops)
        pq = [(0, source, 0)]

        # tracking the minimum transits/stop between cities
        min_stops = {}

        while pq:
            cost, city, stops = heapq.heappop(pq)

            # Already reach the destination with the cheapest cost
            if city == destination: return cost
            # Skip if reach the city with fewer stops or exceeding the limit
            if stops > limit or (city in min_stops and min_stops[city] <= stops):
                continue

            min_stops[city] = stops

            for nxt, price in self.graph[city]:
                heapq.heappush(pq, (cost + price, nxt, stops + 1))
        return -1
