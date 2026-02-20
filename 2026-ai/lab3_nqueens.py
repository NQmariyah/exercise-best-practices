import random

class NQueensSolver:
    def __init__(self, n=8):
        self.n = n
    
    def generate_random_state(self):
        """Membuat state acak awal."""
        # State berupa list angka 0 s.d N-1
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def calculate_cost(self, state):
        """
        Menghitung jumlah pasangan ratu yang saling serang (Objective Function).
        Semakin kecil semakin baik. Goal = 0.
        """
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # 1. Cek satu baris (Row)
                if state[i] == state[j]:
                    conflicts += 1
                # 2. Cek Diagonal
                elif abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbors(self, state):
        """
        Menghasilkan semua kemungkinan tetangga (neighbors).
        Satu tetangga = Satu ratu dipindah ke baris lain di kolom yang sama.
        """
        neighbors = []
        for col in range(self.n):
            for row in range(self.n):
                if state[col] != row: # Jangan buat state yang sama persis
                    new_state = list(state)
                    new_state[col] = row
                    neighbors.append(new_state)
        return neighbors

    def hill_climbing(self, max_restart=0):
        """
        Logika Utama Hill Climbing.
        
        TUGAS MAHASISWA:
        1. Mulai dari random state.
        2. Cari tetangga dengan cost TERKECIL (Steepest Ascent).
        3. Jika cost tetangga >= cost sekarang, BERHENTI (Local Optimum).
        4. Jika cost tetangga < cost sekarang, pindah ke tetangga tersebut.
        """
        
        # --- KODE MAHASISWA DISINI ---
        # Implementasikan loop pencarian
        # Return format: (final_state, final_cost, steps)
        pass

    def visualize_board(self, state):
        """Mencetak papan catur ke terminal."""
        board = [['.' for _ in range(self.n)] for _ in range(self.n)]
        for col, row in enumerate(state):
            board[row][col] = 'Q'
        
        print("\n".join([" ".join(row) for row in board]))
        print(f"Cost: {self.calculate_cost(state)}")

# --- MAIN EXPERIMENT ---
if __name__ == "__main__":
    n = 8
    solver = NQueensSolver(n)
    
    print(f"--- EXPERIMENT 1: Single Run Hill Climbing (N={n}) ---")
    # Jalankan sekali, lihat hasilnya
    # (Mahasiswa harus mengisi fungsi hill_climbing dulu)
    
    print("\n--- EXPERIMENT 2: Failure Analysis (100 Runs) ---")
    # TUGAS MAHASISWA:
    # Jalankan hill_climbing() sebanyak 100 kali.
    # Hitung:
    # 1. Berapa kali sukses (Cost = 0)?
    # 2. Berapa kali gagal (Cost > 0)?
    # 3. Rata-rata cost saat gagal?