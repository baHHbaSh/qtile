import sys

import os
import random
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
terminal = "kitty"
keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([], "f11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "r", lazy.restart(), desc="Full reload the config"),
    Key([mod, "shift"], "Left", lazy.layout.grow_left()),
    Key([mod, "shift"], "Right", lazy.layout.grow_right()),
    Key([mod, "shift"], "Down", lazy.layout.grow_down()),
    Key([mod, "shift"], "Up", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "f", lazy.next_layout(), desc="Toggle between layouts"),
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


groups = [Group(i) for i in "123456789"]
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
    layout.Max()
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
                widget.CPUGraph(
                    type="line", line_width=1, border_width=0, graph_color="#dd3333", background="#000000dd", padding=2
                    ),
                widget.CPU(
                    format="ЦП: {load_percent}%", foreground="#dd3333", background="#000000dd", padding=2
                    ),
                widget.Memory(
                    measure_mem="G", format="ОЗУ: {MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}", foreground="#005599", background="#000000dd", padding=2
                    ),
                widget.ThermalSensor(
                    format='Temp: {temp:.0f}{unit}', foreground="#dd8511", background="#000000dd", padding=2
                    ),
                widget.Battery(
                    format="{percent:2.0%} {hour:d}:{min:02d}", foreground="#999900", background="#000000dd", padding=2
                    ),
                widget.Bluetooth(
                    adapter_format="[{name}+{powered}]", foreground="#000099", background="#000000dd", padding=2
                    ),
                widget.Wlan(
                    format="{essid}:{quality:2}/70", foreground="#995566", background="#000000dd", padding=2
                    ),
                widget.Net(
                    format='{down:.0f}{down_suffix}↓↑{up:.0f}{up_suffix}', foreground="#995566", background="#000000dd", padding=2
                    ),
                widget.Sep(),
                LangShownTextBox,
                widget.Sep(),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", foreground="#dddddd"),
            ],
            24,
            border_width=2,
            border_color="#181046",
            background="#130F1888",
            opacity=.9
        ),
        background="#001320",
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

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # различные всплывающие диалоги
        Match(wm_class="makebranch"),
        Match(wm_type="notification"),   # важное правило для уведомлений
        Match(wm_type="dialog"),
    ]
)

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

idle_inhibitors = []
wmname = "LG3D"

#ShowMessage("Message", "Launch")

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["bash", "/home/the/.config/qtile/Daemons/AutoStart.sh"])