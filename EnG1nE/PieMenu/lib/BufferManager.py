from lib.Connection import Connection
from lib.Node import Node
from lib.Overlay import OverlayWindow

FreeWind = []
FreeWire = []

UsageWind = []
UsageWire = []

def AddWind(Node, Data) -> OverlayWindow:
    Win = None
    if len(FreeWind):
        Win = FreeWind[0]
        FreeWind.remove(Win)
    else:
        Win = OverlayWindow(Node, Data)
    UsageWind.append(Win)    
    return Win

def AddWire(Node1:Node, Node2:Node) -> Connection:
    Wire = None
    if len(FreeWire):
        Wire = FreeWire[0]
        FreeWire.remove(Wire)
    else:
        Wire = Connection(Node1, Node2)
    UsageWire.append(Wire)
    return Wire

def DelWind(a: OverlayWindow) -> None:
    if not a in UsageWind:
        raise ValueError("Win created not in buffer")
    UsageWind.remove(a)
    FreeWind.append(a)

def DelWire(a: Connection) -> None:
    if not a in UsageWire:
        raise ValueError("Win created not in buffer")
    UsageWire.remove(a)
    FreeWire.append(a)