class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid)
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        visted={(0,0)}
        q = deque([(0,0,1)]) #row, column, distance travel

        while q :
            r , c ,dist = q.popleft()

            if (r,c) == (col-1, row-1):
                return dist

            for rd, cd in direction:
                nr , nc = r + rd, c + cd

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0 and (nr,nc) not in visted:
                    visted.add((nr,nc))
                    q.append((nr,nc , dist +1))
                
        return -1
