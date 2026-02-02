class Node:
    def __init__(self, x:int, y:int, w:int, h:int):
        self.x = x
        self.y = y
        self.w = w
        self.y = y
    @staticmethod
    def GetDPosScreenPosition(Node1: Node, Node2: Node, Padding = True)->tuple[int, int, int, int]:
        x = min(Node1.x, Node2.x)
        y = min(Node1.y, Node2.y)
        w = abs(Node1.x - Node2.x)
        h = abs(Node1.y - Node2.y)
        return x, y, w, h