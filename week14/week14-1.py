class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notANS = set()

        for a,b in paths:
            notANS.add(a)

        for a,b in paths:
            if b not in notANS:
                return b     