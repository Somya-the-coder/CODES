"""
question:-
def eliminatedPersons(N, K):
    # N and K are given
    # WRITE YOUR CODE HERE
    
    # Initialize the list of players
    players = list(range(1, N + 1))
    
    # Start passing the ball
    currentIndex = 0
    visited = set()  # To track players who received the ball
    
    while True:
        visited.add(players[currentIndex])  # Mark current player as visited
        currentIndex = (currentIndex + K) % N  # Move K steps ahead in circular manner
        
        # If the ball comes back to the starting player, stop
        if currentIndex == 0:
            break
    
    # Find eliminated players (those who didn't receive the ball)
    eliminated = [player for player in players if player not in visited]
    
    # Print results
    if not eliminated:
        print(0)
    else:
        print(" ".join(map(str, sorted(eliminated))))

def main():
    S = input().split()
    X = int(S[0])
    Y = int(S[1])
    eliminatedPersons(X, Y)

main()
"""
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
