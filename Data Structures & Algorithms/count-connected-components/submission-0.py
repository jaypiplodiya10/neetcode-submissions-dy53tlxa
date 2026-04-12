class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        A = {i:[] for i in range(n)}
        for u,v in edges:
            A[v].append(u); A[u].append(v)
        
        visited = set()
        def dfs(idx):
            visited.add(idx)
            for nei in A[idx]:
                if nei in visited: continue
                dfs(nei)
        
        ans =0
        for idx in range(n):
            if idx not in visited:
                dfs(idx)
                ans +=1
        
        return ans