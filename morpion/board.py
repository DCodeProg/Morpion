class Board: 
    def __init__(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
                
    def is_empty(self, row: int, col: int) -> bool:
        if self.grid[row][col] == " ": 
            return True
        else:
            return False
    
    def place_pawn(self, row: int, col: int, pawn: str):
        if self.is_empty(row,col):
            self.grid[row][col] = pawn
        
    def show_grid(self):
        grid = self.grid
        print(f"{grid[0][0]} │ {grid[0][1]} │ {grid[0][2]}")
        print("──┼───┼───")
        print(f"{grid[1][0]} │ {grid[1][1]} │ {grid[1][2]}")
        print("──┼───┼───")
        print(f"{grid[2][0]} │ {grid[2][1]} │ {grid[2][2]}")
    
    
    
    def is_full(self) -> bool:
        for row in self.grid:
            for col in row:
                if col == " ":
                    return False

        return True
            
        
    
    def check_victory(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return True
            
        for i in range (3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != " ":
                return True
            
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return True 
        
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return True 
        
        return False
        
        
        
                
if __name__ == "__main__":
    print(r"""                         _             
  /\/\   ___  _ __ _ __ (_) ___  _ __  
 /    \ / _ \| '__| '_ \| |/ _ \| '_ \ 
/ /\/\ \ (_) | |  | |_) | | (_) | | | |
\/    \/\___/|_|  | .__/|_|\___/|_| |_|
                  |_|                  
""")
    
    b=Board()
    # print(b.is_empty(1,2))
    b.show_grid()
    print(b.check_victory())