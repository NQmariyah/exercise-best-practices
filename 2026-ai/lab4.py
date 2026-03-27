import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Array 1D indeks 0-8
        self.current_winner = None
        self.nodes_evaluated = 0 # Metrik penting untuk dianalisis

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Cek Baris
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]): return True
        
        # Cek Kolom
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]): return True
        
        # Cek Diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]): return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]): return True
            
        return False

class MinimaxAgent:
    def __init__(self, letter):
        self.letter = letter # 'X' atau 'O'

    def get_move(self, game):
        game.nodes_evaluated = 0 # Reset counter tiap mau melangkah
        if len(game.available_moves()) == 9:
            # Hardcode langkah pertama agar tidak terlalu lama (opsional)
            square = random.choice([0, 2, 4, 6, 8]) 
        else:
            square = self.minimax(game, self.letter)['position']
        
        print(f"AI ({self.letter}) memilih posisi {square}.")
        print(f"Metrik: Membuka {game.nodes_evaluated} kemungkinan masa depan.")
        return square

    def minimax(self, state, player):
        """
        TUGAS MAHASISWA: Implementasikan Algoritma Minimax
        
        Input:
        - state: Objek TicTacToe saat ini (mengandung state.board).
        - player: Karakter 'X' (MAX) atau 'O' (MIN) yang sedang giliran.
        
        Output:
        - Harus me-return sebuah kamus (dictionary): {'position': best_square, 'score': best_score}
        
        Petunjuk Logika:
        1. BASE CASE: Cek dulu apakah state saat ini sudah ada yang menang atau seri.
           Jika ya, kembalikan skor (utility) dan position = None.
        2. Tentukan 'best_score' awal. Jika MAX, mulai dari minus tak terhingga (-math.inf). 
           Jika MIN, mulai dari tak terhingga (math.inf).
        3. Lakukan LOOPING ke semua 'available_moves':
           a. Coba buat langkah di papan (make_move).
           b. Panggil minimax() ini lagi secara rekursif untuk pemain lawan.
           c. Batalkan langkah (undo move) agar papan kembali seperti semula!
           d. Update 'best_score' dan 'best_position' jika hasil rekursif lebih baik.
        4. Return 'best_score' dan 'best_position'.
        """
        
        # --- KODE ANDA DIMULAI DI SINI ---
        pass

# --- GAME PLAYING -- 
class RandomAgent:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        print(f"Random Agent ({self.letter}) memilih posisi {square} secara acak.")
        return square

def play_game(game, x_player, o_player, print_game=True):
    if print_game:
        # Tampilkan nomor indeks papan
        print("Indeks Papan Tic-Tac-Toe:")
        print("| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |\n")
        game.print_board()
        print("")

    letter = 'X'
    while game.empty_squares():
        # Giliran pemain
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Buat langkah
        if game.make_move(square, letter):
            if print_game:
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(f"🎉 PEMENANGNYA ADALAH: {letter}!")
                return letter
            
            # Ganti giliran
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("🤝 PERMAINAN SERI (DRAW)!")
    return "DRAW"

if __name__ == "__main__":
    print("=== PERTANDINGAN: MINIMAX (X) vs RANDOM AGENT (O) ===")
    t = TicTacToe()
    
    # X adalah AI kita yang cerdas, O adalah bot bodoh
    x_player = MinimaxAgent('X')
    o_player = RandomAgent('O')
    
    play_game(t, x_player, o_player, print_game=True)