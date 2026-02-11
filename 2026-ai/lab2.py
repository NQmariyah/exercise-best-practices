import heapq
from collections import deque

# --- KONFIGURASI PETA (MAZE) ---
# Mahasiswa boleh mengubah peta ini untuk uji coba kasus ekstrem
MAP_LAYOUT = [
    "####################",
    "#S#       #       G#",
    "# # ##### # ###### #",
    "# # #       #      #",
    "# # ##### ##### ####",
    "#       # #        #",
    "####### # # ###### #",
    "#       # #      # #",
    "# ####### ###### # #",
    "#                # #",
    "####################"
]

class MazeSolver:
    def __init__(self, maze_layout):
        self.maze = [list(row) for row in maze_layout]
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        self.start = self._find_pos('S')
        self.goal = self._find_pos('G')
        
    def _find_pos(self, char):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == char:
                    return (r, c)
        return None

    def get_neighbors(self, r, c):
        """Mengembalikan tetangga yang valid (tidak nabrak tembok)"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Atas, Bawah, Kiri, Kanan
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.maze[nr][nc] != '#':
                    neighbors.append((nr, nc))
        return neighbors

    # --- 1. BFS ALGORITHM ---
    def solve_bfs(self):
        """
        Gunakan Queue.
        Return: (path, nodes_explored)
        path: List koordinat [(r,c), ...]
        nodes_explored: Jumlah node yang dikunjungi selama pencarian
        """
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])
        nodes_explored = 0

        while queue:
            (current_r, current_c), path = queue.popleft()
            nodes_explored += 1
            
            if (current_r, current_c) == self.goal:
                return path, nodes_explored
            
            # --- TUGAS MAHASISWA: Lanjutkan logika BFS di sini ---
            # Loop neighbors -> cek visited -> add queue
            pass 
            
        return None, nodes_explored

    # --- 2. DFS ALGORITHM ---
    def solve_dfs(self):
        """
        Gunakan Stack.
        """
        stack = [(self.start, [self.start])]
        visited = set([self.start])
        nodes_explored = 0
        
        # --- TUGAS MAHASISWA: Implementasi DFS ---
        # Hati-hati dengan urutan push/pop
        pass
        return None, nodes_explored

    # --- 3. A* ALGORITHM ---
    def heuristic(self, a, b, type='manhattan'):
        (x1, y1), (x2, y2) = a, b
        if type == 'manhattan':
            return abs(x1 - x2) + abs(y1 - y2)
        elif type == 'euclidean':
            return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        elif type == 'bad':
            # CONTOH BAD HEURISTIC: Overestimate gila-gilaan
            # Ini akan membuat A* jadi serakah (Greedy) dan mungkin tidak optimal
            return (abs(x1 - x2) + abs(y1 - y2)) * 10 
        return 0

    def solve_astar(self, heuristic_type='manhattan'):
        """
        Gunakan Priority Queue (heapq).
        Simpan di heap: (f_score, g_score, current_node, path)
        """
        start_node = self.start
        # Priority Queue: (f, g, (r,c), path)
        pq = []
        heapq.heappush(pq, (0, 0, start_node, [start_node]))
        
        visited = set()
        nodes_explored = 0
        
        # --- TUGAS MAHASISWA: Implementasi A* ---
        # Ingat rumus: f = g + h
        pass
        return None, nodes_explored

    def visualize_path(self, path, title):
        if not path:
            print(f"\n[{title}] ❌ NO PATH FOUND")
            return

        print(f"\n[{title}] ✅ PATH FOUND")
        print(f"Path Length : {len(path)} steps")
        # Visualisasi Grid
        display_map = [row[:] for row in self.maze]
        for r, c in path:
            if display_map[r][c] not in ['S', 'G']:
                display_map[r][c] = '*' # Jejak
        
        for row in display_map:
            print("".join(row))

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    solver = MazeSolver(MAP_LAYOUT)
    
    print(f"Start: {solver.start} | Goal: {solver.goal}")
    
    # 1. Run BFS (Baseline)
    # path_bfs, explored_bfs = solver.solve_bfs() # Uncomment jika sudah dibuat
    # solver.visualize_path(path_bfs, f"BFS (Explored: {explored_bfs})")

    # 2. Run DFS
    # path_dfs, explored_dfs = solver.solve_dfs() # Uncomment
    # solver.visualize_path(path_dfs, f"DFS (Explored: {explored_dfs})")

    # 3. Run A* (Good Heuristic)
    # path_astar, explored_astar = solver.solve_astar('manhattan') # Uncomment
    # solver.visualize_path(path_astar, f"A* Manhattan (Explored: {explored_astar})")