from PyQt5.QtWidgets import*
from Node import Node

class Connection(QWidget):
    def __init__(self, Node1:Node, Node2:Node):
        super().__init__()