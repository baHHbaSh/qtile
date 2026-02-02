from enum import Enum
from PyQt5.QtWidgets import*

from lib.BufferManager import*
from lib.Node import Node

from utilits.GetReolution import get_screen_resolution

Screen = get_screen_resolution()

SIZE_WIN = 50

class G(Enum):
    cmd = 0
    img = 1

class Application(QApplication):
    def __init__(self, Data:dict, NodeStartPos = (Screen[0]/2, 0)):
        super().__init__([])
        StartNode = Node(NodeStartPos[0], NodeStartPos[1], 0, 0)
        Middle = AddWind(Node(Screen[0]/2, Screen[1]/2, SIZE_WIN, SIZE_WIN), Data)
        self.Tree = {
            "p.": StartNode,
            "p.Main" : Middle
        }
        AddWire(StartNode, Middle)

    def AddChildWindows(self, ParentPath:str, data:dict):
        for Obj in data:
            if type(data[Obj]) == dict:
                self.Tree[f"{ParentPath}.{Obj}"]


    def Launch(self):
        self.exec_()