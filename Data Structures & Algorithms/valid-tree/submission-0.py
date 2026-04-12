class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        A = {i:[] for i in range(n)}

        for u,v in edges:
            A[u].append(v)
            A[v].append(u)
        
        visited = set()
        
        def dfs(idx, prev):
            if idx in visited: return False

            visited.add(idx)
            for nei in A[idx]:
                if nei == prev: continue
                if not dfs(nei, idx): return False
            
            return True
        
        return dfs(0, -1) and n==len(visited)