class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        A = {}
        for u,v in prerequisites:
            if u not in A: 
                A[u] = [v]
            else:
                A[u].append(v)

        hs = set()  
        def dfs(crs):
            if crs in hs: return False
            if crs not in A: return True

            hs.add(crs)
            if A[crs]:
                for nei in A[crs]:
                    if not dfs(nei): return False
            
            hs.remove(crs)
            A[crs] = None
            return True
        

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True