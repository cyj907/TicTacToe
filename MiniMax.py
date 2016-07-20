from copy import deepcopy

class MiniMax:
    MIN = "min"
    MAX = "max"

    @staticmethod
    def __should_prune__(elem):
        if len(elem["actions"]) == 0 or \
                elem["op"] == MiniMax.MAX and elem["score"] > elem["beta"] or \
                elem["op"] == MiniMax.MIN and elem["score"] < elem["alpha"]:
            return True
        return False

    @staticmethod
    def __explore__(state, alpha, beta, value, player):

        actions = state.getActions()
        bestAct = None
        newAlpha = alpha
        newBeta = beta
        for act in actions:
            if state.curPlayer == player:
                if value > beta:
                    break
            else:
                if value < alpha:
                    break

            newState = deepcopy(state)
            newState.takeAction(state.curPlayer, act)

            if newState.check() != '?':
                newValue = 0
                if state.curPlayer == player:
                    if newState.check() != '*': # win
                        newValue = 10
                    if newValue > value:
                        value = newValue
                        newAlpha = max(newValue, newAlpha)
                        bestAct = act
                else:
                    if newState.check() != '*': # lose
                        newValue = -10
                    if newValue < value:
                        value = newValue
                        newBeta = min(newValue, newBeta)
                        bestAct = act
            else:
                newState.curPlayer = 1-newState.curPlayer
                if state.curPlayer == player: # max node
                    newAct, newValue = MiniMax.__explore__(newState, newAlpha, newBeta, float("inf"), player)
                    if newValue > value:
                        value = newValue
                        newAlpha = max(newValue, newAlpha)
                        bestAct = act
                else:
                    newAct, newValue = MiniMax.__explore__(newState, newAlpha, newBeta, float("-inf"), player)
                    if newValue < value:
                        value = newValue
                        newBeta = min(newValue, newBeta)
                        bestAct = act


        return bestAct, value



    @staticmethod
    def GetPosition2(state):
        player = state.curPlayer
        bestAct, value = MiniMax.__explore__(state, float("-inf"), float("inf"), float("-inf"), player)
        print bestAct, value
        return bestAct / 3, bestAct % 3


    @staticmethod
    def GetPosition(state):
        q = [{"state": deepcopy(state),
              "alpha": float("-inf"),
              "beta": float("inf"),
              "score": float("-inf"),
              "op": MiniMax.MAX,
              "action": None,
              "prev": -1,
              "actions": state.getActions(),
              "depth": 0}]
        curPlayer = state.curPlayer

        # build tree
        while len(q) > 0:
            elem = q.pop()
            actions = elem["actions"]
            previd = elem["prev"]

            if MiniMax.__should_prune__(elem):
                if previd == -1:
                    print elem["action"]
                    return elem["action"] / 3, elem["action"] % 3

                if q[previd]["op"] == MiniMax.MAX:
                    if elem["score"] > q[previd]["score"]:
                        q[previd]["score"] = elem["score"]
                        q[previd]["action"] = elem["state"].curAction
                else:
                    if elem["score"] < q[previd]["score"]:
                        q[previd]["score"] = elem["score"]
                        q[previd]["action"] = elem["state"].curAction
                continue

            newState = deepcopy(elem["state"])
            newState.takeAction(elem["state"].curPlayer, actions.pop())
            newState.curPlayer = 1 - newState.curPlayer
            elem["actions"] = actions

            newScore = None
            if newState.check() == newState.players[curPlayer]:
                newScore = 10 / (elem["depth"] + 1.0)
            elif newState.check() == newState.players[1-curPlayer]:
                newScore = -10 / (elem["depth"] + 1.0)
            elif newState.check() == '*':
                newScore = 0

            if newScore != None:
                if elem["op"] == MiniMax.MAX:
                    if elem["score"] < newScore:
                        elem["score"] = newScore
                        elem["action"] = newState.curAction
                else:
                    if elem["score"] > newScore:
                        elem["score"] = newScore
                        elem["action"] = newState.curAction
                q.append(elem)
            else:
                q.append(elem)
                if elem["op"] == MiniMax.MAX:
                    alpha = max(elem["score"], elem["alpha"])
                    newElem = {"state": newState, "alpha": alpha,
                       "beta": elem["beta"], "score": float("inf"), "op": MiniMax.MIN, "depth": elem["depth"]+1,
                           "action": None, "prev": len(q)-1, "actions": newState.getActions()}
                else:
                    beta = min(elem["score"], elem["beta"])
                    newElem = {"state": newState, "alpha": elem["alpha"],
                       "beta": beta, "score": float("-inf"), "op": MiniMax.MAX, "depth": elem["depth"]+1,
                           "action": None, "prev": len(q)-1, "actions": newState.getActions()}
                q.append(newElem)
