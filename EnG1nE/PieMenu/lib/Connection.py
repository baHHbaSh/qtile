from PyQt5.QtWidgets import*
from lib.Node import Node

class Connection(QWidget):
    def __init__(self, Node1:Node, Node2:Node):
        "Node1 - parent, Node2 - target"
        super().__init__()
        self.setGeometry(*Node.GetDPosScreenPosition(Node1, Node2))
        self.Node1 = Node1
        self.Node2 = Node2
    def SetNode(self, NodeTarget:Node, NodeParent:Node = None):
        self.Node2 = NodeTarget
        if NodeTarget != None:
            self.Node1 = NodeParent