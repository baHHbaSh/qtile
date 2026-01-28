from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4" #win
terminal = guess_terminal()

WinKeys = [
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "right", lazy.screen.next_group(), desc="Swap screen"),
    Key([mod, "control"], "left", lazy.screen.prev_group(), desc="Swap screen"),
    Key(["control", "shift"], "Escape", lazy.spawn(f"{terminal} -e htop")),
    Key([mod], "z", lazy.spawn(f"{terminal} -e bash /home/the/zapret-discord-youtube-linux/main_script.sh")),
    Key([mod], "i", lazy.spawn(f"{terminal} -e bash -c \"fastfetch; read\"")),
    Key([mod], "o", lazy.spawn(f"{terminal} -e iwctl")),
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "a", lazy.spawn("pavucontrol")),
    Key([mod], "l", lazy.spawn("i3lock")),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take screenshot"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Take screenshot"),
]

def InitWinKeys(keys:list):
    keys += WinKeys