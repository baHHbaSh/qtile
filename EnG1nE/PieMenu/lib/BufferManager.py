from Connection import Connection
from Overlay import OverlayWindow

FreeWind = []
FreeWire = []

UsageWind = []
UsageWire = []

def AddWind(x:int, y:int, w:int, h:int, Data) -> OverlayWindow:
    Win = None
    if len(FreeWind):
        Win = FreeWind[0]
        FreeWind.remove(Win)
    else:
        Win = OverlayWindow(x, y, w, h, Data)
    UsageWind.append(Win)
    return Win

def AddWire(x1:int, y1:int, x2:int, y2:int) -> Connection:
    Wire = None
    if len(FreeWire):
        Wire = FreeWire[0]
        FreeWire.remove(Wire)
    else:
        Wire = Connection(x1, y1, x2, y2)
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