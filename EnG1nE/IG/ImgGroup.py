from libqtile.widget.widgetbox import WidgetBox
from libqtile.widget import widgets

from EnG1nE.Sequencer.Seq import*

import psutil



class VideoGroup:
    def __init__(self, Path:str, FPS:int, Widgets:list, cb = lambda x:x, **kwargs):
        "for get widgets use '*VG().GetWidets()'"
        self.SeqButton = Sequence(Path, 1, cb, **kwargs)
        self.WidBox = WidgetBox(widgets = Widgets, **kwargs)
        self.SeqButton.mouse_callbacks = {
            "Button1": lambda: self.WidBox.toggle(),
            "Button2": lambda: self.WidBox.toggle(),
            "Button3": lambda: self.WidBox.toggle(),
            "Button4": lambda: self.WidBox.toggle(),
            "Button5": lambda: self.WidBox.toggle(),
        }
        for w in Widgets:
            w.mouse_callbacks = {
                "Button1": lambda: self.WidBox.toggle(),
                "Button2": lambda: self.WidBox.toggle(),
                "Button3": lambda: self.WidBox.toggle(),
                "Button4": lambda: self.WidBox.toggle(),
                "Button5": lambda: self.WidBox.toggle(),
            }
        self.WidBox.text_closed=''
        self.WidBox.text_open=''
    def GetWidgets(self):
        return self.SeqButton, self.WidBox
    
class CPUGroup(VideoGroup):
    def __init__(self, Path, Widgets, **kwargs):
        super().__init__(Path, 1, Widgets, self.Callback, **kwargs)
    def Callback(self, FPS):
        self.SeqButton.FPS = psutil.cpu_percent() / 5

class RAMGroup(VideoGroup):
    def __init__(self, Path, FPS, Widgets, **kwargs):
        super().__init__(Path, FPS, Widgets, self.Callback, **kwargs)
    def Callback(self):
        mem_info = psutil.virtual_memory()
        percent_used = mem_info.percent
        self.SeqButton.FPS = percent_used / 5

class BataryGroup(VideoGroup):
    def __init__(self, Path, FPS, Widgets, **kwargs):
        super().__init__(Path, FPS, Widgets, self.Callback, **kwargs)
    def Callback(self):
        self.SeqButton.FPS = psutil.sensors_battery().percent / 5

class NetworkGroup(VideoGroup):
    def __init__(self, Path, FPS, Widgets, **kwargs):
        super().__init__(Path, FPS, Widgets, **kwargs)