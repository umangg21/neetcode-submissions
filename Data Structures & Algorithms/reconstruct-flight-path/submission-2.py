class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        tickets.sort(reverse=True)

        for src,dst in tickets:
            adj[src].append(dst)
        
        res = []
        def dfs(src):

            while adj[src]:
                nex = adj[src].pop()
                dfs(nex)
            
            res.append(src)

        dfs("JFK")
        return res[::-1]
        