from copy import copy, deepcopy

class State:
    def __init__(self, firstPlayer):
        self.players = ["0", "1"]
        self.board = ["-" for i in range(9)]
        self.curPlayer = firstPlayer
        self.curAction = None

    def __cannot_win__(self, indices):
        if self.board[indices[0]] != '-':
            if self.board[indices[1]] != '-' and self.board[indices[1]] != self.board[indices[0]]:
                return True
            elif self.board[indices[2]] != '-' and self.board[indices[2]] != self.board[indices[0]]:
                return True
        elif self.board[indices[1]] != '-':
            if self.board[indices[2]] != '-' and self.board[indices[2]] != self.board[indices[1]]:
                return True

        return False

    def getActions(self):
        actions = []
        for i in range(9):
            if self.board[i] == '-':
                actions.append(i)
        return actions

    def check(self):
        # suppose not draw
        if self.board[0] == self.board[1] == self.board[2]:
            if self.board[0] != '-':
                return self.board[0]
        if self.board[3] == self.board[4] == self.board[5]:
            if self.board[3] != '-':
                return self.board[3]
        if self.board[6] == self.board[7] == self.board[8]:
            if self.board[6] != '-':
                return self.board[6]
        if self.board[0] == self.board[3] == self.board[6]:
            if self.board[0] != '-':
                return self.board[0]
        if self.board[1] == self.board[4] == self.board[7]:
            if self.board[1] != '-':
                return self.board[1]
        if self.board[2] == self.board[5] == self.board[8]:
            if self.board[2] != '-':
                return self.board[2]
        if self.board[0] == self.board[4] == self.board[8]:
            if self.board[0] != '-':
                return self.board[0]
        if self.board[2] == self.board[4] == self.board[6]:
            if self.board[2] != '-':
                return self.board[2]

        # draw
        if self.__cannot_win__([0,1,2]) and self.__cannot_win__([3,4,5]) and self.__cannot_win__([6,7,8]) \
            and self.__cannot_win__([0,3,6]) and self.__cannot_win__([1,4,7]) and self.__cannot_win__([2,5,8]) \
            and self.__cannot_win__([0,4,8]) and self.__cannot_win__([2,4,6]):
            return '*'

        # undetermined
        return '?'

    def takeAction(self, player, pos):
        #print self.board[pos], self.board[pos] != '-'
        if self.board[pos] != '-':
            return False
        self.curPlayer = player
        self.board[pos] = self.players[player]
        self.curAction = pos
        return True

    def __deepcopy__(self, memo):
        newState = copy(self)
        newState.player = deepcopy(self.players, memo)
        newState.board = deepcopy(self.board, memo)
        return newState

    def getBoard(self):
        return self.board

    def getBoardStr(self):
        return ''.join(self.board)






