class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m , n = len(classroom) , len(classroom[0])
        start = None
        litter_pos = []

        for i in range(m):
            for j in range (n):

                if classroom[i][j] == "S":
                    start = (i,j)
                elif classroom[i][j] =="L":
                    litter_pos.append((i,j))
        
        k = len(litter_pos)
        full_mask = (1 << k) - 1
        # Making any dic to store the litter position with their index value in mask
        litter_index = {pos : idx for idx, pos  in enumerate (litter_pos)}
        sr , sc = start 
        start_mask = 0
        if (sr, sc ) in litter_index :
            start_mask = start_mask | (1 << litter_index[(sr,sc)])
        
        if start_mask == full_mask:
            return 0
        
        visited = {(sr, sc , start_mask) : energy}  # dic where L is alredy picked with energy level

        q = deque([(sr,sc,energy,start_mask , 0)]) # It carry cordinates of row , energy lvl , bit mask for    
                                                    #that co ordianate , and distance it travel

        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:

            r , c , e, mask , dist = q.popleft()

            if e == 0 :
                continue
            for dr , dc in direction:
                nr , nc = dr +r , dc + c

                if not( 0 <= nr < m  and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == "X":
                    continue
                ne = e -1 
                nmask = mask
                cell = classroom[nr][nc]

                if cell == "L":
                    nmask = mask | (1 << litter_index[(nr,nc)])
                if cell =="R":
                    ne = energy 
                key = (nr,nc,nmask)

                if key in visited and visited[key] >= ne:
                    continue 
                visited[key] = ne

                if nmask == full_mask:
                    return dist + 1

                q.append((nr,nc , ne,nmask , dist + 1))             




        return -1