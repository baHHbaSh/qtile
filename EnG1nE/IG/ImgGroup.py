from libqtile.widget.widgetbox import WidgetBox
from libqtile.widget import widgets

from EnG1nE.Sequencer.Seq import*
from EnG1nE.State.State import*

import subprocess
import re
import psutil

def get_wifi_percentage_iwconfig(interface="wlan0"):
    try:
        output = subprocess.check_output(["iwconfig", interface], stderr=subprocess.STDOUT, encoding="utf-8")
        match = re.search(r"Link Quality=(\d+)/(\d+)", output)
        if match:
            current = int(match.group(1))
            maximum = int(match.group(2))
            return current / maximum
    except Exception:
        raise "Ошибка: проверьте имя интерфейса (wlan0, wlp...)"

print(f"Сигнал (iwconfig): {get_wifi_percentage_iwconfig()}")

class VideoGroup:
    def __init__(self, Path:str, FPS:int, Widgets:list, cb = lambda x:x, **kwargs):
        "for get widgets use '*VG().GetWidets()'"
        self.SeqButton = Sequence(Path, FPS, cb, **kwargs)
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
    
class PercentGroup:
    def __init__(self, Path:str, FPS:int, Widgets:list, cb = lambda x:x, **kwargs):
        "for get widgets use '*VG().GetWidets()'"
        self.SeqButton = State(Path, 1, cb, **kwargs)
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

class RAMGroup(PercentGroup):
    def __init__(self, Path, FPS, Widgets, **kwargs):
        super().__init__(Path, FPS, Widgets, self.Callback, **kwargs)
    def Callback(self, FPS):
        mem_info = psutil.virtual_memory()
        percent_used = mem_info.percent
        self.SeqButton.SetFramePercent(percent_used/100)

class BataryGroup(PercentGroup):
    IsCharged = None
    def __init__(self, Path, FPS, Widgets, **kwargs):
        super().__init__(Path, FPS, Widgets, self.Callback, **kwargs)
    def Callback(self, FPS):
        Bat = psutil.sensors_battery()
        Per = Bat.percent / 100
        IsCha = Bat.power_plugged
        if IsCha != self.IsCharged:
            self.IsCharged = IsCha
            Img = self.GetWidgets()[0]
            Img.background = "#FFCC00" if IsCha else "#55000055"
            Img.RenderWidget()
        self.SeqButton.SetFramePercent(Per)

class NetworkGroup(PercentGroup):
    def __init__(self, Path, FPS, Widgets, **kwargs):
        super().__init__(Path, FPS, Widgets, self.Callback, **kwargs)
    def Callback(self, FPS):
        try:
            self.SeqButton.SetFramePercent(get_wifi_percentage_iwconfig())
        except:
            self.SeqButton.SetFrame(0)