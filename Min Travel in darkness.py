#DIJKSTRA'S ALGORITHM
class Solution:

    def getDistance(self, a: List[int], b: List[int]) -> float:
        # Calculate the Euclidean distance between points a and b
        dist = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        return dist

    def minDistance(self, a: List[int], b: List[int],
                     lights: List[List[int]]) -> int:
        INF = float('inf')
        n = len(lights)
        total = n + 2

        # Create points: start (a), lights, and end (b)
        points = [[a[0], a[1], 0]]  # Starting point has no radius
        for light in lights:
            points.append([light[0], light[1], light[2]])  # (x, y, radius)
        points.append([b[0], b[1], 0])  # Ending point has no radius

        # Initialize distance array with INF and visited array
        dist = [INF] * total
        visited = [False] * total
        dist[0] = 0  # Distance to start is 0

        # Dijkstra's algorithm
        for _ in range(total):
            # Find the node u with the minimum distance that is not yet visited
            minDist = INF
            u = -1
            for v in range(total):
                if not visited[v] and dist[v] < minDist:
                    minDist = dist[v]
                    u = v

            if u == -1:  # All nodes have been visited
                break
            if u == total - 1:  # Reached the target point b
                break

            visited[u] = True

            # Relax the edges
            for v in range(total):
                if not visited[v]:
                    # Calculate the distance between points u and v
                    dist_uv = self.getDistance(points[u], points[v])

                    # Subtract the sum of the radii if within range
                    radius_sum = points[u][2] + points[v][2]
                    dist_uv = max(0, dist_uv - radius_sum)

                    # Update the shortest path distance
                    if dist[v] > dist[u] + dist_uv:
                        dist[v] = dist[u] + dist_uv

        # Return the distance to the last point (target point b)
        return int(dist[total - 1])
