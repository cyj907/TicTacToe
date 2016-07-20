from copy import deepcopy

class MiniMax:
    MIN = "min"
    MAX = "max"

    @staticmethod
    def GetPosition(state):
        # TODO
        q = [{"state": deepcopy(state), "score": None, "op": MiniMax.MAX, "action": None, "prev": None}]
        q2 = []
        curPlayer = 1-state.curPlayer

        # build tree
        while len(q) > 0:
            elem = q.pop()
            elem["id"] = len(q2)
            q2.append(elem)
            for i in range(9):
                if elem["state"].board[i] == '-':
                    newState = deepcopy(elem["state"])
                    newState.takeAction(1-elem["state"].curPlayer,i)
                    newScore = None
                    newAction = i
                    prev = elem
                    if elem["op"] == MiniMax.MAX:
                        newOp = MiniMax.MIN
                    else:
                        newOp = MiniMax.MAX
                    if newState.check() == newState.players[curPlayer]:
                        newScore = 1
                    elif newState.check() == newState.players[1-curPlayer]:
                        newScore = -1
                    elif newState.check() == '*':
                        newScore = 0

                    newElem = {"state": newState, "score": newScore, "op": newOp, "action": newAction,
                                   "prev": prev}
                    q.append(newElem)


        # get Action
        while len(q2) > 0:
            elem = q2.pop()
            prev = elem["prev"]
            if prev == None:
                print elem
                x = elem["bestAction"] / 3
                y = elem["bestAction"] % 3
                return x,y

            if prev["op"] == MiniMax.MAX:
                if prev["score"] == None or elem["score"] > prev["score"]:
                    prev["score"] = elem["score"]
                    prev["bestAction"] = elem["action"]
            else:
                if prev["score"] == None or elem["score"] < prev["score"]:
                    prev["score"] = elem["score"]
                    prev["bestAction"] = elem["action"]
            q2[prev["id"]] = prev

        return None