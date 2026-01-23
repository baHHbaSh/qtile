from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy
import subprocess

win = "mod4" #win

Langs = [
    "us",
    "ru"
]
Lang = 0 #IndexOfLang

LangShownTextBox = widget.TextBox()

def SwitchLang(_, TargetLang= -1) -> None:
    global Lang
    if TargetLang < 0:
        Lang = 0 if Lang else 1
    else:
        Lang = TargetLang

    subprocess.run(["setxkbmap", "-layout", Langs[Lang]])
    Text = f'<span foreground=\"{"#d75f5f"}\">RU</span>' if Lang else f'<span foreground=\"{"#5f6bd7"}\">US</span>'
    LangShownTextBox.text = Text
    LangShownTextBox.draw()

SwitchLang(..., 0)

NewKeyBinds = [
    Key([win], "space", 
        lazy.function(SwitchLang),
        desc="Switch keyboard layout"),
    
    # Переключение раскладки по Shift+Alt (дублирование)
    Key(["shift"], 64,  # mod1 = Alt
        lazy.function(SwitchLang),
        desc="Switch keyboard layout"),
]

def LangInit(KeyBinds: list) -> None:
    KeyBinds += NewKeyBinds