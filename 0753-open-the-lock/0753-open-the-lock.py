from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        st = set(deadends) 
        if "0000" in st:
            return -1
        if target == "0000":
            return 0
        
        q = deque()
        q.append(("0000", 0)) 
        visited = set()
        visited.add("0000")
        
        while q:
            x, moves = q.popleft()
            
            if x == target:
                return moves
            
            
            for i in range(4):
                for d in [-1, 1]:  
                    num = int(x[i])
                    new_num = (num + d) % 10
                    new_state = x[:i] + str(new_num) + x[i+1:]
                    
                    if new_state not in st and new_state not in visited:
                        q.append((new_state, moves + 1))
                        visited.add(new_state)
        
        return -1  
