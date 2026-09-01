class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_positions = []
        start = None

        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'L':
                    litter_positions.append((i, j))
                elif c == 'S':
                    start = (i, j)

        k = len(litter_positions)
        litter_index = {pos: idx for idx, pos in enumerate(litter_positions)}
        full_mask = (1 << k) - 1

        sr, sc = start
        start_mask = 0
        if (sr, sc) in litter_index:
            start_mask |= (1 << litter_index[(sr, sc)])

        if start_mask == full_mask:
            return 0

        visited = {(sr, sc, start_mask): energy}
        q = deque([(sr, sc, energy, start_mask, 0)])  # row, col, energy, mask, moves
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if e == 0:
                continue  # stuck, can't move further

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask
                cell = classroom[nr][nc]

                if cell == 'L' and (nr, nc) in litter_index:
                    nmask = mask | (1 << litter_index[(nr, nc)])
                if cell == 'R':
                    ne = energy  # reset to max capacity

                key = (nr, nc, nmask)
                if key in visited and visited[key] >= ne:
                    continue
                visited[key] = ne

                if nmask == full_mask:
                    return moves + 1

                q.append((nr, nc, ne, nmask, moves + 1))

        return -1