class HistoryManager:
    def __init__(self) -> None:
        self.calcHistory: list[str] = []
        self.calcHistoryTracker: int = -1

    def addToCalcHistory(self, line: str) -> None:
        self.calcHistory.insert(0,line)
        self.calcHistoryTracker = -1

    def getHistoryItem(self) -> str:
        if self.calcHistoryTracker >= len(self.calcHistory):
            self.calcHistoryTracker = len(self.calcHistory)
            return ""
        elif self.calcHistoryTracker < 0:
            self.calcHistoryTracker = -1
            return ""
        return self.calcHistory[self.calcHistoryTracker]

    def getNextHistoryItem(self) -> str:
        self.calcHistoryTracker += 1
        return self.getHistoryItem()

    def getPreviousHistoryItem(self) -> str:
        self.calcHistoryTracker -= 1
        return self.getHistoryItem()


