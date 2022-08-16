from game import *

class ML:
    def __init__(self, aiCount = 100) -> None:
        self.aiList = []
        self.aiCount = aiCount
        self.gamesPlayed = (aiCount-1)*2
        for i in range(aiCount):
            ai = Ai(str(i), "ai"+str(i))
            self.aiList.append(ai)

    def runIteration(self):
        winCounts = [0]*self.aiCount
        for i in range(self.aiCount):
            for j in range(self.aiCount):
                if i == j:
                    continue
                g = Game()
                result = g.play(self.aiList[i], self.aiList[j])
                if result == self.aiList[i].name:
                    winCounts[i] += 1
                elif result == self.aiList[j].name:
                    winCounts[j] += 1
        return [round(x/self.gamesPlayed, 2) for x in winCounts]