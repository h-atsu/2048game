import random
from game import Game


class Solver():
    def __init__(self) -> None:
        pass

    def solve(self, list) -> str:
        d = ['r', 'l', 'u', 'd']
        max_score = 0
        ans = []
        action = {'r': Game.move_right,
                  'l': Game.move_left,
                  'u': Game.move_up,
                  'd': Game.move_down}
        for i in range(4):
            game = Game(list)
            is_movable = action[d[i]](game)
            if game.score >= max_score and is_movable:
                ans = d[i]
        return ans


if __name__ == '__main__':
    game = Game([[2, 2, 2, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]])
    sol = Solver()
    print(sol.solve(game.board))
