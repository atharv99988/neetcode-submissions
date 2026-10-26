class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for node1, node2 in edges : 
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
         
        def dfs(previous, node):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == previous:
                    continue

                if neighbor in visited:
                    return False

                if not dfs(node, neighbor):
                    return False

            return True


        return dfs(-1, 0) and len(visited) == n
