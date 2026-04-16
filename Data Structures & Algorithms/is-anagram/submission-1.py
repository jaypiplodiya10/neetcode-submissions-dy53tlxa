class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs1 = {}; hs2={}; ls= len(s); lt=len(t)

        if ls != lt: return False

        for idx in range(ls):
            if s[idx] not in hs1:
                hs1[s[idx]] = 1
            else:
                hs1[s[idx]] += 1

            if t[idx] not in hs2:
                hs2[t[idx]] = 1
            else:
                hs2[t[idx]] += 1
        
        return True if hs1==hs2 else False

