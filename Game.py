from State import State
from GameUI import GameUI
from MiniMax import MiniMax

class Mode:
    TwoPlayers = 0
    OnePlayerFirst = 1
    OnePlayerSecond = 2

class Game:
    def __init__(self):
        self.gameState = State(0)
        self.gameUI = GameUI(300, 300)

    def run(self, mode):
        turn = 0
        while True:
            if turn == 0:
                if mode == Mode.TwoPlayers:
                    pos = self.gameUI.GetMousePos()
                elif mode == Mode.OnePlayerFirst:
                    pos = self.gameUI.GetMousePos()
                else:
                    self.gameState.curPlayer = turn
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
                if mode == Mode.TwoPlayers:
                    pos = self.gameUI.GetMousePos()
                elif mode == Mode.OnePlayerFirst:
                    self.gameState.curPlayer = turn
                    pos = MiniMax.GetPosition(self.gameState)
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
            while True:
                pass
        elif self.gameState.check() == '0':
            print("Player 0 win!")
            while True:
                pass
        else:
            print("draw!")
            while True:
                pass


game = Game()
game.run(Mode.OnePlayerSecond)


