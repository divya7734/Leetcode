class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges)==0:
            if source == destination:
                return True
            return False
        mp={}
        l=[0]*n
        for i in range(len(edges)):
            u=edges[i][0]
            v=edges[i][1]
            if u not in mp.keys():
                mp[u]=[v]
            else:
                mp[u].append(v)
            
            if v not in mp.keys():
                mp[v]=[u]
            else:
                mp[v].append(u)
        s=[]
        s.append(source)
        l[source]=1
        while len(s)!=0:
            p=s.pop(0)
            for i in range(len(mp[p])):
                if l[mp[p][i]]==0:
                    s.append(mp[p][i])
                    l[mp[p][i]]=1
                if l[destination]==1:
                    return True
        return l[destination] == 1