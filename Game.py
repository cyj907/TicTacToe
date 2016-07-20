from State import State
from GameUI import GameUI
from MiniMax import MiniMax

class Game:
    def __init__(self):
        self.gameState = State()
        self.gameUI = GameUI(300, 300)

    def run(self):
        turn = 0
        while True:
            if turn == 0:
                pos = MiniMax.GetPosition(self.gameState)
                if pos != None:
                    pos_val = pos[0] * 3 + pos[1]
                    actionStat = self.gameState.takeAction(turn, pos_val)
                    if actionStat:
                        turn = 1
                        self.gameUI.drawO(pos)
                        if self.gameState.check() != '?':
                            break
            else:
                pos = self.gameUI.GetMousePos()
                if pos != None:
                    pos_val = pos[0] * 3 + pos[1]
                    actionStat = self.gameState.takeAction(turn, pos_val)
                    if actionStat:
                        turn = 0
                        self.gameUI.drawX(pos)
                        if self.gameState.check() != '?':
                            break

        if self.gameState.check() == '1':
            print("Player 1 win!")
        elif self.gameState.check() == '0':
            print("Player 0 win!")
        else:
            print("draw!")


game = Game()
game.run()


