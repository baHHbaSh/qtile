import os
import subprocess
import time
import threading
import traceback

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from EnG1nE.Language.Lang import*
from EnG1nE.AltTab.AltTab import AltTab
from EnG1nE.Binds.Media import InitMediaKeys
from EnG1nE.Binds.WinBinds import InitWinKeys

mod = "mod4" #win
terminal = guess_terminal()

def show_message(title, text):
    subprocess.run(['zenity', '--info', '--title', title, '--text', text])

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([], "f11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "Left", lazy.layout.grow_left()),
    Key([mod, "shift"], "Right", lazy.layout.grow_right()),
    Key([mod, "shift"], "Down", lazy.layout.grow_down()),
    Key([mod, "shift"], "Up", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]

ImportBinds = [
    LangInit,
    InitWinKeys,
    InitMediaKeys,
    AltTab,
]

for Bind in ImportBinds:
    try:
        Bind(keys)
    except:
        pass
        #ShowMessage("Error", traceback.format_exc())

# Назначить иконки или названия для групп
groups = [
    Group("1", label="^",),
    Group("2", label="💬"),
    Group("3", label="🌐"),
    Group("4", label="📁"),
    Group("5", label="🎮"),
    Group("6", label="🎵"),
    Group("7", label="📧"),
    Group("8", label="🔧"),
    Group("9", label="📦"),
]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

layouts = [
    layout.Bsp(border_focus_stack=["#0ea0aa", "#8f873d"], border_width=1),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Systray(),
                widget.Sep(),
                widget.GroupBox(highlight_method='line'),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#0e684d", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                widget.Clipboard(),
                widget.CPUGraph(type="line", line_width=1, border_width=0, graph_color="#009955"),
                widget.CPU(format="ЦП: {load_percent}%", foreground="#009955"),
                widget.Memory(measure_mem="G", format="ОЗУ: {MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}", foreground="#005599"),
                widget.ThermalSensor(format='Temp: {temp:.0f}{unit}', foreground="#dd1111"),
                widget.Battery(format="Bat: {percent:2.0%}", foreground="#999900"),
                widget.Bluetooth(adapter_format="[{name}+{powered}]", foreground="#000099"),
                widget.Wlan(format="Wi-Fi:{quality}%", foreground="#995566"),
                widget.Net(format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', foreground="#995566"),
                widget.Sep(),
                LangShownTextBox,
                widget.Sep(),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", foreground="#dddddd"),
            ],
            24,
            border_width=[2 for _ in range(4)],
            border_color=["#181046" for _ in range(4)],
            background="#130F18"
        ),
        background="#00132011",
        wallpaper="~/Pictures/D.png",
        wallpaper_mode="fill",
        x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

idle_inhibitors = []
wmname = "LG3D"

#ShowMessage("Message", "Launch")

@hook.subscribe.startup
def start_picom():
    
    def run_picom():
        time.sleep(2)
        # Пробуем убить старый процесс если есть
        subprocess.run(["pkill", "picom"])
        # Запускаем новый
        #picom --daemon --config ~/.config/picom/picom.conf
        subprocess.Popen(["picom", "--daemon", "--config", 
                         os.path.expanduser("~/.config/picom/picom.conf")])
    
    # Запускаем в отдельном потоке
    thread = threading.Thread(target=run_picom)
    thread.daemon = True
    thread.start()

AutoStartApps = [
    "pulseaudio --start",
    "steam",
    "Telegram",
    "google-chrome-stable",
]

@hook.subscribe.startup_once
def autostart():
    for Cmd in AutoStartApps:
        subprocess.Popen(Cmd.split(" "))
