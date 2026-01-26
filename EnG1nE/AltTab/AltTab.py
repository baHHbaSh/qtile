from libqtile.config import Key
from libqtile.lazy import lazy

class AltTab:
    History = ["1", "2"]
    def __init__(self, keys:list):
        keys.append(Key(["mod4"], "Tab", lazy.group[self.AltTab()].toscreen()))
    def LogWin(self, NumOfWin:str, *args):
        if self.History[-1] == NumOfWin:
            return
        self.History.append(NumOfWin)
        while len(self.History) > 2:
            self.History.pop(0)
    def AltTab(self, *args) -> str:
        self.History[0], self.History[1], = self.History[1], self.History[0]
        return self.History[0]