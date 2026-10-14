class HistoryManager:
    def __init__(self):
        self.calcHistory = []
        self.calcHistoryTracker = -1

    def addToCalcHistory(self, line):
        self.calcHistory.insert(0,line)
        self.calcHistoryTracker = -1

    def getHistoryItem(self):
        if self.calcHistoryTracker >= len(self.calcHistory):
            self.calcHistoryTracker = len(self.calcHistory)
            return ""
        elif self.calcHistoryTracker < 0:
            self.calcHistoryTracker = -1
            return ""
        return self.calcHistory[self.calcHistoryTracker]

    def getNextHistoryItem(self):
        self.calcHistoryTracker += 1
        return self.getHistoryItem()

    def getPreviousHistoryItem(self):
        self.calcHistoryTracker -= 1
        return self.getHistoryItem()


