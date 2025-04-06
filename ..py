import tkinter as tk
import time

class SudokuSolverGUI:
        def __init__(self, root): 
            '''Hàm khởi tạo'''
            self.root = root
            self.root.title("Sudoku Solver 11A7")
            self.root.configure(bg='#f0f0f0')
            self.board = [[0 for _ in range(9)] for _ in range(9)] # Tạo bảng trống
            self.entries = [] # Placeholder cho bản sao để đối chiếu vào bảng gốc
            self.solving = False # Tránh spam nút Solve
            self.delay = 0.001 # Thời gian biểu diễn các bước

            # Main frame
            main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
            main_frame.pack(expand=True)

            # Grid frame
            grid_frame = tk.Frame(main_frame, bg='#d0d0d0', padx=3, pady=3)
            grid_frame.pack()

            # Tạo các ô có thể điền số
            for i in range(9):
                row_entries = []
                for j in range(9):
                    # Tạo ô
                    cell_frame = tk.Frame(
                        grid_frame,
                        borderwidth=1,
                        relief='solid',
                        bg='#d0d0d0'
                    )
                    cell_frame.grid(row=i, column=j, padx=1, pady=1)

                    #  Tạo cái để điền
                    entry = tk.Entry(
                        cell_frame,
                        width=2,
                        font=('Arial', 20, 'bold'),
                        justify='center',
                        bg='#ffffff',
                        fg='#333333',
                        relief='flat'
                    )
                    entry.pack(padx=2, pady=2)
                    entry.insert(0, '')
                    row_entries.append(entry)

                    # Add thicker borders for 3x3 blocks
                    if i % 3 == 0 and i != 0:
                        cell_frame.grid(pady=(3,1))
                    if j % 3 == 0 and j != 0:
                        cell_frame.grid(padx=(3,1))
                self.entries.append(row_entries)

            # Button frame
            button_frame = tk.Frame(main_frame, bg='#f0f0f0', pady=15)
            button_frame.pack()

            # Control buttons
            button_style = {
                'font': ('Arial', 12, 'bold'),
                'width': 10,
                'pady': 5,
                'border': 0,
                'cursor': 'hand2'
            }

            # Nút Solve
            self.solve_btn = tk.Button(
                button_frame,
                text="Solve",
                command=self.start_solver,
                bg='#4CAF50',
                fg='white',
                **button_style
            )
            self.solve_btn.pack(side=tk.LEFT, padx=5)

            # Nút Clear 
            self.clear_btn = tk.Button(
                button_frame,
                text="Clear",
                command=self.clear_board,
                bg='#f44336',
                fg='white',
                **button_style
            )
            self.clear_btn.pack(side=tk.LEFT, padx=5)

            # Nút Quit
            self.quit_btn = tk.Button(
                button_frame,
                text="Quit",
                command=root.destroy,  # Destroy the root window
                bg='#9C27B0',
                fg='white',
                **button_style
            )
            self.quit_btn.pack(side=tk.LEFT, padx=5)       

        def clear_board(self):
            '''Hàm nút Clear'''
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].config(bg='white')

        def start_solver(self):
            '''Hàm nút Solve'''
            if not self.solving:
                self.solving = True
                self.read_board()
                self.root.after(10, self.solve_step)

        def read_board(self):
            '''Đối chiếu bảng entries lên bảng board'''
            for i in range(9):
                for j in range(9):
                    val = self.entries[i][j].get()
                    self.board[i][j] = int(val) if val.isdigit() and val != '0' else 0

        def is_valid(self, row, col, num):
            '''Hàm kiểm tra tính hợp lệ của một bảng sudoku'''
            # Kiểm tra hàng
            if num in self.board[row]:
                return False

            # Kiểm tra cột
            if num in [self.board[i][col] for i in range(9)]:
                return False

            # Kiểm tra các ô 3x3
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if self.board[start_row + i][start_col + j] == num:
                        return False
            return True

        def find_empty(self):
            '''Tìm ô đầu tiên trống'''
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        return (i, j)
            return None

        def solve_step(self):
            '''Hàm chính giải sudoku'''
            empty = self.find_empty()
            if not empty:
                self.solving = False
                return True

            row, col = empty

            for num in range(1, 10):
                if self.is_valid(row, col, num):
                    # Update GUI
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].insert(0, str(num))
                    self.entries[row][col].config(bg='#90EE90')
                    self.root.update()

                    time.sleep(self.delay)

                    self.board[row][col] = num

                    if self.solve_step():
                        return True

                    self.board[row][col] = 0
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].config(bg='#FFB6C1')
                    self.root.update()
                    time.sleep(self.delay)
                    self.entries[row][col].config(bg='white')

            return False
if __name__ == "__main__":
        root = tk.Tk()
        app = SudokuSolverGUI(root)
        root.mainloop()