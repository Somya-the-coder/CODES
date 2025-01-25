class Solution:
    def dfs(self, node, adj, vis, teams, alone):
        # Mark the node as visited
        vis[node] = True

        # Traverse all the children of the current node
        for neighbor in adj[node]:
            if not vis[neighbor]:
                self.dfs(neighbor, adj, vis, teams, alone)

        # Process the current node
        sz = len(adj[node])
        if sz == 0:  # Leaf node
            teams[node] = 0
            alone[node] = 1
        elif sz == 1:  # Single child
            child = adj[node][0]
            teams[node] = teams[child]
            alone[node] = alone[child] + 1
        else:  # More than one child
            mx = -1
            mxInd = -1

            # Find the child with the maximum alone value
            for i, child in enumerate(adj[node]):
                if alone[child] > mx:
                    mx = alone[child]
                    mxInd = i

            totalTeams = 0
            totalAlone = 0

            # Calculate total teams and alone counts excluding the max child
            for i, child in enumerate(adj[node]):
                if i != mxInd:
                    totalAlone += alone[child]
                    totalTeams += teams[child]

            # Evaluate based on the conditions
            if totalAlone + (2 * totalTeams) >= alone[adj[node][mxInd]]:
                tempAlone = totalAlone + alone[adj[node][mxInd]]
                alone[node] = 2 if tempAlone % 2 else 1
                teams[node] = (tempAlone // 2) + totalTeams + teams[adj[node][mxInd]]
            else:
                permAlone = alone[adj[node][mxInd]] - (totalAlone + (2 * totalTeams))
                alone[node] = permAlone + 1
                tempAlone = totalAlone + alone[adj[node][mxInd]] - permAlone
                if tempAlone % 2:
                    alone[node] += 1
                teams[node] = (tempAlone // 2) + totalTeams + teams[adj[node][mxInd]]

    def maximumPossibleSquads(self, arr):
        n = len(arr) + 1  # Number of knights (including the King)
        adj = [[] for _ in range(n)]

        # Build the adjacency list from the hierarchy
        for i in range(n - 1):
            adj[arr[i]].append(i + 1)

        teams = [0] * n  # To store the number of teams for each knight
        alone = [0] * n  # To store the number of lone knights for each knight
        vis = [False] * n  # To mark visited knights during DFS

        # Start DFS from the root node (0, which is the King)
        self.dfs(0, adj, vis, teams, alone)

        return teams[0]  # Return the number of teams from the King's node
