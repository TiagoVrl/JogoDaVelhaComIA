import time
from maze import Maze
from collections import deque

def solve_maze_backtracking(maze: Maze):
    s = deque()

    initial_pos = maze.get_init_pos_player()
    s.append(initial_pos)

    visited = set()
    visited.add(initial_pos)

    while s:
        current_pos = s.pop()

        if maze.find_prize(current_pos):
            print("Caminho foi encontrado!")
            maze.mov_player(current_pos)
            return True

        maze.mov_player(current_pos)
        time.sleep(0.01)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            next_row, next_col = current_pos[0] + dr, current_pos[1] + dc
            next_pos = (next_row, next_col)

            if (0 <= next_row < maze.M.shape[0] and
                0 <= next_col < maze.M.shape[1] and
                maze.is_free(next_pos) and
                next_pos not in visited):
                
                s.append(next_pos)
                visited.add(next_pos)
    
    print("Prêmio não encontrado.")
    return False

maze_csv_path = "labirinto1.txt"
maze = Maze() 

maze.load_from_csv(maze_csv_path)

maze.run()
maze.init_player()

solve_maze_backtracking(maze)

time.sleep(5)